# 反馈、校对与迭代：把 Prompt 的失败变成回归资产

Prompt 最昂贵的代价不是“第一次写错”，而是“修完之后不知道什么时候会再坏”。如果不做回归，你每一次“优化”都像打地鼠：修了格式，丢了事实；加强约束，损了可用性；改了风格，系列崩盘。

本章把软件工程的回归测试引入 Prompt：每一次失败都要变成可复现样本、可自动化验收的门禁。

![章节插图占位：回归与发布门禁](../../assets/books/flawless-expression/chapter-hero.svg)

## 你将收获什么

- 一套静态评审清单：发给模型前先拦住低级错误（零成本）。
- 一个回归集目录结构：把 Prompt 当源码管理，版本可追踪、可回滚。
- 一个文本 Prompt 的 A/B 回归流程：修复目标问题，同时不引入退化。
- 一个图片 Prompt 的风格回归流程：系列一致性可检查，差异可控。
- 两个可复制脚本：批量跑测（Gemini CLI）+ 最小断言（JSON/关键字）。

## 1) Prompt 评审清单（静态）

在消耗 token 之前先做静态审查，能拦下大量“明明写错了却还在跑”的浪费。

| 维度 | 检查项 | 通过标准 |
| :--- | :--- | :--- |
| 结构 | 定界清晰 | 是否用标题/分隔符把“指令”和“数据”分开（避免混在一段话里） |
| 角色 | 身份明确 | 是否写清“你是谁”（审计工具/编辑/提取器），而不是只写“请做什么” |
| 约束 | 禁止项明确 | 是否把“不做什么”写成可检测规则（禁止寒暄语/禁止 Markdown 包裹 JSON） |
| 输出 | 协议固定 | 是否提供模板/Schema/列名，并声明顺序与字段不可变 |
| 兜底 | 未知出口 | 缺信息时是否允许拒答并输出缺口清单（而不是硬编） |
| 回滚 | 有退路 | 失败后怎么降级/回滚是否写清（重试一次/返回固定错误结构） |

## 2) 建立回归集：把失败固化下来

任何一次失败，都必须入库成为回归样本，否则你只是在“修一次”，不是“免疫一次”。

### 回归集结构（目录树）

```text
prompts/
├── production/
│   ├── prompt_a.v1.txt
│   └── prompt_b.v3.txt
└── regression/
    ├── case_001_chatty_json/
    │   ├── input.txt
    │   ├── prompt_base.txt
    │   ├── prompt_candidate.txt
    │   └── expected.json
    ├── case_002_missing_fields/
    │   ├── input.txt
    │   ├── prompt_base.txt
    │   ├── prompt_candidate.txt
    │   └── expected.md
    ├── case_003_image_no_text/
    │   ├── prompt_image.txt
    │   └── expected_rules.md
    ├── run_batch.sh
    └── check_results.py
```

说明：
- `expected.*` 是人工校对过的“验收真值”（可以是 JSON，也可以是 Markdown 规则）。
- 图片回归不追求像素级一致，而是追求规则一致（例如“不得出现文字/水印”）。

## 3) 文本 Prompt 的 A/B 回归流程

1. 基线：用 `prompt_base.txt` 跑一遍回归集，记录通过率与失败原因。
2. 变量控制：只改一件事（例如增加“禁止 Markdown 包裹 JSON”），保存为候选 Prompt。
3. 同集 A/B：用同一批 `input.txt` 跑候选 Prompt。
4. 裁决：
   - 目标 Case 是否修复？
   - 是否引入新退化（格式/事实/风格）？
5. 发布：修复成功且无退化才替换 `production/`。

## 4) 最小自动化脚本（可复制）

### 脚本 A：批量跑 Prompt（`run_batch.sh`）

```bash
#!/usr/bin/env bash
set -euo pipefail

MODEL="gemini-3-pro-preview"
PROMPT_FILE=${1:?usage: run_batch.sh <prompt_file> <cases_dir> <out_dir>}
CASES_DIR=${2:?usage: run_batch.sh <prompt_file> <cases_dir> <out_dir>}
OUT_DIR=${3:?usage: run_batch.sh <prompt_file> <cases_dir> <out_dir>}

mkdir -p "$OUT_DIR"

for case_dir in "$CASES_DIR"/*; do
  [ -d "$case_dir" ] || continue
  input="$case_dir/input.txt"
  [ -f "$input" ] || continue

  name=$(basename "$case_dir")
  query_file=$(mktemp)
  cat "$PROMPT_FILE" "$input" > "$query_file"

  echo "Running $name"
  gemini -m "$MODEL" -p "$(cat "$query_file")" > "$OUT_DIR/$name.out"

  rm -f "$query_file"
  sleep 1
done
```

### 脚本 B：最小断言（`check_results.py`）

这个脚本只做两类硬门禁：
- JSON 必须可解析（用于结构化输出）
- 输出不得包含禁用短语（用于“话痨输出”）

```python
import argparse
import json
from pathlib import Path

FORBIDDEN = [
    "好的，这是",
    "希望这对你有帮助",
    "Here is",
    "```json",
]

def looks_like_json(text: str) -> bool:
    text = text.strip()
    return text.startswith("{") or text.startswith("[")

def main(out_dir: Path) -> None:
    failed = 0
    for p in sorted(out_dir.glob("*.out")):
        content = p.read_text(encoding="utf-8", errors="replace")

        if any(x in content for x in FORBIDDEN):
            print(f"[FAIL] {p.name}: forbidden phrase found")
            failed += 1
            continue

        if looks_like_json(content):
            try:
                json.loads(content)
            except json.JSONDecodeError:
                print(f"[FAIL] {p.name}: invalid json")
                failed += 1
                continue

        print(f"[PASS] {p.name}")

    if failed:
        raise SystemExit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("out_dir")
    args = parser.parse_args()
    main(Path(args.out_dir))
```

## 5) 图片 Prompt 的风格回归流程（系列一致性）

图片回归更难，因为你既要控内容，也要控风格。推荐用“三件套”做回归：

1) 风格底座：所有 Prompt 共享的 style 段落（见 [05-medium.md](05-medium.md)）。
2) 负向约束：所有 Prompt 继承同一份 negative_prompt（至少包含 text/letters/numbers/watermark）。
3) 锚点主题：固定 3 个锚点主体（例如“服务器/盾牌/云”），每次改风格都用锚点跑一轮对比。

验收方式（不依赖具体生图工具）：
- 规则验收：Prompt 是否仍包含风格底座与负向约束？是否引入了会破坏风格的词（如 photorealistic/3d render）？
- 视觉验收：把锚点生成的图片平铺对比，线条粗细、色板、背景复杂度一致；若工具支持则锁 seed 以便归因。

### 配图提示词：反馈回路与门禁（无文字底图）

你要表达的是“闭环”，不是“流程图文学”。画一个环，环上有四个节点：写 Prompt、跑回归、评审、发布门禁。

```text
image_prompt:
flat 2D vector illustration, minimalist circular feedback loop with four abstract nodes connected by arrows, clean tech style,
blue and white palette, solid white background, high contrast, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 6) 常见陷阱（失败样本）

### 1) 只改措辞，不改规则

- 现象：输出仍然夹带解释文本，解析器仍然失败。
- 根因：你改了“请输出 JSON”的措辞，但没有写出硬约束与失败判定。
- 复现：同一 Prompt 多次运行，输出格式波动。
- 修复：把输出协议写成不可变模板；禁用短语写成断言；失败返回固定错误结构。
- 回归验证：`check_results.py` 全绿且稳定复跑。

### 2) 只修一次，不入回归

- 现象：同类错误在另一个 Prompt 或另一次改动里复发。
- 根因：没有把失败样本固化成回归 case；组织没有记忆。
- 复现：换一个作者/换一个入口，错误再次出现。
- 修复：任何事故必须新增一个 `case_XXX/`；并在发布前跑一遍回归。
- 回归验证：后续迭代中同类错误被门禁提前拦下。

### 3) 风格漂移（图片系列）

- 现象：系列图第一张扁平，第二张 3D，第三张带阴影渐变。
- 根因：风格底座不一致或被主体描述覆盖；negative_prompt 未继承。
- 复现：每次只写“科技感插图”，模型会自由发挥。
- 修复：风格底座前置 + 继承 negative_prompt；每次改动都跑锚点主题对比。
- 回归验证：锚点主题平铺对比一致；Prompt 规则检查不过即打回。

## 复现检查清单（报告失败/修复时必须记录）

- [ ] 模型版本：`gemini-3-pro-preview` 等（版本变动会引入行为差异）。
- [ ] Prompt 版本：文件名/哈希（别只说“我改了一下”）。
- [ ] 输入样本：触发失败的最小输入（不要脱敏到改变语义）。
- [ ] 输出协议：当次要求的模板/Schema（否则无法判定对错）。
- [ ] 失败判定：命中哪条门禁（解析失败/禁用短语/缺字段）。
- [ ] 回滚指针：回到哪个版本可立即止损。

结语：[conclusion.md](conclusion.md)

质量清单：[C-quality-checklist.md](C-quality-checklist.md)
