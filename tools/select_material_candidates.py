#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Candidate:
    title: str
    url: str
    domain: str
    pub_date: str
    category: str
    authority: float
    total: float
    reason: str


def _read_existing_urls(sources_index: Path) -> set[str]:
    urls: set[str] = set()
    if not sources_index.exists():
        return urls
    for line in sources_index.read_text(encoding="utf-8").splitlines():
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if not obj.get("ok"):
            continue
        url = str(obj.get("url") or "").strip()
        if url:
            urls.add(url)
    return urls


def _safe_float(v: str) -> float:
    try:
        return float(v)
    except Exception:
        return 0.0


def _load_csv(path: Path) -> list[Candidate]:
    rows: list[Candidate] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            url = (r.get("URL") or "").strip()
            title = (r.get("Title") or "").strip()
            domain = (r.get("Source/Domain") or "").strip()
            pub = (r.get("Pub Date") or "").strip()
            cat = (r.get("Category") or "").strip()
            authority = _safe_float((r.get("Authority") or "").strip())
            total = _safe_float((r.get("Total") or "").strip())
            reason = (r.get("Score Reason") or "").strip()
            if not url or not title:
                continue
            rows.append(
                Candidate(
                    title=title,
                    url=url,
                    domain=domain,
                    pub_date=pub,
                    category=cat or "Uncategorized",
                    authority=authority,
                    total=total,
                    reason=reason,
                )
            )
    return rows


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Select top candidates from link-index-combined.csv.")
    p.add_argument(
        "--in-csv",
        default="docs/materials/ai-assisted-software-product/filtered/link-index-combined.csv",
        help="Input combined CSV (harvested links).",
    )
    p.add_argument(
        "--sources-index",
        default="docs/materials/ai-assisted-software-product/sources/index.jsonl",
        help="Existing sources index (dedupe).",
    )
    p.add_argument(
        "--out-md",
        default="docs/materials/ai-assisted-software-product/candidates.md",
        help="Output markdown candidates list.",
    )
    p.add_argument("--per-category", type=int, default=6, help="How many candidates per category.")
    p.add_argument("--min-total", type=float, default=0.58, help="Minimum heuristic total score (0-1).")
    p.add_argument("--min-authority", type=float, default=0.65, help="Minimum heuristic authority score (0-1).")
    p.add_argument(
        "--exclude-domain",
        action="append",
        default=[
            "openai.com",
            "help.openai.com",
            "www.svpg.com",
            "harvarduxgroup.hsites.harvard.edu",
        ],
        help="Exclude domains (repeatable). Example: --exclude-domain medium.com",
    )
    p.add_argument(
        "--exclude-domain-contains",
        action="append",
        default=["ycombinator", "substack", "medium.com"],
        help="Exclude domains containing token (repeatable).",
    )
    p.add_argument(
        "--exclude-title-regex",
        action="append",
        default=[r"(?i)^show hn[:：]"],
        help="Exclude titles matching regex (repeatable).",
    )
    p.add_argument(
        "--include-pdf",
        action="store_true",
        help="Include .pdf URLs (default: exclude, because snapshotting requires extra tooling).",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()
    in_csv = Path(args.in_csv)
    if not in_csv.exists():
        raise SystemExit(f"Missing input CSV: {in_csv}")

    existing_urls = _read_existing_urls(Path(args.sources_index))
    candidates = _load_csv(in_csv)

    excluded_domains = {d.strip().lower() for d in (args.exclude_domain or []) if d.strip()}
    excluded_domain_contains = {d.strip().lower() for d in (args.exclude_domain_contains or []) if d.strip()}
    excluded_title_patterns = []
    for raw in args.exclude_title_regex or []:
        raw = raw.strip()
        if not raw:
            continue
        excluded_title_patterns.append(re.compile(raw))

    by_category: dict[str, list[Candidate]] = {}
    for c in candidates:
        if c.total < float(args.min_total):
            continue
        if c.authority < float(args.min_authority):
            continue
        if not args.include_pdf and ".pdf" in c.url.lower():
            continue
        if c.url in existing_urls:
            continue
        if excluded_domains and c.domain.lower() in excluded_domains:
            continue
        if excluded_domain_contains and any(token in c.domain.lower() for token in excluded_domain_contains):
            continue
        if excluded_title_patterns and any(p.search(c.title) for p in excluded_title_patterns):
            continue
        by_category.setdefault(c.category, []).append(c)

    for cat in by_category:
        by_category[cat].sort(key=lambda x: x.total, reverse=True)
        by_category[cat] = by_category[cat][: max(0, int(args.per_category))]

    out = Path(args.out_md)
    out.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("# Materials Candidates (Inbox)")
    lines.append("")
    lines.append("> 本页是从历史抓取的外链库中自动挑出的候选资料（未审阅）。")
    lines.append("> 后续流程：`materials_to_markdown.py` 快照 → `gemini_build_material_indexes.py` 评分 → 低分过滤/高分 deepresearch。")
    lines.append("")
    lines.append(
        f"- Rule: per-category={args.per_category}, min-total={args.min_total}, min-authority={args.min_authority}"
    )
    if excluded_domains:
        lines.append(f"- Exclude domains: {', '.join(sorted(excluded_domains))}")
    if excluded_domain_contains:
        lines.append(f"- Exclude domain tokens: {', '.join(sorted(excluded_domain_contains))}")
    if excluded_title_patterns:
        lines.append(f"- Exclude title regex: {', '.join(sorted(p.pattern for p in excluded_title_patterns))}")
    lines.append("")

    for cat in sorted(by_category.keys()):
        items = by_category[cat]
        if not items:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| # | Total | Authority | Title | Domain | Pub Date | URL |")
        lines.append("| --- | ---: | ---: | --- | --- | --- | --- |")
        for idx, c in enumerate(items, start=1):
            title = c.title.replace("|", "\\|")
            lines.append(
                f"| {idx} | {c.total:.4f} | {c.authority:.2f} | {title} | {c.domain} | {c.pub_date} | {c.url} |"
            )
        lines.append("")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote: {out}")
    total_picked = sum(len(v) for v in by_category.values())
    print(f"Picked: {total_picked} URLs across {len(by_category)} categories (deduped vs sources).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
