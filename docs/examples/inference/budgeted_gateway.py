#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import threading
import time
import uuid
from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any


def _now_ms() -> int:
    return int(time.time() * 1000)


def _json_dumps(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def _read_json(handler: BaseHTTPRequestHandler, max_bytes: int = 1_000_000) -> dict[str, Any]:
    length = int(handler.headers.get("content-length") or "0")
    if length <= 0 or length > max_bytes:
        raise ValueError("invalid content-length")
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))


def _sha1(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


@dataclass
class CacheEntry:
    value: dict[str, Any]
    expires_at_ms: int


class TTLCache:
    def __init__(self, ttl_s: int):
        self._ttl_ms = ttl_s * 1000
        self._lock = threading.Lock()
        self._data: dict[str, CacheEntry] = {}

    def get(self, key: str) -> dict[str, Any] | None:
        now = _now_ms()
        with self._lock:
            entry = self._data.get(key)
            if not entry:
                return None
            if entry.expires_at_ms <= now:
                self._data.pop(key, None)
                return None
            return entry.value

    def set(self, key: str, value: dict[str, Any]) -> None:
        now = _now_ms()
        with self._lock:
            self._data[key] = CacheEntry(value=value, expires_at_ms=now + self._ttl_ms)


class Metrics:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.requests_total = 0
        self.requests_ok = 0
        self.requests_error = 0
        self.cache_hit = 0
        self.cache_miss = 0
        self.inflight = 0
        self.latency_ms_sum = 0

    def inc(self, name: str, delta: int = 1) -> None:
        with self._lock:
            setattr(self, name, int(getattr(self, name)) + delta)

    def set_gauge(self, name: str, value: int) -> None:
        with self._lock:
            setattr(self, name, int(value))

    def observe_latency_ms(self, ms: int) -> None:
        with self._lock:
            self.latency_ms_sum += int(ms)

    def render_prometheus(self) -> str:
        with self._lock:
            lines = [
                "# HELP gateway_requests_total Total requests",
                "# TYPE gateway_requests_total counter",
                f"gateway_requests_total {self.requests_total}",
                "# HELP gateway_requests_ok Successful requests",
                "# TYPE gateway_requests_ok counter",
                f"gateway_requests_ok {self.requests_ok}",
                "# HELP gateway_requests_error Failed requests",
                "# TYPE gateway_requests_error counter",
                f"gateway_requests_error {self.requests_error}",
                "# HELP gateway_cache_hit Cache hits",
                "# TYPE gateway_cache_hit counter",
                f"gateway_cache_hit {self.cache_hit}",
                "# HELP gateway_cache_miss Cache misses",
                "# TYPE gateway_cache_miss counter",
                f"gateway_cache_miss {self.cache_miss}",
                "# HELP gateway_inflight Inflight requests",
                "# TYPE gateway_inflight gauge",
                f"gateway_inflight {self.inflight}",
                "# HELP gateway_latency_ms_sum Sum of request latency in ms",
                "# TYPE gateway_latency_ms_sum counter",
                f"gateway_latency_ms_sum {self.latency_ms_sum}",
                "",
            ]
            return "\n".join(lines)


class GeminiProvider:
    def __init__(self, model: str):
        self.model = model

    def generate(self, prompt: str, timeout_s: int) -> str:
        proc = subprocess.run(
            ["gemini", "--model", self.model, prompt],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout_s,
            env={**os.environ, "NO_COLOR": "1"},
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or f"gemini exited {proc.returncode}")
        return proc.stdout.strip()


class MockProvider:
    def generate(self, prompt: str, timeout_s: int) -> str:
        del timeout_s
        time.sleep(0.15)
        return (
            "我先复述你的目标，然后给一个可执行的下一步。\n\n"
            f"你的输入摘要：{prompt[:120].strip().replace('\\n', ' ')}\n\n"
            "下一步：把这个问题拆成 3 个可验证的小问题，每个问题写清楚门槛与回滚。"
        )


def _log(event: str, **fields: Any) -> None:
    payload = {"ts_ms": _now_ms(), "event": event, **fields}
    print(json.dumps(payload, ensure_ascii=False))


class GatewayState:
    def __init__(self, provider: Any, cache_ttl_s: int, concurrency: int):
        self.provider = provider
        self.cache = TTLCache(ttl_s=cache_ttl_s)
        self.metrics = Metrics()
        self.sem = threading.Semaphore(concurrency)


class Handler(BaseHTTPRequestHandler):
    server_version = "BudgetedGateway/0.1"

    def do_GET(self) -> None:  # noqa: N802
        state: GatewayState = self.server.state  # type: ignore[attr-defined]
        if self.path == "/healthz":
            self._send_json(HTTPStatus.OK, {"ok": True})
            return
        if self.path == "/metrics":
            body = state.metrics.render_prometheus().encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("content-type", "text/plain; version=0.0.4; charset=utf-8")
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self._send_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        state: GatewayState = self.server.state  # type: ignore[attr-defined]
        trace_id = self.headers.get("x-trace-id") or uuid.uuid4().hex
        start_ms = _now_ms()
        state.metrics.inc("requests_total")

        if self.path != "/chat":
            self._send_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "not found"}, trace_id=trace_id)
            return

        try:
            body = _read_json(self)
            user_id = str(body.get("user_id") or "anonymous")
            prompt = str(body.get("prompt") or "").strip()
            budget_ms = int(body.get("budget_ms") or 1500)
            timeout_s = max(1, int(body.get("timeout_s") or 20))
            if not prompt:
                raise ValueError("missing prompt")

            key = _sha1(prompt)
            cached = state.cache.get(key)
            if cached:
                state.metrics.inc("cache_hit")
                state.metrics.inc("requests_ok")
                state.metrics.observe_latency_ms(_now_ms() - start_ms)
                _log("cache_hit", trace_id=trace_id, user_id=user_id, key=key)
                self._send_json(HTTPStatus.OK, {"ok": True, "cached": True, **cached}, trace_id=trace_id)
                return
            state.metrics.inc("cache_miss")

            acquired = state.sem.acquire(timeout=max(0.1, budget_ms / 1000))
            if not acquired:
                state.metrics.inc("requests_error")
                state.metrics.observe_latency_ms(_now_ms() - start_ms)
                _log("overloaded", trace_id=trace_id, user_id=user_id)
                self._send_json(
                    HTTPStatus.TOO_MANY_REQUESTS,
                    {"ok": False, "error": "overloaded", "hint": "retry later or increase budget_ms"},
                    trace_id=trace_id,
                )
                return

            try:
                state.metrics.set_gauge("inflight", int(state.metrics.inflight) + 1)
                remaining_ms = max(1, budget_ms - (_now_ms() - start_ms))
                provider_timeout_s = max(1, min(timeout_s, int(remaining_ms / 1000) + 1))
                answer = state.provider.generate(prompt, timeout_s=provider_timeout_s)
            finally:
                state.metrics.set_gauge("inflight", max(0, int(state.metrics.inflight) - 1))
                state.sem.release()

            out = {"answer": answer, "budget_ms": budget_ms}
            state.cache.set(key, out)
            state.metrics.inc("requests_ok")
            state.metrics.observe_latency_ms(_now_ms() - start_ms)
            _log("ok", trace_id=trace_id, user_id=user_id, budget_ms=budget_ms, answer_chars=len(answer))
            self._send_json(HTTPStatus.OK, {"ok": True, "cached": False, **out}, trace_id=trace_id)
        except Exception as exc:
            state.metrics.inc("requests_error")
            state.metrics.observe_latency_ms(_now_ms() - start_ms)
            _log("error", trace_id=trace_id, error=repr(exc))
            self._send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": str(exc)}, trace_id=trace_id)

    def log_message(self, fmt: str, *args: Any) -> None:
        # Silence default http.server logs; we use structured logs instead.
        return

    def _send_json(self, status: int, obj: dict[str, Any], trace_id: str | None = None) -> None:
        payload = dict(obj)
        if trace_id:
            payload["trace_id"] = trace_id
        body = _json_dumps(payload)
        self.send_response(status)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(body)))
        if trace_id:
            self.send_header("x-trace-id", trace_id)
        self.end_headers()
        self.wfile.write(body)


def main() -> int:
    parser = argparse.ArgumentParser(description="A tiny budgeted chat gateway (stdlib-only).")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--provider", choices=["mock", "gemini"], default="mock")
    parser.add_argument("--gemini-model", default="gemini-2.5-flash")
    parser.add_argument("--cache-ttl", type=int, default=60, help="Cache TTL in seconds.")
    parser.add_argument("--concurrency", type=int, default=4, help="Max concurrent generations.")
    args = parser.parse_args()

    if args.provider == "gemini":
        provider: Any = GeminiProvider(model=args.gemini_model)
    else:
        provider = MockProvider()

    state = GatewayState(provider=provider, cache_ttl_s=args.cache_ttl, concurrency=args.concurrency)
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    server.state = state  # type: ignore[attr-defined]
    _log("started", host=args.host, port=args.port, provider=args.provider)
    try:
        server.serve_forever(poll_interval=0.2)
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        _log("stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
