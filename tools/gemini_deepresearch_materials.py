#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CATEGORY_ID = "general"

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
class SourceEntry:
    url: str
    snapshot_rel: str
    title: str | None


def _extract_urls(text: str) -> list[str]:
    urls = re.findall(r"https?://[^\s)>\"]+", text)
    cleaned: list[str] = []
    for raw in urls:
        cleaned.append(raw.rstrip(".,;]"))
    seen: set[str] = set()
    out: list[str] = []
    for url in cleaned:
        if url in seen:
            continue
        seen.add(url)
        out.append(url)
    return out


def _rel_link(from_dir: Path, to_path: Path) -> str:
    try:
        rel = os.path.relpath(to_path, start=from_dir)
    except Exception:
        return to_path.as_posix()
    return Path(rel).as_posix()


def _run_gemini(input_text: str, prompt: str, model: str | None, timeout_s: int) -> str:
    cmd = ["gemini"]
    if model:
        cmd += ["--model", model]
    cmd += ["-p", prompt]
    proc = subprocess.run(
        cmd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        timeout=timeout_s,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gemini exited {proc.returncode}")
    return proc.stdout.rstrip() + "\n"


def _extract_first_heading(md: str) -> str | None:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or None
    return None


def _extract_source_url(note_md: str) -> str | None:
    # Accept both:
    # - 原始来源：https://example.com
    # - 原始来源：一些说明… https://example.com
    match = re.search(r"原始来源：.*?(https?://\S+)", note_md)
    if not match:
        return None
    return match.group(1).rstrip(".,;]")


def _load_sources_index(path: Path) -> dict[str, SourceEntry]:
    mapping: dict[str, SourceEntry] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        obj = json.loads(line)
        if not obj.get("ok"):
            continue
        url = str(obj.get("url") or "").strip()
        rel = str(obj.get("path") or "").strip()
        title = obj.get("title")
        if url and rel:
            mapping[url] = SourceEntry(url=url, snapshot_rel=rel, title=title)
    return mapping


def _load_gemini_labels(path: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        obj = json.loads(line)
        url = str(obj.get("url") or "").strip()
        if url:
            out[url] = obj
    return out


def _load_taxonomy(path: Path) -> tuple[dict[str, dict[str, str]], list[dict[str, str]]]:
    if not path.exists():
        return {}, []
    obj = json.loads(path.read_text(encoding="utf-8"))
    categories: dict[str, dict[str, str]] = {}
    for c in obj.get("categories", []) or []:
        cid = str(c.get("id") or "").strip()
        name = str(c.get("name") or "").strip()
        desc = str(c.get("description") or "").strip()
        if cid and name:
            categories[cid] = {"name": name, "description": desc}
    chapters: list[dict[str, str]] = []
    for ch in obj.get("chapters", []) or []:
        chid = str(ch.get("id") or "").strip()
        title = str(ch.get("title") or "").strip()
        if chid and title:
            chapters.append({"id": chid, "title": title})
    return categories, chapters


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
    seen: set[str] = set()
    out: list[str] = []
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


def _render_deepresearch_index(
    out_path: Path,
    items: list[tuple[str, str, str, float | None, list[str]]],
    chapters: list[dict[str, str]],
    taxonomy_categories: dict[str, dict[str, str]],
) -> None:
    # items: (category_id, title, rel_path, score_total, chapter_targets)
    by_chapter: dict[str, list[tuple[str, str, float | None, str]]] = {}
    for category_id, title, rel, score, chapter_targets in items:
        if chapter_targets:
            for chid in chapter_targets:
                by_chapter.setdefault(chid, []).append((title, rel, score, category_id))
        else:
            by_chapter.setdefault(DEFAULT_CATEGORY_ID, []).append((title, rel, score, category_id))

    for chid in by_chapter:
        by_chapter[chid].sort(key=lambda x: (x[2] is None, -(x[2] or 0.0), x[0]))

    lines: list[str] = []
    lines.append("# Deep Research Index")
    lines.append("")
    lines.append("> 本目录为每篇资料生成一份更深入的“可落地扩展笔记”，用于补充/强化《AI 辅助软件产品》。")
    lines.append("")

    chapter_title_map = {c["id"]: c["title"] for c in chapters}
    ordered_ids = [c["id"] for c in chapters]
    for extra in sorted(by_chapter.keys()):
        if extra not in chapter_title_map:
            ordered_ids.append(extra)

    seen: set[str] = set()
    for chid in ordered_ids:
        if chid in seen:
            continue
        seen.add(chid)
        items_for = by_chapter.get(chid) or []
        if not items_for:
            continue
        title = chapter_title_map.get(chid, f"其他（{chid}）")
        lines.append(f"## {title}")
        lines.append("")
        for item_title, rel, score, category_id in items_for:
            cat_name = taxonomy_categories.get(category_id, {}).get("name", category_id)
            suffix = f"（{score:.2f}）" if score is not None else ""
            lines.append(f"- [{item_title}]({rel}){suffix} · {cat_name}")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gemini_deepresearch_materials",
        description="Generate deep-research notes for each materials reference using Gemini CLI.",
    )
    parser.add_argument(
        "--mode",
        choices=["notes", "labels"],
        default="notes",
        help="notes: generate for ref-*.md notes; labels: generate for high-score labeled sources.",
    )
    parser.add_argument(
        "--notes-dir",
        default="docs/materials/ai-assisted-software-product/notes",
        help="Directory containing ref-*.md notes.",
    )
    parser.add_argument(
        "--sources-index",
        default="docs/materials/ai-assisted-software-product/sources/index.jsonl",
        help="Sources index generated by tools/materials_to_markdown.py",
    )
    parser.add_argument(
        "--labels-jsonl",
        default="docs/materials/ai-assisted-software-product/gemini/index.jsonl",
        help="Gemini labels JSONL generated by tools/gemini_build_material_indexes.py",
    )
    parser.add_argument(
        "--out-dir",
        default="docs/materials/ai-assisted-software-product/deepresearch",
        help="Output directory for deep research markdown files.",
    )
    parser.add_argument(
        "--index-out",
        default="docs/materials/ai-assisted-software-product/deepresearch/index.md",
        help="Output index markdown file.",
    )
    parser.add_argument(
        "--taxonomy",
        default="docs/materials/ai-assisted-software-product/taxonomy.json",
        help="Taxonomy JSON defining allowed categories and chapter ids.",
    )
    parser.add_argument(
        "--urls-from",
        action="append",
        default=[],
        help="Optional markdown file to restrict processing to its URLs (repeatable).",
    )
    parser.add_argument(
        "--min-score-total",
        type=float,
        default=0.0,
        help="labels mode only: keep entries with score_total >= this value (0 disables).",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=0,
        help="labels mode only: cap generated items (0 = no limit).",
    )
    parser.add_argument(
        "--out-subdir",
        default="",
        help="Optional subdirectory under --out-dir to place outputs (e.g. high-score).",
    )
    parser.add_argument(
        "--category-id",
        action="append",
        default=[],
        help="labels mode only: restrict to category_id (repeatable).",
    )
    parser.add_argument(
        "--chapter-id",
        action="append",
        default=[],
        help="labels mode only: restrict to chapter target id (repeatable).",
    )
    parser.add_argument("--model", default="", help="Gemini model override (optional).")
    parser.add_argument("--timeout", type=int, default=240, help="Per-item Gemini timeout in seconds.")
    parser.add_argument("--sleep-ms", type=int, default=250, help="Sleep between Gemini calls (ms).")
    parser.add_argument("--max-chars", type=int, default=90000, help="Max snapshot chars passed to Gemini.")
    parser.add_argument("--force", action="store_true", help="Regenerate files even if they already exist.")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    notes_dir = Path(args.notes_dir)
    sources_index = Path(args.sources_index)
    labels_path = Path(args.labels_jsonl)
    out_dir = Path(args.out_dir)
    index_out = Path(args.index_out)
    project_dir = sources_index.parent.parent
    out_base = out_dir
    if args.out_subdir.strip():
        out_base = out_dir / args.out_subdir.strip()
    out_base.mkdir(parents=True, exist_ok=True)

    sources = _load_sources_index(sources_index)
    labels = _load_gemini_labels(labels_path)
    taxonomy_categories, chapters = _load_taxonomy(Path(args.taxonomy))
    chapter_ids = {c["id"] for c in chapters}

    model = args.model.strip() or None
    generated: list[tuple[str, str, str, float | None, list[str]]] = []

    url_allow: set[str] | None = None
    if args.urls_from:
        url_allow = set()
        for raw in args.urls_from:
            p = Path(raw)
            if not p.exists():
                continue
            url_allow.update(_extract_urls(p.read_text(encoding="utf-8", errors="replace")))

    if args.mode == "notes":
        note_paths = sorted(notes_dir.glob("ref-*.md"))
        for i, note_path in enumerate(note_paths, start=1):
            note_md = note_path.read_text(encoding="utf-8", errors="replace")
            url = _extract_source_url(note_md)
            if not url:
                continue
            if url_allow is not None and url not in url_allow:
                continue
            src = sources.get(url)
            if not src:
                continue

            snapshot_path = sources_index.parent / src.snapshot_rel
            if not snapshot_path.exists():
                continue
            snapshot_md = snapshot_path.read_text(encoding="utf-8", errors="replace")
            if args.max_chars and args.max_chars > 0 and len(snapshot_md) > args.max_chars:
                snapshot_md = snapshot_md[: args.max_chars].rstrip() + "\n\n[TRUNCATED]\n"

            title = _extract_first_heading(note_md) or _extract_first_heading(snapshot_md) or note_path.stem
            out_path = out_base / f"{note_path.stem}.md"
            out_rel = _rel_link(index_out.parent, out_path)

            label = labels.get(url, {})
            category_id = str(label.get("category_id") or "").strip() or DEFAULT_CATEGORY_ID
            if taxonomy_categories and category_id not in taxonomy_categories:
                category_id = DEFAULT_CATEGORY_ID
            chapter_targets: list[str] = []
            raw_chapters = label.get("chapter_targets")
            if isinstance(raw_chapters, list):
                for x in raw_chapters:
                    s = str(x).strip()
                    if not s:
                        continue
                    if chapter_ids and s not in chapter_ids:
                        continue
                    chapter_targets.append(s)
            chapter_targets = _normalize_chapter_targets(category_id, chapter_targets, chapter_ids)
            score_total: float | None = None
            try:
                if "score_total" in label:
                    score_total = float(label["score_total"])
            except Exception:
                score_total = None

            generated.append((category_id, title, out_rel, score_total, chapter_targets))

            if out_path.exists() and not args.force:
                continue

            prompt = (
                f"Explain {title} with deep research for a Chinese technical book project.\n"
                f"RESOURCE_URL: {url}\n"
                f"NOTE_FILE: {note_path.name}\n"
                f"SNAPSHOT_FILE: {src.snapshot_rel}\n\n"
                "Write Markdown ONLY (no code fences). Use Chinese. Structure:\n"
                "## TL;DR (1-2 sentences)\n"
                "## 核心观点（5-8 条）\n"
                "## 可落地做法（面向产品/工程/评测，给出步骤）\n"
                "## 检查清单（至少 1 份，可直接复用）\n"
                "## 常见坑与对策\n"
                "## 可用于丰富《AI 辅助软件产品》的写作点（对应章节/段落建议）\n"
                "Constraints: avoid fabricating exact numbers/citations; if unsure, mark '待核验'.\n"
                "Keep the total length compact (aim ~800-1500 Chinese characters, excluding checklists).\n"
            )

            stdin = "\n".join(
                [
                    "## Existing note (for alignment)",
                    note_md.strip(),
                    "",
                    "## Source snapshot (for grounding)",
                    snapshot_md.strip(),
                    "",
                ]
            )

            print(f"[{i}/{len(note_paths)}] {note_path.name} -> {out_path}")
            body = _run_gemini(stdin, prompt, model=model, timeout_s=args.timeout)

            category_name = taxonomy_categories.get(category_id, {}).get("name", category_id)
            chapters_str = ", ".join(chapter_targets) if chapter_targets else ""
            note_link = _rel_link(out_path.parent, note_path)
            snapshot_link = _rel_link(out_path.parent, project_dir / src.snapshot_rel)
            header_lines = [
                f"# Deep Research: {title}",
                "",
                f"- Source: {url}",
                f"- Note: {note_link}",
                f"- Snapshot: {snapshot_link}",
                f"- Category: {category_name} ({category_id})",
                f"- Chapters: {chapters_str}",
                "",
            ]
            out_path.write_text("\n".join(header_lines) + body, encoding="utf-8")

            if args.sleep_ms > 0:
                time.sleep(args.sleep_ms / 1000)
    else:
        allowed_category_ids = {c.strip() for c in (args.category_id or []) if c.strip()}
        allowed_chapter_ids = {c.strip() for c in (args.chapter_id or []) if c.strip()}

        picked: list[tuple[str, dict[str, Any]]] = []
        for url, label in labels.items():
            if url_allow is not None and url not in url_allow:
                continue
            if allowed_category_ids:
                cid = str(label.get("category_id") or "").strip()
                if cid not in allowed_category_ids:
                    continue
            if allowed_chapter_ids:
                raw_chapters = label.get("chapter_targets")
                chs: list[str] = []
                if isinstance(raw_chapters, list):
                    chs = [str(x).strip() for x in raw_chapters if str(x).strip()]
                if not any(ch in allowed_chapter_ids for ch in chs):
                    continue
            score_total: float | None = None
            try:
                if "score_total" in label:
                    score_total = float(label["score_total"])
            except Exception:
                score_total = None
            if args.min_score_total and args.min_score_total > 0:
                if score_total is None or score_total < float(args.min_score_total):
                    continue
            picked.append((url, label))

        def sort_key(item: tuple[str, dict[str, Any]]) -> tuple[float, str]:
            url, label = item
            try:
                score = float(label.get("score_total") or 0.0)
            except Exception:
                score = 0.0
            return (-score, url)

        picked.sort(key=sort_key)
        if args.max_items and args.max_items > 0:
            picked = picked[: int(args.max_items)]

        for i, (url, label) in enumerate(picked, start=1):
            src = sources.get(url)
            if not src:
                continue
            snapshot_path = sources_index.parent / src.snapshot_rel
            if not snapshot_path.exists():
                continue
            snapshot_md = snapshot_path.read_text(encoding="utf-8", errors="replace")
            if args.max_chars and args.max_chars > 0 and len(snapshot_md) > args.max_chars:
                snapshot_md = snapshot_md[: args.max_chars].rstrip() + "\n\n[TRUNCATED]\n"

            title = (
                str(label.get("title") or "").strip()
                or src.title
                or _extract_first_heading(snapshot_md)
                or Path(src.snapshot_rel).stem
            )
            stem = Path(src.snapshot_rel).stem
            out_path = out_base / f"src-{stem}.md"
            out_rel = _rel_link(index_out.parent, out_path)

            category_id = str(label.get("category_id") or "").strip() or DEFAULT_CATEGORY_ID
            if taxonomy_categories and category_id not in taxonomy_categories:
                category_id = DEFAULT_CATEGORY_ID
            chapter_targets: list[str] = []
            raw_chapters = label.get("chapter_targets")
            if isinstance(raw_chapters, list):
                for x in raw_chapters:
                    s = str(x).strip()
                    if not s:
                        continue
                    if chapter_ids and s not in chapter_ids:
                        continue
                    chapter_targets.append(s)
            chapter_targets = _normalize_chapter_targets(category_id, chapter_targets, chapter_ids)

            score_total: float | None = None
            try:
                if "score_total" in label:
                    score_total = float(label["score_total"])
            except Exception:
                score_total = None

            generated.append((category_id, title, out_rel, score_total, chapter_targets))

            if out_path.exists() and not args.force:
                continue

            prompt = (
                f"Explain {title} with deep research for a Chinese technical book project.\n"
                f"RESOURCE_URL: {url}\n"
                f"SNAPSHOT_FILE: {src.snapshot_rel}\n"
                f"LABELS_JSON: {json.dumps(label, ensure_ascii=False)}\n\n"
                "Write Markdown ONLY (no code fences). Use Chinese. Structure:\n"
                "## TL;DR (1-2 sentences)\n"
                "## 核心观点（5-10 条，尽量说人话）\n"
                "## 可落地做法（面向产品/工程/评测，给出可执行步骤）\n"
                "## 检查清单（至少 1 份，可直接复用）\n"
                "## 常见坑与对策\n"
                "## 可用于丰富《AI 辅助软件产品》的写作点（对应章节/段落建议）\n"
                "Constraints: avoid fabricating exact numbers/citations; if unsure, mark '待核验'.\n"
                "Length: aim ~1000-1800 Chinese characters, excluding checklists.\n"
            )

            stdin = "\n".join(
                [
                    "## Labels (metadata only)",
                    json.dumps(label, ensure_ascii=False, indent=2).strip(),
                    "",
                    "## Source snapshot (for grounding)",
                    snapshot_md.strip(),
                    "",
                ]
            )

            print(f"[{i}/{len(picked)}] {url} -> {out_path}")
            body = _run_gemini(stdin, prompt, model=model, timeout_s=args.timeout)

            category_name = taxonomy_categories.get(category_id, {}).get("name", category_id)
            chapters_str = ", ".join(chapter_targets) if chapter_targets else ""
            snapshot_link = _rel_link(out_path.parent, project_dir / src.snapshot_rel)
            header_lines = [
                f"# Deep Research: {title}",
                "",
                f"- Source: {url}",
                f"- Snapshot: {snapshot_link}",
                f"- Category: {category_name} ({category_id})",
                f"- Chapters: {chapters_str}",
                "",
            ]
            out_path.write_text("\n".join(header_lines) + body, encoding="utf-8")

            if args.sleep_ms > 0:
                time.sleep(args.sleep_ms / 1000)

    index_out.parent.mkdir(parents=True, exist_ok=True)
    _render_deepresearch_index(
        index_out,
        generated,
        chapters=chapters,
        taxonomy_categories=taxonomy_categories,
    )
    print(f"Wrote: {index_out} (items={len(generated)})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
