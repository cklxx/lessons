# 绝对正确的提示词：作战手册总览

本书讲提示词工程的工程写法，目标是让 Prompt 变成可版本控制、可测试、可回滚的交付物。你会用同一套方法写两类 Prompt。第一类面向文本生成，用来稳定产出 Markdown、JSON、表格或代码，方便进入下游流程。第二类面向图片生成，用来产出可复用的图片配置，先生成无文字底图，文字留给后期排版。

建议先读序章，把基本共识先对齐：[00-prologue.md](00-prologue.md)

![总览插图占位：提示词工程化作战手册](../../assets/books/flawless-expression/chapter-hero.svg)

这本书适合需要把模型输出接进流程的人，例如 AI 应用开发者、内容工程师、产品经理。它更关心确定性交付，要求格式可解析、逻辑可审计、失败可兜底。它不太适合纯发散闲聊，也不适合把合规和敏感风险交给模型自行处理。

你将产出一组可复用资产，包括 Prompt 合同、证据矩阵、论证骨架、去歧义规则、输出协议库、回归流程，以及文本和图片的配方库与发布清单。每一项都围绕同一件事，让结果能复跑，能裁决，能回滚。

## 3) 怎么用：最小可复跑闭环（工具无关）

不要在网页聊天框里凭感觉调试。用任何可脚本化的入口建立最小闭环，让输出落地为文件。下面示例里的 `<LLM_CLI>` 是占位符，替换成你手头能从 stdin 读入 prompt 并把结果写到 stdout 的命令即可。

### 文本生成（直接跑 Prompt）

将 Prompt 封装为脚本，输出重定向到文件以供校验：

```bash
mkdir -p out
cat <<'PROMPT' | <LLM_CLI> > out/checklist.md
你是中文技术文档编辑。
任务：把输入内容改写为一份可执行的检查清单。
约束：只输出 Markdown；每条不超过一行；必须包含失败判定与回滚。
输入：<把你的材料粘贴在这里>
PROMPT
```

### 图片生成（先让模型产出“文生图 Prompt 文本”）

这一步的目标是让模型生成一份可复制、可微调的图片 Prompt 配置文件，包含 image_prompt、negative_prompt 和 params。拿到文件后再交给生图工具执行。

```bash
mkdir -p out
cat <<'PROMPT' | <LLM_CLI> > out/image_config.txt
你是文生图提示词工程师。请为‘技术示意图（无文字）’生成一份可复制的提示词配置。
输出必须包含三段：image_prompt / negative_prompt / params。
要求：扁平矢量、蓝白配色、箭头表达数据流；禁止任何文字、数字、水印。
PROMPT
```

## 4) 图片生成 Prompt 的最小语法（可复制）

图片 Prompt 建议按配置文件来写，核心字段通常包括 subject、scene、style、composition、lighting_color、constraints、params 和 negative_prompt。negative_prompt 里把禁止文字、水印、签名写死，可以显著降低生成伪文字的概率。

示例（可作为系列插图的风格底座）：

```text
image_prompt:
flat 2D vector art, minimalist tech diagram, blue and white color palette, clean composition, high contrast, white background,
abstract server blocks and database cylinders connected by arrows, simple geometric data packets

negative_prompt:
text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

如果你想用七天把方法跑通，可以按这个顺序读：分级与合同（[01-mindset.md](01-mindset.md)），事实与拒答（[02-facts.md](02-facts.md)），论证与结构（[03-argument.md](03-argument.md)），语言去歧义（[04-language.md](04-language.md)），载体与输出协议（[05-medium.md](05-medium.md)），反馈与回归（[06-feedback.md](06-feedback.md)），最后读结语把 SOP 固化（[conclusion.md](conclusion.md)）。配方库与清单在附录：文本配方（[A-text-prompts.md](A-text-prompts.md)），图片配方（[B-image-prompts.md](B-image-prompts.md)），质量清单（[C-quality-checklist.md](C-quality-checklist.md)）。
