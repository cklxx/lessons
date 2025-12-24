# 05 媒介与格式：别让交付格式毁了你的 Prompt

Prompt 的一半是“内容”，另一半是“载体”。

很多 Prompt 工程师死在最后一步：你让模型用自然语言输出本该是 JSON 的数据，下游解析器直接报错；你让模型在图片里硬写文字，结果生成了一堆乱码火星文。

这一章不讲虚的，直接给你一套决策树和三个强制协议。别让模型猜你要什么格式，直接把模具扣在它脸上。

![章节插图：载体选择与交付协议](../../assets/books/flawless-expression/chapter-hero.svg)

## 你的痛点与交付物

**你现在的处境：**
- 也就是写个脚本处理数据，结果模型有时候返回 JSON，有时候返回 Markdown，正则表达式写得比 Prompt 还长。
- 想做个技术示意图，结果图片里的文字全是错别字，根本没法用。
- 输出的报告格式满天飞，标题层级乱跳，自动化脚本读不到重点。

**本章交付物：**
- **一张决策表**：一眼看出该用 JSON、Markdown 还是表格。
- **三套文本协议**：直接复制进 Prompt，锁死输出格式。
- **一套图片配置块**：把画图变成填空题，杜绝文字乱码。
- **一个 CLI 脚本**：演示如何生成可被机器读取的结构化数据。

## 决策树：到底该输出什么？

别拍脑袋选格式。问自己两个问题，答案就出来了。

### 第一层：谁是消费者？
1. **解析器 / API / 脚本** -> 必须用 **JSON**。不要用 Markdown，不要用自然语言。
2. **人类（决策者 / 开发者）** -> 用 **Markdown 报告**。固定标题层级，方便快速扫描。
3. **人类（对比者 / 审核员）** -> 用 **表格（Table）**。固定列名，强制对齐。
4. **视觉资产** -> 用 **图片 Prompt**。生成无文字底图，文字后期 P 上去。

### 第二层：是否需要自动化？
- **是** -> 必须提供 Schema（结构定义）和失败判定。禁止任何寒暄（"好的，这是结果。"）。
- **否** -> 依然建议给结构，避免模型写出长篇大论的废话。

### 第三层：图片里有字吗？
- **有关键信息** -> **严禁**让模型画字。生成底图，文字后期叠加。
- **纯装饰/氛围** -> 可以让模型发挥，但要用 Negative Prompt 压制乱码风险。

## 文本输出协议：复制这三段就够了

把这些协议块直接粘到你的 Prompt 末尾。

### 1. Markdown 报告协议（给人看）

用于日报、Code Review、架构设计文档。

```text
### Output Protocol
1. Format: Markdown only.
2. Headings: Use strictly level 2 (##) and level 3 (###). Do NOT use level 1 (#).
3. Structure:
   - ## Executive Summary (Max 3 sentences, straight to the point)
   - ## Risk Analysis (Must include "Severity" and "Mitigation")
   - ## Action Items (Bulleted list)
4. Constraints: No conversational filler (e.g., "Here is the report"). No introductory text.
```

### 2. JSON Schema 协议（给机器看）

用于 API 对接、数据清洗、自动化流。

```text
### Output Protocol
1. Format: Raw JSON string only. NO Markdown code blocks (no ```json wrapper).
2. Schema Compliance: Output MUST match the following schema exactly. NO new fields.
3. Error Handling: If unable to generate valid JSON, return: {"error": "SCHEMA_FAIL", "reason": "<reason>"}

### JSON Schema
{
  "type": "object",
  "properties": {
    "status": { "type": "string", "enum": ["success", "failed"] },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "integer" },
          "value": { "type": "string" }
        },
        "required": ["id", "value"]
      }
    }
  },
  "required": ["status", "data"]
}
```

### 3. 表格对比协议（一目了然）

用于竞品分析、参数对比、选型决策。

```text
### Output Protocol
1. Format: Markdown Table only.
2. Columns: Feature | Solution A | Solution B | Verdict | Risk Level
3. Content:
   - "Feature": Sort by importance (High to Low).
   - Empty cells: Must be filled with "N/A".
   - "Verdict": Must be one of [A wins, B wins, Tie].
```

## 图片生成：把 Prompt 变成工程配置文件

不要用自然语言写小作文。把图片 Prompt 拆成三个工程配置块：**画面描述、负向约束、参数设置**。

### 通用配置模板

```text
image_prompt:
subject: <核心主体，名词+修饰词>
scene: <背景环境，越简单越好>
style: <风格定义，如 flat vector, isometric, sketch>
lighting: <光影设定，如 soft lighting, cinematic, studio light>
composition: <构图视角，如 top-down, centered, wide angle>

negative_prompt:
<所有你不想要的东西，必须包含文字和水印的禁令>

params:
aspect_ratio=<比例>, quality=<质量>
```

### 实战：技术架构图底图（无文字版）

这个 Prompt 的核心是**不让模型写字**。我们只要一个干净的底座。

![插图占位：生成的无文字架构底图](../../assets/books/flawless-expression/placeholder-diagram.svg)

```text
image_prompt:
flat 2D vector art, minimalist tech diagram foundation, 
subject: abstract server blocks and cylinder databases connected by smooth flow arrows,
style: corporate memphis tech style, blue and grey color palette, clean lines,
background: solid white background, high contrast,
composition: centered layout, ample whitespace for text overlay

negative_prompt:
text, letters, numbers, characters, watermark, signature, handwriting, logo, brand name, photorealistic, 3d render, shading, complex details, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

### 实战：章节视觉分隔图（氛围版）

用于给长文档做视觉呼吸，不需要承载具体信息。

```text
image_prompt:
digital illustration of "code architecture", 
subject: glowing geometric structures floating in void, abstract representation of data streams,
style: synthwave aesthetic, neon blue and magenta,
lighting: volumetric lighting, cinematic atmosphere,
composition: wide shot, minimal details

negative_prompt:
text, letters, numbers, watermark, complex machinery, biological forms, messy details, low resolution, blurry

params:
aspect_ratio=16:9, quality=high
```

## Gemini CLI 实战：自动化 JSON 管道

这是本章的终极形态：用 CLI 结合 JSON 协议，把非结构化文本直接转成下游脚本可用的数据文件。

场景：你是运维工程师，要把一段乱七八糟的日志报错分析成结构化的 JSON，存到文件里供后续脚本读取。

```bash
gemini -m gemini-3-pro-preview -p "
你是日志分析专家。请分析下面的系统日志片段，提取关键错误信息，并输出为纯 JSON。

### 输入日志
[2024-05-20 10:00:01] ERROR Connection refused to DB-01 (192.168.1.5)
[2024-05-20 10:00:02] WARN Retry attempt 1 failed
[2024-05-20 10:00:05] CRITICAL Service PaymentGateway crashed: OutOfMemory

### 输出协议
1. 格式：纯 JSON 字符串（不要 Markdown 代码块）。
2. 结构：一个对象数组，每个对象包含 timestamp, level, service, message 四个字段。
3. 字段说明：
   - timestamp: 统一格式化为 ISO8601。
   - level: 统一大写 (ERROR, WARN, CRITICAL)。
   - service: 涉及的服务或组件名（如 DB-01, PaymentGateway）。
" > analysis_result.json
```

**验证方法**：运行完这行命令，直接用 `cat analysis_result.json | jq .` 检查。如果 `jq` 报错，说明你的 Prompt 协议还没锁死。

## 验收清单 & 炸弹排查

在交付 Prompt 之前，过一遍这个清单。如果有一项没过，这就是个残次品。

1.  **解析器友好性**：如果是给机器看的，有没有禁止 Markdown 代码块（````json <payload> `````）？这东西是解析器的噩梦。
2.  **Schema 锁死**：JSON 输出是否定义了 Schema？如果没有，模型今天叫 `user_name`，明天叫 `userName`，你的代码就崩了。
3.  **图片无字化**：生成示意图时，Negative Prompt 里有没有写死 `text, letters, watermark`？没有的话，等着看鬼画符吧。
4.  **兜底逻辑**：如果模型处理不了（比如输入为空），它会胡编乱造还是返回标准的 Error 结构？
5.  **去废话**：输出里还有没有 "好的，这是您要的表格" 这种废话？有就删掉，这都是干扰噪声。

上一章：[04-language.md](04-language.md) · 下一章：[06-feedback.md](06-feedback.md)

配方库：文本模板 [A-text-prompts.md](A-text-prompts.md) · 图片配置 [B-image-prompts.md](B-image-prompts.md)
