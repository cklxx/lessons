#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin


FRAGMENT_DEST_RE = re.compile(r"\]\(#[^)]*\)")
INLINE_LINK_RE = re.compile(r"(\]\()([^\s)]+)(\s+\"[^\"]*\")?\)")
REF_DEF_RE = re.compile(r"(?m)^\[([^\]]+)\]:\s+(\S+)(.*)$")


@dataclass(frozen=True)
class Result:
    path: Path
    changed: bool
    removed_links: int


def _extract_base_url(md: str) -> str | None:
    for line in md.splitlines()[:40]:
        if line.startswith("- URL:"):
            value = line[len("- URL:") :].strip()
            return value or None
    return None


def _rewrite_target(target: str, base_url: str) -> str:
    t = target.strip()
    if not t:
        return t
    if t.startswith("#"):
        return t
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", t):
        return t
    return urljoin(base_url, t)


def _sanitize_markdown(md: str) -> tuple[str, int, int]:
    removed_fragments = len(FRAGMENT_DEST_RE.findall(md))
    md2 = FRAGMENT_DEST_RE.sub("]", md)
    md2 = re.sub(r"\[\s*\]", "", md2)

    rewritten = 0
    base_url = _extract_base_url(md2)
    if base_url:
        def repl_inline(match: re.Match[str]) -> str:
            nonlocal rewritten
            before = match.group(1)
            target = match.group(2)
            after = match.group(3) or ""
            new_target = _rewrite_target(target, base_url)
            if new_target != target:
                rewritten += 1
            return f"{before}{new_target}{after})"

        md2 = INLINE_LINK_RE.sub(repl_inline, md2)

        def repl_ref(match: re.Match[str]) -> str:
            nonlocal rewritten
            label = match.group(1)
            target = match.group(2)
            rest = match.group(3) or ""
            new_target = _rewrite_target(target, base_url)
            if new_target != target:
                rewritten += 1
            return f"[{label}]: {new_target}{rest}"

        md2 = REF_DEF_RE.sub(repl_ref, md2)

    return md2, removed_fragments, rewritten


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Sanitize generated materials snapshots for mkdocs strict build.")
    p.add_argument(
        "--dir",
        default="docs/materials/ai-assisted-software-product/sources/md",
        help="Directory containing snapshot markdown files.",
    )
    p.add_argument(
        "--glob",
        default="*.md",
        help="Glob pattern to select files.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write changes; only report.",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.dir)
    if not root.exists():
        raise SystemExit(f"Missing directory: {root}")

    files = sorted(root.glob(args.glob))
    results: list[Result] = []
    total_removed = 0
    total_rewritten = 0
    for path in files:
        before = path.read_text(encoding="utf-8", errors="replace")
        after, removed, rewritten = _sanitize_markdown(before)
        changed = after != before
        results.append(Result(path=path, changed=changed, removed_links=removed))
        total_removed += removed
        total_rewritten += rewritten
        if changed and not args.dry_run:
            path.write_text(after, encoding="utf-8")

    changed = sum(1 for r in results if r.changed)
    print(
        f"Scanned: {len(results)} files, changed: {changed}, "
        f"removed_fragment_links: {total_removed}, rewritten_relative_links: {total_rewritten}"
    )
    for r in results:
        if r.changed:
            print(f"- {r.path}: removed {r.removed_links}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
