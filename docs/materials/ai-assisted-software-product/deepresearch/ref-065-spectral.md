# Deep Research: [65] Spectral（OpenAPI linter）：把接口契约变成可自动验收的门禁

- Source: https://github.com/stoplightio/spectral
- Note: ../notes/ref-065-spectral.md
- Snapshot: ../sources/md/github-com-stoplightio-spectral-26c88b5d55ba.md
- Category: PRD & Specs (prd_spec)
- Chapters: 03-prd, 07-engineering, 09-backend
## TL;DR
Spectral 是一个强大的 JSON/YAML 规则校验工具（Linter），核心价值在于将 OpenAPI 等接口文档从供人参考的文本转化为CI/CD 流水线中的强制门禁；通过可编程的规则集，它确保 API 契约在语法、风格和安全性上的一致性，是构建高质量 AI Agent 工具接口（Tooling）的基石。

## 核心观点
1.  **契约即代码（Contract as Code）**：API 定义文件（OpenAPI/AsyncAPI）不应被视为静态文档，而应作为代码库的一部分，接受同等严格的自动化检查。
2.  **治理左移（Shift-Left Governance）**：在代码提交（Git Hook）或合并请求（PR）阶段即拦截不合规的 API 设计，避免将非标准化接口泄漏到下游或生产环境。
3.  **语义级校验**：Spectral 不仅检查 JSON 结构（Syntax），还能通过自定义函数检查业务语义（Semantics），例如所有 DELETE 接口必须包含二次确认的描述或分页参数命名必须统一。
4.  **面向 Agent 的接口优化**：在 AI 时代，OpenAPI 是 LLM 理解工具的Prompt。Spectral 可强制要求 `description` 字段的详细程度和格式，直接提升 Agent 的工具调用成功率。
5.  **规则集复用（Rulesets）**：支持继承业界标准（如 OWASP 安全规范、Zalando 风格指南），降低了从零构建 API 规范的成本。
6.  **单一事实源（SSOT）维护**：通过强制校验，确保存储库中的 OpenAPI 文件始终反映真实且合规的系统状态，为 Mock Server 和代码生成提供可靠输入。

## 可落地做法

### 1. 面向产品经理/架构师：定义契约标准
*   **制定风格指南**：不仅规定 URL 命名（如 kebab-case），更要规定描述的质量。例如：所有 `operationId` 必须是动宾结构（`getUser`），以便 AI 理解意图。
*   **确定错误模型**：统一所有 API 的错误返回结构（如 RFC 7807 Problem Details），并在 Spectral 中强制校验。

### 2. 面向工程团队：集成自动化门禁
*   **步骤一：初始化**
    在项目根目录创建 `.spectral.yaml`，继承推荐规则集：
    ```yaml
    extends: [spectral:oas, spectral:oas3]
    rules:
      operation-description: error # 强制要求操作描述
      path-params: error
    ```
*   **步骤二：本地校验**
    使用 CLI 进行快速反馈：`npx spectral lint openapi.yaml`。
*   **步骤三：CI 流水线集成**
    在 GitHub Actions 或 GitLab CI 中添加步骤，若 Lint 失败则阻止合并：
    ```yaml
    - name: Lint API
      run: npx spectral lint reference/openapi.yaml --fail-on-error
    ```

### 3. 面向 AI 研发：增强语义检查
*   编写自定义规则，检查 `description` 是否包含足够的上下文信息（供 LLM 阅读）。
*   检查是否遗漏了 `operationId`，这是大多数 Agent 框架识别工具的唯一键。

## 检查清单（AI Agent 友好型 API 规范）

此清单可直接配置为 Spectral 自定义规则：

- [ ] **完整性**：所有 `Path` 和 `Operation` 必须包含 `summary` 和 `description`。
- [ ] **语义清晰**：`description` 长度不得少于 20 个字符（确保对 LLM 有足够提示）。
- [ ] **标识符**：所有 Operation 必须包含唯一的 `operationId`，且不包含特殊字符。
- [ ] **示例数据**：所有 Request Body 和 Response (2xx) 必须包含 `example` 或 `examples`（用于 Few-Shot Prompting）。
- [ ] **类型约束**：所有参数必须定义 `type`，字符串类型建议定义 `pattern` 或 `enum`（减少 LLM 幻觉）。
- [ ] **默认值**：可选参数建议提供 `default` 值。
- [ ] **安全定义**：根节点必须定义 `security` 或 `securitySchemes`。

## 常见坑与对策

1.  **坑：规则噪音过大**
    *   **现象**：引入初期报错成千上万，导致团队直接放弃。
    *   **对策**：采用渐进式治理。初期只开启 Critical/Error 级别的核心规则（如语法错误），将风格建议设为 Warning 或 Info，随时间逐步收紧。
2.  **坑：Linter 无法验证逻辑**
    *   **现象**：Spectral 通过了，但接口实现与文档不一致。
    *   **对策**：Spectral 只是静态检查。必须配合 **Contract Testing**（如 Dredd 或 Pact）来验证文档与代码的一致性。
3.  **坑：忽略对 AI 的适配**
    *   **现象**：文档符合 OpenAPI 语法，但描述过于简略（如 Update user），导致 Agent 无法正确推理参数。
    *   **对策**：专门编写针对 AI 可读性的 Spectral 规则，将文档质量量化。

## 可用于丰富《AI 辅助软件产品》的写作点

*   **第 3 章（PRD 与工程合同）**：
    *   介绍技术 PRD的验收标准。不仅是文字描述，而是通过 Spectral 校验的 OpenAPI 文件。
    *   **核心概念**：将非功能性需求（如接口规范）代码化。
*   **第 7 章（工程化与门禁）**：
    *   作为 CI/CD Pipeline 图谱中的关键一环（Quality Gate）。
    *   展示如何用 Spectral 拦截不合格的 API 变更，防止污染下游。
*   **第 10 章（Agent 工具调用与 RAG）**：
    *   **重点推荐**：这是本书区别于传统软件工程书的亮点。
    *   论述：**OpenAPI Spec = Prompt for Tools**。
    *   实战：如何利用 Spectral 编写AI 友好度规则集，确保 Agent 能够准确理解和调用工具。这是提升 Agent 系统稳定性的低成本高杠杆手段。
