#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal


Choice = Literal["A", "B", "Tie"]


@dataclass(frozen=True)
class Item:
    id: str
    prompt: str
    a: str
    b: str


def _load_jsonl(path: Path) -> list[Item]:
    items: list[Item] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        items.append(
            Item(
                id=str(obj.get("id") or f"item-{len(items)+1}"),
                prompt=str(obj.get("prompt") or "").strip(),
                a=str(obj.get("a") or "").strip(),
                b=str(obj.get("b") or "").strip(),
            )
        )
    return items


def _mock_judge(prompt: str, a: str, b: str) -> tuple[Choice, str]:
    def score(x: str) -> int:
        s = 0
        s += min(len(x), 800) // 80  # reward some detail but cap it
        s += 2 if "步骤" in x or "清单" in x else 0
        s += 2 if "风险" in x or "回滚" in x else 0
        s -= 2 if "待核验" in x else 0
        s -= 2 if "不知道" in x else 0
        return s

    sa, sb = score(a), score(b)
    if abs(sa - sb) <= 1:
        return "Tie", f"mock: close scores sa={sa} sb={sb}"
    return ("A", f"mock: sa={sa} sb={sb}") if sa > sb else ("B", f"mock: sa={sa} sb={sb}")


def _gemini_judge(model: str, prompt: str, a: str, b: str, timeout_s: int) -> tuple[Choice, str]:
    judge_prompt = f"""你是严谨的评审（Judge）。请在 A 与 B 两个答案中选更好的一个，或判定 Tie。

评审规则（务必遵守）
1) 不要因为更长就更高分。
2) 优先看：是否回答了问题、步骤是否可执行、是否有边界/风险/回滚、是否避免编造事实。
3) 输出必须为 JSON（不要 Markdown，不要代码块），字段：
   - choice: "A" | "B" | "Tie"
   - reason: 一句话中文理由（<=60 字）

用户问题：
{prompt}

答案 A：
{a}

答案 B：
{b}
"""
    proc = subprocess.run(
        ["gemini", "--model", model, judge_prompt],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout_s,
        env={**os.environ, "NO_COLOR": "1"},
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"gemini exited {proc.returncode}")
    text = proc.stdout.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"gemini output not JSON: {text[:200]}")
    obj = json.loads(text[start : end + 1])
    choice = str(obj.get("choice") or "").strip()
    reason = str(obj.get("reason") or "").strip()
    if choice not in ("A", "B", "Tie"):
        raise ValueError(f"invalid choice: {choice}")
    return choice, reason


def _aggregate(c1: Choice, c2: Choice) -> Choice:
    if c1 == "Tie" or c2 == "Tie":
        return "Tie"
    # after swapping, same winner means stable; otherwise treat as tie
    return c1 if c1 == c2 else "Tie"


def main() -> int:
    parser = argparse.ArgumentParser(description="Pairwise judge with A/B swap (mock or gemini).")
    parser.add_argument("--in", dest="in_path", required=True, help="Input JSONL: {id,prompt,a,b}")
    parser.add_argument("--judge", choices=["mock", "gemini"], default="mock")
    parser.add_argument("--model", default="gemini-2.5-flash")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--sleep-ms", type=int, default=200)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--out", default="docs/examples/evaluation/report.json")
    args = parser.parse_args()

    items = _load_jsonl(Path(args.in_path))
    if not items:
        raise SystemExit("empty input")

    rng = random.Random(args.seed or 0)
    out: dict[str, Any] = {"judge": args.judge, "model": args.model, "items": []}

    for it in items:
        if args.judge == "gemini":
            c1, r1 = _gemini_judge(args.model, it.prompt, it.a, it.b, timeout_s=args.timeout)
            c2, r2 = _gemini_judge(args.model, it.prompt, it.b, it.a, timeout_s=args.timeout)  # swapped
            # normalize swapped result back to A/B in original order
            if c2 == "A":
                c2n: Choice = "B"
            elif c2 == "B":
                c2n = "A"
            else:
                c2n = "Tie"
            final = _aggregate(c1, c2n)
            reason = f"{r1} | swap: {r2}"
        else:
            c1, r1 = _mock_judge(it.prompt, it.a, it.b)
            c2, r2 = _mock_judge(it.prompt, it.b, it.a)
            c2n = "B" if c2 == "A" else ("A" if c2 == "B" else "Tie")
            final = _aggregate(c1, c2n)
            reason = f"{r1} | swap: {r2}"

        out["items"].append(
            {
                "id": it.id,
                "choice_1": c1,
                "choice_2_swapped_normalized": c2n,
                "final": final,
                "reason": reason,
            }
        )
        if args.sleep_ms > 0:
            time.sleep(args.sleep_ms / 1000 + rng.random() * 0.05)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

