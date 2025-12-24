# 附录 C：质量控制与复现清单（Prompt 版）

如果你把“优化 Prompt”理解为“改几个词然后看这一次输出挺顺眼”，那你不是在做工程，你是在玩老虎机。没有门禁与回归，任何改动都可能把系统从“偶尔能用”推到“稳定出错”。

这份清单的目标是把 Prompt 的质量控制变成可执行流程：**先验收、再改动、跑回归、过门禁、能回滚**。序章先读：[00-prologue.md](00-prologue.md)。

## 1) 发布门禁（Release Gate）

在把任何 Prompt 当作“可复用交付物”之前，必须通过以下检查。做不到就别上线。

### 文本 Prompt 门禁
- [ ] **载体明确**：输出是 Markdown/JSON/表格之一；禁止“随便写写”。
- [ ] **协议固定**：模板/Schema/列名固定；字段名与顺序不可变。
- [ ] **纯净度**：明确禁止寒暄语、解释性前言、无关总结；禁止 Markdown 代码块包裹 JSON。
- [ ] **未知出口**：材料不足时允许拒答并输出缺口字段清单；禁止编造补全。
- [ ] **失败判定**：命中即失败的规则可检测（解析失败/缺字段/禁用短语/证据缺失）。
- [ ] **回滚/降级**：失败后动作写清楚（重试一次/降级简版/返回固定错误结构/切回旧版本）。

### 图片 Prompt 门禁（无文字底图）
- [ ] **禁止文字**：negative prompt 必含 text/letters/numbers/watermark/signature；正文也明确 no text。
- [ ] **风格底座**：全书统一 style_base；每张图只改主体变量（见 [B-image-prompts.md](B-image-prompts.md)）。
- [ ] **留白充足**：预留叠字区域；禁止背景纹理过密导致文字不可读。
- [ ] **一致性回归**：固定锚点主体做对比（服务器/盾牌/云）；改风格先跑锚点验证（见 [06-feedback.md](06-feedback.md)）。

## 2) 回归集结构（建议）

Prompt 不做回归，只会出现两种结局：要么你不敢改，要么你改一次坏一次。回归集建议参考 [06-feedback.md](06-feedback.md) 的目录树，并补齐“验收真值”。

最小结构（示例）：

```text
prompts/
├── production/
│   └── prompt_x.v1.txt
└── regression/
    ├── case_chatty_json/
    │   ├── input.txt
    │   ├── prompt_base.txt
    │   ├── prompt_candidate.txt
    │   └── expected_rules.md
    ├── case_missing_fields/
    │   ├── input.txt
    │   ├── prompt_base.txt
    │   ├── prompt_candidate.txt
    │   └── expected_rules.md
    ├── run_batch.sh
    └── check_results.py
```

验收真值不要追求“完美答案”，要追求“可判定门禁”。你需要的是可预测失败，而不是漂亮文案。

## 3) 文本 Prompt 的三道门（建议顺序）

### 门一：格式门（Format）
- JSON：必须可解析；字段必须齐全；禁止新增字段。
- 表格：列名固定；行顺序可解释；空值统一写 N/A。
- Markdown：标题层级固定；清单每条一行；禁止长段散文。

### 门二：纯净度门（Purity）
- 禁用短语门禁：把“好的，这是”“希望对你有帮助”等写进断言。
- 包裹门禁：禁止 Markdown 代码块包裹 JSON；禁止在 JSON 前后加解释文本。

### 门三：事实门（Fact）
- 未知出口：材料不足必须拒答 + 缺口字段清单。
- 证据绑定：关键结论必须能定位到来源标识（证据矩阵与冲突并列见 [02-facts.md](02-facts.md)）。

## 4) 图片 Prompt 的三道门（建议顺序）

### 门一：无文字门（No Text）
- negative prompt 必须包含 text/letters/numbers/watermark/signature。
- image_prompt 必须明确 no text；关键文字后期叠加。

### 门二：风格一致门（Style）
- style_base 与 negative_prompt_base 统一继承，禁止每张图临时换风格词（如 photorealistic/3d render）。
- 构图统一：同系列尽量统一视角与留白策略。

### 门三：可维护门（Maintainability）
- 叠字区域固定：留白区稳定，避免每次换标题就改构图。
- 资产命名与归档：按章节与主题归档，避免散落一地。

## 5) 最小命令集（可复现闭环）

### 单次试跑（Gemini CLI）

把 Prompt 文件化后，单次试跑的最小方式是：把 Prompt 与输入拼成一个 query 再执行。

```bash
MODEL="gemini-3-pro-preview"
PROMPT_FILE="prompts/production/prompt_x.v1.txt"
INPUT_FILE="prompts/regression/case_chatty_json/input.txt"

gemini -m "$MODEL" -p "$( { cat "$PROMPT_FILE"; printf '\n\n输入：\n'; cat "$INPUT_FILE"; } )" > out/result.out
```

### 文档构建门禁（MkDocs）

```bash
python3 -m mkdocs build --strict
```

### 引用检查（避免误触 citation 规则）

```bash
python3 tools/check_citations.py
```

这三条命令跑不通，你就别谈“可复现”。跑通了再谈“优化”。
