#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, quote_plus, unquote, urlparse
from html import unescape


@dataclass(frozen=True)
class SearchResult:
    title: str
    url: str


_DDG_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _strip_html_tags(s: str) -> str:
    return re.sub(r"<[^>]*?>", "", s)


def _decode_ddg_href(raw_href: str) -> str:
    href = unescape(raw_href)
    if href.startswith("//"):
        href = "https:" + href
    if href.startswith("/l/?") or "duckduckgo.com/l/?" in href:
        parsed = urlparse(("https://duckduckgo.com" + href) if href.startswith("/l/?") else href)
        qs = parse_qs(parsed.query)
        uddg = qs.get("uddg", [""])[0]
        if uddg:
            return unquote(unescape(uddg))
    return href


def _ddg_search(query: str, max_results: int) -> list[SearchResult]:
    url = f"https://duckduckgo.com/html/?q={quote_plus(query)}"
    proc = subprocess.run(
        ["curl", "-sSL", "-A", _DDG_UA, url],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"curl search failed (code={proc.returncode}): {proc.stderr.strip()}")
    html = proc.stdout

    results: list[SearchResult] = []
    for match in re.finditer(
        r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        html,
        flags=re.I | re.S,
    ):
        raw_href = match.group(1)
        raw_title = match.group(2)
        title = _strip_html_tags(unescape(raw_title)).strip()
        link = _decode_ddg_href(raw_href).strip()
        if not title or not link:
            continue
        results.append(SearchResult(title=title, url=link))
        if len(results) >= max_results:
            break
    return results


def _render_sources_md(results: list[SearchResult]) -> str:
    if not results:
        return "- （无）"
    return "\n".join(f"- {r.title} — {r.url}" for r in results)


def _extract_json_from_gemini_stdout(text: str) -> dict:
    decoder = json.JSONDecoder()
    best: dict | None = None

    for match in re.finditer(r"\{", text):
        candidate = text[match.start() :].lstrip()
        try:
            obj, _end = decoder.raw_decode(candidate)
        except Exception:
            continue
        if isinstance(obj, dict) and "response" in obj:
            best = obj

    if best is not None:
        return best

    start = text.find("{")
    if start == -1:
        raise ValueError("gemini output did not contain JSON")
    candidate = text[start:].lstrip()
    obj, _end = decoder.raw_decode(candidate)
    if not isinstance(obj, dict):
        raise ValueError("gemini JSON payload was not an object")
    return obj


def _run_gemini(prompt: str, model: str) -> str:
    cmd = [
        "gemini",
        "--output-format",
        "json",
        "--allowed-tools",
        "read_file",
        "--model",
        model,
        prompt,
    ]
    proc = subprocess.run(
        cmd,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env={**os.environ, "NO_COLOR": "1"},
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gemini failed (code={proc.returncode}). Output:\n{proc.stdout}")
    payload = _extract_json_from_gemini_stdout(proc.stdout)
    response = payload.get("response")
    if not isinstance(response, str) or not response.strip():
        raise RuntimeError(f"gemini returned empty response. Raw:\n{proc.stdout}")
    return response.strip() + "\n"


def _chapter_query_from_file(path: Path) -> str:
    try:
        first_line = path.read_text(encoding="utf-8").splitlines()[0].strip()
    except Exception:
        first_line = ""
    if first_line.startswith("#"):
        first_line = first_line.lstrip("#").strip()
    base = path.stem.replace("-", " ")
    return f"{first_line or base} AI 产品开发 实战 方法论 最佳实践"


def generate_one(in_path: Path, out_path: Path, model: str, max_results: int, sleep_s: float) -> None:
    query = _chapter_query_from_file(in_path)
    sources = _ddg_search(query, max_results=max_results)
    sources_md = _render_sources_md(sources)

    prompt = f"""你是一位顶尖的中文非虚构作者与产品技术合伙人。请把“章节草稿/讲义风格”的内容改写成可直接出版的“书籍版章节”。

任务
- 读取文件：{in_path.as_posix()}
- 输出为一个完整的 Markdown 章节（只输出正文，不要前后说明）。

写作要求
1) 保留原文件的标题与小节层级（# / ## / ###），但把要点扩写成连贯段落（每个 ## 小节至少 2 段）。
2) 叙事要有节奏：开头用 1–2 段建立问题与张力；中段给方法、例子与反例；结尾给清单与行动建议。
3) 每章至少包含：2 个具体案例（可信、细节具体，可虚构但要现实），1 个失败/反例故事（说明代价与教训），1 组“读者练习”（3–5 条可执行任务）。
4) 允许保留必要的清单/表格/模板，但避免整章都是 bullet；优先用段落解释“为什么/怎么做/做错会怎样”。
5) 不要编造你没有依据的事实或数据；不要虚构引用或论文。若需要外部视角，只能使用我提供的“延伸阅读”链接，并把它们集中放在章末“延伸阅读”小节中（Markdown 链接列表）。
6) 避免使用“写作元结构”做标题或小节名，例如“X层思考 / 第1层 / 读者目标 / 论证链条 / 落地与验收”；如果需要结构，请把结构隐入段落，用自然过渡词（先/再/同时/最后）完成。
7) 不要把整章包在 ``` 代码块里；不要说“我将要/我已经读取文件”；不要输出与正文无关的提示。

延伸阅读（仅可使用以下链接；不要新增）
{sources_md}
"""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(_run_gemini(prompt=prompt, model=model), encoding="utf-8")
    if sleep_s > 0:
        time.sleep(sleep_s)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate book-edition chapters via gemini + one DDG search per chapter.")
    parser.add_argument("--in-root", default=".", help="Repo root (default: .)")
    parser.add_argument("--out-dir", required=True, help="Output directory (relative to in-root)")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Gemini model to use (default: gemini-2.5-flash)")
    parser.add_argument("--max-results", type=int, default=8, help="DDG results per chapter (default: 8)")
    parser.add_argument("--sleep-s", type=float, default=0.5, help="Sleep between chapters (default: 0.5)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs")
    parser.add_argument("files", nargs="+", help="Input markdown files (relative to in-root)")
    args = parser.parse_args()

    in_root = Path(args.in_root).resolve()
    out_dir = (in_root / args.out_dir).resolve()

    for rel in args.files:
        in_path = (in_root / rel).resolve()
        if not in_path.exists():
            print(f"ERROR: missing input: {rel}", file=sys.stderr)
            return 2
        out_path = out_dir / in_path.name
        if out_path.exists() and not args.overwrite:
            print(f"skip (exists): {out_path.relative_to(in_root)}")
            continue
        print(f"generate: {out_path.relative_to(in_root)}")
        try:
            generate_one(
                in_path=in_path,
                out_path=out_path,
                model=args.model,
                max_results=args.max_results,
                sleep_s=args.sleep_s,
            )
        except Exception as e:
            print(f"ERROR generating {rel}: {e}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
