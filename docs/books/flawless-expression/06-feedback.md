# 反馈、校对与迭代：把 Prompt 的失败变成回归资产

Prompt 开发最昂贵的代价不是“第一次写错”，而是“修完之后不知道什么时候会再坏”。如果你不做回归测试，每一次所谓的“优化”都只是在打地鼠：修好了 JSON 格式，弄丢了关键事实；加强了语气约束，牺牲了指令可用性；改了一种画风，结果整个系列崩盘。

本章把软件工程的“回归测试”引入 Prompt 开发：每一次失败，都必须变成一个可复现的样本、一道可自动验收的门禁。

![章节插图占位：回归与发布门禁](../../assets/books/flawless-expression/chapter-hero.svg)

## 你的痛点与本章交付物

**你现在卡在哪：**
你改了 Prompt 的一句话，感觉这次稳了，但不敢保证之前跑通的 50 个 Case 还能不能过。你每次发布都心惊胆战，因为你的“测试”全靠人工肉眼抽查。

**这章能把你从哪救出来：**
把“靠运气发布”变成“靠数据发布”。建立一套只要跑一遍就能告诉你“改对了没”和“改坏了没”的自动化防线。

**交付物：**
1.  **静态评审清单**：发给模型前先拦住低级错误的检查表。
2.  **回归测试集结构**：把 Prompt 当源码管理，版本可追踪、可回滚。
3.  **自动化测试脚本**：两个拿来就能用的脚本（批量运行 + 结果断言）。
4.  **A/B 测试流程**：文本与图片 Prompt 的稳健迭代方法。

## 1. 静态评审：别把垃圾发给模型

在消耗 Token 和时间之前，先用人眼做第一道静态审查。这能拦下 80% “明明写错了却还在跑”的低级浪费。

| 维度 | 检查项 | 通过标准 |
| :--- | :--- | :--- |
| **结构** | 定界清晰 | 是否用标题或明显的分隔符把“指令区”和“数据区”物理隔绝？不要让数据里的文字干扰指令。 |
| **角色** | 身份明确 | 是否写清了“你是谁”（如：审计工具、提取器），而不是只写卑微的“请帮我做”？ |
| **约束** | 负向明确 | “不做什么”是否写成了可检测的规则？（如：禁止使用 Markdown 包裹 JSON，禁止输出寒暄语）。 |
| **输出** | 协议固定 | 是否提供了 JSON Schema 或固定的模板结构？是否声明了字段顺序不可变？ |
| **兜底** | 异常出口 | 当信息缺失时，是否有明确的拒答话术或特定的错误码？（不要让模型瞎编）。 |
| **回滚** | 降级策略 | 失败后是重试还是返回兜底文本？这一步想清楚了吗？ |

## 2. 建立回归集：把失败固化下来

任何一次线上事故或测试失败，都必须入库成为一个“回归样本”。否则你只是在“修一个 Bug”，而不是“免疫一类 Bug”。

### 标准回归集目录结构

建议在你的代码库中建立如下结构。这不是建议，是工程标准。

```text
prompts/
├── production/
│   ├── prompt_analyst.v1.txt      <-- 线上正在跑的版本
│   └── prompt_writer.v3.txt
└── regression/
    ├── case_001_chatty_json/      <-- 以前失败过的典型案例
    │   ├── input.txt              <-- 触发问题的原始输入
    │   ├── prompt_base.txt        <-- 当时的 Prompt 快照
    │   ├── prompt_candidate.txt   <-- 你正在修的 Prompt
    │   └── expected.json          <-- 人工校对过的标准答案（真值）
    ├── case_002_missing_fields/
    │   ├── input.txt
    │   ├── <...>
    │   └── expected.md            <-- 也可以是 Markdown 规则
    ├── run_batch.sh               <-- 批量运行脚本
    └── check_results.py           <-- 自动断言脚本
```

**关键点：**
*   `expected.*` 是你的真理。它必须是人工确认过的。
*   每一个 Case 对应一个具体的边缘情况（比如：输入为空、输入包含干扰字符、需要提取的字段不存在）。

## 3. 文本 Prompt 的 A/B 回归流程

不要直接改生产环境的 Prompt。遵循以下流程：

1.  **基线（Baseline）：** 用 `production/` 里的 Prompt 跑一遍所有回归 Case，记录通过率。这是你的底线。
2.  **变量控制：** 复制一份 Prompt 到 `regression/` 目录下，只改动你想优化的那个点（比如增加一句“禁止输出 Markdown 代码块”）。不要同时改两件事。
3.  **同集跑测：** 用同一批 `input.txt` 跑你的候选 Prompt。
4.  **裁决：**
    *   **修复目标达成？** 那个让你头疼的 Case 过了吗？
    *   **无退化（No Regression）？** 之前那 49 个通过的 Case 还在通过吗？
    *   **格式/风格检查：** 输出格式是否依然符合下游解析器的要求？
5.  **发布：** 只有修复成功且无退化，才替换 `production/` 下的文件。

### 模板：文本 Prompt 修复专用模版

当你修复一个 Prompt 时，不要只在脑子里想，把它写下来作为提交记录的一部分。

```markdown
# Prompt 修复记录

## 1. 问题描述
- **现象**：模型偶尔会在 JSON 前面加一句“好的，这是结果”。
- **影响**：导致后端 JSON 解析器报错 `Unexpected token`。
- **Case ID**：`case_001_chatty_json`

## 2. 修改方案
- **原 Prompt**：请输出 JSON 格式。
- **新 Prompt**：你是一个无情的 JSON 生成机器。严禁输出任何非 JSON 字符。严禁使用 ```json 包裹。直接输出原始 JSON 字符串。

## 3. 回归结果
- **目标 Case**：通过。
- **全量回归**：50/50 通过。
- **新增风险**：无。
```

## 4. 最小自动化脚本（拿去用）

这一步是把“人肉测试”变成“机器测试”的关键。你需要一个可脚本化的模型调用入口（CLI/API/SDK 皆可），并让它满足：stdin 输入 prompt，stdout 输出结果。

### 脚本 A：批量运行器 (`run_batch.sh`)

这个脚本会遍历你的回归目录，把 Prompt 和 Input 拼在一起发给模型，并把结果存下来。

```bash
#!/usr/bin/env bash
set -euo pipefail

# 配置模型调用命令与模型名（按需）
LLM_CMD=${LLM_CMD:-llm}
MODEL=${MODEL:-}

PROMPT_FILE=${1:?用法: run_batch.sh <prompt_file> <cases_dir> <out_dir>}
CASES_DIR=${2:?用法: run_batch.sh <prompt_file> <cases_dir> <out_dir>}
OUT_DIR=${3:?用法: run_batch.sh <prompt_file> <cases_dir> <out_dir>}

mkdir -p "$OUT_DIR"

echo "开始执行回归测试，使用模型: $MODEL"

for case_dir in "$CASES_DIR"/*; do
  [ -d "$case_dir" ] || continue
  input="$case_dir/input.txt"
  [ -f "$input" ] || continue

  name=$(basename "$case_dir")
  
  echo "正在运行 Case: $name"
  
  # 将 Prompt 与 Input 拼接后喂给模型，并把结果写入输出目录
  if [ -n "${MODEL}" ]; then
    { cat "$PROMPT_FILE"; printf '\n\n'; cat "$input"; } | "$LLM_CMD" -m "$MODEL" > "$OUT_DIR/$name.out"
  else
    { cat "$PROMPT_FILE"; printf '\n\n'; cat "$input"; } | "$LLM_CMD" > "$OUT_DIR/$name.out"
  fi

  # 稍微停顿，避免触发极其严格的速率限制（如果你的配额很低）
  sleep 1
done

echo "回归测试执行完毕。结果保存在 $OUT_DIR"
```

### 脚本 B：最小断言器 (`check_results.py`)

这个脚本只做最硬的门禁检查：是不是 JSON？有没有废话？

```python
import argparse
import json
import sys
from pathlib import Path

# 绝对禁止出现的“废话”列表
FORBIDDEN_PHRASES = [
    "好的，这是",
    "Here is the",
    "Sure, I can help",
    "```json",  # 我们要求纯 JSON，不要 Markdown 包裹
    "```",
]

def looks_like_json(text: str) -> bool:
    text = text.strip()
    return text.startswith("{") or text.startswith("[")

def check_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8", errors="replace").strip()
    
    # 检查 1: 禁用词
    for phrase in FORBIDDEN_PHRASES:
        if phrase in content:
            print(f"[失败] {file_path.name}: 发现了禁用词 '{phrase}'")
            return False

    # 检查 2: JSON 合法性 (如果你的目标是 JSON)
    if looks_like_json(content):
        try:
            json.loads(content)
        except json.JSONDecodeError:
            print(f"[失败] {file_path.name}: JSON 解析失败")
            return False
    else:
        # 如果不是 JSON 格式，根据你的需求决定是否报错
        # 这里假设所有输出都必须是 JSON
        print(f"[失败] {file_path.name}: 输出不是 JSON 结构")
        return False

    print(f"[通过] {file_path.name}")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("out_dir", help="包含模型输出文件的目录")
    args = parser.parse_args()
    
    out_dir = Path(args.out_dir)
    if not out_dir.exists():
        print(f"错误: 目录 {out_dir} 不存在")
        sys.exit(1)

    failed_count = 0
    total_count = 0

    for p in sorted(out_dir.glob("*.out")):
        total_count += 1
        if not check_file(p):
            failed_count += 1

    print(f"\n总结: 总计 {total_count}, 失败 {failed_count}")
    
    if failed_count > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## 5. 图片 Prompt 的风格回归（系列一致性）

图片生成最怕的是“第一张是极简风，第二张变成了赛博朋克”。图片回归不看像素，看**规则**。

### 风格一致性“三件套”

1.  **风格底座 (Style Base)**：把所有的风格描述提取出来，做成一个固定的文本块，所有 Prompt 必须强制包含。
2.  **负向约束 (Negative Prompt)**：这是一道防火墙。必须包含所有你痛恨的元素。
3.  **锚点测试 (Anchor Test)**：选定 3 个固定的主体（比如：一个方块、一只猫、一棵树）。每次修改风格参数时，先跑这 3 个锚点，平铺对比。

### 可复制图片 Prompt 配置

直接拿这个作为你的图片生成规范。

```text
image_prompt:
<主体描述>, flat 2D vector illustration, minimalist design, circular feedback loop structure, four abstract nodes connected by arrows, clean tech style, blue and white color palette, solid white background, high contrast, no text labels

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, shadows, blur, messy background, humans, faces, distortion, noise

params:
aspect_ratio=16:9, quality=high, seed=42
```

**验收标准：**
*   **规则验收**：检查最终的 Prompt 字符串，是否完整包含了上面的 `negative_prompt`？
*   **视觉验收**：生成出来的图片，背景是不是纯白的？有没有出现那该死的文字？

## 6. 常见陷阱与自救

### 1) 只改措辞，不改规则
**现象：** 你把“请输出 JSON”改成了“跪求输出 JSON”，结果模型偶尔还是会输出废话。
**根因：** 你在试图用情感感化模型，而不是用规则约束它。
**自救：** 别废话。直接在 Prompt 里加上 `Negative Constraint`：禁止输出任何非 JSON 字符。并在代码层用 `check_results.py` 这种脚本做硬拦截。

### 2) 只有修复，没有记忆
**现象：** 上周修好的 Bug，这周换了个同事写 Prompt 又出现了。
**根因：** 你们的组织没有记忆。失败的 Case 没有进回归库。
**自救：** 建立 Git 提交规范。修改 Prompt 必须附带一个新的 `regression/case_xxx`。没有 Case 不许合并。

### 3) 图片风格漂移
**现象：** 系列插图画到第 10 张时，画风已经完全变了。
**根因：** 你的风格描述和主体描述混在一起了，主体描述太长冲淡了风格权重。
**自救：** 强制分离。风格描述必须永远放在 Prompt 的最前或最后（取决于模型特性，通常最前权重大），并且使用完全一致的词汇。

## 结语

不要相信你的直觉，不要相信模型的“承诺”。只相信测试结果。把每一次失败都变成资产，你的 Prompt 工程才会越来越稳固。

下一步，去检查你的质量清单：[C-quality-checklist.md](C-quality-checklist.md)
