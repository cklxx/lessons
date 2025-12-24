# 绝对正确的提示词：作战手册总览

本书不是一本“咒语大全”，而是一套**提示词工程（Prompt Engineering）的工程规范**。我们要把提示词从玄学的聊天记录，变成可版本控制、可测试、可回滚的交付物。

在这里，你将学会用同一套工程方法写两类 Prompt：

- **文本生成 Prompt**：产出结构稳定的 Markdown、JSON、表格或代码。
- **图片生成 Prompt**：产出风格统一、可控差异、无乱码的视觉资产配置文件。

先读序章，把“念咒语”的心态彻底戒掉：[00-prologue.md](00-prologue.md)

![总览插图占位：提示词工程化作战手册](../../assets/books/flawless-expression/chapter-hero.svg)

## 1) 适用性与画像

| 维度 | 适用场景 / 核心画像 | 不适用场景 / 反向画像 |
| :--- | :--- | :--- |
| **对象** | AI 应用开发者、内容工程师、产品经理、需要把输出接进自动化流程的人 | 只想靠运气“一次就中”的投机者 |
| **目标** | 确定性交付：格式必须可解析、逻辑必须可审计、失败必须可兜底 | 纯发散闲聊：不关心结构，不关心能不能复现 |
| **场景** | 结构化提取、批量写作、RAG/Agent 编排、技术文档、资产化绘图 | 无明确目标的聊天；试图把合规/敏感风险外包给模型的行为 |

## 2) 武器库：本书交付物清单

这一套方法论交付的不是“话术”，而是“资产”：

- **Prompt 合同**：明确 ID、版本、输入约束、输出协议、失败判定与回滚策略（见 [01-mindset.md](01-mindset.md)）。
- **证据矩阵**：对“事实类输出”强制要求举证；冲突证据必须并列，严禁模型擅自调和（见 [02-facts.md](02-facts.md)）。
- **论证骨架**：把结论拆解为可审计的逻辑节点，写清前提与失效条件（见 [03-argument.md](03-argument.md)）。
- **去歧义规则**：把“尽快/优化/专业”等形容词替换为具体的阈值、窗口与排除条件（见 [04-language.md](04-language.md)）。
- **输出协议库**：定义 Markdown 报告、JSON Schema、表格对比及图片配置块的标准格式（见 [05-medium.md](05-medium.md)）。
- **回归集与 A/B**：建立失败样本库，任何 Prompt 修改必须先跑回归测试再发布（见 [06-feedback.md](06-feedback.md)）。
- **文本 Prompt 配方库**：摘要、抽取、对比、审查、评测等高频任务的工业级模板（见 [A-text-prompts.md](A-text-prompts.md)）。
- **图片 Prompt 配方库**：无文字底图的系列配方与风格底座，确保视觉一致性（见 [B-image-prompts.md](B-image-prompts.md)）。
- **质量控制清单**：发布门禁、最小命令集与复现规范（见 [C-quality-checklist.md](C-quality-checklist.md)）。

## 3) 怎么用：最小命令闭环（Gemini CLI）

不要在网页聊天框里凭感觉调试。使用 CLI 建立最小闭环，让输出落地为文件。

### 文本生成（直接跑 Prompt）

将 Prompt 封装为脚本，输出重定向到文件以供校验：

```bash
gemini -m gemini-3-pro-preview -p "
你是中文技术文档编辑。
任务：把输入内容改写为一份可执行的检查清单。
约束：只输出 Markdown；每条不超过一行；必须包含失败判定与回滚。
输入：<把你的材料粘贴在这里>
" > out/checklist.md
```

### 图片生成（先让模型产出“文生图 Prompt 文本”）

这一步的目标不是让 Gemini 直接画图，而是让它生成一份可复制、可微调的**图片 Prompt 配置文件**（含 negative prompt 与参数）。你拿到这个文件后，再扔给生图工具。

```bash
gemini -m gemini-3-pro-preview -p "
你是文生图提示词工程师。请为‘技术示意图（无文字）’生成一份可复制的提示词配置。
输出必须包含三段：image_prompt / negative_prompt / params。
要求：扁平矢量、蓝白配色、箭头表达数据流；禁止任何文字、数字、水印。
" > out/image_config.txt
```

## 4) 图片生成 Prompt 的最小语法（可复制）

把图片 Prompt 当作代码配置文件写，严禁当成作文写。一个最小可复用的结构必须包含以下字段：

- `subject`：主体（具体名词 + 核心属性）
- `scene`：环境/背景（越少越好，保持干净）
- `style`：媒介与风格（flat vector / isometric / sketch）
- `composition`：构图与视角（top-down / centered / wide）
- `lighting_color`：光影与色调（soft light / monochrome / palette）
- `constraints`：硬约束（no text / no watermark / no faces）
- `params`：宽高比、清晰度等工具特定参数
- `negative_prompt`：明确禁止项（把乱码与低质内容挡在门外）

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

## 5) 七日特训路径（游泳道）

- **Day 1：分级与合同** —— 建立契约意识，把 Prompt 当交付物（[01-mindset.md](01-mindset.md)）
- **Day 2：事实与拒答** —— 解决幻觉问题，“不知道就说不知道”（[02-facts.md](02-facts.md)）
- **Day 3：论证骨架** —— 逻辑透明化，写清前提与失效条件（[03-argument.md](03-argument.md)）
- **Day 4：去歧义** —— 语言参数化，把形容词改成参数（[04-language.md](04-language.md)）
- **Day 5：输出协议** —— 规范化接口，文本/JSON/表格/图片配置块（[05-medium.md](05-medium.md)）
- **Day 6：回归与 A/B** —— 建立反馈环，把失败变成资产（[06-feedback.md](06-feedback.md)）
- **Day 7：默认 SOP** —— 团队协作规范，发布、回滚与复现（[conclusion.md](conclusion.md)）

## 6) 目录（读完能产出什么）

1. [第 1 章：提示词心智模型：正确性的定义与边界](01-mindset.md)
   - **交付目标**：Prompt 分级标准 + Prompt 合同模板（含失败判定与回滚）。
2. [第 2 章：事实与知识：如何写“可核查/可溯源”的 Prompt](02-facts.md)
   - **交付目标**：拒答/追问/不确定性规则 + 证据矩阵模板 + 冲突并列策略。
3. [第 3 章：论证与结构：让 Prompt 输出可审计](03-argument.md)
   - **交付目标**：论证骨架表 + 前提表 + 反驳预案 + 可审计输出协议。
4. [第 4 章：语言与措辞：如何写不歧义的 Prompt（文本+图片）](04-language.md)
   - **交付目标**：歧义扫描与替换表 + 参数化四件套 + 可控差异的风格变体写法。
5. [第 5 章：媒介与格式：为文本/结构化输出/图片选择最优 Prompt 载体](05-medium.md)
   - **交付目标**：输出协议库（Markdown/JSON/表格）+ 图片 Prompt 配置块模板（含 negative prompt）。
6. [第 6 章：反馈、校对与迭代：把 Prompt 的失败变成回归资产](06-feedback.md)
   - **交付目标**：回归集目录结构 + A/B 流程 + 最小自动化脚本（批量跑测 + 断言）。
7. [结语：让提示词成为默认交付物（文本+图片）](conclusion.md)
   - **交付目标**：个人/团队 Prompt SOP（发布前清单、版本管理、回滚策略）。
8. [附录 A：文本 Prompt 配方库](A-text-prompts.md)
   - **交付目标**：常用任务的 Prompt 模板（输入/输出契约、门禁、回滚一次写清）。
9. [附录 B：图片 Prompt 配方库（无文字底图）](B-image-prompts.md)
   - **交付目标**：系列插图的风格底座 + 常见示意图配方（可叠字、可维护）。
10. [附录 C：质量控制与复现清单（Prompt 版）](C-quality-checklist.md)
    - **交付目标**：发布门禁、回归结构、最小命令集（可复现闭环）。
