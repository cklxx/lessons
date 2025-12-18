# Deep Research: [69] OpenID Connect Core 1.0：把“登录”做成可互操作的协议

- Source: https://openid.net/specs/openid-connect-core-1_0.html
- Note: ../notes/ref-069-oidc-core.md
- Snapshot: ../sources/md/openid-net-specs-openid-connect-core-1-0-html-cfd2790a544c.md
- Category: User / Auth / Audit (user_auth)
- Chapters: 09-backend, 11-user
## TL;DR
OpenID Connect (OIDC) 是构建在 OAuth 2.0 之上的身份认证标准层，它通过引入 **ID Token (JWT)** 将“用户身份”结构化、签名化，使得身份验证可以像 REST API 一样在不同系统、应用乃至 AI Agent 之间安全互通，彻底解决了 OAuth 2.0 只能“授权”无法标准化“认证”的痛点。

## 核心观点
1.  **AuthN (认证) 与 AuthZ (授权) 的分层**：OAuth 2.0 负责传递“访问权限”（Access Token），OIDC 在此基础上增加了“身份证明”（ID Token）和用户信息接口（UserInfo Endpoint），明确了“你是谁”的标准答案。
2.  **ID Token 是核心载体**：ID Token 是一个签名的 JSON Web Token (JWT)，它自包含且防篡改。客户端无需再次请求服务器，即可通过公钥校验 Token 的合法性并提取用户 ID (`sub`)、签发者 (`iss`) 和有效期 (`exp`)。
3.  **身份的全局唯一性由 (iss, sub) 决定**：在开放网络中，单纯的 User ID 可能会冲突，必须结合 Issuer（签发者 URL）和 Subject（用户 ID）来唯一标识一个用户。
4.  **标准化用户信息获取**：OIDC 规范了 UserInfo Endpoint 的响应格式（Standard Claims），如 `name`, `email`, `picture` 等，极大降低了应用对接多方登录源（如 Google, 微软, 企业 SSO）的解析成本。
5.  **Discovery 机制实现自动化对接**：通过 `.well-known/openid-configuration` 标准端点，客户端（包括 AI Agent）可以动态发现认证服务器的配置（端点地址、支持的算法、公钥等），无需硬编码。
6.  **安全基线标准化**：OIDC 强制要求 TLS，并详细定义了 `nonce`（防重放）、`state`（防 CSRF）以及不同流程（Code Flow, Implicit Flow, Hybrid Flow）的安全约束，减少了开发者“造轮子”带来的安全漏洞。

## 可落地做法
### 1. 产品侧：身份体系设计
*   **统一身份源决策**：在 MVP 阶段，决策是自建简单的 IDP 还是直接接入 Auth0/Clerk/Keycloak。对于 AI 产品，推荐支持 Social Login 以降低由于注册门槛导致的用户流失。
*   **Claims 映射**：梳理产品需要哪些用户属性（如 AI 偏好设置、订阅等级），并将其映射到 OIDC 的 Standard Claims 或 Custom Claims 中。

### 2. 工程侧：集成与校验
*   **服务端集成步骤**：
    1.  **获取配置**：启动时请求 IDP 的 Discovery URL，缓存 JWKS (公钥集)。
    2.  **重定向登录**：构建包含 `scope=openid profile email` 和 `response_type=code` 的授权链接。
    3.  **换取 Token**：后端通过 Authorization Code 向 Token Endpoint 换取 ID Token 和 Access Token。
    4.  **本地会话**：验证 ID Token 通过后，创建应用自身的 Session (Cookie/JWT)，不要直接透传 ID Token 给前端作为长期凭证。
*   **AI Agent 对接**：如果是 AI Agent 代表用户执行操作，需支持 **On-Behalf-Of** 模式，或者使用 Token Exchange 机制。

### 3. 评测侧：安全验证
*   **Redirect URI 白名单**：严格测试回调地址匹配，防止通配符绕过。
*   **Token 泄露审计**：检查 ID Token 是否被不当记录在日志、URL 参数中。

## 检查清单：ID Token 校验 (Must-Do)
在接收到 ID Token 后，必须执行以下校验，否则视为安全漏洞：

- [ ] **签名验证 (Signature)**：使用 IDP 提供的公钥（从 JWKS 获取）验证 JWT 签名，且算法 `alg` 不能为 `none`。
- [ ] **签发者验证 (Issuer)**：Token 中的 `iss` 字段必须完全匹配 IDP 的 Discovery 配置 URL。
- [ ] **受众验证 (Audience)**：Token 中的 `aud` 字段必须包含（或等于）你的 `client_id`，防止利用其他应用的 Token 欺骗你的服务。
- [ ] **有效期验证 (Expiry)**：当前时间必须在 `iat` (Issued At) 之后，且在 `exp` (Expiration Time) 之前（允许少量时钟偏差）。
- [ ] **Nonce 验证**：如果在登录请求中发送了 `nonce`（隐式流必须发送），必须校验 Token 中的 `nonce` 值与请求时生成的随机值一致（防重放）。
- [ ] **Authorized Party (azp)**：如果 `aud` 包含多个受众，需额外校验 `azp` 是否为你的 `client_id`。

## 常见坑与对策
*   **坑：混淆 Access Token 和 ID Token。**
    *   *现象*：客户端拿着 Access Token 去解析用户信息，或者服务端试图校验 Access Token 的签名（很多 Access Token 是不透明字符串）。
    *   *对策*：牢记 **ID Token 给客户端看（证明身份），Access Token 给资源服务器看（证明权限）**。
*   **坑：忽视 `sub` 的稳定性。**
    *   *现象*：依赖 `email` 作为用户主键。
    *   *对策*：Email 可能变更或回收。必须使用 `sub` 作为系统内的用户主键，Email 仅作为属性。
*   **坑：忽略 `aud` 校验（Token 替换攻击）。**
    *   *现象*：攻击者使用自己在 Google 创建的 Client 获取有效 Token，发送给你的后端，如果只验签名不验 `aud`，攻击者就成功伪装成了该 Google 用户。
    *   *对策*：**Audience Check 是仅次于签名的最重要检查**。

## 可用于丰富《AI 辅助软件产品》的写作点
*   **第 11 章 (用户模块：认证、授权与审计)**：
    *   **身份模型**：介绍 OIDC Claims 如何作为 AI 理解用户的“结构化上下文”（Context）。例如，AI 可以读取 `locale` 自动切换语言，读取 `zoneinfo` 处理时区。
    *   **无密码未来**：结合 OIDC 与 Passkeys (WebAuthn)，阐述现代 AI 产品应如何设计“无感登录”体验。
*   **第 10 章 (Agentic Workflow)**：
    *   **Agent 身份标识**：当多个 AI Agent 协作时，如何证明“我是 Agent A，我代表用户 Bob”？OIDC 的 Client Credentials Flow 和 Token Exchange 是实现 **Agent-to-Agent 安全通信**的标准协议。
    *   **自动化服务发现**：利用 OIDC Discovery 协议，AI Agent 可以自动读取 `.well-known` 配置，自主学习如何接入一个新的第三方服务，无需人工配置复杂的认证参数。
*   **第 17 章 (部署与运维)**：
    *   **集中式审计**：强调 OIDC 使得跨系统的用户行为审计成为可能（基于统一的 `sub`），这对于 AI 系统的合规性和溯源（Provenance）至关重要。
