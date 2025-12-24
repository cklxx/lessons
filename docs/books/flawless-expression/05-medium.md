# 媒介与格式：为文本/结构化输出/图片选择最优 Prompt 载体

Prompt 的一半是“写什么”，另一半是“怎么交付”。选择错误的载体会让下游链路断裂：让模型用自然语言输出本该是 JSON 的数据；让图片模型在图里渲染关键文字；最后一定是返工与事故。

本章把“载体选择”写成决策树，并给出可复制的输出协议：Markdown 报告、JSON Schema、表格对比，以及图片 Prompt 的工程化配置块。

![章节插图占位：载体选择与交付协议](../../assets/books/flawless-expression/chapter-hero.svg)

## 你将收获什么

- 一个媒介选择决策树（纯文本）：用消费对象决定输出是 Markdown/JSON/表格/图片。
- 三类文本输出模板：Markdown 报告协议、JSON Schema 协议、表格对比协议。
- 一个图片 Prompt 配置块模板：主体/风格/构图/光影/参数/负向约束/一致性策略。
- 两个图片 Prompt 示例：技术示意图底图（无文字）与章节封面插画（可当分隔图）。
- 一个 Gemini CLI 示例：生成可被脚本解析的 JSON 输出。

## 媒介选择决策树（纯文本可复制）

```text
1) 谁是结果的第一消费者？
   - 解析器/脚本/API：输出必须结构化（JSON 优先）。
   - 人类阅读（决策/复盘/说明）：输出 Markdown 报告（固定标题层级）。
   - 人类对比（竞品/参数/清单）：输出二维表（列名固定）。
   - 视觉资产（插图/封面/示意）：输出图片 Prompt（生成底图，关键文字后期叠加）。

2) 结果是否需要被自动化处理？
   - 需要：给 Schema/模板 + 失败判定；禁止寒暄语与多余解释。
   - 不需要：仍建议给结构（标题/清单/表格），避免散文。

3) 图片是否包含关键文字信息？
   - 是：不要让图片模型写字。生成无文字底图，文字后期叠加。
   - 否：可以用图片模型生成插图/氛围/封面分隔图。
```

## 文本输出：三类可复制协议

### 1) Markdown 报告协议（面向人类）

```text
输出协议：
1) 只输出 Markdown。
2) 标题层级固定为：## / ###（不要输出 #）。
3) 第一段必须是“执行摘要”（最多 3 句话）。
4) 必须包含：风险、失败判定、回滚/降级建议。
5) 禁止：前言式寒暄、长段散文、空泛口号。
```

### 2) JSON Schema 协议（面向解析器）

```text
输出协议：
1) 只输出 JSON 字符串本体（不要 Markdown 代码块包裹）。
2) 字段名与类型必须完全匹配下列 Schema；不允许新增字段。
3) 若无法生成合法 JSON：返回固定错误结构 {\"error\":\"SCHEMA_FAIL\",\"reason\":\"<reason>\"}。
```

Schema 示例（用于放进 Prompt 里约束输出）：

```json
{
  "type": "object",
  "properties": {
    "summary": { "type": "string" },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "issue": { "type": "string" },
          "fix": { "type": "string" }
        },
        "required": ["id", "issue", "fix"]
      }
    }
  },
  "required": ["summary", "items"]
}
```

### 3) 表格对比协议（面向速览与对齐）

```text
输出协议：
1) 输出 Markdown 表格，列名固定：功能点/方案A/方案B/推荐结论/风险。
2) “功能点”按重要性降序排列。
3) 单元格为空必须写 N/A（避免读者猜）。
```

## 图片生成：把 Prompt 写成配置块（可维护、可复用）

图片 Prompt 推荐拆成“配置块”，从而做到风格复用、差异可控。

### 配置块模板（可复制）

```text
image_prompt:
subject: <主体（名词 + 属性）>
scene: <环境/背景（尽量少）>
style: <flat vector / sketch / isometric 等>
composition: <centered / top-down / wide 等>
lighting_color: <soft light / monochrome / palette 等>
constraints: <硬约束（no text / no faces / clean background）>

negative_prompt:
<禁止项：text/letters/numbers/watermark + 低质/噪声/写实/3d 等>

params:
aspect_ratio=<...>, quality=<...>
```

## 图片 Prompt 示例 1：技术示意图底图（无文字）

```text
image_prompt:
flat 2D vector art, minimalist tech diagram, blue and white palette, solid white background,
abstract server blocks and database cylinders connected by arrows showing data flow, simple geometric data packets, high contrast

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 图片 Prompt 示例 2：章节封面插画（用于视觉分隔）

封面/分隔图的原则：可以氛围化，但不要承载关键定义（关键定义必须在正文用文字复述）。

```text
image_prompt:
abstract illustration of a “prompt engineer”, a glowing notebook hovering above a terminal window,
clean futuristic style, soft gradient background, minimal composition, calm color palette (blue/purple), cinematic light

negative_prompt:
text, letters, numbers, watermark, signature, photorealistic faces, crowded background, blurry, noisy, low quality

params:
aspect_ratio=16:9, quality=high
```

### 配图提示词：载体选择决策树（无文字底图）

决策树配图不要画满文字。画“分叉箭头 + 不同载体图标”的底图，文字后期叠加即可。

```text
image_prompt:
flat 2D vector illustration, minimal decision tree with branching arrows leading to simple icons (document, table grid, code brackets, image frame),
blue and white palette, solid white background, clean composition, high contrast, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 文本 Prompt 示例（Gemini CLI）：输出可解析 JSON

目标：让模型返回“错误类型 + 修复建议”的 JSON，便于脚本后处理。

```bash
gemini -m gemini-3-pro-preview -p "
你是静态分析工具。请分析下面的代码片段可能出现的异常，并以纯 JSON 输出。

输出协议：
1) 只输出 JSON 字符串（不要 Markdown 代码块包裹）。
2) 输出是一个数组，每个对象包含 error_type 与 fix_suggestion 两个字段。

代码片段：
result = 10 / user_input
"
```

## 复现检查清单

1. 载体匹配：是否为解析器/脚本输出选择了 JSON（而不是自然语言）？
2. 结构定义：是否给了模板/Schema/列名，并固定顺序与字段？
3. 纯净度：是否禁止寒暄语、多余解释、Markdown 包裹导致的解析失败？
4. 图片约束：是否明确禁止文字/水印/签名，避免伪文字事故？
5. 系列一致性：是否固定风格底座与 negative prompt（必要时锁 seed）？

## 常见陷阱（失败样本）

### 1) 话痨 JSON

- 现象：输出前后带解释文本，解析器直接失败。
- 根因：没有把“只输出 JSON 本体”写成硬约束。
- 复现：只写“输出 JSON”而不给 Schema/模板/禁止项。
- 修复：写清输出协议；失败时返回固定错误结构；必要时在流程里增加清洗器。
- 回归验证：输出可直接 `json.loads`/`jq` 解析通过。

### 2) 图片乱码文字

- 现象：示意图里出现不可读字符或类似水印。
- 根因：让图片模型渲染关键文字，触发模型弱项。
- 复现：Prompt 含“label every component / detailed metrics text”。
- 修复：生成无文字底图 + 后期叠字；negative prompt 明确禁止 text/letters/numbers/watermark。
- 回归验证：连续生成多张底图均无可见字符。

### 3) Schema 幻觉

- 现象：同一 Prompt 多次运行字段名漂移（userName/user_name 混用）。
- 根因：没有显式 Schema 或字段模板，模型按概率选命名风格。
- 复现：重复运行 5 次，观察字段是否一致。
- 修复：把字段模板或 JSON Schema 放进 Prompt；禁止新增字段；缺字段视为失败。
- 回归验证：连续运行 10 次字段名与结构完全一致。

上一章：[04-language.md](04-language.md) · 下一章：[06-feedback.md](06-feedback.md)

配方库：文本见 [A-text-prompts.md](A-text-prompts.md) · 图片见 [B-image-prompts.md](B-image-prompts.md)
