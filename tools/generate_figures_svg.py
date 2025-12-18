#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    w: int
    h: int
    title: str
    subtitle: str = ""


class Svg:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.parts: list[str] = []

    def header(self) -> None:
        self.parts.append(
            "\n".join(
                [
                    '<?xml version="1.0" encoding="UTF-8"?>',
                    f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">',
                    "<style>",
                    "  .bg { fill: #0b1220; }",
                    "  .card { fill: #0f1b34; stroke: #2b3a61; stroke-width: 2; rx: 14; }",
                    "  .card2 { fill: #0f233d; stroke: #2b3a61; stroke-width: 2; rx: 14; }",
                    "  .title { font: 700 18px ui-sans-serif, system-ui, -apple-system; fill: #e8eefc; }",
                    "  .sub { font: 500 13px ui-sans-serif, system-ui, -apple-system; fill: #b7c6ea; }",
                    "  .small { font: 500 12px ui-sans-serif, system-ui, -apple-system; fill: #b7c6ea; }",
                    "  .note { font: 500 12px ui-sans-serif, system-ui, -apple-system; fill: #9fb2de; }",
                    "  .arrow { stroke: #6aa1ff; stroke-width: 3; fill: none; marker-end: url(#arrowhead); }",
                    "  .arrow2 { stroke: #6dd6a8; stroke-width: 3; fill: none; marker-end: url(#arrowhead2); }",
                    "  .dash { stroke-dasharray: 7 6; }",
                    "</style>",
                    "<defs>",
                    '<marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">',
                    '<polygon points="0 0, 10 3.5, 0 7" fill="#6aa1ff"/>',
                    "</marker>",
                    '<marker id="arrowhead2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">',
                    '<polygon points="0 0, 10 3.5, 0 7" fill="#6dd6a8"/>',
                    "</marker>",
                    "</defs>",
                    f'<rect class="bg" x="0" y="0" width="{self.width}" height="{self.height}" />',
                ]
            )
        )

    def footer(self) -> None:
        self.parts.append("</svg>")

    def box(self, b: Box, variant: int = 1) -> None:
        cls = "card" if variant == 1 else "card2"
        self.parts.append(f'<rect class="{cls}" x="{b.x}" y="{b.y}" width="{b.w}" height="{b.h}" rx="14" />')
        self.parts.append(f'<text class="title" x="{b.x+16}" y="{b.y+30}">{_esc(b.title)}</text>')
        if b.subtitle:
            self.parts.append(f'<text class="sub" x="{b.x+16}" y="{b.y+54}">{_esc(b.subtitle)}</text>')

    def arrow(self, x1: int, y1: int, x2: int, y2: int, kind: int = 1, dashed: bool = False) -> None:
        cls = "arrow" if kind == 1 else "arrow2"
        if dashed:
            cls += " dash"
        self.parts.append(f'<path class="{cls}" d="M{x1} {y1} L{x2} {y2}" />')

    def text(self, x: int, y: int, s: str, cls: str = "note") -> None:
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}">{_esc(s)}</text>')

    def render(self) -> str:
        return "\n".join(self.parts) + "\n"


def _esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def fig_tokens() -> str:
    svg = Svg(1200, 420)
    svg.header()
    svg.text(24, 40, "Design Tokens → 出码 → 约束 AI 生成（最小闭环）", cls="title")

    b1 = Box(60, 90, 260, 110, "Tokens (JSON)", "唯一事实源 / 版本化")
    b2 = Box(360, 90, 280, 110, "出码", "CSS Variables / 多端产物")
    b3 = Box(680, 90, 260, 110, "UI 组件", "只引用 Token，不写魔法值")
    b4 = Box(60, 240, 880, 130, "门禁与回归", "Token 变更 → a11y/Lighthouse/视觉回归 → 退化即阻断")

    svg.box(b1, 1)
    svg.box(b2, 2)
    svg.box(b3, 1)
    svg.box(b4, 2)

    svg.arrow(320, 145, 360, 145)
    svg.arrow(640, 145, 680, 145)
    svg.arrow(210, 200, 210, 240, kind=2)
    svg.arrow(800, 200, 800, 240, kind=2)

    svg.text(360, 215, "脚本：docs/examples/ui/design_tokens_to_css.py", cls="small")
    svg.footer()
    return svg.render()


def fig_inference() -> str:
    svg = Svg(1200, 520)
    svg.header()
    svg.text(24, 40, "推理优化的可控闭环：预算 → 缓存/并发 → 降级 → 证据留档", cls="title")

    b1 = Box(60, 90, 260, 110, "请求入口", "trace_id / user_id / 版本")
    b2 = Box(360, 90, 280, 110, "预算与队列", "timeout / 并发上限")
    b3 = Box(680, 90, 420, 110, "推理后端", "vLLM / TensorRT-LLM / TGI")

    b4 = Box(60, 250, 420, 120, "缓存与复用", "prompt/检索/工具结果缓存")
    b5 = Box(520, 250, 580, 120, "降级与回退", "缩短上下文 / 关工具 / 切低成本路径")
    b6 = Box(60, 410, 1040, 80, "观测与门禁", "延迟/成本/错误率越界 → 阻断/回滚；回归集更新")

    for b in (b1, b2, b3, b4, b5, b6):
        svg.box(b, 1 if b in (b1, b3, b4) else 2)

    svg.arrow(320, 145, 360, 145)
    svg.arrow(640, 145, 680, 145)
    svg.arrow(500, 200, 500, 250, kind=2)
    svg.arrow(820, 200, 820, 250, kind=2)
    svg.arrow(260, 370, 260, 410, kind=2)
    svg.arrow(820, 370, 820, 410, kind=2)

    svg.text(62, 505, "可运行示例：docs/examples/inference/budgeted_gateway.py", cls="small")
    svg.footer()
    return svg.render()


def fig_observability() -> str:
    svg = Svg(1200, 480)
    svg.header()
    svg.text(24, 40, "观测性三件套（Logs / Metrics / Traces）如何服务“灰度与回滚”", cls="title")

    b1 = Box(80, 90, 320, 110, "Logs", "结构化事件：谁/做了什么/为什么失败")
    b2 = Box(440, 90, 320, 110, "Metrics", "守门指标：P95/成本/错误率")
    b3 = Box(800, 90, 320, 110, "Traces", "把一次请求串成一条链路")
    b4 = Box(80, 250, 1040, 170, "发布决策", "灰度观察窗口 → 指标越界 → 降级/限流/回滚 → 失败样本回写回归集")

    svg.box(b1, 1)
    svg.box(b2, 2)
    svg.box(b3, 1)
    svg.box(b4, 2)

    svg.arrow(240, 200, 240, 250, kind=2)
    svg.arrow(600, 200, 600, 250, kind=2)
    svg.arrow(960, 200, 960, 250, kind=2)
    svg.text(84, 455, "建议：把 trace_id 写进日志与响应头，形成可追溯闭环", cls="small")
    svg.footer()
    return svg.render()


def fig_judge() -> str:
    svg = Svg(1200, 520)
    svg.header()
    svg.text(24, 40, "LLM-as-a-Judge 回归门禁：成对比较 + 交换位置去偏", cls="title")

    b1 = Box(70, 90, 340, 110, "测试集（JSONL）", "prompt + A/B 输出")
    b2 = Box(450, 90, 320, 110, "Judge (A,B)", "输出 A/B/Tie + 理由")
    b3 = Box(820, 90, 320, 110, "Judge (B,A)", "交换顺序再评一次")
    b4 = Box(70, 250, 1070, 150, "聚合与裁决", "两次一致才计胜负；不一致 → Tie/丢弃；输出报告并入门禁")
    b5 = Box(70, 420, 1070, 70, "失败样本回流", "把低分/分歧样本写入回归集，形成复利")

    svg.box(b1, 1)
    svg.box(b2, 2)
    svg.box(b3, 2)
    svg.box(b4, 1)
    svg.box(b5, 2)

    svg.arrow(410, 145, 450, 145)
    svg.arrow(770, 145, 820, 145)
    svg.arrow(610, 200, 610, 250, kind=2)
    svg.arrow(610, 400, 610, 420, kind=2)

    svg.text(72, 505, "可运行示例：docs/examples/evaluation/judge_pairwise.py", cls="small")
    svg.footer()
    return svg.render()


def fig_engineering_gates() -> str:
    svg = Svg(1200, 520)
    svg.header()
    svg.text(24, 40, "工程化闭环：门禁 → 证据 → 灰度 → 观测 → 回滚", cls="title")

    b1 = Box(70, 90, 340, 110, "变更输入", "AI 输出 → 小步补丁")
    b2 = Box(450, 90, 320, 110, "自动门禁", "回归/安全/成本阈值")
    b3 = Box(820, 90, 320, 110, "人工审查", "只看高风险点")
    b4 = Box(70, 250, 520, 130, "灰度发布", "小流量观察窗口；不达标就停")
    b5 = Box(630, 250, 510, 130, "观测与处置", "四线指标；降级/限流/回滚")
    b6 = Box(70, 410, 1070, 80, "证据留档与复利", "报告/失败样本入回归集；下次更稳")

    svg.box(b1, 1)
    svg.box(b2, 2)
    svg.box(b3, 1)
    svg.box(b4, 2)
    svg.box(b5, 1)
    svg.box(b6, 2)

    svg.arrow(410, 145, 450, 145)
    svg.arrow(770, 145, 820, 145)
    svg.arrow(980, 200, 980, 250, kind=2)
    svg.arrow(330, 200, 330, 250, kind=2)
    svg.arrow(600, 315, 630, 315)
    svg.arrow(600, 380, 600, 410, kind=2)

    svg.text(74, 505, "建议：把门禁做成一条命令（例如 tools/run_quality_gates.py）", cls="small")
    svg.footer()
    return svg.render()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate lightweight SVG figures (no external deps).")
    parser.add_argument("--out-dir", default="docs/assets", help="Output directory (default: docs/assets)")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    figures = {
        "figure_06_2_tokens_pipeline.svg": fig_tokens(),
        "figure_16_2_inference_control_loop.svg": fig_inference(),
        "figure_17_2_observability_stack.svg": fig_observability(),
        "figure_18_2_judge_regression_loop.svg": fig_judge(),
        "figure_07_2_engineering_gates.svg": fig_engineering_gates(),
    }
    for name, svg in figures.items():
        path = out_dir / name
        path.write_text(svg, encoding="utf-8")
        print(f"Wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
