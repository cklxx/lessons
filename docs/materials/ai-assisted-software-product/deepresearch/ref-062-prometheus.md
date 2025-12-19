# Deep Research: [62] Prometheus：指标监控的事实标准（但别滥用标签）

- Source: https://prometheus.io/docs/introduction/overview/
- Note: ../notes/ref-062-prometheus.md
- Snapshot: ../sources/md/prometheus-io-docs-introduction-overview-e7be7b92116c.md
## TL;DR
Prometheus 是云原生时代指标监控的事实标准，核心价值在于通过多维标签（Labels）实现对系统健康度的灵活查询与可视化。在 LLM 应用中，它是治理模型延迟、错误率与资源消耗的基石，但严禁用于计费或记录高基数数据（如 Prompt 原文）。

## 核心观点
1.  **多维数据模型**：Prometheus 最大的威力在于时间序列 + 标签（Labels）。同一个指标（如 `http_requests_total`）可以通过不同标签（例如 model 等于 gpt-4、status 等于 500）进行切片聚合，这比传统的层级式监控更灵活。
2.  **Pull 模型为主**：Prometheus 主动从目标服务拉取指标，而不是等待服务推送。这降低了被监控服务的复杂性，并能更容易检测到服务宕机（拉取失败即意味着异常）。
3.  **高可靠性设计**：每个 Prometheus Server 都是独立的，不依赖分布式存储。在系统大规模故障时，它是你排查问题的最后一道防线，因此它优先保证可用性而非数据的 100% 完整性。
4.  **PromQL 查询语言**：强大的查询语言允许进行实时的聚合、预测和比对（如计算 Token 生成速率的同环比增长）。
5.  **非精确计费工具**：由于采样和拉取机制，Prometheus 的数据可能存在微小丢失，绝对**不适合**用于按 Token 计费或财务结算（Billing），这类需求应使用专门的日志或数据库系统。
6.  **告警是行动的触发器**：指标收集的终点不是大屏展示，而是通过 Alertmanager 触发自动化运维动作（如扩容、熔断）或人工介入。
7.  **生态丰富**：拥有海量的 Exporters（导出器），几乎可以监控所有基础设施（K8s, DB, GPU）和应用组件。

## 可落地做法

### 1. 工程师：LLM 应用指标埋点规范
*   **定义黄金指标**：在代码中明确埋点 `llm_request_duration_seconds`（直方图，监控延迟分布）、`llm_token_usage_total`（计数器，监控消耗）、`llm_request_errors_total`（计数器，监控失败）。
*   **配置 Exporter**：如果是 Python/FastAPI 后端，使用官方 Client Library 暴露 `/metrics` 接口。
*   **配置抓取（Scrape）**：在 Prometheus 配置文件中添加 Job，设置抓取间隔（通常 15s 或 30s）。

### 2. 产品经理：定义 SLO（服务等级目标）
*   不要只看平均延迟，要看 P95 或 P99 延迟。例如：99% 的 AI 对话请求必须在 2 秒内开始流式响应。
*   将业务目标转化为 Prometheus 的查询表达式，并在 Grafana 中建立看板。

### 3. 运维/SRE：标签治理
*   **审查标签基数**：在上线前严格审查 Label 的取值范围。严禁将 `user_id`、`session_id`、`prompt_content` 或 `error_message`（原始文本）作为标签，这会导致时间序列数量爆炸，撑爆内存。

## 检查清单：Prometheus 指标设计自查表

*   [ ] **指标命名**：是否符合 `应用名_模块_指标_单位` 规范？（例如 `chat_api_response_latency_seconds`）
*   [ ] **类型选择**：
    *   累计值（如 Token 总数）是否使用了 Counter？
    *   状态值（如当前排队人数）是否使用了 Gauge？
    *   分布值（如响应时间）是否使用了 Histogram？
*   [ ] **标签基数（Cardinality）**：所有标签的取值空间是否都是有限且可枚举的（如 `model_name`, `region`, `error_code`）？是否已剔除无限增长的字段（如 `email`, `trace_id`）？
*   [ ] **Bucket 设置**：Histogram 的桶（Buckets）设置是否覆盖了 LLM 的长尾延迟？（LLM 响应可能从 100ms 到 60s 不等，默认桶可能不适用）。
*   [ ] **告警关联**：该指标异常时，是否有对应的告警规则？告警发出后，Runbook（操作手册）是否明确了处理步骤？

## 常见坑与对策

*   **坑 1：基数爆炸（Cardinality Explosion）**
    *   **现象**：Prometheus 内存飙升，OOM 重启，查询超时。
    *   **原因**：开发者误将用户 ID 或请求参数作为 Label。
    *   **对策**：在 CI/CD 阶段扫描代码中的 metrics 定义；在 Prometheus 配置中限制每个 Target 的最大序列数。
*   **坑 2：长期存储**
    *   **现象**：磁盘写满，历史数据查询极慢。
    *   **原因**：试图用 Prometheus 存几年的数据。
    *   **对策**：Prometheus 本地存储仅保留短期（如 15-30 天）。长期存储需对接 Thanos、VictoriaMetrics 或云厂商的托管 Prometheus 服务。
*   **坑 3：告警风暴**
    *   **现象**：一出故障收到几百条短信，掩盖了根本原因。
    *   **原因**：对每个微小的波动都设了告警，且没有配置分组（Grouping）和抑制（Inhibition）。
    *   **对策**：使用 Alertmanager 进行告警收敛；基于症状（Symptom-based，如用户无法对话）而非原因（Cause-based，如CPU > 80%）告警。

## 可用于丰富《AI 辅助软件产品》的写作点

*   **第 12 章 LLMOps（核心对应）**：
    *   **可观测性小节**：直接引用 Prometheus 作为监控标准。
    *   **案例**：展示如何用 PromQL 计算实时 Token 吞吐率和模型 P99 延迟。
    *   **警告框**：特别强调不要把 Prompt 放在 Label 里，这是 AI 工程师最容易犯的错误，解释为何这会导致监控系统崩溃。
*   **第 18 章 评估与迭代**：
    *   区分离线评估（使用数据集）和在线监控（使用 Prometheus）。Prometheus 负责监控模型上线后的**技术健康度**（延迟、错误），而非**内容质量**（幻觉率通常很难通过简单的数值指标直接监控，需要专门的评估管道）。
*   **第 20 章 治理与合规**：
    *   讨论数据隐私：确保监控数据中不包含 PII（个人身份信息），Prometheus 的 Label 经常是数据泄露的隐蔽角落。
