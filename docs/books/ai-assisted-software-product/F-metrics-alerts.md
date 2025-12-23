# 附录 F：指标字典与告警门禁速查（质量/延迟/成本/风险）

AI 全栈产品的“上线”不只是服务可用，更是**行为可解释**：回答质量、端到端延迟、单位成本、以及安全边界都必须可观测、可裁决、可回滚。

本附录把指标与告警写成“可执行门禁”，用于支撑：
- 发布与回滚：[`17-deployment.md`](17-deployment.md)
- 推理预算与降级：[`16-inference.md`](16-inference.md)
- 评测门禁与回归：[`18-evaluation.md`](18-evaluation.md)
- 合规与治理红线：[`20-governance.md`](20-governance.md)

证据包统一结构见：[附录 D：证据包与门禁速查](D-evidence-pack.md)。事故的 10 分钟止损动作库见：[附录 E：10 分钟止损 Runbook 库](E-runbooks.md)。

---

## 1) 全栈指标字典（Metric Dictionary）

### 1.0 统一标签（否则无法归因）
所有关键指标必须至少带这些标签（labels/tags），否则后续“为什么变坏/变贵/变慢”会变成猜测：

- `env`：`prod|staging`
- `entrypoint`：入口（web/api/batch/cron）
- `tenant_id`：租户（脱敏或哈希也行，但必须可聚合）
- `input_len_bucket`：输入长度分桶（例如 `<1k|1k-4k|4k-16k|>16k`）
- `version_set`：版本集合（代码/配置/提示/模型/索引/策略的组合指纹）
- `model_version` / `prompt_version` / `index_version` / `policy_version`：关键子版本（可选但强烈建议）

> 规则：**告警与门禁必须按 `version_set` 对齐口径**。把不同版本混在一起做统计，会制造“优化了但指标变差”的假象。

---

### 1.1 质量类（Quality）——用户视角的可用性

| 指标 | 定义 | 单位 | 建议分桶/标签 | 采集点 | 常见误区 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `quality.empty_response_rate` | 结果区内容为空（排除用户主动取消）的比例 | % | `entrypoint`,`version_set` | 后端/网关 | 把“取消/中断”算成空回复会误报 |
| `quality.format_compliance_rate` | 输出符合结构/Schema 的比例（JSON/表格/字段齐全） | % | `prompt_version`,`model_version` | 后端解析层 | 只做正则而不做结构校验；把“字段缺失”当成功 |
| `quality.user_feedback_score` | 点赞/点踩/危险反馈的加权得分（口径固定） | 0–1 | `entrypoint`,`topic_bucket` | 前端/事件流 | 把沉默当满意；把 UI 体验与内容质量混在一起 |
| `quality.task_completion_rate` | 关键闭环完成率（保存/导出/采纳等） | % | `entrypoint`,`user_segment` | 前端/后端事件 | 只看 DAU/请求量，不看闭环是否完成 |
| `quality.citation_coverage_rate` | 需要引用的回答中，引用覆盖率（或证据卡展开率） | % | `index_version`,`entrypoint` | 评测/后端 | 引用多不等于正确；可能是“编造引用” |
| `quality.unsafe_hallucination_rate` | 无证据强答/绝对化承诺/编造事实的比例 | % | `prompt_version` | 评测/规则扫描 | 只靠人工抽检；没有固定样本集导致口径漂移 |
| `quality.retry_rate` | 用户主动重试/再生成比例 | % | `entrypoint`,`input_len_bucket` | 前端 | 把重试当活跃；其实可能是质量差 |
| `quality.cache_answer_mismatch_rate` | 语义缓存命中后“答非所问/不贴题”的比例 | % | `cache_strategy` | 评测/日志抽样 | 只监控命中率，不监控命中后的质量退化 |

---

### 1.2 延迟类（Latency）——用户体感的速度

| 指标 | 定义 | 单位 | 建议分桶/标签 | 采集点 | 常见误区 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `latency.ttft_ms` | 从请求发出到首 token 出现（TTFT） | ms | `entrypoint`,`device_type` | 前端/网关 | 只看后端耗时，忽略网络与前端渲染 |
| `latency.e2e_p95_ms` | 端到端 P95（含检索/工具/生成/渲染） | ms | `input_len_bucket`,`version_set` | 网关 | 不分桶就会被长文本拉高，误判为退化 |
| `latency.e2e_timeout_rate` | 超时/504 比例 | % | `entrypoint`,`provider` | 网关 | 把上游 429/5xx 当成超时；原因需分桶 |
| `latency.queue_dwell_ms` | 请求在队列/并发闸门内等待的时间 | ms | `priority`,`tenant_id` | 后端/队列 | TTFT 变慢常常不是模型慢，而是排队 |
| `latency.rag_search_p95_ms` | 向量检索 P95 | ms | `index_version`,`top_k` | 检索层 | 只看平均值；P95/P99 才暴露“尾延迟” |
| `latency.tool_call_p95_ms` | 外部工具调用 P95 | ms | `tool_name`,`provider` | 工具层 | 工具失败重试会把延迟指数级放大 |
| `latency.tokens_per_sec` | 输出阶段生成速度（Token/s） | t/s | `model_version` | 推理层 | 把吞吐（RPS）当成体感；体感看 TPS 与 TTFT |
| `latency.client_render_ms` | 客户端渲染开销（尤其长 Markdown） | ms | `device_type` | 前端 | 只优化后端，结果用户仍然“卡屏” |

---

### 1.3 成本类（Cost）——现金流的底线

| 指标 | 定义 | 单位 | 建议分桶/标签 | 采集点 | 常见误区 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `cost.cost_per_request` | 单次请求综合成本（推理+检索+工具） | 货币/次 | `tenant_id`,`entrypoint` | 网关/计费 | 只算模型钱，不算检索/存储/带宽；详见 `12-billing.md` |
| `cost.cost_per_session` | 单会话成本（按会话聚合） | 货币/会话 | `user_segment` | 计费 | 会话边界不清导致“假省钱/假变贵” |
| `cost.tokens_in` / `cost.tokens_out` | 输入/输出 token | tokens | `model_version` | 网关 | 不记录 token 就无法解释账单争议 |
| `cost.tool_calls` | 工具调用次数（按工具类型） | 次 | `tool_name` | 工具层 | 只数总次数不够；要按工具拆分 |
| `cost.cache_hit_rate` | 缓存命中率（语义/检索/工具） | % | `cache_type` | 网关 | 只追命中率会牺牲质量；需配套质量门禁 |
| `cost.retry_waste_rate` | 因重试/失败造成的浪费成本占比 | % | `error_code`,`provider` | 网关/后端 | 失败请求一样计费；不监控会“越错越贵” |
| `cost.tenant_daily_burn` | 租户日消耗（含预算耗尽率） | 货币/天 | `tenant_id` | 计费 | 不分租户就无法止损“单点爆炸” |
| `cost.global_hourly_burn` | 全局小时消耗（破产曲线） | 货币/小时 | `env` | 计费 | 没有“绝对红线”会让你在 30 分钟内破产 |

---

### 1.4 风险类（Risk）——必须阻断的红线

| 指标 | 定义 | 单位 | 建议分桶/标签 | 采集点 | 常见误区 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `risk.unauthorized_access_count` | 越权/跨租户访问命中次数 | 次 | `tenant_id`,`resource_type` | AuthZ/检索层 | “UI 隐藏”不是授权；必须服务端阻断（见 `11-user.md`） |
| `risk.pii_detected_count` | PII 命中次数（输入或输出） | 次 | `pii_type` | 网关/日志管道 | 只做输出端过滤不够；输入端已泄露也算事故 |
| `risk.prompt_injection_attempt_count` | 注入攻击特征命中次数 | 次 | `entrypoint`,`source_bucket` | 网关 | 只匹配关键词会漏；要监控异常长输入/结构异常 |
| `risk.jailbreak_success_rate` | 红队样本越狱成功率（离线门禁） | % | `attack_vector` | 评测 | 不进发布门禁就等于让线上当实验场 |
| `risk.dangerous_tool_call_count` | 高风险工具调用尝试（写操作/外部副作用） | 次 | `tool_name` | 工具层 | 只看失败次数不够；尝试本身就说明被诱导 |
| `risk.audit_gap_count` | 关键动作缺审计字段（who/when/what/trace_id/version_set） | 次 | `action` | 审计管道 | 没审计=没发生过（对外无法解释） |
| `risk.policy_block_rate` | 安全策略拦截率（拒答/阻断） | % | `policy_version` | 网关/策略层 | 拦截率上升可能是攻击，也可能是误伤，需要配套通过率 |
| `risk.cross_tenant_cache_hit_count` | 缓存跨租户命中（应为 0） | 次 | `cache_type` | 网关 | 缓存键不含 `tenant_id` 会造成致命泄露 |

---

## 2) 阈值设置方法（基线分位数 + 倍数 + 绝对红线）

阈值不要写成“经验值”，要写成**三段式**，并区分“告警阈值”与“阻断阈值”：

1) **基线分位数（Baseline）**  
取过去 7 天同口径的分位数（建议 P95/P99），并按分桶统计：`entrypoint × input_len_bucket × version_set`（必要时再细分租户）。

2) **倍数阈值（Multiplier）**  
用于识别相对退化：`current_p99 > baseline_p99 × 1.5`（示例）。

3) **绝对红线（Absolute Redline）**  
用于识别“再慢/再贵就不可用/会破产”的硬约束：例如 TTFT > 3s、单次成本 > 0.5 元、跨租户命中 > 0。

### 示例（示意，不绑定具体监控栈）

```yaml
# 示意：TTFT 阈值（按 entrypoint + input_len_bucket + version_set 分桶）
metric: latency.ttft_ms
window: 5m
warn:
  when: current_p99 > rolling_7d_p99 * 1.5
  action: "暂停扩量，进入 RB-03"
block:
  when: current_p99 > 3000  # 示例：绝对红线 3s
  action: "立即降级/回滚（RB-03）"
```

> 关键点：阈值必须能映射到动作（降级/回滚/暂停），否则告警就是噪音。

---

## 3) 告警→动作映射表（Alert-to-Action）

规则：每条告警都必须能指向一个 Runbook（`E-runbooks.md` 的 RB-xx），并规定证据包落盘要求（`reports/YYYY-MM-DD/<change-id>/`，参照 `D-evidence-pack.md`）。

| 告警名 | 触发条件（示例） | 默认级别 | 首要止血动作 | 对应 Runbook | 证据包要求（必须落盘） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `alert.cost_surge` | `cost.global_hourly_burn` > 基线×5 持续 5m | S0 | 立刻降级高成本路径 + 限流 | `E-runbooks.md`（RB-02） | `reports/YYYY-MM-DD/<change-id>/`：成本曲线、Top 租户/入口、路由与配额快照（见 `D-evidence-pack.md`） |
| `alert.provider_outage` | 上游 5xx/429 > 5% 持续 5m | S1 | 熔断依赖 + 备用路由 | `E-runbooks.md`（RB-07） | `reports/YYYY-MM-DD/<change-id>/`：错误样本、熔断/切换日志、关键链路验证（见 `D-evidence-pack.md`） |
| `alert.format_break` | `quality.format_compliance_rate` < 99% 持续 10m | S2 | 回退 `prompt_version`/关闭实验开关 | `E-runbooks.md`（RB-01） | `reports/YYYY-MM-DD/<change-id>/`：失败样本 JSONL、解析错误统计、回退指针（见 `D-evidence-pack.md`） |
| `alert.latency_spike` | `latency.e2e_p95_ms` > 基线×1.5 持续 10m 或超时率 > 1% | S1 | 削减链路（关工具/减 top_k/短上下文） | `E-runbooks.md`（RB-03） | `reports/YYYY-MM-DD/<change-id>/`：慢请求 trace、关键指标截图、降级配置（见 `D-evidence-pack.md`） |
| `alert.quality_dip` | 点踩率 10m 内 +20pp 或回归门禁失败 | S1 | 停止扩量 + 回退版本集合 | `E-runbooks.md`（RB-01） | `reports/YYYY-MM-DD/<change-id>/`：回归报告、坏案例簇、回退后恢复证明（见 `D-evidence-pack.md`） |
| `alert.cross_tenant` | `risk.unauthorized_access_count` > 0 | S0 | 维护模式/只读模式 + 关闭导出/分享 | `E-runbooks.md`（RB-04） | `reports/YYYY-MM-DD/<change-id>/`：复现请求/响应、审计事件、策略版本与 diff（见 `D-evidence-pack.md`） |
| `alert.rag_degraded` | 空结果率 +10pp 或相关性/忠实度低于基线 | S1 | 索引别名切回上个快照 + 暂停摄入 | `E-runbooks.md`（RB-05） | `reports/YYYY-MM-DD/<change-id>/`：坏案例三元组、索引 manifest、别名切换记录（见 `D-evidence-pack.md`） |
| `alert.injection_or_jailbreak` | 注入命中显著上升或越狱样本成功 | S1/S0 | 启用严格安全模式 + 移除高风险工具 | `E-runbooks.md`（RB-06） | `reports/YYYY-MM-DD/<change-id>/`：攻击样本/输出、策略版本、回归结果（见 `D-evidence-pack.md`） |
| `alert.billing_discrepancy` | 对账差异 > 0 或投诉激增 | S1 | 暂停扣费/出账任务 + 冻结争议账单 | `E-runbooks.md`（RB-08） | `reports/YYYY-MM-DD/<change-id>/`：差异清单、事件 id、冲正计划（见 `D-evidence-pack.md`） |
| `alert.eval_drift` | 同样本在无改动下分布大幅波动（胜率/ Tie 率） | S2 | 冻结发布 + 固定 judge 口径 + 重建基线 | `E-runbooks.md`（RB-09） | `reports/YYYY-MM-DD/<change-id>/`：旧/新口径对比、校准集结果、基线摘要（见 `D-evidence-pack.md`） |
| `alert.data_pipeline_contamination` | PII 命中 > 0 或校验失败率 > 5% | S0/S1 | 停止摄入/训练/索引 + 隔离批次 + 回滚快照 | `E-runbooks.md`（RB-10） | `reports/YYYY-MM-DD/<change-id>/`：校验报告、manifest 指纹、清理日志（见 `D-evidence-pack.md`） |

---

## 4) 最小仪表盘清单（12 格以内）

你不需要几十个面板，你需要一个能在 30 秒内回答“要不要回滚/降级”的驾驶舱：

1. `error_rate`：系统挂了吗？（S0/S1 判定入口）
2. `latency.ttft_ms`（P95/P99）：用户开始等了吗？（RB-03）
3. `latency.e2e_p95_ms`：端到端是否退化？（RB-03）
4. `cost.global_hourly_burn`：现金流是否失控？（RB-02）
5. `cost.cost_per_request`：单位成本是否越界？（RB-02）
6. `quality.user_feedback_score`：用户是否觉得“变傻”？（RB-01）
7. `quality.format_compliance_rate`：结构化输出是否崩了？（RB-01）
8. `risk.unauthorized_access_count`：是否发生越权？（RB-04）
9. `risk.pii_detected_count`：是否出现敏感信息？（RB-10）
10. `rag.empty_context_rate` / `latency.rag_search_p95_ms`：知识库是否失效或变慢？（RB-05）
11. `tool.error_rate` / `latency.tool_call_p95_ms`：依赖/工具是否在拖垮你？（RB-07）
12. `version_set_rollout`：当前灰度版本集合分布（能回答“坏的是哪个版本”）

> 设计原则：每个面板都必须能映射到一个动作（暂停/降级/回滚/扩量），否则删掉。

---

## 5) 门禁与演练（把阈值接入 `gate/evidence/release/rollback`）

### 5.1 把指标变成四个入口
迁移到你的产品仓库时，推荐把关键阈值接入 4 个入口（见 `C-checklists.md`）：

- `gate`：离线门禁（回归/安全/成本估算）——失败退出码非 0
- `evidence`：生成证据包（版本集合 + 报告 + diff + 回滚指针）
- `release`：灰度发布（按表推进/暂停/回滚）
- `rollback`：一键回滚/降级（10 分钟止损）

最低落地要求：
- `gate` 产出的报告必须能落盘到 `reports/YYYY-MM-DD/<change-id>/`；
- `rollback` 必须能在 10 分钟内把 `error_rate/latency/cost` 拉回基线区间，并留下“恢复证明”。

### 5.2 每月 30 分钟演练（按分钟执行）
目的：确认**告警能响、回滚能用、证据能落盘、恢复能证明**。每月一次，固定日历，不要拖到事故发生时才发现“按钮是坏的”。

演练场景（示例）：一次错误的 `prompt_version` 导致格式错误率上升并引发延迟退化。

| 时间 | 动作 | 产出（必须） |
| :--- | :--- | :--- |
| 0:00–2:00 | 创建证据包目录：`reports/YYYY-MM-DD/<change-id>/`（例如 `<change-id>=drill-format-latency`） | `meta.json`（定级 S2） |
| 2:00–6:00 | 在 staging 注入故障：发布一个会破坏结构化输出的 prompt 版本（只影响演练入口） | 触发 `alert.format_break` 或等价告警 |
| 6:00–10:00 | 按 `E-runbooks.md` 执行 RB-01：停止扩量/关闭开关/回退 `prompt_version` | `rollback_plan.md` + 回退指针 |
| 10:00–15:00 | 验证恢复：格式合规率回到基线；TTFT/端到端延迟回落 | 恢复截图 + 关键指标导出 |
| 15:00–25:00 | 固定证据：导出失败样本 JSONL、门禁输出、版本集合 | `version_set.json` + `samples/*.jsonl` |
| 25:00–30:00 | 复盘回写：把触发样本加入回归集/门禁；更新阈值或告警规则 | 在变更卡/发布说明中记录结论 |

证据包字段与推荐文件名见：[`D-evidence-pack.md`](D-evidence-pack.md)。  
演练的止损动作与回退口径见：[`E-runbooks.md`](E-runbooks.md)。

