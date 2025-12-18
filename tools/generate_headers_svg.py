#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class HeaderSpec:
    filename: str
    a: str
    b: str
    accent: str


SPECS: list[HeaderSpec] = [
    HeaderSpec("chapter_16_header.svg", "#0b1020", "#2a4b8d", "#7ee2ff"),
    HeaderSpec("chapter_17_header.svg", "#0b1020", "#2a7a62", "#b7ffb0"),
    HeaderSpec("chapter_18_header.svg", "#0b1020", "#6a2a8d", "#ffd38a"),
    HeaderSpec("chapter_19_header.svg", "#0b1020", "#8d5a2a", "#ffe08a"),
    HeaderSpec("chapter_20_header.svg", "#0b1020", "#8d2a3c", "#ffd1dc"),
    HeaderSpec("conclusion_header.svg", "#0b1020", "#1f3a63", "#b7c9ff"),
]


def _hash_to_unit(seed: str) -> float:
    h = hashlib.sha256(seed.encode("utf-8")).digest()
    n = int.from_bytes(h[:8], "big")
    return (n % 10_000) / 10_000.0


def render_svg(spec: HeaderSpec) -> str:
    # Header canvas: wide banner suitable for MkDocs title image.
    w, h = 1600, 420
    u = _hash_to_unit(spec.filename)
    shift = int(90 + 140 * u)
    circle_x = int(1100 + 320 * u)
    circle_y = int(120 + 90 * (1 - u))

    wave_top = 240 + int(40 * u)
    wave_mid = 290 + int(60 * (1 - u))
    wave_bot = 330 + int(55 * u)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{spec.a}"/>
      <stop offset="100%" stop-color="{spec.b}"/>
    </linearGradient>
    <radialGradient id="glow" cx="70%" cy="25%" r="70%">
      <stop offset="0%" stop-color="{spec.accent}" stop-opacity="0.45"/>
      <stop offset="60%" stop-color="{spec.accent}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{spec.accent}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="wave" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{spec.accent}" stop-opacity="0.14"/>
      <stop offset="55%" stop-color="{spec.accent}" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="{spec.accent}" stop-opacity="0.18"/>
    </linearGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14"/>
    </filter>
  </defs>

  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#glow)"/>

  <circle cx="{circle_x}" cy="{circle_y}" r="{190 + shift // 6}" fill="{spec.accent}" opacity="0.08" filter="url(#soft)"/>
  <circle cx="{circle_x - 260}" cy="{circle_y + 120}" r="{130 + shift // 10}" fill="{spec.accent}" opacity="0.06" filter="url(#soft)"/>

  <path d="M 0 {wave_top} C {320 + shift} {wave_top - 90}, {780 + shift} {wave_top + 110}, {w} {wave_top - 10} L {w} {h} L 0 {h} Z"
        fill="url(#wave)"/>
  <path d="M 0 {wave_mid} C {280 + shift} {wave_mid - 70}, {820 + shift} {wave_mid + 120}, {w} {wave_mid - 10}"
        fill="none" stroke="{spec.accent}" stroke-opacity="0.22" stroke-width="3"/>
  <path d="M 0 {wave_bot} C {260 + shift} {wave_bot - 50}, {900 + shift} {wave_bot + 100}, {w} {wave_bot - 10}"
        fill="none" stroke="{spec.accent}" stroke-opacity="0.14" stroke-width="2"/>
</svg>
"""


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / "docs" / "assets"
    out_dir.mkdir(parents=True, exist_ok=True)

    for spec in SPECS:
        (out_dir / spec.filename).write_text(render_svg(spec), encoding="utf-8")
        print(f"Wrote {out_dir / spec.filename}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

