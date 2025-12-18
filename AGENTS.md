# Repository Guidelines

This repository is a MkDocs Material–based “digital bookshelf” where the primary source is Markdown under `docs/` and the output is a static site.

## Project Structure & Module Organization

- `docs/`: content source (Markdown).
  - `docs/books/`: long-form book content (one folder per book).
  - `docs/materials/`: curated research pool and generated indexes/notes.
  - `docs/assets/`: images and other static assets referenced by pages.
  - `docs/styles/`: CSS overrides (e.g. `docs/styles/overrides.css`).
- `mkdocs.yml`: site configuration + navigation (`nav`).
- `tools/`: Python utilities for materials ingestion/indexing/citation checks.
- `skills/`: small helper scripts (e.g. image generation).
- `site/`: generated build output (do not edit; ignored by Git).

## Build, Test, and Development Commands

Typical local setup:

- `python3 -m venv .venv && source .venv/bin/activate`: create/activate virtualenv.
- `python3 -m pip install -U pip && python3 -m pip install -r requirements.txt`: install dependencies.
- `mkdocs serve`: run local dev server at `http://127.0.0.1:8000`.
- `mkdocs build --strict`: “release-style” build; fails on broken links/config.
- `python3 tools/check_citations.py`: verify `[n]` citations exist in `references.md`.

## Coding Style & Naming Conventions

- Markdown: prefer relative links with explicit `.md` (MkDocs rewrites on build).
- Filenames: use `kebab-case.md`; avoid renames after publishing (URLs are path-based).
- Assets: place images in `docs/assets/` and reference via relative paths.
- Python scripts: target `python3`, 4-space indentation, keep changes minimal and readable.

## Testing Guidelines

There is no dedicated unit test suite. Treat these as required checks before merging:

- `mkdocs build --strict`
- `python3 tools/check_citations.py` (when editing book chapters/references)

## Commit & Pull Request Guidelines

- Commits commonly follow a Conventional-Commits-like pattern: `docs: ...`, `docs(materials): ...`, `feat: ...`, `chore(materials): ...`.
- PRs should include: a short summary, impacted paths (e.g. `docs/books/...`), and screenshots/links for visual changes when applicable.
- Keep generated artifacts out of PRs (do not commit `site/`).

## Security & Configuration Tips

- Copy `.env.example` to `.env` for local tooling (e.g. Gemini cookies) and never commit `.env`.
