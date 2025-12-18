#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Step:
    name: str
    cmd: list[str]


def _run(step: Step) -> int:
    print(f"\n==> {step.name}\n$ {' '.join(step.cmd)}", flush=True)
    proc = subprocess.run(step.cmd, check=False)
    return int(proc.returncode)


def _mkdocs_cmd() -> list[str]:
    # Prefer the repo-local venv mkdocs binary so the command works even if
    # the user hasn't activated `.venv`.
    root = Path(__file__).resolve().parents[1]
    candidates = [
        root / ".venv" / "bin" / "mkdocs",
        root / ".venv" / "Scripts" / "mkdocs.exe",
        root / ".venv" / "Scripts" / "mkdocs",
    ]
    for p in candidates:
        if p.exists():
            return [str(p), "build", "--strict"]
    return [sys.executable, "-m", "mkdocs", "build", "--strict"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run repo quality gates (citations + mkdocs strict build).")
    parser.add_argument(
        "--skip-mkdocs",
        action="store_true",
        help="Skip mkdocs strict build (only run citations).",
    )
    parser.add_argument(
        "--skip-citations",
        action="store_true",
        help="Skip citations check (only run mkdocs).",
    )
    args = parser.parse_args()

    steps: list[Step] = []
    if not args.skip_citations:
        steps.append(Step("Citations", [sys.executable, "tools/check_citations.py"]))
    if not args.skip_mkdocs:
        steps.append(Step("MkDocs strict build", _mkdocs_cmd()))

    if not steps:
        print("Nothing to run (both checks skipped).")
        return 0

    failed: list[tuple[str, int]] = []
    for step in steps:
        code = _run(step)
        if code != 0:
            failed.append((step.name, code))

    if failed:
        print("\nFAILED:")
        for name, code in failed:
            print(f"- {name}: exit {code}")
        return 1

    print("\nOK: all gates passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
