# 附录 A：模板库（PRD / 访谈 / 架构 / 评测）

> 本附录提供可直接复制使用的模板。你可以按需裁剪，并把这些模板作为团队的共同语言。

使用方式（建议先看完再复制）：

- 模板中的占位符用 `<...>` 表示；复制后只替换最少的 1–3 个关键占位符即可开跑。
- 任何会进入交付/门禁的文档，至少要能回答：**怎么验收、失败怎么算、怎么回滚、证据放哪**。
- 需要对外发布的内容（包含图片）建议对照：[写作风格与格式约定](style-guide.md) 与 [全书质量控制与复现清单（QCR）](quality-checklist.md)。

## A.1 访谈记录模板

```markdown
### 基本信息
- 访谈日期：
- 访谈对象（画像/角色）：
- 场景（何时/何地/做什么）：

### 关键任务与现有替代
- 任务：
- 当前做法（工具/流程/成本）：
- 最不满意的点：

### 痛点证据（原话）
1.
2.

### 我们的推断（与证据分开）
- 推断：
- 不确定点：

### 结论与行动（可选，但强烈建议）
- 是否值得解决（Yes/No/Pending）：
- 需要补的证据：
- 下一步行动：<继续访谈/做原型/先做 Wizard-of-Oz/暂不做>

### 后续追问
- 问题：
```

## A.2 PRD 模板（精简但可落地）

```markdown
# <产品/功能名称> PRD

## 背景与问题

## 目标 / 非目标

## 用户与场景

## 需求范围（用户故事 & 用例）

## 功能需求（按模块）

## 非功能需求（性能/可用性/安全/隐私/成本）

## 指标与埋点

## 验收标准（Given/When/Then）

## 失败判定（阻断条件）

## 回滚与止损

## 风险与开放问题

## 证据留档（可选）
- 证据目录：<例如 reports/YYYY-MM-DD/<change-id>>
- 对比表/评测报告：<路径>
```

## A.3 架构设计模板（ADR + 拓扑）

```markdown
# ADR-0001：<决策标题>
> 命名建议：使用四位递增序号，例如 ADR-0001, ADR-0002…

## 背景

## 决策

## 备选方案与取舍

## 影响面

## 风险与缓解

## 验证与验收（可裁决）
- 验证方法：<压测/回归/灰度观察窗口>
- 失败判定：<出现什么现象就算失败>
- 回滚/降级：<如何撤回该决策或降级到安全路径>
```

## A.4 评测集模板（RAG/Agent）

```markdown
| id | question | expected_answer | required_citations | tags | difficulty | notes |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
```

## A.5 示例（可复制）端到端模板（全书统一）

> 用于把讲方法落到读者可直接复用的最小闭环。建议每章至少提供 1 个。

````markdown
### 示例（可复制）：<一句话标题>

**目标：** <一句话说明要达成什么>

**前置条件：**
- <环境/依赖/权限/安装包>

**上下文：**
- 项目形态：<Web/CLI/服务端/训练管线...>
- 角色：<产品/工程/模型/运维...>
- 输入：<数据/接口/仓库结构/约束...>

**约束：**
- 禁止：<不要做什么/不要改变什么>
- 资源：<时间/算力/预算/权限>
- 质量门槛：<准确率/延迟/成本/合规边界>

**输出格式：**
- 产物：<文件/报告/表格/图>
- 命名：<路径/文件名规则>

**步骤：**
1. <Step 1>
2. <Step 2>

**验证命令：**
```bash
<command>
# 预期输出包含：<关键日志/返回值/状态码>
```

**失败判定：**
- <出现什么现象就算失败（日志/指标/报错/截图差异）>

**回滚：**
- <回滚到哪个版本/配置/模型 checkpoint；如何确认已回滚>
````

## A.6 《端到端管线图》模板

> 用法：把 0→1 的推进拆成一条能裁决的流水线；每一格都要写清做到什么算完，否则你会在后期用返工补账。

| 阶段 | 核心问题 | 输入 | 输出（交付物） | 门槛（做到什么算完） | 失败判定/回滚 |
| --- | --- | --- | --- | --- | --- |
| 需求 | 值不值得做？ | 痛点/证据/反例 | 决策白板 | 有证据 + 有止损线 | 证据不足就停 |
| PRD | 做什么、不做什么？ | 假设与范围 | 目标/非目标 + 用例（含异常） | 验收标准可裁决 | 缺异常流视为未完成 |
| 原型 | 关键路径通吗？ | PRD | 页面树/用户流/状态清单 | 关键路径能走通 | 断点未修复不进工程化 |
| 实现 | 做出来符合预期吗？ | 原型/契约 | 可合并补丁 | 回归与门禁全绿 | 回归失败不合并 |
| 上线 | 能安全发布吗？ | 通过门禁的版本 | 灰度发布 | 关键指标不退化 | 退化即回滚 |
| 治理 | 能长期活吗？ | 线上数据 | 对比表/评测报告 | 同口径可解释 | 成本/风险越界就止损 |

## A.7 《变更/实验卡片》模板

> 用法：每次你要做一个功能/改一个策略/换一个模型/调一个参数，先写这张卡。写完你就知道该不该做、做完怎么验收、失败怎么回滚。

```markdown
# [编号] 变更标题（一句话说清楚）

## 1) 价值假设（Why）
- 现状：现在的问题是什么？（带证据：日志/样本/反馈）
- 目标：你要改善哪个指标/哪一步闭环？
- 反例：什么情况下这件事不成立？你如何证伪？
- 止损线：达不到什么就停？

## 2) 交付计划（What）
- 影响面：会影响哪些模块/接口/权限/成本？
- 验收标准：做到什么算完？（清单或 Given/When/Then）
- 门槛：成功阈值 + 失败判定（提前写）
- 证据：你会产出哪些可复核证据（对比表/报告/日志/截图）？

## 3) 治理与回滚（Risk & Rollback）
- 风险：安全/合规/成本/性能风险分别是什么？
- 守门指标：哪些指标不能退化？阈值是多少？
- 回滚：如何一键回滚/降级？触发条件是什么？

## 4) 证据留档（Evidence）
- 对比表/评测报告：<路径或链接>
- 决策记录：<路径或链接>
```

## A.8 复现包 `manifest.json` 模板（与 QCR 对齐）

> 用法：把一次改动压缩成固定字段集合，避免“我也不知道当时用了什么版本/口径”。建议把它放在复现包目录根（例如 `reports/YYYY-MM-DD/<change-id>/manifest.json`）。
>
> 替换点：优先补齐 `code_ref`、`config_hash`、`data_snapshot`、`model_version`、`random_control`、`eval_spec` 与 `gates`。

```json
{
  "change_id": "<date-or-ticket-id>",
  "summary": "<一句话描述你改了什么>",
  "version_set": {
    "code_ref": "<git commit/tag>",
    "config_hash": "<config hash/version>",
    "data_snapshot": "<snapshot_id or path>",
    "model_version": "<model_id/checkpoint>",
    "prompt_or_policy_version": "<prompt_id/index_id/policy_id>"
  },
  "env_info": {
    "os": "<os/version>",
    "runtime": "<python/node/java version>",
    "hardware": "<cpu/gpu type if relevant>"
  },
  "random_control": {
    "seed": 42,
    "temperature": 0.0
  },
  "eval_spec": {
    "dataset_or_regression_set": "<eval_set_id/version>",
    "metrics": ["<primary_metric>", "<guardrail_metric_1>", "<guardrail_metric_2>"],
    "window": "<time window or sample size>",
    "notes": "<口径说明：去重/分桶/阈值等>"
  },
  "gates": {
    "decision": "go|hold|rollback",
    "primary_metric_result": "<number or pass/fail>",
    "guardrails_result": "<pass/fail + brief reason>",
    "evidence_paths": ["<path/to/metrics.json>", "<path/to/diff.md>"]
  },
  "rollback": {
    "trigger": "<触发条件>",
    "action": "<回滚到哪个 version_set / 如何降级>",
    "proof": "<path/to/rollback.md>"
  },
  "compliance": {
    "data_license": "<allowed/unknown/blocked + note>",
    "pii_sanitized": true
  }
}
```
