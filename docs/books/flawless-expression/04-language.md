# 语言与措辞：如何写不歧义的 Prompt（文本+图片）

即便你的目标正确、结构正确，模糊指令仍会让输出偏离预期。模型会用“概率最高的平庸解”填补你没写清的部分：你说“专业一点”，它可能堆术语；你说“好看一点”，它可能加光污染。

本章把自然语言升级为可执行指令：把形容词替换成参数，把隐含条件写成触发/排除条件，用示例与反例锁定口径。

## 你将收获什么

- 一套去歧义工作流：扫描 → 替换 → 验收。
- 一张歧义扫描与替换表：把“优化/尽快/简洁/专业/高对比”等改成可裁决参数。
- Prompt 语言四件套：阈值/窗口/触发条件/排除条件的写法（文本与图片通用）。
- 一个可复制示例：把模糊需求改写为可执行 Prompt（Gemini CLI）。
- 一个可复制示例：同主题 3 个“风格一致但可控差异”的图片 Prompt 变体。

## 核心原则：把形容词替换为参数

人类靠默契补全，模型靠约束执行。你不写清，它就会猜。

### 歧义扫描与替换表（可复制）

| 模糊词 | 模型可能误解 | 参数化替换（阈值/窗口/条件/数量） |
| :--- | :--- | :--- |
| 简明扼要 | 删掉关键步骤或证据 | 字数 ≤ 200；必须包含 3 个要点；每点一行 |
| 专业 | 堆术语/装腔/过度客套 | 语气：技术说明；禁止口号；给出 1 个可执行例子 |
| 优化 | 随意大改引入副作用 | 主指标：<...>；守门：<...>；接口/语义保持不变 |
| 尽快 | 对模型无意义 | 输出顺序：先结论、后依据、最后行动项（最多 5 条） |
| 适当 | 无法裁决 | 阈值：P95 ≤ <...>；窗口：连续 <...> 分钟 |
| 高对比度 | 变成霓虹/刺眼 | 固定配色：蓝白灰；背景纯白；线条粗细固定 |

## Prompt 语言四件套（缺一项就会“猜”）

1) 阈值（Threshold）：多少算多，多少算少。
- 错：列出高延迟请求。
- 对：列出响应时间 `> 500ms` 的请求。

2) 窗口（Window）：在什么范围内生效。
- 错：分析日志。
- 对：分析最近 200 行，或最后一次报错后的 100 行。

3) 触发条件（Trigger）：什么情况下做动作 A。
- 错：如果看着不对就报错。
- 对：当且仅当 `status != success` 时输出错误码与修复建议。

4) 排除条件（Exclusion / Negative）：绝对不要做什么。
- 错：别废话。
- 对：禁止引言/总结/客套话；只输出 JSON；禁止 Markdown 代码块包裹 JSON。

## 文本 Prompt 实战：把模糊需求改写为可执行协议

场景：你要让模型重构一段 Python 代码并解释原因。

原始模糊版：

> 帮我看看这段代码，写得好一点，加上注释，别太长。

结构化改写版（可直接运行）：

```bash
gemini -m gemini-3-pro-preview -p "
你是 Python 代码审计工具（不是聊天助手）。

输入：一段 Python 代码。
任务：在不改变外部行为的前提下提升性能与可读性。

四件套约束：
1) 阈值：把最差时间复杂度从 O(n^2) 降到 O(n log n) 或更好（若做不到就说明原因并给替代方案）。
2) 窗口：只允许改动函数 process_data；其他函数签名与返回结构必须保持不变。
3) 触发条件：只有发现可向量化或可用数据结构替代时才允许引入新依赖；否则仅用标准库。
4) 排除条件：禁止删除异常处理；禁止改输入格式；禁止改字段名。

输出格式（顺序固定）：
1) 先输出重构后的完整代码块。
2) 再输出‘改动点列表’（3 条，每条一行）。
3) 再输出‘回滚说明’（一行：如何撤回到旧逻辑）。

代码：
<把你的代码粘贴在这里>
"
```

## 图片 Prompt 实战：同主题 3 变体（风格一致但可控差异）

核心技巧：固定“风格底座”，只改“主体变量”，并继承同一份 negative prompt。

风格底座（所有变体共享）：

```text
flat vector art, minimalist tech style, thin blue line art on white background, clean composition, high contrast, 4k
```

negative prompt（所有变体共享）：

```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces
```

变体 A（数据处理）：

```text
subject: a stylized server rack processing geometric data blocks flowing through arrows
style: flat vector art, minimalist tech style, thin blue line art on white background, clean composition, high contrast, 4k
negative_prompt: text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces
params: aspect_ratio=16:9
```

变体 B（安全防护）：

```text
subject: a digital shield hovering over a locked folder, encryption symbolism, geometric shapes
style: flat vector art, minimalist tech style, thin blue line art on white background, clean composition, high contrast, 4k
negative_prompt: text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces
params: aspect_ratio=16:9
```

变体 C（云端部署）：

```text
subject: a simplified cloud icon with an upward arrow launching a rocket, abstract deployment metaphor
style: flat vector art, minimalist tech style, thin blue line art on white background, clean composition, high contrast, 4k
negative_prompt: text, letters, numbers, watermark, signature, photorealistic, 3d render, shading, gradients, blur, messy background, humans, faces
params: aspect_ratio=16:9
```

## 复现检查清单（防呆测试）

1. 是否把模糊词替换成参数（阈值/数量/窗口）？
2. 是否写清了“不做什么”（排除条件/negative prompt）？
3. 是否锁定了输出载体与模板（Markdown/JSON/表格）？
4. 是否把关键约束放在显眼位置（不要埋在长背景里）？
5. 是否定义了失败判定与回滚说明（失败后做什么）？

## 常见陷阱（失败样本）

### 1) 幻觉式扩写

- 现象：总结/改写时编造原文没有的数据或引语。
- 根因：Prompt 写了“丰富/补充背景”，但没写“仅基于输入材料”。
- 复现：给一段短文并要求“更具说服力”，模型会补常识与虚构例子。
- 修复：加入“严格基于输入；缺信息输出未知；禁止引入外部事实”。
- 回归验证：输入缺关键字段时输出缺口清单，而不是补全。

### 2) 风格漂移

- 现象：系列图片第一张扁平，第二张突然 3D 或带阴影渐变。
- 根因：风格底座不稳定，negative prompt 不继承或不够强。
- 复现：连续生成同主题图片，但每次只写“科技感图标”。
- 修复：固定风格底座 + 继承 negative prompt；需要时锁定 seed（工具支持才用）。
- 回归验证：把 10 张图平铺对比，线条/色板/光影一致。

### 3) 指令遗忘

- 现象：Prompt 很长，模型忽略了结尾的输出格式要求。
- 根因：关键约束被埋在背景里；缺少结构化标题定界。
- 复现：把输出格式写在中间段落，模型容易漏。
- 修复：用“背景在前、数据在中、输出协议在最后”的三明治结构；用标题明确 `Output Format`。
- 回归验证：多轮/长输入下仍能稳定产出符合协议的结果。

上一章：[03-argument.md](03-argument.md) · 下一章：[05-medium.md](05-medium.md)
