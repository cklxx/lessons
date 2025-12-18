#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def _rewrite_text(md: str) -> str:
    out_lines: list[str] = []
    for line in md.splitlines(keepends=True):
        # Convert adjacent quote boundaries into a natural list separator, e.g.
        # “排期”“资源”“对齐会议” -> 排期、资源、对齐会议
        line = line.replace("”“", "、")

        # Remove Chinese double quotes in prose; prefer plain wording or backticks for code.
        line = line.replace("“", "").replace("”", "")
        out_lines.append(line)

    return "".join(out_lines)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Normalize Chinese double quotes in Markdown.")
    p.add_argument("paths", nargs="+", help="Files or directories to process.")
    p.add_argument("--dry-run", action="store_true", help="Only print what would change.")
    return p


def main() -> int:
    args = build_parser().parse_args()
    targets: list[Path] = []
    for raw in args.paths:
        p = Path(raw)
        if p.is_dir():
            targets.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            targets.append(p)

    changed = 0
    for path in targets:
        original = path.read_text(encoding="utf-8", errors="replace")
        rewritten = _rewrite_text(original)
        if rewritten == original:
            continue
        changed += 1
        if args.dry_run:
            print(f"Would update: {path}")
            continue
        path.write_text(rewritten, encoding="utf-8")
        print(f"Updated: {path}")

    print(f"Done. changed_files={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
