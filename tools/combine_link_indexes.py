#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


EXPECTED_FIELDS = [
    "Title",
    "URL",
    "Source/Domain",
    "Pub Date",
    "Category",
    "Relevance",
    "Authority",
    "Recency",
    "Completeness",
    "Readability",
    "Total",
    "Score Reason",
]


@dataclass(frozen=True)
class LinkRow:
    title: str
    url: str
    domain: str
    pub_date: str
    category: str
    relevance: float
    authority: float
    recency: float
    completeness: float
    readability: float
    total: float
    reason: str
    source_file: str


def _safe_float(v: str) -> float:
    try:
        x = float(v)
    except Exception:
        return 0.0
    if math.isnan(x) or math.isinf(x):
        return 0.0
    return x


def _iter_csv_rows(paths: Iterable[Path]) -> list[LinkRow]:
    out: list[LinkRow] = []
    for path in paths:
        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames or []
            if "URL" not in fields or "Title" not in fields:
                continue
            for row in reader:
                url = (row.get("URL") or "").strip()
                title = (row.get("Title") or "").strip()
                if not url or not title:
                    continue
                out.append(
                    LinkRow(
                        title=title,
                        url=url,
                        domain=(row.get("Source/Domain") or "").strip(),
                        pub_date=(row.get("Pub Date") or "").strip(),
                        category=(row.get("Category") or "").strip() or "Uncategorized",
                        relevance=_safe_float((row.get("Relevance") or "").strip()),
                        authority=_safe_float((row.get("Authority") or "").strip()),
                        recency=_safe_float((row.get("Recency") or "").strip()),
                        completeness=_safe_float((row.get("Completeness") or "").strip()),
                        readability=_safe_float((row.get("Readability") or "").strip()),
                        total=_safe_float((row.get("Total") or "").strip()),
                        reason=(row.get("Score Reason") or "").strip(),
                        source_file=path.as_posix(),
                    )
                )
    return out


def _pick_best(a: LinkRow, b: LinkRow) -> LinkRow:
    # Prefer higher total, then authority, then recency.
    def key(x: LinkRow) -> tuple[float, float, float, int]:
        return (x.total, x.authority, x.recency, len(x.reason))

    return a if key(a) >= key(b) else b


def _domain_match(value: str, suffixes: set[str], contains: set[str]) -> bool:
    v = value.lower().strip()
    if not v:
        return False
    if any(v.endswith(s) for s in suffixes):
        return True
    if any(token in v for token in contains):
        return True
    return False


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Combine link-index batch CSVs into one deduped file.")
    p.add_argument(
        "--in-dir",
        default="docs/materials/ai-assisted-software-product/raw",
        help="Directory containing link-index-*.csv batches.",
    )
    p.add_argument(
        "--glob",
        default="link-index-batch*.csv",
        help="Glob pattern (relative to --in-dir) to select input CSVs.",
    )
    p.add_argument(
        "--out",
        default="docs/materials/ai-assisted-software-product/filtered/link-index-combined.csv",
        help="Output combined CSV path.",
    )
    p.add_argument(
        "--exclude-domain-suffix",
        action="append",
        default=[],
        help="Exclude domains by suffix (repeatable). Example: --exclude-domain-suffix .substack.com",
    )
    p.add_argument(
        "--exclude-domain-contains",
        action="append",
        default=[],
        help="Exclude domains containing token (repeatable). Example: --exclude-domain-contains ycombinator",
    )
    p.add_argument(
        "--exclude-title-regex",
        action="append",
        default=[],
        help="Exclude titles matching regex (repeatable). Example: --exclude-title-regex '(?i)^show hn[:：]'",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()
    in_dir = Path(args.in_dir)
    if not in_dir.exists():
        raise SystemExit(f"Missing input dir: {in_dir}")

    paths = sorted(in_dir.glob(args.glob))
    if not paths:
        raise SystemExit(f"No CSV matches: {in_dir / args.glob}")

    rows = _iter_csv_rows(paths)
    suffixes = {s.strip().lower() for s in (args.exclude_domain_suffix or []) if s.strip()}
    contains = {s.strip().lower() for s in (args.exclude_domain_contains or []) if s.strip()}
    title_patterns = [re.compile(p) for p in (args.exclude_title_regex or []) if p.strip()]

    best_by_url: dict[str, LinkRow] = {}
    skipped_domain = 0
    skipped_title = 0
    for row in rows:
        if (suffixes or contains) and _domain_match(row.domain, suffixes=suffixes, contains=contains):
            skipped_domain += 1
            continue
        if title_patterns and any(p.search(row.title) for p in title_patterns):
            skipped_title += 1
            continue
        prev = best_by_url.get(row.url)
        best_by_url[row.url] = row if prev is None else _pick_best(prev, row)

    combined = list(best_by_url.values())
    combined.sort(key=lambda r: (r.category, -r.total, -r.authority, r.title))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EXPECTED_FIELDS)
        writer.writeheader()
        for r in combined:
            writer.writerow(
                {
                    "Title": r.title,
                    "URL": r.url,
                    "Source/Domain": r.domain,
                    "Pub Date": r.pub_date,
                    "Category": r.category,
                    "Relevance": r.relevance,
                    "Authority": r.authority,
                    "Recency": r.recency,
                    "Completeness": r.completeness,
                    "Readability": r.readability,
                    "Total": r.total,
                    "Score Reason": r.reason,
                }
            )

    print(f"Wrote: {out} (inputs={len(paths)} rows={len(rows)} unique={len(combined)})")
    if skipped_domain or skipped_title:
        print(f"Skipped: domain={skipped_domain} title={skipped_title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

