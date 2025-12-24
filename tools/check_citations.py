#!/usr/bin/env python3
from __future__ import annotations

import glob
import os
import re
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK_DIR = os.path.join(ROOT, "docs", "books", "ai-assisted-software-product")
REFERENCES = os.path.join(BOOK_DIR, "references.md")

_CITATION_RE = re.compile(r"\[(\d+)\]")
_FENCE_START_RE = re.compile(r"^\s*([`~]{3,})")


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


def _strip_inline_code(text: str) -> str:
    out: list[str] = []
    i = 0
    in_code = False
    fence_len = 0

    while i < len(text):
        if not in_code:
            if text[i] == "`":
                j = i
                while j < len(text) and text[j] == "`":
                    j += 1
                in_code = True
                fence_len = j - i
                i = j
                continue
            out.append(text[i])
            i += 1
            continue

        if text[i] == "`":
            j = i
            while j < len(text) and text[j] == "`":
                j += 1
            if j - i == fence_len:
                in_code = False
                fence_len = 0
            i = j
            continue

        i += 1

    return "".join(out)


def parse_citations_from_markdown(path: str) -> list[int]:
    cleaned: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            fence_match = _FENCE_START_RE.match(raw_line)
            if fence_match:
                fence = fence_match.group(1)
                if not in_fence:
                    in_fence = True
                    fence_char = fence[0]
                    fence_len = len(fence)
                else:
                    if fence[0] == fence_char and len(fence) >= fence_len:
                        in_fence = False
                        fence_char = ""
                        fence_len = 0
                continue

            if in_fence:
                continue

            cleaned.append(_strip_inline_code(raw_line))

    text = "".join(cleaned)
    return [int(m.group(1)) for m in _CITATION_RE.finditer(text)]


def main() -> int:
    if not os.path.exists(REFERENCES):
        print(f"ERROR: missing references file: {REFERENCES}", file=sys.stderr)
        return 2

    reference_numbers = parse_reference_numbers(REFERENCES)
    if not reference_numbers:
        print(f"ERROR: no numbered references found in: {REFERENCES}", file=sys.stderr)
        return 2

    md_files = sorted(glob.glob(os.path.join(BOOK_DIR, "**", "*.md"), recursive=True))
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
