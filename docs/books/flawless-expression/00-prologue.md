# 序章：提示词不是咒语，是交付物

如果你抱着寻找“让模型瞬间听话的魔法咒语”的心态打开这本书，请现在就停下来。市面上大多数所谓 Prompt 教程，本质是把偶然成功包装成方法论：教你堆情绪、堆形容词、堆段子，最后交付一份“看上去很努力”的聊天记录。

这不是无害的低效，这是**工程事故的源头**：你把不确定性塞进了流程默认值，然后指望上线后它自己变稳定。

本书只做一件事：把提示词从“聊天技巧”拉回“工程交付”。

你将用同一套标准写两类 Prompt：

- **文本生成 Prompt**：输出稳定的 Markdown/JSON/表格/代码，能被脚本消费。
- **图片生成 Prompt**：输出可复用的“文生图提示词文本”（含 negative prompt 与参数建议），生成无文字底图，关键文字后期叠加。

![序章插图占位：从咒语到交付物](../../assets/books/flawless-expression/prologue-hero.svg)

## 你需要先接受的残酷事实（尖锐批判）

1. **你以为你在“写 Prompt”，其实你在“赌采样”。** 不写输出协议与失败判定，就是把解析失败交给运气。
2. **你以为“更长更详细”更专业，其实只是把矛盾堆在一起。** 超长 Prompt 常见结局是：模型挑它最爱的一段执行，其余当噪声。
3. **你以为“模型会懂”，其实你在偷懒。** “专业一点/好看一点/尽快”不是约束，是情绪表达。
4. **你以为“多试几次就行”，其实你在放弃复现。** 不能复现的问题无法修；无法修的问题只能祈祷。
5. **你以为“输出看起来对就够了”，其实你在给幻觉开绿灯。** 事实类输出没有证据链，就是伪造。

## 本书的三条底线

只要你想把 Prompt 接进流程（脚本、Agent、批处理、交付给别人复用），就必须过这三道门：

1. **可验收**：写清 Pass/Fail，能脚本化检查；“差不多”一律视为 Fail。
2. **可复现**：同模型版本、同输入、同协议约束下，输出结构必须收敛；波动必须可解释、可降级。
3. **可回滚**：Prompt 必须文件化、可版本控制；改动必须可回到上一版立刻止损。

## 你最常犯的五个错误（以及怎么修）

1) **把背景当指令**
- 现象：写了很多“你是谁”，却没把“要交付什么”写成协议。
- 修复：把 Prompt 分成 Role/Task/Constraints/Output 四段，段落顺序固定；数据与指令物理隔离。

2) **迷信一步到位**
- 现象：试图用一段超长 Prompt 覆盖所有边缘情况，结果每次改动都引入新退化。
- 修复：分级（见 [01-mindset.md](01-mindset.md)）；机器执行级 Prompt 必须“少而硬”，复杂性转移到流程与回归。

3) **只写“要什么”，不写“不要什么”**
- 现象：输出夹带寒暄语、解释性前言、Markdown 代码块包裹，导致解析失败。
- 修复：把禁止项写成硬约束与失败判定；对图片 Prompt 必须默认禁止文字、数字、水印。

4) **不提供可复用样本**
- 现象：你用抽象描述要求复杂格式，模型按概率猜结构，字段名漂移。
- 修复：提供一个“完美输出样例”或模板；字段顺序与命名不可变（宁可少也不要变）。

5) **在聊天界面调试生产**
- 现象：复制粘贴试几次“看起来差不多”就上线。
- 修复：建立回归集与门禁（见 [06-feedback.md](06-feedback.md)）；每次改 Prompt 先跑回归再发布。

## 最小可行单元：Prompt 交付合同（可复制）

不要直接“写正文”。先写合同：你要的不是漂亮语言，而是稳定接口。

```markdown
### Prompt 交付合同

| 维度 | 定义/约束 |
| :--- | :--- |
| ID & Version | <例如：prompt.extract.errors.v1> |
| 级别 | Draft / Collaboration / Machine Execution |
| 任务 | <一句话：只做一件事> |
| 输入契约 | 格式 <纯文本/Markdown/JSON>；必填字段 <...>；最大长度 <...> |
| 输出契约 | 载体 <Markdown/JSON/表格>；模板/Schema <...>；禁止出现 <寒暄语/额外解释/未定义字段> |
| 判定标准 | Pass/Fail 规则 <可脚本化检查点> |
| 失败判定 | 命中即失败 <解析失败/缺字段/禁用短语> |
| 回滚/降级 | 失败后动作 <重试一次/降级简版/返回固定错误结构/切回旧版本> |
```

只替换 `<...>`，不要改字段名与顺序。稳定来自一致性，不来自灵感。

## Gemini CLI：最小可复现闭环

把 Prompt 当文件，而不是当聊天记录。最小闭环是：Prompt 文件 + 输入文件 + 输出落盘。

```bash
MODEL="gemini-3-pro-preview"
PROMPT_FILE="prompts/prompt.txt"
INPUT_FILE="cases/input.txt"

gemini -m "$MODEL" -p "$( { cat "$PROMPT_FILE"; printf '\n\n输入：\n'; cat "$INPUT_FILE"; } )" > out/result.md
```

如果你不能把一次结果落盘、复跑、对比、回滚，你就不配把它叫“工程”。

## 配图建议（占位图 + 图片 Prompt 文本）

你需要的不是“酷炫配图”，而是**可复用的系列底图**：无文字、风格统一、信息用构图表达，关键文字后期叠加。

用于生成本章配图的图片 Prompt 文本（输出给你的生图工具）：

```text
image_prompt:
flat 2D vector illustration, split-screen concept, left side chaotic abstract swirls and noisy shapes, right side clean structured blocks and checklists,
blue and white palette, minimalist composition, solid white background, high contrast, crisp edges, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

下一页先读总览：[index.md](index.md)
