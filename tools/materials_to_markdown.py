#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from urllib.parse import urljoin

import requests

try:
    import html2text  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: html2text. Install with: pip install html2text\n"
        f"Original error: {exc}"
    )


SourceType = Literal["html", "pdf", "github_readme", "unknown"]

FRAGMENT_DEST_RE = re.compile(r"\]\(#[^)]*\)")


@dataclass(frozen=True)
class SnapshotResult:
    url: str
    ok: bool
    status: int | None
    source_type: SourceType
    title: str | None
    out_path: Path | None
    error: str | None
    elapsed_ms: int
    extra: dict[str, str]


def _extract_urls(text: str) -> list[str]:
    urls = re.findall(r'https?://[^\s)>"\']+', text)
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


def _slugify(url: str, max_len: int = 64) -> str:
    value = url.strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = re.sub(r"[?#].*$", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    if not value:
        return "resource"
    return value[:max_len].strip("-")


def _hash12(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]


def _is_github_repo(url: str) -> tuple[str, str] | None:
    match = re.match(r"^https?://github\.com/([^/]+)/([^/#?]+)(?:/)?$", url)
    if not match:
        return None
    owner, repo = match.group(1), match.group(2)
    return owner, repo


def _is_arxiv_abs(url: str) -> str | None:
    match = re.match(r"^https?://arxiv\.org/abs/([^/#?]+)$", url)
    if not match:
        return None
    return match.group(1)


def _html_to_markdown(html: str) -> str:
    cleaned = re.sub(r"(?is)<script[^>]*>.*?</script>", "", html)
    cleaned = re.sub(r"(?is)<style[^>]*>.*?</style>", "", cleaned)
    cleaned = re.sub(r"(?is)<noscript[^>]*>.*?</noscript>", "", cleaned)

    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_images = True
    converter.ignore_emphasis = False
    converter.ignore_links = False
    converter.skip_internal_links = False
    converter.single_line_break = True
    return converter.handle(cleaned).strip() + "\n"


def _sanitize_generated_markdown(md: str) -> str:
    # Generated snapshots may contain many same-page fragment links (`#...`), but HTML→Markdown
    # conversion does not guarantee those anchors survive. Strip fragment destinations to keep
    # mkdocs strict builds clean.
    md = FRAGMENT_DEST_RE.sub("]", md)
    # Drop empty labels that may remain after stripping destinations.
    md = re.sub(r"\[\s*\]", "", md)
    return md


def _extract_html_title(html: str) -> str | None:
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", html)
    if not match:
        return None
    title = re.sub(r"\s+", " ", match.group(1)).strip()
    return title or None


def _is_relative_link(target: str) -> bool:
    t = target.strip()
    if not t:
        return False
    if t.startswith("#"):
        return False
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", t):
        return False
    return True


def _rewrite_markdown_links(md: str, map_target) -> str:
    def repl_inline(match: re.Match[str]) -> str:
        before = match.group(1)
        target = match.group(2)
        after = match.group(3) or ""
        if _is_relative_link(target):
            target = map_target(target)
        return f"{before}{target}{after})"

    # Inline links/images: ](target "title") or ](target)
    md = re.sub(r"(\]\()([^\s)]+)(\s+\"[^\"]*\")?\)", repl_inline, md)

    def repl_ref(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        rest = match.group(3) or ""
        if _is_relative_link(target):
            target = map_target(target)
        return f"[{label}]: {target}{rest}"

    # Reference definitions: [id]: target "title"
    md = re.sub(r"(?m)^\[([^\]]+)\]:\s+(\S+)(.*)$", repl_ref, md)
    return md


def _absolutize_links_for_html(md: str, base_url: str) -> str:
    def map_target(target: str) -> str:
        return urljoin(base_url, target)

    return _rewrite_markdown_links(md, map_target)


def _github_default_branch(owner: str, repo: str, timeout_s: int, user_agent: str) -> str:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"User-Agent": user_agent, "Accept": "application/vnd.github+json"}
    resp = requests.get(url, headers=headers, timeout=timeout_s)
    if resp.status_code != 200:
        return "main"
    try:
        payload = resp.json()
    except Exception:
        return "main"
    branch = str(payload.get("default_branch") or "").strip()
    return branch or "main"


def _absolutize_links_for_github_readme(md: str, owner: str, repo: str, branch: str) -> str:
    def map_target(target: str) -> str:
        t = target.strip()
        frag = ""
        if "#" in t:
            t, frag = t.split("#", 1)
            frag = "#" + frag
        t = t.lstrip("./")
        t = t.lstrip("/")
        return f"https://github.com/{owner}/{repo}/blob/{branch}/{t}{frag}"

    return _rewrite_markdown_links(md, map_target)


def _fetch_github_readme(owner: str, repo: str, timeout_s: int, user_agent: str) -> tuple[str, str | None]:
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {
        "User-Agent": user_agent,
        "Accept": "application/vnd.github.raw",
    }
    resp = requests.get(url, headers=headers, timeout=timeout_s)
    if resp.status_code != 200:
        raise RuntimeError(f"GitHub README fetch failed: {resp.status_code}")
    content_type = resp.headers.get("content-type", "")
    if "text/" not in content_type and "application/octet-stream" not in content_type:
        # Still return; GitHub often replies with text/plain for raw.
        pass
    text = resp.text
    # Try to infer a title from the first heading.
    title: str | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip() or None
            break
    return text, title


def _pdftotext(pdf_bytes: bytes) -> str:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        pdf_path = tmp / "doc.pdf"
        txt_path = tmp / "doc.txt"
        pdf_path.write_bytes(pdf_bytes)
        subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), str(txt_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return txt_path.read_text(encoding="utf-8", errors="replace")


def _snapshot_url(url: str, out_dir: Path, timeout_s: int, user_agent: str) -> SnapshotResult:
    start = time.time()
    out_path: Path | None = None
    status: int | None = None
    error: str | None = None
    ok = False
    title: str | None = None
    source_type: SourceType = "unknown"
    extra: dict[str, str] = {}

    try:
        repo_info = _is_github_repo(url)
        if repo_info:
            owner, repo = repo_info
            source_type = "github_readme"
            readme, title = _fetch_github_readme(owner, repo, timeout_s, user_agent)
            branch = _github_default_branch(owner, repo, timeout_s=timeout_s, user_agent=user_agent)
            readme = _absolutize_links_for_github_readme(readme, owner=owner, repo=repo, branch=branch)
            slug = _slugify(url)
            out_path = out_dir / f"{slug}-{_hash12(url)}.md"
            out_path.write_text(
                "\n".join(
                    [
                        f"# {title or slug}",
                        "",
                        f"- URL: {url}",
                        f"- Retrieved: {dt.datetime.now(dt.UTC).isoformat()}",
                        "- Source: GitHub README (via API)",
                        "",
                        "----",
                        "",
                        readme.rstrip(),
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            ok = True
            status = 200
            return SnapshotResult(
                url=url,
                ok=ok,
                status=status,
                source_type=source_type,
                title=title,
                out_path=out_path,
                error=None,
                elapsed_ms=int((time.time() - start) * 1000),
                extra=extra,
            )

        arxiv_id = _is_arxiv_abs(url)
        if arxiv_id:
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            extra["pdf_url"] = pdf_url

            headers = {"User-Agent": user_agent}
            abs_resp = requests.get(url, headers=headers, timeout=timeout_s)
            status = abs_resp.status_code
            abs_resp.raise_for_status()
            abs_html = abs_resp.text
            abs_title = _extract_html_title(abs_html)
            title = abs_title

            pdf_resp = requests.get(pdf_url, headers=headers, timeout=timeout_s)
            pdf_resp.raise_for_status()
            pdf_text = _pdftotext(pdf_resp.content)

            source_type = "pdf"
            slug = _slugify(url)
            out_path = out_dir / f"{slug}-{_hash12(url)}.md"
            md = "\n".join(
                [
                    f"# {title or slug}",
                    "",
                    f"- URL: {url}",
                    f"- PDF: {pdf_url}",
                    f"- Retrieved: {dt.datetime.now(dt.UTC).isoformat()}",
                    "",
                    "## Abstract page (HTML → Markdown)",
                    "",
                    _html_to_markdown(abs_html).rstrip(),
                    "",
                    "## Full text (PDF → text)",
                    "",
                    "```text",
                    pdf_text.rstrip(),
                    "```",
                    "",
                ]
            )
            out_path.write_text(md, encoding="utf-8")
            ok = True
            status = 200
            return SnapshotResult(
                url=url,
                ok=ok,
                status=status,
                source_type=source_type,
                title=title,
                out_path=out_path,
                error=None,
                elapsed_ms=int((time.time() - start) * 1000),
                extra=extra,
            )

        headers = {"User-Agent": user_agent}
        resp = requests.get(url, headers=headers, timeout=timeout_s)
        status = resp.status_code
        resp.raise_for_status()

        content_type = resp.headers.get("content-type", "").lower()
        if "application/pdf" in content_type or url.lower().endswith(".pdf"):
            source_type = "pdf"
            pdf_text = _pdftotext(resp.content)
            title = url
            md = "\n".join(
                [
                    f"# {url}",
                    "",
                    f"- URL: {url}",
                    f"- Retrieved: {dt.datetime.now(dt.UTC).isoformat()}",
                    "",
                    "```text",
                    pdf_text.rstrip(),
                    "```",
                    "",
                ]
            )
        else:
            source_type = "html"
            html = resp.text
            title = _extract_html_title(html)
            body_md = _absolutize_links_for_html(_html_to_markdown(html).rstrip(), base_url=url)
            md = "\n".join(
                [
                    f"# {title or url}",
                    "",
                    f"- URL: {url}",
                    f"- Retrieved: {dt.datetime.now(dt.UTC).isoformat()}",
                    "",
                    body_md,
                    "",
                ]
            )

        slug = _slugify(url)
        out_path = out_dir / f"{slug}-{_hash12(url)}.md"
        out_path.write_text(_sanitize_generated_markdown(md), encoding="utf-8")
        ok = True
    except subprocess.CalledProcessError:
        error = "pdftotext failed"
    except requests.RequestException as exc:
        error = f"{type(exc).__name__}: {exc}"
    except Exception as exc:  # pragma: no cover
        error = repr(exc)

    elapsed_ms = int((time.time() - start) * 1000)
    return SnapshotResult(
        url=url,
        ok=ok,
        status=status,
        source_type=source_type,
        title=title,
        out_path=out_path if ok else None,
        error=error,
        elapsed_ms=elapsed_ms,
        extra=extra,
    )


def _read_cached_snapshot(path: Path) -> tuple[SourceType, str | None]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return "unknown", None

    title: str | None = None
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip() or None
            break

    if "Source: GitHub README" in text:
        return "github_readme", title
    if re.search(r"(?m)^- PDF:\\s+https?://", text):
        return "pdf", title
    return "html", title


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="materials_to_markdown",
        description="Extract URLs from docs/materials markdown and snapshot them as Markdown files.",
    )
    parser.add_argument(
        "--root",
        default="docs/materials",
        help="Root directory to scan for Markdown files.",
    )
    parser.add_argument(
        "--out",
        default="docs/materials/ai-assisted-software-product/sources/md",
        help="Output directory for generated Markdown snapshots (committable).",
    )
    parser.add_argument(
        "--include-raw",
        action="store_true",
        help='Include "raw/" markdown files (WARNING: may be very large, e.g. link indexes).',
    )
    parser.add_argument(
        "--include-sources",
        action="store_true",
        help='Include already-generated "sources/" markdown snapshots (usually not desired).',
    )
    parser.add_argument(
        "--include-gemini",
        action="store_true",
        help='Include already-generated "gemini/" outputs (usually not desired).',
    )
    parser.add_argument(
        "--include-indexes",
        action="store_true",
        help='Include generated indexes markdown files (e.g. indexes.md). Usually not desired for URL discovery.',
    )
    parser.add_argument(
        "--include-deepresearch",
        action="store_true",
        help='Include generated deepresearch markdown files. Usually not desired for URL discovery.',
    )
    parser.add_argument("--timeout", type=int, default=30, help="Per-request timeout in seconds.")
    parser.add_argument(
        "--user-agent",
        default="lessons-material-snapshots/1.0",
        help="User-Agent header used for HTTP requests.",
    )
    parser.add_argument("--sleep-ms", type=int, default=150, help="Sleep between requests (ms).")
    parser.add_argument("--max", type=int, default=0, help="Max URLs to snapshot (0 = no limit).")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-download even if a cached snapshot file already exists.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Only print extracted URLs; do not fetch.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root not found: {root}")

    md_files = sorted(root.rglob("*.md"))
    excluded_parts: set[str] = set()
    if not args.include_raw:
        excluded_parts.add("raw")
    if not args.include_sources:
        excluded_parts.add("sources")
    if not args.include_gemini:
        excluded_parts.add("gemini")
    if not args.include_deepresearch:
        excluded_parts.add("deepresearch")
    if excluded_parts:
        md_files = [p for p in md_files if not any(part in excluded_parts for part in p.parts)]
    if not args.include_indexes:
        md_files = [p for p in md_files if p.name != "indexes.md"]

    urls: list[str] = []
    for path in md_files:
        urls.extend(_extract_urls(path.read_text(encoding="utf-8", errors="replace")))

    seen: set[str] = set()
    deduped: list[str] = []
    for url in urls:
        if url in seen:
            continue
        seen.add(url)
        deduped.append(url)

    if args.max and args.max > 0:
        deduped = deduped[: args.max]

    if args.dry_run:
        print("\n".join(deduped))
        return 0

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[SnapshotResult] = []
    for i, url in enumerate(deduped, start=1):
        slug = _slugify(url)
        cached_path = out_dir / f"{slug}-{_hash12(url)}.md"
        if not args.force and cached_path.exists():
            source_type, title = _read_cached_snapshot(cached_path)
            print(f"[{i}/{len(deduped)}] {url} (cached)")
            results.append(
                SnapshotResult(
                    url=url,
                    ok=True,
                    status=200,
                    source_type=source_type,
                    title=title,
                    out_path=cached_path,
                    error=None,
                    elapsed_ms=0,
                    extra={},
                )
            )
        else:
            print(f"[{i}/{len(deduped)}] {url}")
            results.append(_snapshot_url(url, out_dir, args.timeout, args.user_agent))
        if args.sleep_ms > 0:
            time.sleep(args.sleep_ms / 1000)

    ok = sum(1 for r in results if r.ok)
    failed = len(results) - ok
    print(f"\nDone. ok={ok} failed={failed} out={out_dir}")

    index_path = out_dir.parent / "index.jsonl"
    with index_path.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(
                json.dumps(
                    {
                        "url": r.url,
                        "ok": r.ok,
                        "status": r.status,
                        "source_type": r.source_type,
                        "title": r.title,
                        "path": str(r.out_path.relative_to(out_dir.parent)) if r.out_path else None,
                        "error": r.error,
                        "elapsed_ms": r.elapsed_ms,
                        "extra": r.extra,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    print(f"Wrote: {index_path}")

    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
