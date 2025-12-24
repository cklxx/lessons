# 序章：提示词不是咒语，是交付物

**你现在卡在哪：** 你觉得 AI 时灵时不灵，写 Prompt 像在抽卡，每次上线都提心吊胆。  
**这章能救你什么：** 让你认清 Prompt 是接口，是工程交付物，必须能测试、能回滚、能复现。  
**本章交付物：** 两个文本 Prompt 标准模板、一个图片 Prompt 配置块、一条 CLI 最小闭环命令。

如果你抱着寻找“让模型瞬间听话的魔法咒语”的心态打开这本书，**请现在就停下来**。市面上大多数所谓 Prompt 教程，本质是把偶然的成功包装成方法论：教你堆情绪、堆形容词、堆段子，最后交付一份“看上去很努力”的聊天记录。

这不是无害的低效，这是**工程事故的源头**。你把不确定性塞进流程默认值里，然后指望上线后它自己变稳定。别做梦了。

本书只做一件事：把提示词从“聊天技巧”拉回“工程交付”。

你将学会用同一套标准写两类 Prompt：

1. **文本生成 Prompt**：输出稳定的 Markdown/JSON/表格/代码，能被脚本直接消费，而不是拿来读的。
2. **图片生成 Prompt**：输出可复用的“文生图配置”（含负向提示词与参数），生成无文字底图，把信息表达交给构图，把文字交给后期叠加。

![序章插图：从玄学到工程](../../assets/books/flawless-expression/prologue-hero.svg)

## 你以为你在写 Prompt，其实你在赌博（尖锐批判）

承认吧，你现在的开发流程大概率是这样的：

1. **你在赌采样**：不写严格的输出协议与失败判定，把解析失败交给运气。
2. **你在堆垃圾**：以为写得越长越详细越专业，其实只是把矛盾堆在一起，让模型挑它最爱的一段执行。
3. **你在偷懒**：写“专业一点、好看一点、尽快”，这不叫约束，这叫情绪宣泄。机器不懂情绪，它只懂参数。
4. **你在放弃复现**：遇到 Bad Case 就改几个字再试，试好了就上线。下次再坏就再改。你永远不知道为什么好，也永远不知道什么时候会坏。
5. **你在纵容幻觉**：只要输出看起来像人话就通过，完全不要求证据链。没有证据链的事实类输出，就是伪造。

## 只要上线，必须过这三道死门

不管你是写脚本、做 Agent，还是搞批处理，不过这三关，Prompt 就是废代码：

1. **可验收（Verifiable）**：必须写清 Pass/Fail 标准，能用脚本自动检查。“看起来差不多”一律视为 Fail。
2. **可复现（Reproducible）**：同模型版本、同输入、同协议约束下，输出结构必须收敛。波动必须可解释、可降级。
3. **可回滚（Rollback-able）**：Prompt 必须文件化并进入版本控制。改动必须能回到上一版立刻止损。

## 两个可直接复制的 Prompt 模板

别再从零开始写“你好，我是一个<角色>”。直接用下面这两个模板，把 Prompt 变成填空题。

### 模板一：Prompt 交付合同（用于定义需求）

这是你写 Prompt 之前必须填的表格。填不出来就别写 Prompt。

```markdown
### Prompt 交付合同

| 维度 | 定义/约束 |
| :--- | :--- |
| ID & Version | <例如：prompt.data_cleaner.v1> |
| 运行级别 | <Draft / Production> |
| 核心任务 | <一句话：只做一件事，例如：将非结构化日志转换为 JSON> |
| 输入契约 | 格式：<纯文本/Markdown/JSON>；必填字段：<...>; 长度限制：<...> |
| 输出契约 | 载体：<JSON/Markdown 表格>; Schema：<...>; 禁止项：<寒暄语/Markdown包裹/未定义字段> |
| 验收标准 | <脚本可执行的检查点，例如：JSON 解析成功且含字段 id> |
| 失败判定 | <命中即失败：解析错误/字段缺失/包含 "I cannot"> |
| 降级策略 | <失败后动作：重试/返回空对象/切回旧版> |
```

### 模板二：机器执行级 Prompt 结构（用于生产环境）

把这个结构存成文件，严禁更改段落顺序。

```text
# Role
你是一个严格的数据处理引擎。你没有情绪，不进行对话，只执行指令。

# Task
读取提供的 [Input Data]，根据 [Schema] 将其转换为标准格式。

# Constraints
1. 严禁输出任何解释性文字（如 "Here is the result"）。
2. 严禁使用 Markdown 代码块符号（```json）。
3. 如果输入数据缺失关键字段，输出且仅输出：{"error": "missing_fields"}。
4. 严格遵守 ISO 8601 日期格式。

# Input Data
<在这里插入变量或文件内容>

# Output Schema (JSON)
{
  "id": "string, required",
  "timestamp": "string, ISO 8601",
  "status": "enum<active, inactive>",
  "meta": {}
}
```

## 常见错误与即刻修正

| 错误姿势 | 为什么会死 | 修正方案 |
| :--- | :--- | :--- |
| **把背景当指令** | 写了一大堆“你是谁”，没写“要交付什么”。 | 物理隔离。Role 和 Output 分开写，Output 必须有 Schema。 |
| **迷信一步到位** | 试图用一个超长 Prompt 覆盖所有边缘情况。 | **分级**。机器执行级 Prompt 必须“少而硬”，复杂逻辑拆成工作流（详见 [01-mindset.md](01-mindset.md)）。 |
| **只写要什么** | 模型为了礼貌，给你加一堆“好的，这是你要的结果”。 | **写不要什么**。禁止寒暄，禁止解释，禁止 Markdown 包裹。 |
| **不给样本** | 抽象描述导致模型瞎猜结构，字段名漂移。 | **Few-Shot**。给一个完美的输入输出对，告诉它照着做，别发挥。 |
| **聊天框调试** | 复制粘贴试几次，凭感觉上线。 | **CLI + 门禁**。建立回归测试集，每次改动必须跑通所有 Case（详见 [06-feedback.md](06-feedback.md)）。 |

## 最小闭环：Gemini CLI 实战

把 Prompt 当文件，把输入当文件，把输出落盘。这就是工程。

假设你保存了上面的模板二为 `prompts/cleaner.txt`，输入数据在 `data/input.txt`。

```bash
gemini -m gemini-3-pro-preview -p "$( { cat prompts/cleaner.txt; printf '\n\n'; cat data/input.txt; } )" > out/result.json
```

如果你不能把一次运行的结果存成文件、跟上一次结果做 diff 对比，你就没资格说自己在做工程。

## 图片 Prompt 交付物：拒绝文字底图

你需要的不是“酷炫的画”，而是**可复用的素材**。文字直接印在图上是后期噩梦。

**标准图片 Prompt 配置块（直接喂给生图工具）：**

```text
image_prompt:
flat 2D vector illustration, split-screen concept, left side chaotic abstract swirls and noisy shapes representing uncertainty, right side clean structured blocks and checklists representing engineering order,
blue and white palette, minimalist composition, solid white background, high contrast, crisp edges, ample whitespace for later typography, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces, distorted shapes

params:
aspect_ratio=16:9, quality=high
```

请注意：**negative_prompt 里的 `text, letters, numbers` 是必须项**。

下一页先读总览：[index.md](index.md)
