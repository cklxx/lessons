#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _flatten_tokens(obj: Any, prefix: str = "") -> dict[str, str]:
    out: dict[str, str] = {}
    if isinstance(obj, dict):
        if "$value" in obj:
            out[prefix.rstrip(".")] = str(obj["$value"])
            return out
        for k, v in obj.items():
            if k.startswith("$"):
                continue
            child_prefix = f"{prefix}{k}."
            out.update(_flatten_tokens(v, child_prefix))
    return out


def _to_css_var(name: str) -> str:
    # token path -> --token-path
    return "--" + name.replace(".", "-")

def _to_css_value(raw: str) -> str:
    v = raw.strip()
    # DTCG-style alias: "{color.blue.600}" -> "var(--color-blue-600)"
    if v.startswith("{") and v.endswith("}") and len(v) > 2:
        inner = v[1:-1].strip().strip(".")
        if inner:
            return f"var({_to_css_var(inner)})"
    return raw


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Design Tokens JSON to CSS variables.")
    parser.add_argument("--in", dest="in_path", required=True)
    parser.add_argument("--out", dest="out_path", required=True)
    args = parser.parse_args()

    src = Path(args.in_path)
    data = json.loads(src.read_text(encoding="utf-8"))
    flat = _flatten_tokens(data)

    lines: list[str] = []
    lines.append("/* Generated from Design Tokens JSON */")
    lines.append(":root {")
    for k in sorted(flat.keys()):
        lines.append(f"  {_to_css_var(k)}: {_to_css_value(flat[k])};")
    lines.append("}")
    lines.append("")

    out = Path(args.out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
