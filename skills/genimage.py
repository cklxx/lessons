#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    script_dir: Path
    repo_root: Path
    docs_dir: Path


def _resolve_paths() -> Paths:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    docs_dir = repo_root / "docs"
    return Paths(script_dir=script_dir, repo_root=repo_root, docs_dir=docs_dir)


def _load_env_file(env_path: Path) -> bool:
    if not env_path.exists():
        return False

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ and value != "":
            os.environ[key] = value
    return True


def _slugify(value: str, max_len: int = 48) -> str:
    value = value.strip().lower()
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value[:max_len].strip("-")


def _pick_output_dir(base: Path, name: str) -> Path:
    base.mkdir(parents=True, exist_ok=True)
    candidate = base / name
    if not candidate.exists():
        return candidate
    for i in range(1, 1000):
        suffixed = base / f"{name}-{i:03d}"
        if not suffixed.exists():
            return suffixed
    raise RuntimeError(f"Output directory already exists too many times under: {base}")


def _require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(
            f"Missing env var `{name}`.\n\n"
            "Set cookies via environment variables or a `.env` file.\n"
            "Example:\n"
            f"  export {name}='...'\n"
        )
    return value


def _read_cookie_env() -> tuple[str, str]:
    secure_1psid = (os.getenv("Secure_1PSID") or os.getenv("SECURE_1PSID") or "").strip()
    if not secure_1psid:
        _require_env("Secure_1PSID")
    secure_1psidts = (os.getenv("Secure_1PSIDTS") or os.getenv("SECURE_1PSIDTS") or "").strip()
    return secure_1psid, secure_1psidts


async def _maybe_close(client) -> None:
    close_fn = getattr(client, "close", None)
    if close_fn is None:
        return
    result = close_fn()
    if asyncio.iscoroutine(result):
        await result


def _md_link_for_image(image_path: Path, md_from: str | None, md_prefix: str | None, docs_dir: Path) -> str:
    link_path: Path = image_path
    if md_from:
        md_from_path = Path(md_from).expanduser()
        if not md_from_path.is_absolute():
            md_from_path = (Path.cwd() / md_from_path).resolve()
        md_dir = md_from_path.parent
        link_path = Path(os.path.relpath(image_path, md_dir))
    else:
        try:
            link_path = image_path.relative_to(docs_dir)
        except Exception:
            link_path = image_path

    link = str(link_path).replace(os.sep, "/")
    if md_prefix:
        link = f"{md_prefix.rstrip('/')}/{link.lstrip('/')}"
    return link


async def run(args: argparse.Namespace) -> int:
    paths = _resolve_paths()

    loaded = False
    if args.env:
        loaded = _load_env_file(Path(args.env).expanduser())
    else:
        loaded = _load_env_file(paths.repo_root / ".env") or _load_env_file(Path.cwd() / ".env")

    secure_1psid, secure_1psidts = _read_cookie_env()

    if args.dry_run:
        present = []
        for name in ("Secure_1PSID", "Secure_1PSIDTS", "SECURE_1PSID", "SECURE_1PSIDTS"):
            if os.getenv(name, "") != "":
                present.append(name)
        print("Dry run OK.")
        print(f"- Loaded .env: {bool(loaded)}")
        print(f"- Cookie env present: {', '.join(present) if present else 'none'}")
        _ = secure_1psid  # validated via _read_cookie_env()
        return 0

    try:
        from gemini_webapi import GeminiClient
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "Missing dependency `gemini-webapi`.\n"
            "Install:\n"
            "  pip install gemini-webapi\n"
        ) from exc

    output_base = Path(args.out).expanduser()
    if not output_base.is_absolute():
        output_base = (paths.repo_root / output_base).resolve()

    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    default_name = f"img-{now}"
    name = args.name or _slugify(args.prompt) or default_name
    output_dir = _pick_output_dir(output_base, name)
    output_dir.mkdir(parents=True, exist_ok=True)

    prompt = args.prompt.strip()
    if args.style:
        prompt = f"{prompt}\n\nStyle requirements:\n{args.style.strip()}\n"

    client = GeminiClient(secure_1psid, secure_1psidts, proxy=args.proxy)
    await client.init(
        timeout=args.timeout,
        auto_close=False,
        close_delay=args.close_delay,
        auto_refresh=True,
    )

    try:
        response = await client.generate_content(prompt)
        images = list(getattr(response, "images", []) or [])
        if not images:
            print("No images returned. Try adjusting the prompt.")
            return 2

        max_images = args.max_images if args.max_images > 0 else len(images)
        images = images[:max_images]

        saved: list[Path] = []
        for i, image in enumerate(images):
            filename = f"{args.prefix}{i}.png"
            target = output_dir / filename
            if target.exists() and not args.overwrite:
                raise SystemExit(
                    f"Refusing to overwrite existing file: {target}\n"
                    "Re-run with `--overwrite` or change `--name/--prefix`."
                )
            await image.save(path=str(output_dir), filename=filename, verbose=args.verbose)
            saved.append(target)

        print(f"Saved {len(saved)} image(s) to: {output_dir}")

        if args.print_md:
            alt = (args.alt or name).strip()
            for path in saved:
                link = _md_link_for_image(path, args.md_from, args.md_prefix, paths.docs_dir)
                print(f"![{alt}]({link})")

        return 0
    finally:
        await _maybe_close(client)


def build_parser() -> argparse.ArgumentParser:
    paths = _resolve_paths()
    default_out = paths.docs_dir / "assets" / "skills" / "generated"

    parser = argparse.ArgumentParser(
        prog="genimage",
        description="Generate article insertion images via Gemini WebAPI and save them under docs/assets.",
    )
    parser.add_argument("--prompt", required=True, help="Image generation prompt (text).")
    parser.add_argument("--style", default="", help="Extra style constraints appended to prompt (optional).")
    parser.add_argument(
        "--out",
        default=str(default_out),
        help=f"Output base directory (default: {default_out}).",
    )
    parser.add_argument("--name", default="", help="Output subfolder name (defaults to a slug of prompt or timestamp).")
    parser.add_argument("--prefix", default="img_", help="Filename prefix inside the output subfolder (default: img_).")
    parser.add_argument(
        "--max-images",
        type=int,
        default=4,
        help="Max images to save from the response (default: 4). Use 0 to save all.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting existing files with the same name.")
    parser.add_argument("--print-md", action="store_true", help="Print Markdown image snippets for the saved files.")
    parser.add_argument("--alt", default="", help="Alt text for printed Markdown (default: output folder name).")
    parser.add_argument(
        "--md-from",
        default="",
        help="Compute Markdown links relative to this Markdown file path (recommended).",
    )
    parser.add_argument("--md-prefix", default="", help="Prefix to prepend to Markdown paths (optional), e.g. ../")
    parser.add_argument("--env", default="", help="Path to .env file (default: repo-root .env or current dir .env).")
    parser.add_argument("--proxy", default=None, help="Proxy for GeminiClient, e.g. http://127.0.0.1:7890")
    parser.add_argument("--timeout", type=int, default=30, help="Client init timeout seconds (default: 30).")
    parser.add_argument(
        "--close-delay",
        type=int,
        default=300,
        help="Auto-close delay seconds used by the client (default: 300).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Only validate env loading; do not call Gemini.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if not args.md_from:
        args.md_from = None
    if not args.md_prefix:
        args.md_prefix = None
    raise SystemExit(asyncio.run(run(args)))


if __name__ == "__main__":
    main()
