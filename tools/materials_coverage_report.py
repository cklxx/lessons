#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CATEGORY_CHAPTER_HINTS: dict[str, list[str]] = {
    "product_discovery": ["02-discovery", "05-validation", "19-iteration", "01-method"],
    "prd_spec": ["03-prd", "07-engineering", "09-backend", "10-intelligence"],
    "ux_ui": ["04-prototype", "06-ui", "08-frontend", "05-validation"],
    "engineering": ["07-engineering", "08-frontend", "09-backend", "17-deployment"],
    "backend": ["09-backend", "07-engineering", "17-deployment", "18-evaluation"],
    "rag": ["10-intelligence", "18-evaluation", "13-data", "07-engineering"],
    "agents": ["10-intelligence", "07-engineering", "18-evaluation", "01-method"],
    "data": ["13-data", "18-evaluation", "10-intelligence", "20-governance"],
    "training": ["14-pretrain", "15-posttrain", "18-evaluation", "13-data"],
    "inference": ["16-inference", "17-deployment", "18-evaluation", "07-engineering"],
    "ops": ["17-deployment", "18-evaluation", "07-engineering", "20-governance"],
    "evaluation": ["18-evaluation", "17-deployment", "10-intelligence", "07-engineering"],
    "user_auth": ["11-user", "20-governance", "07-engineering", "09-backend"],
    "billing": ["12-billing", "19-iteration", "20-governance", "09-backend"],
    "governance": ["20-governance", "11-user", "12-billing", "13-data"],
    "general": ["01-method"],
}


@dataclass(frozen=True)
class Taxonomy:
    categories: dict[str, dict[str, str]]  # id -> {name, description}
    chapters: list[dict[str, str]]  # [{id,title}]


def _load_taxonomy(path: Path) -> Taxonomy:
    obj = json.loads(path.read_text(encoding="utf-8"))
    cats: dict[str, dict[str, str]] = {}
    for c in obj.get("categories", []) or []:
        cid = str(c.get("id") or "").strip()
        name = str(c.get("name") or "").strip()
        desc = str(c.get("description") or "").strip()
        if cid and name:
            cats[cid] = {"name": name, "description": desc}
    chapters: list[dict[str, str]] = []
    for ch in obj.get("chapters", []) or []:
        chid = str(ch.get("id") or "").strip()
        title = str(ch.get("title") or "").strip()
        if chid and title:
            chapters.append({"id": chid, "title": title})
    return Taxonomy(categories=cats, chapters=chapters)


def _extract_source_url(note_md: str) -> str | None:
    match = re.search(r"原始来源：.*?(https?://\S+)", note_md)
    if not match:
        return None
    return match.group(1).rstrip(".,;]")


def _normalize_chapter_targets(category_id: str, raw: list[str], chapter_ids: set[str]) -> list[str]:
    if not chapter_ids:
        return raw[:4]
    allowed_ordered = [c for c in CATEGORY_CHAPTER_HINTS.get(category_id, ["01-method"]) if c in chapter_ids]
    if not allowed_ordered:
        allowed_ordered = ["01-method"] if "01-method" in chapter_ids else sorted(chapter_ids)[:1]
    allowed_set = set(allowed_ordered)
    picked = [c for c in raw if c in allowed_set]
    if not picked:
        picked = allowed_ordered[:]
    primary = allowed_ordered[0] if allowed_ordered else None
    if primary and primary not in picked:
        picked.insert(0, primary)
    out: list[str] = []
    seen: set[str] = set()
    for c in picked:
        if c in seen:
            continue
        seen.add(c)
        out.append(c)
    for c in allowed_ordered:
        if len(out) >= 4:
            break
        if c not in out:
            out.append(c)
    return out[:4]


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))
    return rows


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Build a coverage report for materials/notes/deepresearch.")
    p.add_argument(
        "--taxonomy",
        default="docs/materials/ai-assisted-software-product/taxonomy.json",
        help="Taxonomy JSON.",
    )
    p.add_argument(
        "--labels-jsonl",
        default="docs/materials/ai-assisted-software-product/gemini/index.jsonl",
        help="Gemini labels jsonl.",
    )
    p.add_argument(
        "--sources-index",
        default="docs/materials/ai-assisted-software-product/sources/index.jsonl",
        help="Sources index jsonl.",
    )
    p.add_argument(
        "--notes-dir",
        default="docs/materials/ai-assisted-software-product/notes",
        help="Notes directory containing ref-*.md.",
    )
    p.add_argument(
        "--deepresearch-dir",
        default="docs/materials/ai-assisted-software-product/deepresearch",
        help="Deepresearch directory containing ref-*.md.",
    )
    p.add_argument(
        "--out",
        default="docs/materials/ai-assisted-software-product/coverage.md",
        help="Output markdown path.",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    taxonomy = _load_taxonomy(Path(args.taxonomy))
    chapter_ids = {c["id"] for c in taxonomy.chapters}

    sources_rows = [r for r in _read_jsonl(Path(args.sources_index)) if r.get("ok")]
    sources_by_url = {str(r.get("url") or "").strip(): r for r in sources_rows}

    label_rows = _read_jsonl(Path(args.labels_jsonl))
    label_by_url: dict[str, dict[str, Any]] = {}
    for r in label_rows:
        url = str(r.get("url") or "").strip()
        if url and url in sources_by_url:
            label_by_url[url] = r

    notes_dir = Path(args.notes_dir)
    deep_dir = Path(args.deepresearch_dir)

    note_urls: dict[str, str] = {}  # url -> note filename
    missing_source: list[str] = []
    missing_deep: list[str] = []
    for note_path in sorted(notes_dir.glob("ref-*.md")):
        md = note_path.read_text(encoding="utf-8", errors="replace")
        url = _extract_source_url(md)
        if not url:
            continue
        note_urls[url] = note_path.name
        if url not in sources_by_url:
            missing_source.append(note_path.name)
        if not (deep_dir / note_path.name).exists():
            missing_deep.append(note_path.name)

    # Coverage counters.
    by_chapter: dict[str, list[str]] = {c["id"]: [] for c in taxonomy.chapters}
    by_category: dict[str, list[str]] = {cid: [] for cid in taxonomy.categories}

    covered_urls = sorted(note_urls.keys())
    for url in covered_urls:
        label = label_by_url.get(url) or {}
        category_id = str(label.get("category_id") or "").strip() or "general"
        if taxonomy.categories and category_id not in taxonomy.categories:
            category_id = "general"
        raw_chapters = label.get("chapter_targets")
        chapters: list[str] = []
        if isinstance(raw_chapters, list):
            for x in raw_chapters:
                s = str(x).strip()
                if s and s in chapter_ids:
                    chapters.append(s)
        chapters = _normalize_chapter_targets(category_id, chapters, chapter_ids)

        by_category.setdefault(category_id, []).append(url)
        for chid in chapters:
            by_chapter.setdefault(chid, []).append(url)

    # Sort deterministic.
    for v in by_chapter.values():
        v.sort()
    for v in by_category.values():
        v.sort()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out_lines: list[str] = []
    out_lines.append("# Materials Coverage Report")
    out_lines.append("")
    out_lines.append(f"_Generated at {now} by `tools/materials_coverage_report.py`._")
    out_lines.append("")
    out_lines.append("## Summary")
    out_lines.append("")
    out_lines.append(f"- Notes: {len(list(notes_dir.glob('ref-*.md')))}")
    out_lines.append(f"- Sources snapshots: {len(sources_rows)}")
    out_lines.append(f"- Gemini labels (urls): {len(label_by_url)}")
    out_lines.append(f"- Deepresearch missing: {len(missing_deep)}")
    out_lines.append("")

    if missing_source:
        out_lines.append("## Missing Sources Snapshot")
        out_lines.append("")
        for n in missing_source[:30]:
            out_lines.append(f"- {n}")
        out_lines.append("")
    if missing_deep:
        out_lines.append("## Missing Deepresearch")
        out_lines.append("")
        for n in missing_deep[:30]:
            out_lines.append(f"- {n}")
        out_lines.append("")

    out_lines.append("## By Chapter")
    out_lines.append("")
    out_lines.append("| Chapter | Count | Notes |")
    out_lines.append("| --- | ---: | --- |")
    for ch in taxonomy.chapters:
        chid = ch["id"]
        urls = by_chapter.get(chid) or []
        count = len(urls)
        sample = ", ".join([Path(sources_by_url[u]["path"]).name for u in urls[:3] if u in sources_by_url])
        out_lines.append(f"| {ch['title']} ({chid}) | {count} | {sample} |")
    out_lines.append("")

    out_lines.append("## By Category")
    out_lines.append("")
    out_lines.append("| Category | Count | Chapter Focus (heuristic) |")
    out_lines.append("| --- | ---: | --- |")
    for cid, meta in taxonomy.categories.items():
        urls = by_category.get(cid) or []
        count = len(urls)
        focus = ", ".join(CATEGORY_CHAPTER_HINTS.get(cid, [])[:3])
        out_lines.append(f"| {meta['name']} ({cid}) | {count} | {focus} |")
    out_lines.append("")

    low_chapters = [ch for ch in taxonomy.chapters if len(by_chapter.get(ch["id"]) or []) < 2]
    low_categories = [cid for cid in taxonomy.categories if len(by_category.get(cid) or []) < 2]

    out_lines.append("## Thin Areas (Need More Materials)")
    out_lines.append("")
    out_lines.append("### Chapters (<2)")
    out_lines.append("")
    if low_chapters:
        for ch in low_chapters:
            out_lines.append(f"- {ch['title']} ({ch['id']})")
    else:
        out_lines.append("- (none)")
    out_lines.append("")

    out_lines.append("### Categories (<2)")
    out_lines.append("")
    if low_categories:
        for cid in low_categories:
            out_lines.append(f"- {taxonomy.categories[cid]['name']} ({cid})")
    else:
        out_lines.append("- (none)")
    out_lines.append("")

    Path(args.out).write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
