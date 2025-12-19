# Deep Research: [61] OpenTelemetry：观测性三件套（logs/metrics/traces）

- Source: https://opentelemetry.io/docs/
- Note: ../notes/ref-061-opentelemetry.md
- Snapshot: ../sources/md/opentelemetry-io-docs-8de8f872c85e.md
## TL;DR
OpenTelemetry (OTel) 是目前业界公认的可观测性（Observability）标准框架，它通过统一的 API 和协议（OTLP）解决了日志（Logs）、指标（Metrics）和分布式追踪（Traces）的数据采集与传输难题，让开发者无需绑定特定厂商即可看清系统内部状态。

## 核心观点
1.  **观测性三支柱（Signals）**：OTel 将可观测性数据标准化为三大信号：
    *   **Traces (追踪)**：记录请求在分布式服务间的完整调用链路，回答失败发生在哪里、为什么失败。
    *   **Metrics (指标)**：聚合的数值数据（如 QPS、延迟分布），反映系统整体健康度和趋势。
    *   **Logs (日志)**：传统的离散事件记录，通过 Trace ID 关联后价值倍增。
2.  **上下文传播（Context Propagation）是灵魂**：利用 Baggage 和 Trace Context 在服务间透传元数据（如 User ID、Request ID），是串联分布式系统的关键。
3.  **厂商中立（Vendor-Neutral）**：OTel 只负责生成和导出数据（Generate & Export），不负责存储和展示。它支持导出到 Prometheus、Jaeger 或商业化 SaaS（Datadog, Dynatrace 等），解耦了采集层与分析层。
4.  **采集器（Collector）模式**：推荐使用 OTel Collector 作为中间代理，负责接收应用数据、处理（过滤/脱敏/转换）并分发给后端，降低应用侧负担。
5.  **语义约定（Semantic Conventions）**：定义了标准的属性命名规范（如 `http.method`、`db.system`），确保不同语言、不同框架产生的数据具有一致的含义，便于统一分析。
6.  **零代码无侵入（Zero-code Instrumentation）**：对于 Java、Python、.NET 等语言，OTel 提供了自动注入探针（Auto-instrumentation），无需修改代码即可获取基础的 HTTP/DB 监控数据。

## 可落地做法
### 第一步：策略选择与环境准备
*   **工程团队**：优先采用 **Auto-instrumentation (Zero-code)** 快速覆盖 80% 的通用框架（Spring Boot, Flask, Django 等）。
*   **架构师**：决定 Collector 的部署模式（Sidecar 模式适合 K8s，Gateway 模式适合统一管理流量）。

### 第二步：核心信号接入
1.  **Traces**：在入口服务生成 Trace ID，确保 HTTP Header（如 `traceparent`）在微服务间正确传递。
2.  **Metrics**：定义黄金指标（延迟、流量、错误率、饱和度），通过 OTel SDK 暴露。
3.  **Logs**：配置 Log Appender 将 Trace ID 自动注入每一行日志，实现日志与追踪关联。

### 第三步：连接与验证
*   **配置 Exporter**：将数据通过 OTLP 协议发送给 Collector 或直接发送给后端（如 Grafana Tempo/Loki/Mimir）。
*   **验证数据流**：使用 `stdout` exporter 在控制台先行验证数据格式是否符合预期，检查 `service.name` 等资源属性是否正确。

## 检查清单：OpenTelemetry 接入验收
*   [ ] **依赖安装**：是否已引入对应语言的 OTel API 和 SDK 库？
*   [ ] **资源标识**：是否配置了 `service.name`、`service.version` 和 `deployment.environment`？
*   [ ] **传播确认**：跨服务调用时，下游是否成功接收并延续了上游的 `trace_id`？
*   [ ] **敏感脱敏**：是否在 Collector 或 SDK 层配置了过滤器，剔除 PII（个人隐私信息）？
*   [ ] **采样策略**：生产环境是否配置了合理的采样率（Sampling Rate）以控制成本？
*   [ ] **错误关联**：异常（Exception）堆栈是否被正确捕获并附加到 Span Event 中？

## 常见坑与对策
1.  **坑：基数爆炸（High Cardinality）**
    *   **现象**：Metrics 中包含如 UUID、URL 参数等高离散度 Tag，导致后端存储崩溃。
    *   **对策**：严格审查 Metric Attributes，使用通配符归一化 URL（如 `/api/user/{id}`），避免将随机值作为 Label。
2.  **坑：采样丢失关键错误**
    *   **现象**：为了省钱开启概率采样（如 10%），导致低频报错的 Trace 没被采到。
    *   **对策**：使用 **Tail-based Sampling**（尾部采样），先全量缓存 Trace，根据结束状态（是否 Error/高延迟）决定是否保留。
3.  **坑：上下文断连**
    *   **现象**：在使用线程池、异步队列或自定义 RPC 时，Trace ID 丢失。
    *   **对策**：显式使用 OTel 的 Context Propagators API 手动传递 Context，或检查异步框架的自动埋点支持情况。

## 可用于丰富《AI 辅助软件产品》的写作点
*   **第 5 章（后端 MVP / 可观测性）**：
    *   强调可观测性驱动开发（ODD）。在编写代码的同时，就应该思考如果这行代码报错，我怎么在不看源码的情况下知道原因？
    *   推荐在 MVP 阶段就引入 OTel，哪怕只是打印到控制台，也能养成结构化日志的习惯。
*   **第 12 章（LLMOps / 监控）**：
    *   **LLM 也是外部依赖**：将对 OpenAI/Anthropic 的调用视为一种特殊的 DB 或 RPC 调用。
    *   **GenAI 语义约定**：利用 OTel 最新的 GenAI Semantic Conventions，记录 `gen_ai.system` (模型名), `gen_ai.usage.input_tokens` (Token 消耗), `gen_ai.temperature` 等属性。
    *   **Trace 可视化 RAG**：用 Trace 串联用户提问 -> 向量检索 -> Prompt 组装 -> LLM 生成的全过程，这是调试 RAG 效果的神器。
