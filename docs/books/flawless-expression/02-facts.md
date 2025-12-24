# 事实与知识：如何写“可核查/可溯源”的 Prompt

事实类输出最致命的缺陷不是文笔差，而是“一本正经地编造”。当你要求模型生成非虚构内容时，Prompt 必须像一份审计合同：**不知道就说不知道，有结论必能举证，有冲突就并列展示**。

![章节插图占位：证据矩阵与审计账本](../../assets/books/flawless-expression/chapter-hero.svg)

## 你将收获什么

- 一套“拒答/追问/标注不确定性”的指令规则，让模型不再硬凑答案。
- 一个可复制的证据矩阵模板：结论、证据、来源标识、冲突备注一次对齐。
- 一种冲突证据处理策略：不求平均、不替人裁决，优先把矛盾摊在桌面上。
- 一份发布前自检清单：覆盖文本事实与图片“文字乱码”两类高频事故。

## 三条铁律：未知出口、证据矩阵、冲突并列

1) 未知出口：材料缺失时必须输出“材料未提及/无法确认”，并列出缺口字段；禁止补全常识。

2) 证据矩阵：任何关键结论必须绑定到“最小证据单元”（输入片段、文档段落、数据行、条款条目等）。

3) 冲突并列：当不同来源不一致，必须并列展示差异与可能原因（口径/时间窗/样本/环境），由人类裁决。

## 文本生成：拒答、追问与不确定性标注

把“安全出口”写进 Prompt，是防幻觉的关键。你需要明确告诉模型：回答不了不是失败，编造才是失败。

推荐写法（可复制到任何事实类 Prompt 的顶部）：

```text
事实规则：
1) 仅基于“输入材料”回答；禁止引入外部知识补全。
2) 若材料不足：输出“材料未提及/无法确认”，并列出需要补充的字段清单。
3) 若存在冲突：并列展示冲突来源与差异点；禁止擅自取平均或选择其一。
4) 对推断内容必须标注不确定性：高/中/低，并说明不确定性来自哪里（缺字段/样本不足/口径不一致）。
```

## 证据矩阵模板（必交付）

证据矩阵不是“引用列表”，而是“结论的审计账本”。表填不出来，就说明结论还不能发布。

```markdown
| claim_id | 结论（命题一句话） | 证据（最小单元） | 来源标识（文件/章节/片段 id） | 冲突/反例 | 不确定性 |
| ---: | --- | --- | --- | --- | --- |
| 1 | <...> | <...> | <...> | <无则留空> | 高/中/低 |
```

替换点：只替换 `<...>`，不要新增列名（列名稳定比“更全面”更重要）。

### 配图提示词：证据矩阵的“账本”隐喻（无文字底图）

证据矩阵本质是审计账本。配图不要画复杂表格文字，画“账本 + 标签 + 勾叉”的隐喻就够了。

```text
image_prompt:
flat 2D vector illustration, minimalist ledger book and stacked cards representing evidence units, simple tags and checkmark/cross icons as shapes,
blue and white palette, solid white background, clean composition, high contrast, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 冲突证据处理策略（别让模型替你裁判）

当来源冲突时，Prompt 里要明确模型的职责边界：它负责“整理矛盾”，不负责“替你选边”。

可复制的指令片段：

```text
冲突处理规则：
1) 如果同一结论出现多个互相矛盾的来源：按来源分行并列，不合并。
2) 每条冲突必须补一列“差异原因猜测”（口径/时间窗/样本/环境），但必须标记为推断。
3) 只输出整理结果；不要给最终裁决建议（除非我显式要求）。
```

## 文本 Prompt 示例（可直接运行）

目标：把输入材料整理成证据矩阵，并允许输出“缺口清单”。

```bash
gemini -m gemini-3-pro-preview -p "
任务：基于输入材料，生成一张证据矩阵（Markdown 表格）。

硬约束：
1) 仅基于输入材料回答；禁止外部补全。
2) 缺信息就输出‘材料未提及/无法确认’，并列出缺口字段清单。
3) 发现冲突就并列，不要调和。

输出：
1) 先输出证据矩阵表格（列名固定：claim_id/结论/证据/来源标识/冲突/不确定性）。
2) 再输出‘缺口字段清单’（若为空则输出‘无’）。

输入材料：
<把你的资料片段粘贴在这里，建议包含来源标识>
"
```

## 图片生成：事实类图片的核心是“禁止文字”

图片模型最常见的事故是生成“伪文字/乱码”。事实类图片 Prompt 的正确做法是：**把文字从生成任务里移除**——先生成干净底图，再用人工/矢量工具叠加真正的文字与数字。

### 图片 Prompt 示例：技术示意图底图（无文字）

```text
image_prompt:
clean minimalist technical diagram, flat vector style, blue and white palette, solid white background,
abstract server blocks and database cylinders connected by arrows showing data flow, simple geometric data packets, high contrast

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, blurry, noisy background, photorealistic, 3d render, gradients, shadows, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 复现检查清单（发布前必核）

1. 拒答测试：Prompt 是否明确允许输出“材料未提及/无法确认”？
2. 证据矩阵：是否要求每条结论都绑定最小证据单元与来源标识？
3. 抽查复核：随机抽查 3 条结论，能否在输入材料中定位到对应证据？
4. 冲突处理：Prompt 是否要求并列展示冲突而非调和？
5. 不确定性：是否要求对推断内容标注高/中/低并说明来源？
6. 图片净化：图片 Prompt 是否包含 `negative_prompt` 并明确禁止文字/水印/签名？

## 常见陷阱（失败样本）

### 1) 强迫式幻觉

- 现象：材料覆盖不到的时间段/范围，模型仍给出确定答案。
- 根因：Prompt 暗示“一定有答案”，且没有未知出口。
- 复现：提问一个材料中不存在的事实，看模型是否开始补全常识。
- 修复：加入“若材料不足必须拒答 + 缺口字段清单”；并把“编造”写成失败判定。
- 回归验证：同一缺口输入下，模型稳定输出“无法确认 + 缺口字段清单”。

### 2) 伪造引用

- 现象：输出看似有理有据，但引用的来源标识不存在或无法对应到输入材料。
- 根因：Prompt 要求“给来源”，但没要求“来源必须来自输入材料集合”。
- 复现：不提供材料，要求“写一篇带引用的报告”，模型会生成看起来真实的引用。
- 修复：约束“来源标识必须来自输入材料中出现过的标识”；缺标识则拒答。
- 回归验证：所有来源标识都可在输入中被检索到，且能定位到具体片段。

### 3) 图片外星文字

- 现象：示意图中出现不可读的字母或类似水印的乱码。
- 根因：Prompt 让模型生成“带文字的仪表盘/架构图”，触发模型的弱项。
- 复现：Prompt 含 “dashboard with detailed metrics text” 或 “label every component”.
- 修复：改成“无文字底图 + 后期叠字”；并在 negative prompt 中明确禁止 text/letters/numbers/watermark。
- 回归验证：连续生成多张底图均无可见字符，适合作为后期叠字底稿。

下一章：[03-argument.md](03-argument.md)
