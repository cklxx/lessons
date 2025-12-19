# Deep Research: [79] Problem Details for HTTP APIs（RFC 9457）：把错误变成可解释、可对账、可回归的合同

- Source: https://www.rfc-editor.org/rfc/rfc9457
- Note: ../notes/ref-079-problem-details.md
- Snapshot: ../sources/md/www-rfc-editor-org-rfc-rfc9457-394ea6adfbc8.md
- Category: Backend & Reliability (backend)
- Chapters: 09-backend, 07-engineering, 17-deployment, 18-evaluation
## TL;DR
RFC 9457（替代 RFC 7807）定义了一种标准化的 JSON/XML 格式（`application/problem+json`），用于在 HTTP API 错误响应中携带机器可读的细节信息，解决了 HTTP 状态码语义过宽、无法承载业务特定错误（如余额不足、参数特定字段校验失败）的痛点。

## 核心观点

1.  **错误是资源，不是随意的字符串**：错误响应应该有固定的结构（Schema），像正常资源一样被设计。
2.  **五大标准字段**：
    *   `type` (URI)：错误的唯一分类标识，这是机器判断错误类型的依据（类似错误码，但全局唯一且可解析）。
    *   `title`：简短的人类可读摘要，不随具体实例变化（如余额不足）。
    *   `status`：HTTP 状态码的冗余副本，防止中间件（如代理）修改头部状态码后导致上下文丢失。
    *   `detail`：针对当前特定请求的详细说明（如当前余额 30，但本次费用 50）。
    *   `instance` (URI)：标识具体错误发生的实例（如 `/account/123/logs/error-99`），用于排查和对账。
3.  **可扩展性（Extensions）**：允许在标准字段外增加业务特定字段（如 `balance`, `accounts`, `validation_errors`），让前端或 Agent 能根据这些数据直接采取行动（如跳转充值、高亮错误表单项）。
4.  **解耦 UI 文案与 API 逻辑**：`type` 用于代码逻辑判断，`title`/`detail` 仅供参考或默认展示，客户端可根据 `type` 自行映射多语言文案。
5.  **安全性隔离**：`detail` 旨在帮助客户端修正请求，而非向开发者暴露内部堆栈（Stack Trace），明确界定了用户可见错误与内部日志的边界。
6.  **默认类型**：如果 `type` 未提供，默认为 `about:blank`，意味着语义等同于该 HTTP 状态码本身。
7.  **内容协商**：支持通过 `Accept-Language` 协商 `title` 和 `detail` 的语言，虽然这通常增加了后端复杂性，但在国际化场景下符合标准。

## 可落地做法

### 1. 后端工程化（统一异常处理）
*   **中间件层**：在框架（如 FastAPI, Spring Boot）的顶层 Exception Handler 中，拦截所有自定义业务异常，统一转换为 `ProblemDetails` 对象。
*   **错误注册表**：维护一个枚举或常量类，定义系统中所有 `type` URI 及其对应的默认 `title` 和 `status`。建议使用绝对路径 URI（如 `https://api.example.com/probs/quota-exceeded`）以避免相对路径解析歧义。
*   **响应头设置**：确保 Content-Type 严格设置为 `application/problem+json`，便于客户端识别。

### 2. 前端/Agent 消费策略
*   **拦截器逻辑**：HTTP Client 拦截器检测到 `Content-Type: application/problem+json` 时，自动解析 Body。
*   **策略分发**：
    *   如果 `type` 是已知业务错误（如 `insufficient_funds`），调用对应 UI 组件（弹窗充值）。
    *   如果 `type` 未知但 `status` 是 4xx/5xx，展示 `title` 和 `detail` 作为通用错误提示。
    *   如果包含 `instance`，在报错截图中展示该 ID，方便用户报修。

### 3. 测试与评测
*   **回归断言**：测试用例不再断言错误文案包含余额字样，而是断言响应 JSON 的 type 字段等于 https://.../out-of-credit。
*   **模糊测试**：确保所有异常路径返回的 JSON 均符合 RFC 9457 Schema，避免解析层二次崩溃。

## 检查清单：API 错误规范性

- [ ] **Content-Type 正确**：错误响应头是否为 `application/problem+json`？
- [ ] **Type URI 稳定**：`type` 字段是否为稳定、不包含动态参数的 URI？
- [ ] **Status 一致性**：Body 中的 `status` 字段是否与 HTTP 响应头中的状态码一致？
- [ ] **敏感信息屏蔽**：`detail` 和扩展字段中是否已过滤掉数据库连接串、内部 IP、堆栈跟踪？
- [ ] **扩展字段强类型**：自定义字段（如 `balance`）是否使用了正确的数据类型（数字而非字符串），便于机器处理？
- [ ] **Instance 可溯源**：`instance` 字段（如果有）能否在服务器日志中通过 Grep 找到对应请求的完整上下文？
- [ ] **文档化**：`type` URI 如果可访问，是否返回了该错误类型的人类可读文档？（可选但推荐）

## 常见坑与对策

1.  **坑：相对 URI 导致的解析混乱**
    *   **现象**：不同 Endpoint 返回相同的相对路径（例如 type 返回 error-1），被解析为完全不同的绝对 URI。
    *   **对策**：始终使用绝对 URI，或以 `/` 开头的根路径 URI。
2.  **坑：把 Problem Details 当作日志**
    *   **现象**：在 `detail` 中塞入 Java/Python 的 `e.printStackTrace()`。
    *   **对策**：生产环境严格禁止堆栈外泄。堆栈进日志（关联 `instance` ID），`detail` 只写服务暂时不可用，请稍后重试。
3.  **坑：过度复用 HTTP 状态码**
    *   **现象**：所有业务错误都返 400，客户端只能靠正则匹配 `title` 来区分是缺参数还是缺库存。
    *   **对策**：必须依赖 `type` 区分业务逻辑。状态码仅用于 HTTP 层面的通用语义（网关、缓存等）。
4.  **坑：滥用 Batch Error**
    *   **现象**：试图在一个响应中返回多个错误（如表单的 10 个字段校验失败）。
    *   **对策**：RFC 建议仅返回最主要的一个错误，或者通过扩展字段（如 `errors: []` 数组）来携带具体的子错误列表，但顶层结构仍保持单一 Problem 对象。

## 可用于丰富《AI 辅助软件产品》的写作点

*   **第 9 章 后端架构（MVP 开发）**：
    *   在API 契约设计一节中，强制要求使用 RFC 9457。这不仅是为了规范，更是为了让未来的 **AI Agent** 能更好地理解错误。Agent 调用工具失败时，结构化的 `type` 和 `detail` 能让 LLM 精准修正参数并重试（Self-Correction），而模糊的文本错误会导致 Agent 陷入死循环。
*   **第 11 章 用户体验（Generative UI）**：
    *   探讨如何根据 Problem Details 的扩展字段动态生成错误处理 UI。例如，捕获到 `validation_error` 类型且带有字段指针（Pointer）时，AI 生成的 UI 可以直接在对应的输入框旁高亮提示，而不是仅弹出一个通用的 Toast。
*   **第 18 章 评测（Evaluation）**：
    *   在确定性测试部分，强调利用 Problem Details 实现白盒级的错误断言。在构建Judge Agent时，Judge 可以根据 API 返回的 `type` 来判定测试用例是否通过了特定的边界条件（如限流、权限控制），而无需依赖不可靠的字符串匹配。
