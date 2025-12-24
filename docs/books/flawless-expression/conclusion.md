# 结语：让提示词成为默认交付物（文本+图片）

提示词工程不是玄学，而是一门工程学科：版本控制、回归测试、发布门禁、回滚预案缺一不可。当你把 Prompt 当成交付物而不是聊天记录，你就获得了“可复刻高质量输出”的能力。

![结语插图占位：把提示词变成默认交付](../../assets/books/flawless-expression/chapter-hero.svg)

## 你应该带走的资产（最小集合）

1. Prompt 分级标准（草稿/协作/机器执行）：决定写到什么强度（见 [01-mindset.md](01-mindset.md)）。
2. 事实规则与证据矩阵：不编造、能举证、冲突并列（见 [02-facts.md](02-facts.md)）。
3. 论证骨架与失效条件：结论可审计、可反驳、可熔断（见 [03-argument.md](03-argument.md)）。
4. 去歧义替换表：把形容词变参数，把“不做什么”写成硬约束（见 [04-language.md](04-language.md)）。
5. 输出协议库：Markdown/JSON/表格/图片 Prompt 配置块（见 [05-medium.md](05-medium.md)）。
6. 回归集与 A/B 流程：失败样本入库，改动先跑回归再发布（见 [06-feedback.md](06-feedback.md)）。

## 文本 Prompt 默认 SOP（可复制）

> 用法：保存为 `PROMPT_SOP.md`，每次写生产级 Prompt 都按这个顺序走。

```markdown
# 生产级 Prompt SOP

## 0) 分级（决定写到什么强度）
- 级别：Draft / Collaboration / Machine Execution
- 风险：<面向客户/内部工具/一次性草稿>
- 受众：<人类/解析器/下游系统>

## 1) 合同（先写验收，再写正文）
- Prompt ID & Version：<...>
- 输入契约：格式 <...>；必填字段 <...>；最大长度 <...>
- 输出契约：载体 <Markdown/JSON/表格>；模板/Schema <...>
- 失败判定：<解析失败/缺字段/禁用短语>
- 回滚/降级：<重试一次/返回固定错误结构/切回旧版本>

## 2) 正文（用结构而不是散文）
- Role：你是谁（工具/审计员/编辑/提取器）
- Task：一句话任务（只做一件事）
- Constraints：阈值/窗口/触发/排除条件（可裁决）
- Output Format：固定顺序与字段名（不可变）

## 3) 回归（把失败变资产）
- 新增/更新回归样本：<case_id>
- A/B：基线 vs 候选（同一输入集）
- 门禁：格式通过 + 禁用短语为 0 + 关键字段齐全

## 4) 发布（可追溯）
- 版本号：v<YYYYMMDD>.<n>
- 变更摘要：改了什么/为什么改/影响面
- 回滚指针：回到哪个版本可立刻止损
```

替换点：只替换 `<...>`，不要改字段顺序与命名（顺序稳定是可复现的前提）。

## 图片 Prompt 默认 SOP（含风格一致性）

> 用法：用于生成系列插图/图标/封面分隔图；关键文字一律后期叠加。

```markdown
# 视觉资产 Prompt SOP

## 1) 风格底座（所有 Prompt 共享）
style_base:
- style: flat vector / sketch / isometric（选一个并固定）
- palette: <蓝白灰 / 紫青渐变 等>
- background: solid white / solid dark（选一个并固定）
- quality: high, clean composition, high contrast

## 2) 主体变量（每张图只改这里）
subject:
- 主体：<...>
- 动作/关系：<...>
- 构图：centered / top-down / wide（选一个）

## 3) 负向约束（所有 Prompt 继承同一份）
negative_prompt:
- text, letters, numbers, watermark, signature
- photorealistic, 3d render, shading, gradients, blur
- messy background, humans, faces

## 4) 参数建议（按工具填写）
params:
- aspect_ratio: 16:9
- quality: high
- seed: <工具支持才填写；用于复现与归因>
```

### 配图提示词：默认 SOP 的“清单化”隐喻（无文字底图）

```text
image_prompt:
flat 2D vector illustration, minimalist stack of checklists and a version tag icon, clean tech style, blue and white palette,
solid white background, high contrast, crisp edges, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 命令行最小用法（Gemini CLI）

把 Prompt 当文件管理时，最小可用方式是“读文件 → 作为 -p 的内容传入 → 保存输出”：

```bash
gemini -m gemini-3-pro-preview -p "$(cat prompts/prompt.txt)" > out/result.md
```

## 发布前 7 项核对清单

1. 意图对齐：是否需要澄清问题？模糊输入是否有追问/拒答策略？
2. 输出协议：载体与模板/Schema 是否固定？字段名是否不可变？
3. 纯净度：是否禁止寒暄语、解释性前言、Markdown 包裹导致的解析失败？
4. 事实规则：是否启用“未知出口 + 证据矩阵 + 冲突并列”（见 [02-facts.md](02-facts.md)）？
5. 论证可审计：是否输出依据检查点与失效条件（见 [03-argument.md](03-argument.md)）？
6. 图片安全：图片 Prompt 是否默认禁止文字/水印/签名，关键文字是否后期叠加（见 [05-medium.md](05-medium.md)）？
7. 回归与回滚：是否跑过回归集（见 [06-feedback.md](06-feedback.md)）？回滚指针是否明确可执行？

回到总览页：[index.md](index.md)
