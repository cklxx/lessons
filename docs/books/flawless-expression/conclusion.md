# 结语：把提示词当成代码交付（文本+图片）

提示词工程不是玄学，别再像求签一样对着模型祈祷了。这是一门严肃的工程学科：版本控制、回归测试、发布门禁、回滚预案，这些软件工程的铁律，在提示词里一样都不能少。

当你把 Prompt 当成正式的交付物（Deliverable），而不是随手敲在聊天框里的一次性垃圾，你就掌握了“可复刻、高质量输出”的核心能力。

![结语插图：把提示词变成标准交付物](../../assets/books/flawless-expression/chapter-hero.svg)

## 你现在的军火库（最小资产包）

如果前面的章节你都忘了，至少把这六样武器带走。它们是你对抗“随机性”和“幻觉”的底气：

1.  **分级标准**：动手前先定级。是写个草稿，还是要进生产环境？（详见 [01-mindset.md](01-mindset.md)）
2.  **事实矩阵**：不准编造。要么有证据，要么闭嘴，要么列出冲突。（详见 [02-facts.md](02-facts.md)）
3.  **论证骨架**：结论必须可审计。逻辑链断了，结论就是废纸。（详见 [03-argument.md](03-argument.md)）
4.  **去歧义词表**：把形容词变成参数。别说“简洁”，要说“不超过50字”。（详见 [04-language.md](04-language.md)）
5.  **输出协议**：Markdown 是你的 API。锁死格式，下游系统才能活。（详见 [05-medium.md](05-medium.md)）
6.  **回归测试集**：失败是最好的肥料。把错题存进库里，下次发版前先跑一遍。（详见 [06-feedback.md](06-feedback.md)）

## 文本 Prompt 标准作业程序（SOP）

把下面的内容保存为 `PROMPT_SOP.md`。以后写任何生产级 Prompt，不要从零开始，直接填空。

### 模板 1：生产级任务通用 SOP

```markdown
# 生产级 Prompt 规范

## 0. 元数据（写给人类看的）
- **ID**: <PROMPT_ID_001>
- **版本**: v1.0.0
- **风险等级**: <生产环境/高风险>
- **受众**: <自动化脚本/API>

## 1. 契约（先定规矩，再谈任务）
- **输入约束**:
  - 格式必须是 <JSON/Markdown>。
  - 必填字段包括 <user_query, context_list>。
  - 长度超过 <2000 token> 截断。
- **输出约束**:
  - 必须返回 <JSON对象>。
  - 必须包含字段 <status, reasoning, result>。
  - 严禁包含 <Markdown代码块标记, 解释性废话>。
- **熔断机制**:
  - 如果缺少上下文，返回 <特定的错误码 ERR_NO_CONTEXT>。
  - 如果检测到敏感词，直接返回 <空对象>。

## 2. 核心指令（结构化指令）
- **角色**: 你是 <资深代码审计员>，不是 <助手>。
- **任务**: 对输入的 <代码片段> 进行 <安全性分析>。
- **步骤**:
  1.  检查 <SQL注入风险>。
  2.  检查 <硬编码密钥>。
  3.  输出 <分析报告>。

## 3. 验证（怎么证明你是对的）
- **回归样本**: <test_case_001.json> 应输出 <pass>。
- **A/B 策略**: 新版本上线前，需与基线版本 <v0.9> 对比 <误报率>。
```

### 模板 2：长文档生成专用 SOP

```markdown
# 长文档生成 Prompt 规范

## 1. 风格定义（Tone & Voice）
- **语气**: <专业、犀利、直接>。
- **禁语**: 禁止使用 <然而、综上所述、小编认为>。
- **句式**: 多用 <短句>，少用 <从句套从句>。

## 2. 结构骨架（Skeleton）
- **一级标题**: 必须包含 <背景、问题、方案、结论>。
- **段落**: 每段不超过 <5行>。
- **列表**: 只要超过 <3项> 并列内容，必须使用无序列表。

## 3. 内容填充规则
- **引用**: 所有数据必须来自 <提供的参考文档>，不得使用 <训练数据>。
- **占位**: 遇到不确定的数据，写 <DATA_MISSING>，不要编造。
```

## 图片 Prompt 标准作业程序（SOP）

记住铁律：**AI 画不好字**。图就是图，字是后期加上去的。

### 配图提示词：SOP 视觉化（无文字版）

```text
image_prompt:
flat vector illustration, a strict industrial assembly line for documents, robotic arms stamping "PASSED" or "REJECTED" icons on papers,
isometric view, clean lines, technical blueprint style, blue and white color scheme, minimal details, solid white background

negative_prompt:
text, letters, words, numbers, signature, watermark, handwriting, messy, cluttered, photorealistic, 3d render, shading, shadows, gradients, human faces, distortion

params:
aspect_ratio=16:9, quality=high
```

## 命令行实战（Gemini CLI）

把 Prompt 当代码跑。别在网页框里点来点去，用命令行让流程自动化。

**场景**：你写好了一个 `prompts/production_check.txt`，要把 `data/input_code.py` 作为输入传进去，并把结果存下来。

```bash
# 1. 准备输入
# 假设你的 prompt 里有一个占位符 <INPUT_CODE>
# 我们可以先用 sed 或者其他工具替换，或者直接把两个文件拼接
# 这里演示最简单的拼接方式

cat prompts/production_check.txt data/input_code.py > combined_prompt.txt

# 2. 执行 Gemini
# 注意：使用 -p 传入内容，指定模型，结果重定向到文件

gemini -m gemini-3-pro-preview -p "$(cat combined_prompt.txt)" > reports/audit_result_v1.md

# 3. (可选) 验证输出是否存在且不为空
if [ -s "reports/audit_result_v1.md" ]; then
    echo "Audit complete. Report saved."
else
    echo "Error: Output is empty."
    exit 1
fi
```

## 发布前 7 项死刑清单

上线前，对着这个清单过一遍。只要有一项不满足，就别发布，发了也是事故。

1.  **意图对齐**：Prompt 是不是还在猜谜？模糊的输入有没有拒答或者追问策略？
2.  **协议锁死**：输出格式（JSON/Markdown）锁死了吗？字段名变不变？下游解析器会不会挂？
3.  **废话过滤**：是不是还带着“好的，这是您的结果”这种寒暄？Markdown 代码块包裹去掉了吗？
4.  **事实熔断**：遇到不知道的事，是瞎编还是返回 `<UNKNOWN>`？证据链条完整吗？（见 [02-facts.md](02-facts.md)）
5.  **逻辑审计**：输出里有没有包含“思考过程”或“检查点”？让人类能看懂它是怎么错的。（见 [03-argument.md](03-argument.md)）
6.  **视觉纯净**：生图 Prompt 里是不是还没加 `text` 到负向提示词里？关键文字是不是还指望 AI 给你画出来？（见 [05-medium.md](05-medium.md)）
7.  **回归通过**：跑过回归测试集了吗？跟上个版本比，是不是变差了？回滚版本号记下来了吗？（见 [06-feedback.md](06-feedback.md)）

做到了这几点，你交付的就不是一堆聊天记录，而是可靠的软件资产。

回到目录：[index.md](index.md)
