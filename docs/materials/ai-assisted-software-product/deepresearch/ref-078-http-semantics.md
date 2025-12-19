# Deep Research: [78] HTTP Semantics（RFC 9110）：把请求/重试/状态码写成可推理的契约

- Source: https://www.rfc-editor.org/rfc/rfc9110
- Note: ../notes/ref-078-http-semantics.md
- Snapshot: ../sources/md/www-rfc-editor-org-rfc-rfc9110-e593c606c957.md
- Category: Backend & Reliability (backend)
- Chapters: 09-backend, 17-deployment, 07-engineering, 18-evaluation
## TL;DR
RFC 9110 将 HTTP 的语义（方法、状态码、头字段）与具体版本的传输语法（HTTP/1.1/2/3）解耦，确立了分布式系统中组件间交互的通用契约；对于 AI 产品，它是构建**Agent 可靠工具调用**、**推理计费幂等性**以及**智能网关流控**的底层基石。

## 核心观点
1.  **语义独立性**：HTTP 语义（Intent）独立于传输版本（Wire Format）。无论底层是 TCP 还是 QUIC，GET 的含义不变，429 的含义不变。AI Agent 对接 API 时应依赖这些语义而非特定协议细节。
2.  **方法属性（安全与幂等）**：
    *   **Safe (GET, HEAD)**：只读，无副作用。Agent 可随意重试或预取。
    *   **Idempotent (PUT, DELETE)**：多次执行效果等同于一次。这是**自动化恢复**的关键，Agent 在网络超时后可安全重试。
    *   **Non-idempotent (POST)**：通常不幂等。在 AI 计费和推理场景中，必须配合 `Idempotency-Key` 才能安全重试。
3.  **状态码即控制流**：状态码不仅仅是错误提示，更是 Agent 的**决策分支**。
    *   `4xx`：客户端错误（提示 Agent 修改 Prompt 或参数）。
    *   `5xx`：服务端错误（提示 Agent 等待后重试）。
    *   `429` + `Retry-After`：显式流控契约。
4.  **无状态架构（Statelessness）**：每个请求必须包含理解该请求所需的全部上下文。这对 RAG 系统至关重要，意味着上下文窗口（Context Window）的状态维护应由应用层而非传输层负责，便于水平扩展。
5.  **中间件（Intermediaries）可见性**：HTTP 设计允许代理（Proxy/Gateway）在不知晓具体业务逻辑的情况下提供缓存、鉴权和流控。AI Gateway（如 LLM 路由、缓存）正是基于此特性构建的。
6.  **缓存语义**：明确的缓存控制（`Cache-Control`, `Vary`）对于降低昂贵的 LLM 推理成本至关重要，同样的输入（Prompt）在一定时间内应返回同样的输出（Completion）。
7.  **统一接口（Uniform Interface）**：通过统一的接口（URI + Method）隐藏实现细节，允许后端架构演进（如从单体到微服务，或更换模型提供商）而不破坏前端或 Agent 的调用契约。

## 可落地做法

### 1. 工程侧：构建幂等契约
*   **步骤一**：梳理所有非 GET 接口。
*   **步骤二**：对于涉及资金扣除、Token 消耗或状态变更的 POST 接口，强制要求客户端（或 Agent SDK）在 Header 中携带 `Idempotency-Key` 或 `Request-ID`。
*   **步骤三**：后端中间件层拦截请求，缓存 Key 及执行结果。若 Key 重复，直接返回缓存结果，不执行业务逻辑。

### 2. 产品侧：定义错误恢复策略
*   **步骤一**：将业务错误映射到标准 HTTP 状态码。例如：
    *   余额不足 -> `402 Payment Required`
    *   上下文超长 -> `413 Content Too Large`
    *   模型过载 -> `429 Too Many Requests`
*   **步骤二**：为 Agent 编写 "System Prompt" 指导其如何处理这些状态码（例如：如果收到 402，请停止任务并通知用户充值；如果收到 429，请等待 Retry-After 秒数）。

### 3. 评测侧：鲁棒性测试
*   **步骤一**：在测试环境中模拟 HTTP 故障（Chaos Engineering）。
*   **步骤二**：观察 Agent 行为。它是否在 `500` 时死循环？是否在 `400` 时未能修正参数？是否忽略了 `Retry-After`？

## 检查清单：AI API 语义合规性
*   [ ] **幂等性**：关键写操作（POST）是否支持 `Idempotency-Key`？
*   [ ] **状态码准确性**：是否避免了万能 200？（即返回 200 但 Body 里写 `error: true`，这会欺骗 Agent）。
*   [ ] **参数错误反馈**：`400 Bad Request` 的响应体中是否包含了具体的字段错误描述（便于 Agent 自我修正）？
*   [ ] **流控契约**：`429` 响应是否必须携带 `Retry-After` 头？
*   [ ] **内容协商**：是否通过 `Accept` 头正确处理了 JSON 与 Event-Stream（流式）的切换？
*   [ ] **安全方法**：GET 请求是否确保无副作用（不产生 Token 消耗或数据修改）？

## 常见坑与对策
*   **坑**：把所有 AI 推理错误都归为 `500 Internal Server Error`。
    *   **后果**：Agent 认为是服务抖动，无限重试，导致成本爆炸或死循环。
    *   **对策**：区分 `4xx`（输入有问题，不可重试）和 `5xx`（服务有问题，可退避重试）。
*   **坑**：忽略 `Vary` 头进行缓存。
    *   **后果**：不同用户或不同权限级别的请求复用了同一个缓存的推理结果，导致数据泄露。
    *   **对策**：缓存 Key 必须包含 `Authorization` 或租户 ID。
*   **坑**：POST 用于查询。
    *   **后果**：导致中间件无法安全缓存结果，且 Agent 默认不敢重试。
    *   **对策**：虽然 LLM 输入长常用 POST，但若语义是查询/计算，应明确标记为幂等，或使用支持 Body 的 GET 变体（非标但常用）/ PUT（视情况）。

## 可用于丰富《AI 辅助软件产品》的写作点
*   **第 7 章（工程合同）**：重点阐述 **"HTTP Status as a Protocol for Agents"**。Agent 不像人类能看懂弹窗文字，标准状态码是 Agent 唯一能听懂的指令。
*   **第 9 章（后端架构）**：在设计 **AI Gateway** 时，利用 RFC 9110 定义的中间件角色，说明如何透明地处理重试、缓存和鉴权，而不需要修改模型服务的代码。
*   **第 12 章（计费）**：结合 **Idempotency** 概念，讲解如何设计不重扣费的 Token 计费系统，特别是在流式传输（Streaming）中断重连的场景下。
*   **第 17 章（部署与运维）**：在可观测性部分，强调通过监控 HTTP 状态码分布来识别模型服务健康度（如 `429` 飙升意味着算力不足，`400` 飙升意味着 Prompt 结构可能发生了破坏性变更）。
