# 语言与措辞：如何写不歧义的 Prompt（文本+图片）

即便你的目标正确、结构正确，模糊指令仍会让输出偏离预期。模型会用“概率最高的平庸解”填补你没写清的部分：你说“专业一点”，它可能堆术语；你说“好看一点”，它可能加光污染。

本章把自然语言升级为可执行指令：把形容词替换成参数，把隐含条件写成触发与排除条件，用示例与反例锁定口径。

![章节插图占位：把形容词变成参数](../../assets/books/flawless-expression/chapter-hero.svg)

## 你现在卡在哪里？

你发现模型总是“听不懂人话”：
- 你说“简明扼要”，它把关键数据删了。
- 你说“风格统一”，它第一张图是扁平风，第二张图突然变成了 3D。
- 你说“帮我润色”，它把你的原意改没了，还加了一堆客套话。

这不是模型笨，是你给的指令太“人类”。人类靠默契补全上下文，模型靠约束执行逻辑。你不写清，它就会猜。

**本章交付物：**
- **去歧义工作流**：扫描 → 替换 → 验收。
- **歧义扫描表**：把“优化/尽快/简洁/专业”翻译成计算机能懂的参数。
- **Prompt 语言四件套**：阈值、窗口、触发条件、排除条件。
- **作战模板**：直接可用的代码重构 Prompt 和风格一致的图片生成配置。

## 核心原则：把形容词替换为参数

停止使用形容词。形容词是主观的，参数是客观的。

### 歧义扫描与替换表（照着改）

别再说“适当”，模型不知道什么叫“适当”。

| 模糊指令（你是这么说的） | 模型理解（它是这么猜的） | 参数化替换（你应该这么写） |
| :--- | :--- | :--- |
| **简明扼要** | 删掉一切它觉得不重要的东西 | 字数 ≤ 200；必须包含 3 个核心结论；每点独立一行 |
| **专业一点** | 堆砌术语、装腔作势、过度客套 | 语气：技术说明书风格；禁止使用营销口号；必须包含 1 个代码示例 |
| **优化这段代码** | 随意重写，甚至改坏逻辑 | 目标：降低时间复杂度；守门员：接口签名不变；约束：通过现有单元测试 |
| **尽快** | 对模型毫无意义 | 输出顺序：先给结论，再给依据，最后给 3 个行动项 |
| **高对比度** | 霓虹灯配色、刺眼 | 限制色板：仅限蓝（#0000FF）、白（#FFFFFF）、灰；背景纯白；线条宽度固定 2px |

## Prompt 语言四件套（缺一项就会“猜”）

想让模型像程序一样稳定执行，你就得像写程序一样写 Prompt。

### 1) 阈值（Threshold）：多少算多？
- **错误**：找出高延迟请求。
- **正确**：列出响应时间 `> 500ms` 的请求。

### 2) 窗口（Window）：范围在哪里？
- **错误**：分析日志。
- **正确**：仅分析最后一次报错前的 100 行日志。

### 3) 触发条件（Trigger）：什么时候动手？
- **错误**：看着不对就报错。
- **正确**：当且仅当 `status_code != 200` 时，输出错误码与修复建议。

### 4) 排除条件（Exclusion）：绝对不要做什么？
这是最容易被忽略的。模型默认倾向于“多说点”。
- **错误**：别废话。
- **正确**：禁止输出引言；禁止输出总结；禁止输出‘希望这对你有帮助’；只输出 JSON 字符串；禁止用 Markdown 代码块包裹。

## 文本 Prompt 实战：代码重构协议

场景：你要让模型重构一段 Python 代码。普通的 Prompt 会导致它随意改动逻辑，或者删掉你需要的注释。

**错误示范**：
> 帮我看看这段代码，写得好一点，加上注释，别太长。

**正确示范（Gemini CLI 可执行版）**：

此命令将任务定义为一次严格的“代码审计”，并输出了回滚方案，直接存为文件。

```bash
gemini -m gemini-3-pro-preview -p "
角色：你是一个 Python 代码审计与重构工具。

输入：一段 Python 遗留代码。
目标：在不改变外部行为（接口签名、返回数据结构）的前提下，提升性能与可读性。

执行协议（四件套）：
1. 阈值：只有当时间复杂度能从 O(n^2) 降至 O(n log n) 或更低时，才允许修改算法逻辑。
2. 窗口：仅限修改内部实现，禁止修改函数名和参数列表。
3. 触发条件：如果发现魔法数字（Magic Numbers），必须提取为常量。
4. 排除条件：
   - 禁止删除原有的异常处理逻辑（try-except）。
   - 禁止修改日志打印格式。
   - 禁止输出任何闲聊（如'好的，这是代码'）。

输出格式（Markdown）：
## 重构后代码
\`\`\`python
<代码块>
\`\`\`

## 改动清单
- [行号] <原逻辑> -> <新逻辑> (原因)

## 回滚策略
<如果新代码导致崩溃，如何用 1 行命令切回旧版本>

待处理代码：
def process_data(data):
    res = []
    for i in data:
        if i in res: continue
        res.append(i)
    return res
" > refactored_code.md
```

## 图片 Prompt 实战：风格一致性控制

做图最怕“抽卡”。第一张图很完美，第二张图风格全变了。
解决办法：把 Prompt 拆解为“风格底座”（不变）+“主体变量”（变）+“负面约束”（不变）。

### 核心技巧
- **风格底座**：所有图共用这一段，一个字都别改。
- **负面约束**：这是防守底线，必须包含 text, watermark 等。

### 案例：生成一套“云原生架构”系列配图

所有配图必须看起来像出自同一个设计师之手。

**变体 A：数据处理模块**

```text
image_prompt:
subject: a stylized server rack processing geometric data blocks flowing through arrows
style: flat vector art, minimalist tech style, thin blue line art on white background, clean composition, high contrast, 4k

negative_prompt:
text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces, complex details

params:
aspect_ratio=16:9
```

**变体 B：安全防护模块**

```text
image_prompt:
subject: a digital shield hovering over a locked folder, encryption symbolism, geometric shapes
style: flat vector art, minimalist tech style, thin blue line art on white background, clean composition, high contrast, 4k

negative_prompt:
text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces, complex details

params:
aspect_ratio=16:9
```

**注意**：上面两段 Prompt 中，只有 `subject` 在变，`style` 和 `negative_prompt` 完全一致。这就是一致性的来源。

### 视觉隐喻：参数化仪表盘

不要让人脸出现在技术文档里，难以控制且容易恐怖谷。用仪表盘作为隐喻。

```text
image_prompt:
flat 2D vector illustration, minimalist dashboard with dials, sliders and toggle switches represented by simple geometric shapes,
blue and white palette, solid white background, clean composition, high contrast, no text, UI elements only

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, shadows, blur, messy background, humans, faces, organic shapes

params:
aspect_ratio=16:9, quality=high
```

![图示：参数化仪表盘示例](../../assets/books/flawless-expression/placeholder-diagram.svg)

## 防呆检查清单（Self-Defense Checklist）

在按下回车之前，扫一眼这个清单。如果有一项没做到，你的 Prompt 就是“赌博”。

1.  **形容词查杀**：还有没有“简洁”、“适当”、“好看”这种词？换成数字或标准参考系了吗？
2.  **边界锁定**：有没有写清“什么不该做”？（Negative Prompt / Exclusion Criteria）。
3.  **格式硬编码**：输出是 JSON、Markdown 还是 CSV？有没有禁止 Markdown 代码块包裹（如果是给程序读的话）？
4.  **失败兜底**：如果模型做不到（比如找不到数据），是让它编一个，还是输出 `NULL`？你定义了吗？
5.  **上下文隔离**：有没有告诉模型“只使用我提供的信息，不要使用你的外部知识库”？（防止幻觉）。

## 常见失败模式（别踩坑）

### 1. 幻觉式扩写
- **现象**：让你总结会议纪要，结果它编造了参会人没说过的话。
- **病因**：你说了“补充细节”或“使其更完整”。
- **解药**：显式约束“严格基于输入文本；缺失信息输出 <UNKNOWN>；禁止引入外部事实”。

### 2. 风格漂移
- **现象**：系列图风格不统一。
- **病因**：每次 Prompt 都是手敲的，形容词顺序不一样，或者漏了 negative prompt。
- **解药**：建立 Prompt 库，复制粘贴“风格底座”。如果工具支持，锁定 Seed。

### 3. 指令遗忘（长文本灾难）
- **现象**：输入太长，模型忘了你最后要求的“输出 JSON 格式”。
- **病因**：关键约束被埋在了长篇大论的背景资料里。
- **解药**：三明治结构。
    1.  **背景/角色**（开头）。
    2.  **输入数据**（中间）。
    3.  **输出协议/格式约束**（必须放在最后，因为模型有近因效应）。

上一章：[03-argument.md](03-argument.md) · 下一章：[05-medium.md](05-medium.md)
