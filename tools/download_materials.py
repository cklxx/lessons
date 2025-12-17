#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DownloadResult:
    url: str
    ok: bool
    status: int | None
    path: Path | None
    error: str | None
    elapsed_ms: int


def _extract_urls(text: str) -> list[str]:
    urls = re.findall(r"https?://[^\s)>\"]+", text)
    cleaned: list[str] = []
    for raw in urls:
        url = raw.rstrip(".,;]")
        cleaned.append(url)
    # Preserve order while de-duping
    seen: set[str] = set()
    deduped: list[str] = []
    for url in cleaned:
        if url in seen:
            continue
        seen.add(url)
        deduped.append(url)
    return deduped


def _slugify(value: str, max_len: int = 48) -> str:
    value = value.strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = re.sub(r"[?#].*$", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    if not value:
        return "resource"
    return value[:max_len].strip("-")


def _download(url: str, out_dir: Path, timeout_s: int, user_agent: str, sleep_ms: int) -> DownloadResult:
    start = time.time()
    status: int | None = None
    target: Path | None = None
    error: str | None = None
    ok = False

    try:
        req = urllib.request.Request(url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            status = getattr(resp, "status", None) or 200
            content = resp.read()

        slug = _slugify(url)
        short = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
        target = out_dir / f"{slug}-{short}.html"
        target.write_bytes(content)
        ok = True
    except urllib.error.HTTPError as exc:
        status = exc.code
        error = f"HTTPError {exc.code}"
    except urllib.error.URLError as exc:
        error = f"URLError {exc.reason}"
    except Exception as exc:  # pragma: no cover
        error = repr(exc)
    finally:
        if sleep_ms > 0:
            time.sleep(sleep_ms / 1000)

    elapsed_ms = int((time.time() - start) * 1000)
    return DownloadResult(url=url, ok=ok, status=status, path=target, error=error, elapsed_ms=elapsed_ms)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="download_materials",
        description="Download external reference pages for offline reading (HTML snapshots).",
    )
    parser.add_argument(
        "--input",
        default="docs/materials/ai-assisted-software-product/filtered/top-resources.md",
        help="Input file (Markdown recommended) from which URLs will be extracted.",
    )
    parser.add_argument(
        "--out",
        default="docs/materials/ai-assisted-software-product/downloads",
        help="Output directory (gitignored by default).",
    )
    parser.add_argument("--max", type=int, default=0, help="Max URLs to download (0 = no limit).")
    parser.add_argument("--timeout", type=int, default=20, help="Per-request timeout in seconds.")
    parser.add_argument(
        "--user-agent",
        default="lessons-material-downloader/1.0",
        help="User-Agent header used for HTTP requests.",
    )
    parser.add_argument("--sleep-ms", type=int, default=100, help="Sleep between requests (ms).")
    parser.add_argument("--dry-run", action="store_true", help="Only print extracted URLs; do not download.")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    input_path = Path(args.input).expanduser()
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    urls = _extract_urls(input_path.read_text(encoding="utf-8"))
    if args.max and args.max > 0:
        urls = urls[: args.max]

    if args.dry_run:
        print("\n".join(urls))
        return 0

    out_dir = Path(args.out).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[DownloadResult] = []
    for i, url in enumerate(urls, start=1):
        print(f"[{i}/{len(urls)}] {url}")
        results.append(_download(url, out_dir, args.timeout, args.user_agent, args.sleep_ms))

    ok = sum(1 for r in results if r.ok)
    failed = len(results) - ok
    print(f"\nDone. ok={ok} failed={failed} out={out_dir}")

    index_path = out_dir / "index.tsv"
    lines = ["url\tok\tstatus\tpath\terror\telapsed_ms"]
    for r in results:
        rel = ""
        if r.path is not None:
            try:
                rel = os.path.relpath(r.path, out_dir)
            except Exception:
                rel = str(r.path)
        lines.append(
            "\t".join(
                [
                    r.url,
                    "1" if r.ok else "0",
                    "" if r.status is None else str(r.status),
                    rel,
                    "" if r.error is None else r.error,
                    str(r.elapsed_ms),
                ]
            )
        )
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote: {index_path}")

    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

