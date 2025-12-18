#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ScoredEntry:
    title: str
    url: str
    category_id: str
    category: str
    chapter_targets: list[str]
    one_liner: str
    summary: str
    key_points: list[str]
    tags: list[str]
    scores: dict[str, float]
    score_total: float
    score_reason: str
    snapshot_path: str
    note_path: str | None


DEFAULT_CATEGORIES: list[str] = [
    "Discovery & Product Strategy",
    "Prototyping & UX",
    "Engineering & Tooling",
    "Data, RAG, and Agents",
    "Deployment, MLOps, and Evaluation",
    "Governance & Ethics",
    "General References",
]

SCORE_WEIGHTS: dict[str, float] = {
    "relevance": 0.35,
    "authority": 0.20,
    "recency": 0.15,
    "depth": 0.15,
    "actionability": 0.15,
}

CATEGORY_CHAPTER_HINTS: dict[str, list[str]] = {
    # Product / requirements / UX
    "product_discovery": ["02-discovery", "05-validation", "19-iteration", "01-method"],
    "prd_spec": ["03-prd", "07-engineering", "09-backend", "10-intelligence"],
    "ux_ui": ["04-prototype", "06-ui", "08-frontend", "05-validation"],
    # Engineering / backend / ops
    "engineering": ["07-engineering", "08-frontend", "09-backend", "17-deployment"],
    "backend": ["09-backend", "07-engineering", "17-deployment", "18-evaluation"],
    # Intelligence layer
    "rag": ["10-intelligence", "18-evaluation", "13-data", "07-engineering"],
    "agents": ["10-intelligence", "07-engineering", "18-evaluation", "01-method"],
    # Data / training / inference
    "data": ["13-data", "18-evaluation", "10-intelligence", "20-governance"],
    "training": ["14-pretrain", "15-posttrain", "18-evaluation", "13-data"],
    "inference": ["16-inference", "17-deployment", "18-evaluation", "07-engineering"],
    # Ops / evaluation / governance
    "ops": ["17-deployment", "18-evaluation", "07-engineering", "20-governance"],
    "evaluation": ["18-evaluation", "17-deployment", "10-intelligence", "07-engineering"],
    "user_auth": ["11-user", "20-governance", "07-engineering", "09-backend"],
    "billing": ["12-billing", "19-iteration", "20-governance", "09-backend"],
    "governance": ["20-governance", "11-user", "12-billing", "13-data"],
    "general": ["01-method"],
}


def _clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def _weighted_total(scores: dict[str, float]) -> float:
    total = 0.0
    for k, w in SCORE_WEIGHTS.items():
        total += _clamp(float(scores.get(k, 0.0)), 0.0, 10.0) * w
    return round(total, 2)


def _find_json_object(text: str) -> dict[str, Any]:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Gemini output did not contain a JSON object")
    payload = text[start : end + 1]
    return json.loads(payload)


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
    return proc.stdout.strip()


def _load_taxonomy(path: Path) -> tuple[dict[str, dict[str, str]], list[dict[str, str]]]:
    """
    Returns (category_by_id, chapters).
    category_by_id maps category_id -> {name, description}.
    chapters is a list of {id, title}.
    """
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


def _extract_note_url_map(notes_dir: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in sorted(notes_dir.glob("ref-*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"原始来源：\s*(https?://\S+)", text)
        if not match:
            continue
        url = match.group(1).rstrip(".,;]")
        mapping[url] = path.as_posix()
    return mapping


def _normalize_entry(
    obj: dict[str, Any],
    snapshot_path: str,
    note_path: str | None,
    taxonomy_categories: dict[str, dict[str, str]],
    chapter_ids: set[str],
) -> ScoredEntry:
    scores = obj.get("scores", {}) or {}
    parsed_scores: dict[str, float] = {}
    for k in SCORE_WEIGHTS:
        try:
            parsed_scores[k] = float(scores.get(k, 0.0))
        except Exception:
            parsed_scores[k] = 0.0
    score_total = _weighted_total(parsed_scores)

    category_id = str(obj.get("category_id") or "").strip()
    category_name = str(obj.get("category") or "").strip()
    if taxonomy_categories:
        if category_id not in taxonomy_categories:
            category_id = "general"
        category_name = taxonomy_categories.get(category_id, {}).get("name", "General References")
    else:
        # Backward-compatible fallback to old coarse categories.
        if category_name not in DEFAULT_CATEGORIES:
            category_name = "General References"
        category_id = category_name

    def _list_str(key: str) -> list[str]:
        raw = obj.get(key, [])
        if isinstance(raw, list):
            return [str(x).strip() for x in raw if str(x).strip()]
        return []

    chapter_targets: list[str] = []
    raw_chapters = obj.get("chapter_targets")
    if isinstance(raw_chapters, list):
        for x in raw_chapters:
            s = str(x).strip()
            if not s:
                continue
            if chapter_ids and s not in chapter_ids:
                continue
            chapter_targets.append(s)
    # Normalize chapter targets: ensure relevance and avoid cross-category pollution.
    if taxonomy_categories and chapter_ids:
        allowed = CATEGORY_CHAPTER_HINTS.get(category_id, ["01-method"])
        allowed_ordered = [c for c in allowed if c in chapter_ids]
        allowed_set = set(allowed_ordered)
        if allowed_ordered:
            chapter_targets = [c for c in chapter_targets if c in allowed_set]
            if not chapter_targets:
                chapter_targets = allowed_ordered[:]
            # Ensure the primary target is included and is first.
            primary = allowed_ordered[0] if allowed_ordered else None
            if primary and primary not in chapter_targets:
                chapter_targets.insert(0, primary)
            # De-dupe while preserving order and cap length.
            seen: set[str] = set()
            deduped: list[str] = []
            for c in chapter_targets:
                if c in seen:
                    continue
                seen.add(c)
                deduped.append(c)
            chapter_targets = deduped
            # Prefer to include additional relevant chapters from hints when we still have room.
            for c in allowed_ordered:
                if len(chapter_targets) >= 4:
                    break
                if c not in chapter_targets:
                    chapter_targets.append(c)
            chapter_targets = chapter_targets[:4]
    else:
        chapter_targets = chapter_targets[:4]

    title = str(obj.get("title") or "").strip() or Path(snapshot_path).stem
    url = str(obj.get("url") or "").strip()
    one_liner = str(obj.get("one_liner") or "").strip()
    summary = str(obj.get("summary") or "").strip()
    score_reason = str(obj.get("score_reason") or obj.get("why") or "").strip()

    return ScoredEntry(
        title=title,
        url=url,
        category_id=category_id,
        category=category_name,
        chapter_targets=chapter_targets,
        one_liner=one_liner,
        summary=summary,
        key_points=_list_str("key_points"),
        tags=_list_str("tags"),
        scores=parsed_scores,
        score_total=score_total,
        score_reason=score_reason,
        snapshot_path=snapshot_path,
        note_path=note_path,
    )


def _render_indexes_md(
    entries: list[ScoredEntry],
    out_path: Path,
    taxonomy_categories: dict[str, dict[str, str]],
    chapters: list[dict[str, str]],
) -> None:
    by_category: dict[str, list[ScoredEntry]] = {}
    for e in entries:
        by_category.setdefault(e.category_id, []).append(e)
    for k in list(by_category.keys()):
        by_category[k].sort(key=lambda x: x.score_total, reverse=True)

    by_chapter: dict[str, list[ScoredEntry]] = {}
    for e in entries:
        for chid in e.chapter_targets:
            by_chapter.setdefault(chid, []).append(e)
    for k in list(by_chapter.keys()):
        by_chapter[k].sort(key=lambda x: x.score_total, reverse=True)

    lines: list[str] = []
    lines.append("# Indexes: AI-Assisted Software Product / Materials")
    lines.append("")
    lines.append("> 本页由 `tools/gemini_build_material_indexes.py` 生成，用于给资料做标签、分类、按章节归档并排序。")
    lines.append("")
    lines.append("## Scoring")
    lines.append("")
    lines.append("维度（0–10）：Relevance / Authority / Recency / Depth / Actionability。")
    lines.append("加权总分：`0.35·R + 0.20·A + 0.15·Re + 0.15·D + 0.15·Ac`（范围 0–10）。")
    lines.append("")
    lines.append(f"共 {len(entries)} 篇。优先按“章节适配”分组；组内按总分降序。")
    lines.append("")

    if chapters:
        for ch in chapters:
            chid = ch["id"]
            items = by_chapter.get(chid) or []
            if not items:
                continue
            lines.append(f"## {ch['title']}（{chid}）")
            lines.append("")
            lines.append("| # | Score | Title | Category | Tags | Notes | Source |")
            lines.append("| --- | --- | --- | --- | --- | --- | --- |")
            for idx, e in enumerate(items, start=1):
                title_link = f"[{e.title}]({Path(e.snapshot_path).as_posix()})"
                note_link = f"[note]({Path(e.note_path).as_posix()})" if e.note_path else ""
                tags = ", ".join(e.tags[:8])
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            str(idx),
                            f"{e.score_total:.2f}",
                            title_link,
                            e.category,
                            tags,
                            note_link,
                            f"[link]({e.url})",
                        ]
                    )
                    + " |"
                )
            lines.append("")

    lines.append("## 按领域分类（补充视角）")
    lines.append("")
    for cid, meta in (taxonomy_categories or {}).items():
        items = by_category.get(cid) or []
        if not items:
            continue
        lines.append(f"### {meta['name']}（{cid}）")
        lines.append("")
        lines.append("| # | Score | Title | Chapters | Tags | Notes | Source |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for idx, e in enumerate(items, start=1):
            title_link = f"[{e.title}]({Path(e.snapshot_path).as_posix()})"
            note_link = f"[note]({Path(e.note_path).as_posix()})" if e.note_path else ""
            tags = ", ".join(e.tags[:8])
            chs = ", ".join(e.chapter_targets[:4])
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(idx),
                        f"{e.score_total:.2f}",
                        title_link,
                        chs,
                        tags,
                        note_link,
                        f"[link]({e.url})",
                    ]
                )
                + " |"
            )
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gemini_build_material_indexes",
        description="Use Gemini CLI to label + score downloaded material snapshots and build indexes.md.",
    )
    parser.add_argument(
        "--sources-index",
        default="docs/materials/ai-assisted-software-product/sources/index.jsonl",
        help="Input index.jsonl generated by tools/materials_to_markdown.py",
    )
    parser.add_argument(
        "--out-jsonl",
        default="docs/materials/ai-assisted-software-product/gemini/index.jsonl",
        help="Output JSONL with Gemini labels + scores.",
    )
    parser.add_argument(
        "--out-md",
        default="docs/materials/ai-assisted-software-product/indexes.md",
        help="Output Markdown indexes file.",
    )
    parser.add_argument(
        "--taxonomy",
        default="docs/materials/ai-assisted-software-product/taxonomy.json",
        help="Taxonomy JSON defining allowed categories and chapter ids.",
    )
    parser.add_argument(
        "--notes-dir",
        default="docs/materials/ai-assisted-software-product/notes",
        help="Directory containing per-reference notes (used to link URLs back to notes).",
    )
    parser.add_argument("--model", default="", help="Gemini model override (optional).")
    parser.add_argument("--timeout", type=int, default=180, help="Per-item Gemini timeout in seconds.")
    parser.add_argument(
        "--max-chars",
        type=int,
        default=60000,
        help="Max characters passed to Gemini per item (0 = no limit).",
    )
    parser.add_argument("--max", type=int, default=0, help="Max items to process (0 = no limit).")
    parser.add_argument("--sleep-ms", type=int, default=200, help="Sleep between Gemini calls (ms).")
    parser.add_argument("--resume", action="store_true", help="Skip URLs already present in out-jsonl.")
    parser.add_argument(
        "--rewrite",
        action="store_true",
        help="Rewrite out-jsonl from scratch (overwrites file, ignores --resume).",
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Skip Gemini calls; only render out-md from the existing out-jsonl.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    sources_index = Path(args.sources_index)
    if not sources_index.exists():
        raise SystemExit(f"Missing sources index: {sources_index}")

    sources_dir = sources_index.parent
    project_dir = sources_dir.parent  # docs/materials/ai-assisted-software-product

    taxonomy_categories, chapters = _load_taxonomy(Path(args.taxonomy))
    chapter_ids = {c["id"] for c in chapters}
    category_ids = sorted(taxonomy_categories.keys()) if taxonomy_categories else []
    chapter_desc = ", ".join([f"{c['id']}={c['title']}" for c in chapters]) if chapters else ""

    notes_dir = Path(args.notes_dir)
    note_map = _extract_note_url_map(notes_dir) if notes_dir.exists() else {}
    note_map_rel: dict[str, str] = {}
    for url, path_str in note_map.items():
        try:
            note_map_rel[url] = str(Path(path_str).relative_to(project_dir))
        except Exception:
            note_map_rel[url] = path_str

    out_jsonl = Path(args.out_jsonl)
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    if args.render_only:
        if not out_jsonl.exists():
            raise SystemExit(f"Missing out-jsonl for --render-only: {out_jsonl}")
        parsed: list[ScoredEntry] = []
        for line in out_jsonl.read_text(encoding="utf-8").splitlines():
            obj = json.loads(line)
            if obj.get("ok") is False:
                continue
            snapshot_path = str(obj.get("snapshot_path") or "")
            if not snapshot_path:
                continue
            note_path = obj.get("note_path")
            parsed.append(
                _normalize_entry(
                    obj,
                    snapshot_path=snapshot_path,
                    note_path=note_path,
                    taxonomy_categories=taxonomy_categories,
                    chapter_ids=chapter_ids,
                )
            )
        out_md = Path(args.out_md)
        _render_indexes_md(parsed, out_md, taxonomy_categories=taxonomy_categories, chapters=chapters)
        print(f"Wrote: {out_md} (entries={len(parsed)})")
        return 0

    existing: set[str] = set()
    if args.resume and not args.rewrite and out_jsonl.exists():
        for line in out_jsonl.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
            except Exception:
                continue
            url = str(obj.get("url") or "").strip()
            if url and obj.get("ok") is not False:
                existing.add(url)

    sources: list[dict[str, Any]] = []
    for line in sources_index.read_text(encoding="utf-8").splitlines():
        obj = json.loads(line)
        if not obj.get("ok"):
            continue
        sources.append(obj)

    if args.max and args.max > 0:
        sources = sources[: args.max]

    base_prompt = (
        "Explain the resource snapshot for a Chinese technical book project (AI-Assisted Software Product). "
        "Use ONLY the content from stdin; do not guess based on unrelated knowledge. "
        "Return ONLY a single JSON object (no markdown, no code fences) with keys: "
        "title, url, category_id, category, chapter_targets, one_liner, summary, key_points, tags, scores, score_reason. "
        f"category_id MUST be one of: {', '.join(category_ids) if category_ids else 'general'}. "
        "chapter_targets MUST be a JSON array of 1-4 items chosen from CHAPTER_IDS, matching the content's most likely usage chapters. "
        "scores MUST be numbers 0-10 for keys: relevance, authority, recency, depth, actionability. "
        "Write one_liner/summary/key_points/tags/score_reason in Chinese. Keep summary <= 140 Chinese characters. "
        "title MUST exactly match RESOURCE_TITLE, and url MUST exactly match RESOURCE_URL."
    )

    model = args.model.strip() or None
    written = 0
    mode = "w" if args.rewrite else "a"
    with out_jsonl.open(mode, encoding="utf-8") as f:
        for i, src in enumerate(sources, start=1):
            url = str(src.get("url") or "").strip()
            if args.resume and not args.rewrite and url in existing:
                continue

            snapshot_rel = src.get("path")
            if not snapshot_rel:
                continue

            snapshot_path = sources_dir / snapshot_rel
            if not snapshot_path.exists():
                continue

            content = snapshot_path.read_text(encoding="utf-8", errors="replace")
            if args.max_chars and args.max_chars > 0 and len(content) > args.max_chars:
                content = content[: args.max_chars].rstrip() + "\n\n[TRUNCATED]\n"

            snapshot_title = ""
            for line in content.splitlines():
                if line.startswith("# "):
                    snapshot_title = line[2:].strip()
                    break
            if not snapshot_title:
                snapshot_title = snapshot_path.stem

            prompt = (
                f"RESOURCE_URL: {url}\n"
                f"RESOURCE_TITLE: {snapshot_title}\n\n"
                f"CHAPTER_IDS: {', '.join(sorted(chapter_ids)) if chapter_ids else ''}\n"
                f"CHAPTERS: {chapter_desc}\n"
                + base_prompt
            )
            print(f"[{i}/{len(sources)}] {url}")
            try:
                output = _run_gemini(content, prompt, model=model, timeout_s=args.timeout)
                obj = _find_json_object(output)
                obj["ok"] = True
                obj["url"] = url
                obj["title"] = snapshot_title
                obj["snapshot_path"] = str(snapshot_path.relative_to(project_dir))
                note_path = note_map_rel.get(url)
                if note_path:
                    obj["note_path"] = note_path
                if taxonomy_categories:
                    cid = str(obj.get("category_id") or "").strip()
                    if cid not in taxonomy_categories:
                        obj["category_id"] = "general"
                    obj["category"] = taxonomy_categories.get(obj["category_id"], {}).get(
                        "name", "General References"
                    )
                scores = obj.get("scores", {}) or {}
                obj["score_total"] = _weighted_total(
                    {k: float(scores.get(k, 0.0) or 0.0) for k in SCORE_WEIGHTS}
                )
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
                written += 1
            except Exception as exc:
                err_obj = {
                    "url": url,
                    "ok": False,
                    "error": repr(exc),
                    "snapshot_path": str(snapshot_path.relative_to(project_dir)),
                }
                f.write(json.dumps(err_obj, ensure_ascii=False) + "\n")
                written += 1

            if args.sleep_ms > 0:
                time.sleep(args.sleep_ms / 1000)

    parsed: list[ScoredEntry] = []
    for line in out_jsonl.read_text(encoding="utf-8").splitlines():
        obj = json.loads(line)
        if obj.get("ok") is False:
            continue
        snapshot_path = str(obj.get("snapshot_path") or "")
        if not snapshot_path:
            continue
        note_path = obj.get("note_path")
        parsed.append(
            _normalize_entry(
                obj,
                snapshot_path=snapshot_path,
                note_path=note_path,
                taxonomy_categories=taxonomy_categories,
                chapter_ids=chapter_ids,
            )
        )

    out_md = Path(args.out_md)
    _render_indexes_md(parsed, out_md, taxonomy_categories=taxonomy_categories, chapters=chapters)
    print(f"Wrote: {out_md} (entries={len(parsed)})")
    suffix = f"(+{written} lines appended)" if mode == "a" else f"(rewrote, entries={len(parsed)})"
    print(f"Wrote: {out_jsonl} {suffix}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
