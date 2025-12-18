# Deep Research: [22] OAuth 2.0（RFC 6749）：认证授权的“最小事实源”

- Source: https://www.rfc-editor.org/rfc/rfc6749
- Note: ../notes/ref-022-oauth2.md
- Snapshot: ../sources/md/www-rfc-editor-org-rfc-rfc6749-9c8f86060b94.md
- Category: User / Auth / Audit (user_auth)
- Chapters: 09-backend, 11-user
## TL;DR
OAuth 2.0 不是简单的“登录协议”，而是一个**授权委托框架**（Authorization Framework）。它的核心价值在于让用户（资源拥有者）在不把密码告诉第三方应用（客户端）的前提下，通过发放受限令牌（Token），允许其代表自己访问受保护资源。

## 核心观点

1.  **授权而非认证（AuthZ vs AuthN）**：RFC 6749 明确指出 OAuth 解决的是“授权”问题。虽然业界常通过“授权”的副产品（如获取用户信息）来实现“伪登录”，但标准本身并未定义用户身份的标准格式（那是 OIDC 的工作）。
2.  **角色分离架构**：协议定义了四种解耦角色——**资源拥有者**（用户）、**客户端**（第三方应用）、**授权服务器**（发证机关）、**资源服务器**（数据保管方）。这种分离是现代微服务和 API 经济的基石。
3.  **令牌化解密**：**Access Token** 是核心凭证。对客户端而言，它通常是不透明的字符串（Opaque）；对服务端而言，它包含 Scope（权限范围）和有效期。这种抽象屏蔽了底层验证逻辑的复杂性。
4.  **四种授权模式适配不同场景**：
    *   **Authorization Code**：最安全，适用于有后端的 Web 应用（支持 Refresh Token）。
    *   **Implicit**（隐式模式）：针对早期浏览器端应用，安全性较低（现已不推荐，倾向于 Auth Code + PKCE），Token 直接在 URL 片段中返回。
    *   **Resource Owner Password Credentials**：用户直接把账号密码给客户端，仅适用于高度信任场景（如官方 App），是向 Token 架构迁移的过渡方案。
    *   **Client Credentials**：无用户参与，用于服务间调用（Machine-to-Machine）。
5.  **Scope 限制权力边界**：Scope 参数是授权逻辑的原子单位，它定义了 Token 能做什么（例如 `read:email` vs `send:email`），体现了“最小权限原则”。
6.  **安全依赖 TLS**：RFC 6749 强制要求在传输 Token 和凭证时必须使用 TLS（HTTPS），协议本身不负责消息加密，依赖传输层安全。
7.  **Refresh Token 机制**：通过短效 Access Token 和长效 Refresh Token 的组合，在保障安全（Token 泄露风险窗口小）的同时优化用户体验（减少频繁登录）。

## 可落地做法

### 1. 产品设计：定义清晰的授权“合同”
*   **步骤**：在设计第三方接入（或 AI Agent 接入）界面时，必须展示：客户端是谁？请求什么权限（Scope）？数据将如何被使用？
*   **AI 场景**：当 AI Agent 需要调用外部 API（如 Google Calendar）时，需设计“授权插槽”，让用户完成 OAuth 流程后，Agent 仅获得 Token 而非用户密码。

### 2. 工程实现：Token 生命周期管理
*   **存储**：客户端（特别是浏览器端/移动端）严禁存储 `client_secret`。Access Token 应存储在内存或 HttpOnly Cookie 中，避免 LocalStorage 带来的 XSS 风险。
*   **刷新**：后端需实现自动刷新逻辑。当 API 返回 401 且错误码提示 Token 过期时，利用 Refresh Token 换取新 Token 并重试请求，此过程对用户透明。
*   **状态绑定**：在发起授权请求时必须生成随机 `state` 参数，并在回调时校验，防止 CSRF 攻击。

### 3. 错误处理与可观测性
*   严格区分 **401 Unauthorized**（Token 无效/过期 -> 需刷新或重新登录）和 **403 Forbidden**（Scope 不足 -> 需提示用户升级权限）。
*   在日志中记录授权失败的原因（`error` 参数），如 `invalid_grant` 或 `unauthorized_client`，以便排查集成问题。

## 检查清单：OAuth 2.0 集成安全审计

*   [ ] **通信安全**：所有端点（授权、Token、重定向）是否强制使用 HTTPS？
*   [ ] **重定向验证**：授权服务器是否严格校验 `redirect_uri`（完全匹配而非模糊匹配），防止重定向劫持？
*   [ ] **防 CSRF**：客户端是否发送并验证了 `state` 参数？
*   [ ] **Scope 最小化**：客户端是否仅申请了业务必需的 Scope？
*   [ ] **Client Secret 保护**：Client Secret 是否仅保留在后端，未泄露到前端代码或版本库中？
*   [ ] **Token 撤销**：是否提供了撤销 Token 的机制（RFC 7009）？
*   [ ] **错误回显**：在授权失败时，是否避免将敏感堆栈信息暴露给用户，而是返回标准的 `error` 代码？

## 常见坑与对策

*   **坑 1：混淆 AuthN 与 AuthZ**
    *   *现象*：拿着 OAuth Access Token 当作“用户身份证明”，认为持有 Token 就是用户本人。
    *   *对策*：仅将 OAuth 用于获取资源访问权。如需身份认证，请叠加 OIDC (OpenID Connect) 层，解析 ID Token。
*   **坑 2：Implicit 模式的滥用**
    *   *现象*：在 SPA（单页应用）中直接使用隐式流，导致 Token 在浏览器历史记录或 Referer 中泄露。
    *   *对策*：即使是纯前端应用，现代最佳实践也推荐使用 **Authorization Code Flow with PKCE**（虽然 PKCE 是 RFC 7636 定义的，但它是修补 RFC 6749 在公共客户端安全缺陷的标准解法）。
*   **坑 3：宽泛的 Scope**
    *   *现象*：开发者为了省事申请 `all` 或 `root` 权限。
    *   *对策*：强制细粒度 Scope 设计，便于后续做功能解耦和风险控制。

## 可用于丰富《AI 辅助软件产品》的写作点

*   **第 11 章（用户模块）：AI Agent 的“代理权”**
    *   探讨如何将 OAuth 2.0 模型应用于 AI Agent。Agent 本质上是一个特殊的“客户端”。用户不是把密码给 Agent，而是通过 OAuth 授权 Agent 代表自己去操作 GitHub、Jira 或 Slack。这里可以引入“资源拥有者（用户） -> 授权给 -> 客户端（AI Agent）”的概念模型。
*   **第 9 章（后端契约）：标准化的错误语义**
    *   在构建 AI 可调用的 API 时，严格遵守 RFC 6749 的错误响应结构（`error`, `error_description`）。AI（作为客户端开发者）能够通过解析标准错误字段，自动判断是需要重新向用户请求授权（Invalid Grant），还是放弃操作（Access Denied），从而实现更健壮的 Tool Use 循环。
*   **第 13 章（数据）：隐私边界**
    *   利用 Scope 机制作为 AI 读取用户数据的“防火墙”。例如，只授予 AI `calendar.readonly` 权限，物理隔离其修改日程的能力，这是构建用户对 AI 信任的关键技术手段。
