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
    category: str
    one_liner: str
    summary: str
    key_points: list[str]
    tags: list[str]
    scores: dict[str, float]
    score_total: float
    score_reason: str
    snapshot_path: str
    note_path: str | None


CATEGORIES: list[str] = [
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


def _normalize_entry(obj: dict[str, Any], snapshot_path: str, note_path: str | None) -> ScoredEntry:
    scores = obj.get("scores", {}) or {}
    parsed_scores: dict[str, float] = {}
    for k in SCORE_WEIGHTS:
        try:
            parsed_scores[k] = float(scores.get(k, 0.0))
        except Exception:
            parsed_scores[k] = 0.0
    score_total = _weighted_total(parsed_scores)

    category = str(obj.get("category") or "General References").strip()
    if category not in CATEGORIES:
        category = "General References"

    def _list_str(key: str) -> list[str]:
        raw = obj.get(key, [])
        if isinstance(raw, list):
            return [str(x).strip() for x in raw if str(x).strip()]
        return []

    title = str(obj.get("title") or "").strip() or Path(snapshot_path).stem
    url = str(obj.get("url") or "").strip()
    one_liner = str(obj.get("one_liner") or "").strip()
    summary = str(obj.get("summary") or "").strip()
    score_reason = str(obj.get("score_reason") or obj.get("why") or "").strip()

    return ScoredEntry(
        title=title,
        url=url,
        category=category,
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


def _render_indexes_md(entries: list[ScoredEntry], out_path: Path) -> None:
    grouped: dict[str, list[ScoredEntry]] = {c: [] for c in CATEGORIES}
    for e in entries:
        grouped.setdefault(e.category, []).append(e)
    for cat in list(grouped.keys()):
        grouped[cat].sort(key=lambda x: x.score_total, reverse=True)

    lines: list[str] = []
    lines.append("# Indexes: AI-Assisted Software Product / Materials")
    lines.append("")
    lines.append("> 本页由 `gemini -p \"Explain …\"` 生成，用于给资料做标签、分类与排序。")
    lines.append("")
    lines.append("## Scoring")
    lines.append("")
    lines.append("维度（0–10）：Relevance / Authority / Recency / Depth / Actionability。")
    lines.append("加权总分：`0.35·R + 0.20·A + 0.15·Re + 0.15·D + 0.15·Ac`（范围 0–10）。")
    lines.append("")
    lines.append(f"共 {len(entries)} 篇。按分类分组；组内按总分降序。")
    lines.append("")

    for cat in CATEGORIES:
        items = grouped.get(cat) or []
        if not items:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        lines.append(
            "| # | Score | Title | Tags | Notes | Source | Score breakdown |"
        )
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for idx, e in enumerate(items, start=1):
            title_link = f"[{e.title}]({Path(e.snapshot_path).as_posix()})"
            note_link = f"[note]({Path(e.note_path).as_posix()})" if e.note_path else ""
            tags = ", ".join(e.tags[:10])
            breakdown = (
                f"R {e.scores['relevance']:.1f} / "
                f"A {e.scores['authority']:.1f} / "
                f"Re {e.scores['recency']:.1f} / "
                f"D {e.scores['depth']:.1f} / "
                f"Ac {e.scores['actionability']:.1f}"
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(idx),
                        f"{e.score_total:.2f}",
                        title_link,
                        tags,
                        note_link,
                        f"[link]({e.url})",
                        breakdown,
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
    return parser


def main() -> int:
    args = build_parser().parse_args()
    sources_index = Path(args.sources_index)
    if not sources_index.exists():
        raise SystemExit(f"Missing sources index: {sources_index}")

    sources_dir = sources_index.parent
    project_dir = sources_dir.parent  # docs/materials/ai-assisted-software-product

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

    existing: set[str] = set()
    if args.resume and out_jsonl.exists():
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
        "title, url, category, one_liner, summary, key_points, tags, scores, score_reason. "
        f"category MUST be one of: {', '.join(CATEGORIES)}. "
        "scores MUST be numbers 0-10 for keys: relevance, authority, recency, depth, actionability. "
        "Write one_liner/summary/key_points/tags/score_reason in Chinese. Keep summary <= 120 Chinese characters. "
        "title MUST exactly match RESOURCE_TITLE, and url MUST exactly match RESOURCE_URL."
    )

    model = args.model.strip() or None
    written = 0
    with out_jsonl.open("a", encoding="utf-8") as f:
        for i, src in enumerate(sources, start=1):
            url = str(src.get("url") or "").strip()
            if args.resume and url in existing:
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
        parsed.append(_normalize_entry(obj, snapshot_path=snapshot_path, note_path=note_path))

    out_md = Path(args.out_md)
    _render_indexes_md(parsed, out_md)
    print(f"Wrote: {out_md} (entries={len(parsed)})")
    print(f"Wrote: {out_jsonl} (+{written} lines appended)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
