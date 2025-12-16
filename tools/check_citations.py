#!/usr/bin/env python3
from __future__ import annotations

import glob
import os
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK_DIR = os.path.join(ROOT, "docs", "books", "ai-assisted-software-product")
REFERENCES = os.path.join(BOOK_DIR, "references.md")


def parse_reference_numbers(path: str) -> set[int]:
    numbers: set[int] = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.lstrip()
            i = 0
            while i < len(s) and s[i].isdigit():
                i += 1
            if i > 0 and i < len(s) and s[i] == ".":
                numbers.add(int(s[:i]))
    return numbers


def parse_citations_from_markdown(path: str) -> list[int]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    out: list[int] = []
    i = 0
    while True:
        start = text.find("[", i)
        if start == -1:
            break
        end = text.find("]", start + 1)
        if end == -1:
            break
        inner = text[start + 1 : end]
        if inner.isdigit():
            out.append(int(inner))
        i = end + 1
    return out


def main() -> int:
    if not os.path.exists(REFERENCES):
        print(f"ERROR: missing references file: {REFERENCES}", file=sys.stderr)
        return 2

    reference_numbers = parse_reference_numbers(REFERENCES)
    if not reference_numbers:
        print(f"ERROR: no numbered references found in: {REFERENCES}", file=sys.stderr)
        return 2

    md_files = sorted(glob.glob(os.path.join(BOOK_DIR, "*.md")))
    md_files = [p for p in md_files if os.path.abspath(p) != os.path.abspath(REFERENCES)]

    cited: dict[int, set[str]] = {}
    for path in md_files:
        for n in parse_citations_from_markdown(path):
            cited.setdefault(n, set()).add(os.path.relpath(path, ROOT))

    cited_numbers = set(cited.keys())
    missing = sorted(n for n in cited_numbers if n not in reference_numbers)
    unused = sorted(n for n in reference_numbers if n not in cited_numbers)

    max_ref = max(reference_numbers)
    print(f"References: {len(reference_numbers)} entries (max={max_ref})")
    print(f"Citations:  {len(cited_numbers)} distinct numbers across {len(md_files)} files")

    if missing:
        print("\nERROR: citations missing in references.md:")
        for n in missing:
            files = ", ".join(sorted(cited[n]))
            print(f"  [{n}] cited in: {files}")

    if unused:
        print("\nNOTE: references never cited (ok if intentional):")
        print("  " + ", ".join(f"[{n}]" for n in unused))

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
