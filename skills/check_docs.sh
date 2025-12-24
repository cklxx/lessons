#!/usr/bin/env bash
set -euo pipefail

python3 tools/check_citations.py
python3 -m mkdocs build --strict

