#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


_CITATION_BRACKET_RE = re.compile(r"\[(\d+)\]")
_FENCE_START_RE = re.compile(r"^\s*([`~]{3,})")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _discover_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(p for p in path.rglob("*.md") if p.is_file()))
        else:
            files.append(path)
    return sorted(dict.fromkeys(files))


def _guardrails(text: str, *, allow_bracket_digits: bool) -> list[str]:
    errors: list[str] = []
    if not allow_bracket_digits and _CITATION_BRACKET_RE.search(text):
        errors.append("Found bracket-only numeric citation like [12]. This repo's citation checker may treat it as a missing reference.")
    if "TODO" in text:
        errors.append("Found TODO in output.")
    text_for_ellipsis_check = text.replace("<...>", "")
    if "..." in text_for_ellipsis_check or "……" in text_for_ellipsis_check:
        errors.append("Found ellipsis (... or …… ) in output.")
    return errors


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


def _extract_numeric_citations(markdown: str) -> set[int]:
    cleaned: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    for raw_line in markdown.splitlines(keepends=True):
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
    return {int(m.group(1)) for m in _CITATION_BRACKET_RE.finditer(text)}


def _run_gemini(*, model: str, prompt: str, stdin_text: str) -> str:
    cmd = ["gemini", "-m", model, "-p", prompt, "-o", "text"]
    try:
        proc = subprocess.run(
            cmd,
            input=stdin_text,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise SystemExit("Missing `gemini` CLI in PATH.") from exc

    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise SystemExit(f"gemini failed (exit={proc.returncode}).\n{stderr}")

    return proc.stdout


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gemini_md",
        description="Rewrite/enrich Markdown via Gemini CLI with guardrails.",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Markdown file(s) or directory(ies). Directories are scanned recursively for *.md.",
    )
    parser.add_argument(
        "--model",
        default="gemini-3-pro-preview",
        help="Gemini model name (default: gemini-3-pro-preview).",
    )
    parser.add_argument(
        "--prompt-file",
        default="",
        help="Path to a prompt instruction file. If omitted, reads prompt from --prompt.",
    )
    parser.add_argument(
        "--prompt",
        default="",
        help="Prompt instruction text appended after stdin (original Markdown).",
    )
    parser.add_argument(
        "--out-dir",
        default="",
        help="Write outputs to this directory, preserving relative paths.",
    )
    parser.add_argument(
        "--suffix",
        default=".gemini.md",
        help="When writing to --out-dir, append this suffix to filenames (default: .gemini.md).",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite input files in place (runs guardrails; writes only when passing).",
    )
    parser.add_argument(
        "--allow-bracket-digits",
        action="store_true",
        help="Allow bracket-only digits like [12] in output (useful when editing books that intentionally use numbered citations).",
    )
    parser.add_argument(
        "--no-new-citations",
        action="store_true",
        help="When citations like [12] are allowed, ensure Gemini does not introduce new numeric citations not present in the original file.",
    )
    parser.add_argument(
        "--no-guardrails",
        action="store_true",
        help="Disable output guardrails checks.",
    )
    return parser


def _load_prompt(args: argparse.Namespace) -> str:
    prompt = args.prompt.strip()
    if args.prompt_file:
        prompt_path = Path(args.prompt_file).expanduser()
        prompt = _read_text(prompt_path).strip()
    if not prompt:
        raise SystemExit("Missing prompt instructions. Provide --prompt-file or --prompt.")
    return prompt


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    prompt = _load_prompt(args)
    inputs = _discover_markdown_files([Path(p).expanduser() for p in args.paths])
    repo_root = Path(__file__).resolve().parent.parent

    out_dir = Path(args.out_dir).expanduser() if args.out_dir else None
    if len(inputs) > 1 and not (out_dir or args.in_place):
        raise SystemExit("Multiple inputs require --out-dir or --in-place.")

    for path in inputs:
        if not path.exists():
            raise SystemExit(f"Input not found: {path}")

        original = _read_text(path)
        original_citations = _extract_numeric_citations(original) if args.no_new_citations else set()
        output = _run_gemini(model=args.model, prompt=prompt, stdin_text=original)

        if not args.no_guardrails:
            problems = _guardrails(output, allow_bracket_digits=args.allow_bracket_digits)
            if problems:
                joined = "\n".join(f"- {p}" for p in problems)
                raise SystemExit(f"Guardrails failed for {path}:\n{joined}")

        if args.no_new_citations:
            output_citations = _extract_numeric_citations(output)
            added = sorted(n for n in output_citations if n not in original_citations)
            if added:
                joined = ", ".join(f"[{n}]" for n in added)
                raise SystemExit(f"Guardrails failed for {path}:\n- Introduced new numeric citations not present in original: {joined}")

        if args.in_place:
            path.write_text(output, encoding="utf-8")
            continue

        if out_dir:
            rel = path
            try:
                rel = path.relative_to(repo_root)
            except Exception:
                rel = Path(path.name)
            target = out_dir / rel
            target = target.with_name(f"{target.stem}{args.suffix}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(output, encoding="utf-8")
            continue

        sys.stdout.write(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
