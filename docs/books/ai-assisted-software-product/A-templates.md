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
- 项目形态：<Web/CLI/服务端/训练管线等>
- 角色：<产品/工程/模型/运维等>
- 输入：<数据/接口/仓库结构/约束等>

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

## A.9 事故复盘（Postmortem）模板（分钟级时间线 + 可执行回写）

> 用法：事故结束后 24 小时内完成。重点不是写得漂亮，而是把“复现路径”变成门禁、把“止损动作”变成默认配置、把“证据”变成可审计资产。
>
> 对齐口径：证据包见 `D-evidence-pack.md`；10 分钟止损动作见 `E-runbooks.md`；指标与阈值见 `F-metrics-alerts.md`。

```markdown
# [INC-YYYY-MM-DD-XXX] 事故复盘：<一句话标题>

- 严重级别：S0/S1/S2/S3
- 状态：已恢复/已降级/持续观察
- 证据包目录：`reports/YYYY-MM-DD/<change-id>/`

## 1) 执行摘要（3 句话）
- 发生了什么（可复现事实，不写观点）：…
- 影响了谁/多大（用户数/请求数/金额/风险）：…
- 我们如何止损（回滚/降级/熔断，引用 RB-xx）：…

## 2) 影响面（必须量化）
- 用户影响：<受影响租户/用户/入口>，<比例/数量>
- 业务影响：<转化/留存/退款/投诉>，<变化>
- 成本影响：<成本曲线/峰值/预算耗尽>，<变化>
- 风险影响：<越权/PII/注入/违规内容>，命中情况

## 3) Timeline（分钟级）
| 时间 | 事件 | 信号/证据 | 动作 | 结果 |
| --- | --- | --- | --- | --- |
| 00:00 | 触发 | <告警/工单/面板截图> | - | - |
| 00:02 | 发现 | <trace_id/错误码> | <暂停扩量/降级> | <指标变化> |
| 00:05 | 止血 | <回滚指针> | <rollback/release 操作> | <恢复证明> |
| 00:10 | 验证 | <黄金链路用例> | <复跑> | <通过/失败> |

## 4) 版本集合与回滚指针（必须写清）
- 事故时刻 `version_set`：<code/config/prompt/model/index/policy>
- 10 分钟止损动作：RB-xx（写明做了哪些可逆动作）
- 回滚指针：回到哪个 `version_set`；如何证明已恢复（指标口径 + 证据路径）

## 5) 5 Whys（必须落到机制缺失）
1. 为什么发生：…
2. 为什么没提前发现：…
3. 为什么门禁没挡住：…
4. 为什么回滚/降级不够快：…
5. 为什么同类问题可能复发：…

## 6) 根因与促发因素（可验证）
- 根因（可复现）：…
- 促发因素（让根因更易发生）：…
- 哪些猜测已被证伪：…

## 7) 行动项（必须可执行、可验证、可回滚）
| Action | Owner | Deadline | 落地位置 | 验收门槛 | 证据 |
| --- | --- | --- | --- | --- | --- |
| 把触发样本加入阻断级回归 | <me> | <date> | `18-evaluation.md` 对应回归集 | 门禁退出码=0 | `reports/<...>/` |
| 更新阈值（三段式） | <me> | <date> | `F-metrics-alerts.md` + 告警配置 | 告警不误报且可触发 | `reports/<...>/` |
| 更新 Runbook | <me> | <date> | `E-runbooks.md` | 10 分钟止损可演练 | `reports/<...>/` |

## 8) 复发预防：门禁回写清单
- 新增阻断级样本：<id 列表>
- 新增/调整门禁阈值：<metric + threshold>
- 新增/调整默认回滚指针：<version_set>
- 更新演练脚本：<drill id>

## 9) 沟通记录（可选，但建议）
- 对内：何时通知、通知了什么、谁确认
- 对外：是否公告、公告口径、用户补偿策略（若涉及计费见 `12-billing.md`）
```

## A.10 阈值与告警→动作映射模板（对齐 Runbook）

> 用法：把“指标”写成“可执行门禁”。每条阈值必须能回答：触发后做什么（降级/回滚/暂停），证据存哪里，怎么证明恢复。

```markdown
# 观测门禁：阈值与告警→动作映射

## 1) 指标与阈值（三段式）
| Metric | Baseline（7d P95/P99） | Warn（×k） | Block（×k 或红线） | 分桶 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `latency.ttft_ms` | <p99> | <p99*1.5> | <min(p99*3, 3000ms)> | entrypoint + input_len_bucket + version_set | TTFT 红线优先 |
| `cost.global_hourly_burn` | <p95> | <p95*2> | <min(p95*5, hard_cap)> | env + version_set | 破产曲线 |
| `risk.unauthorized_access_count` | 0 | 0 | 0 | tenant_id + resource_type | 命中即 S0 |

## 2) 告警→动作→证据→Runbook
| Alert | Trigger | Default Severity | First Action | Runbook | Evidence Pack |
| --- | --- | --- | --- | --- | --- |
| `alert.latency_spike` | TTFT/端到端超阈值 | S1 | 削减链路/降级 | RB-03 | `reports/YYYY-MM-DD/<change-id>/`（见 `D-evidence-pack.md`） |
| `alert.cost_surge` | 成本/小时超阈值 | S0 | 限流/降级/熔断 | RB-02 | 同上 |
| `alert.cross_tenant` | 越权命中>0 | S0 | 维护/只读 | RB-04 | 同上 |

## 3) 恢复判定（必须量化）
- 指标回到基线区间并稳定 <30m>
- 黄金链路手工复跑 <3 条> 通过
- 证据包齐全：`meta.json`、`version_set.json`、`rollback_plan.md`、`signals/`、`samples/`
```
