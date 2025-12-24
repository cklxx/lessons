# 提示词心智模型：正确性的定义与边界

绝对正确的 Prompt 不是追求“像人一样会说”，而是让模型输出在目标场景下**格式确定、依据可审计、失败可兜底**。

本章把提示词工程重新定义为软件工程的一部分：Prompt 是交付物，需要版本控制、验收门槛、回归样本与回滚机制。

![章节插图占位：提示词从聊天到交付](../../assets/books/flawless-expression/chapter-hero.svg)

## 先把幻觉掐死：你不是在“沟通”，你是在“定义接口”

很多人写 Prompt 的姿势像写朋友圈：先抒情，再许愿，最后祈祷模型懂你。你以为你在“表达”，模型只会把它当作一段噪声上下文，继续按概率补全它最熟悉的套路句式。

换句话说：**不写接口，你就只能赌采样。**

## 你将收获什么

- 一套提示词分级标准：什么时候可以写草稿，什么时候必须写到“机器可执行”。
- 一个 Prompt 合同模板：输入、输出协议、失败判定与回滚策略一次写清。
- 两个可复制示例：文本生成 Prompt（Gemini CLI）+ 图片生成 Prompt（输出为文生图提示词文本）。
- 一份复现检查清单：提交 Prompt 前先做“静态审查”。
- 三条失败样本：话痨输出、幻觉补全、逻辑跳步（含复现与修复）。

## 提示词正确性的三个等级

你不需要把所有 Prompt 都写成“生产级”。按下游容错率分三档：

### Level 1：草稿级（Draft）

- 场景：个人探索、头脑风暴、一次性生成。
- 验收：人能看懂即可；允许多轮澄清；允许结构不稳定。
- 风险：不可复用；不可接入自动化。

### Level 2：协作级（Collaboration）

- 场景：团队内部复用、文档产出、批量内容生产。
- 验收：结构一致（标题层级/表格列/字段名稳定），别人照着就能用。
- 风险：若进入下游流程（脚本/Agent），需要升级到 Level 3。

### Level 3：机器执行级（Machine Execution）

- 场景：API 输出、Agent 工具链、CI 批处理、任何需要解析器消费的输出。
- 验收：语法零容忍：严格遵循 JSON/Schema 或固定 Markdown 模板；失败必须可检测（退出码/错误码/关键字）。
- 风险：不写失败判定与回滚，就是把事故写进系统默认值。

## 核心工具：Prompt 合同模板（先写验收，再写正文）

不要直接开始“写 Prompt 正文”。先把它当作合同填一遍，缺字段就不允许进入协作或机器执行。

```markdown
### Prompt 交付合同

| 维度 | 定义/约束 |
| :--- | :--- |
| ID & Version | <例如：prompt.code_review.v1> |
| 级别 | Draft / Collaboration / Machine Execution |
| 任务 | <一句话：要模型完成什么> |
| 受众 | <人类读者/解析器/下游系统> |
| 输入契约 | 格式：<纯文本/Markdown/JSON>；必填字段：<...>；最大长度：<...> |
| 输出契约 | 格式：<Markdown/JSON>；禁止出现：<寒暄语/多余解释/未定义字段> |
| 判定标准 | Pass/Fail 规则：<可脚本化的检查点> |
| 失败判定 | 命中即失败：<JSON 解析失败/缺关键字段/出现违禁短语> |
| 回滚/降级 | 失败后动作：<重试一次/降级为简版/返回固定错误结构> |
```

替换点：只替换 `<...>`，其余字段保持不变，避免每次写 Prompt 都变口径。

## 实战示例：文本生成 Prompt（可直接运行）

目标：生成一份“可解析、可审查”的代码审查报告；禁止客套话；无问题输出 `PASS`。

```bash
gemini -m gemini-3-pro-preview -p "
你是 Python 代码审查工具（不是聊天助手）。

输入：一段 Python 代码。
输出：只输出 Markdown（不要输出任何对话、问候、解释性前言）。

硬约束：
1) 若无明显问题，直接输出 PASS。
2) 若有问题，必须按固定结构输出（见下方模板），且表格列名不得改动。
3) 禁止输出推理过程；改为输出“审查依据列表”（最多 6 条）。

输出模板：

## 审查摘要
- 评分：<0-100>
- 状态：PASS/WARN/FAIL

## 问题清单
| 行号 | 级别 | 问题描述 | 建议修复 |
| --- | --- | --- | --- |

## 审查依据列表
1. <...>

代码：
```python
def fetch_data(url):
    import requests
    return requests.get(url).content
```
"
```

## 实战示例：图片生成 Prompt（输出为“文生图提示词文本”）

目标：为技术文档生成“系统架构示意图”的底图，禁止文字与水印，避免乱码风险。

```text
image_prompt:
technical sketch style, flat 2D vector art, minimal color palette (blue, white, grey), clean composition,
abstract software architecture diagram with three layers (client/server/database) represented by geometric shapes,
directional arrows showing data flow, high contrast, solid white background

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, 3d, isometric, photorealistic, shadow, blurry, messy lines, noisy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

### 配图提示词：三阶能力台阶（无文字底图）

如果你想给本章加一张“能力进阶”的插图，用台阶比“炫酷人物”更可靠：它不会误导读者，也更容易做成系列。

```text
image_prompt:
flat 2D vector illustration, three-step staircase made of simple geometric blocks, upward arrow suggesting progress, minimal tech style,
blue and white palette, solid white background, clean composition, high contrast, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 复现检查清单（提交前必过）

1. 是否清除了“尽快/适当/专业/好看”等模糊词，并改写为阈值/数量/窗口？
2. 是否明确了输出载体（Markdown/JSON/表格），并给了固定模板或 Schema？
3. 是否写清“不做什么”（禁止项），而不是只写“别废话”这种不可执行要求？
4. 是否要求输出审计线索（依据列表/检查点列表/不确定性清单），方便复核？
5. 是否包含失败判定（命中即失败）和降级/回滚动作（失败后做什么）？
6. 若涉及事实，请使用 [02-facts.md](02-facts.md) 的“拒答/举证/冲突并列”规则，而不是让模型补全常识。
7. 若是图片 Prompt，是否包含 `negative_prompt` 并明确 `no text` 语义（禁止文字/水印/签名）？

## 常见陷阱（失败样本）

### 1) 话痨输出（Chatty Output）

- 现象：要求输出 JSON/表格，模型在前后加“好的，这是结果”，导致解析失败。
- 根因：模型默认处于对话礼貌模式；你没把“输出纯净度”写成硬约束。
- 复现：只写“请输出 JSON”且不提供模板/禁止项。
- 修复：补充“只输出数据结构本体；禁止任何前后缀文本；禁止 Markdown 代码块包裹 JSON”。
- 回归验证：连续运行 10 次，输出可直接 `json.loads` 或按模板解析通过。

### 2) 幻觉补全（Hallucination Fill-in）

- 现象：输入缺少信息，模型仍给出确定结论或编造“来源/数字/术语解释”。
- 根因：你隐含传达了“必须回答”；没有给“未知出口”。
- 复现：提问一个只在你公司内部存在的库/流程，且不给上下文。
- 修复：加规则“仅基于提供材料；缺信息必须回答‘材料未提及/无法确认’，并列出需要补的输入字段”。
- 回归验证：输入缺关键字段时，模型输出“缺口清单”，而不是编造细节。

### 3) 逻辑跳步（Un-auditable Leap）

- 现象：模型给出决策结论，但无法指出依据来自哪里，或结论与依据不匹配。
- 根因：你只要结论，不要“检查点”；模型会跳到概率最高的答案句式。
- 复现：让模型做复杂判断题，但不要求输出结构化检查点。
- 修复：强制输出“依据列表/阈值检查/最终结论”三段式结构，且每段有固定字段。
- 回归验证：检查“阈值检查”与“最终结论”是否一致；不一致即判失败并回炉重写。

下一章：[02-facts.md](02-facts.md)
