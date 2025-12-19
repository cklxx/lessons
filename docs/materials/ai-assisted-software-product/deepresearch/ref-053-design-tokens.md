# Deep Research: [53] Design Tokens：让设计和代码说同一种话

- Source: https://www.designtokens.org/TR/drafts/format/
- Note: ../notes/ref-053-design-tokens.md
- Snapshot: ../sources/md/www-designtokens-org-tr-drafts-format-3248b3ab62e4.md
## TL;DR
Design Tokens (DTCG) 标准定义了一种基于 JSON 的通用数据格式，用于在设计工具、代码和 AI 之间无损传递颜色、间距等视觉决策；它是构建生成式 UI不可或缺的约束层，确保 AI 生成的界面符合品牌规范而非产生幻觉。

## 核心观点
1.  **JSON 唯一事实源**：所有设计决策（颜色、字体、阴影）必须存储为标准化的 JSON 文件，而非散落在 Figma 或 CSS 变量中。
2.  **令牌（Token）即对象**：一个合法的 Token 必须包含 `$value`（值），通常包含 `$type`（类型），不再是简单的键值对。
3.  **别名（Alias）构建语义层**：推荐使用 `{group.token}` 语法引用其他 Token。通过原始值 -> 语义 Token -> 组件 Token的三层架构，实现一处修改、全站更新。
4.  **严格的类型系统**：规范定义了 `color`, `dimension`, `duration` 等标准类型，这为 AI 提供了极佳的校验机制——AI 必须输出符合类型约束的值。
5.  **组合与继承**：支持组合 Token（如阴影由颜色+位移组成）和 `$extends` 继承机制，允许不同主题（Theme）仅覆盖差异部分。
6.  **分组仅作组织**：Group（分组）用于文件结构整理，不应承载业务逻辑；工具不应推断分组的语义。
7.  **JSON Pointer 高级引用**：除了简单的花括号引用，还支持 JSON Pointer，通过 $ref 指向 #/path/val 来访问数组特定元素或属性，适合复杂系统。

## 可落地做法
1.  **建立分层 Token 库**：
    *   **基础层 (Primitive)**：定义 `blue-500: #1e3a8a`。
    *   **语义层 (Semantic)**：定义 `color.action.primary: {blue-500}`。
    *   **组件层 (Component)**：定义 `button.bg.default: {color.action.primary}`。
2.  **配置自动化管线**：
    *   使用 Style Dictionary 或类似工具，读取 JSON 源文件。
    *   自动生成多端产物：Web (CSS Variables), iOS (Swift Structs), Android (Compose Objects)。
3.  **注入 AI 上下文**：
    *   将 Token 的 JSON 简化版（去除描述和扩展数据）作为 System Prompt 的一部分。
    *   指令示例：生成 React 组件时，所有颜色必须引用 `theme.tokens.json` 中的键名，禁止使用十六进制值。

## 检查清单
- [ ] **结构合规性**：每个 Token 对象是否都直接包含了 `$value` 属性？
- [ ] **类型显性化**：根节点或 Token 自身是否声明了 `$type`（如 `color`, `dimension`）？
- [ ] **引用闭环**：所有的别名引用 `{...}` 是否都能解析到具体的值？是否存在循环引用（A->B->A）？
- [ ] **命名语义化**：Token 名称是否描述了它是什么或它用在哪，而不是它长什么样（即用 `error-bg` 而非 `red-bg`）？
- [ ] **零魔法值**：除了基础层 Token，其他 Token 的值是否都使用了引用？
- [ ] **单位统一**：维度单位是否统一使用了规范推荐的 `px` 或 `rem`？

## 常见坑与对策
*   **坑**：Token 命名仅区分大小写（如 `Color` 和 `color`）。
    *   **对策**：很多下游工具不区分大小写，必须强制全小写或 kebab-case 命名规范。
*   **坑**：过度嵌套导致路径过长（如 `sys.color.action.btn.primary.hover.bg`）。
    *   **对策**：控制在 3-4 层以内，过深的层级会消耗 AI 的上下文窗口且增加幻觉概率。
*   **坑**：混合使用 Group 和 Token。
    *   **对策**：一个节点要么是 Token（有 `$value`），要么是 Group（无 `$value`），禁止既当 Token 又当文件夹。
*   **坑**：修改基础 Token 未做回归测试。
    *   **对策**：引入视觉回归测试（Visual Regression Testing），每次 Token 变更自动触发截图比对。

## 可用于丰富《AI 辅助软件产品》的写作点
*   **第 3 章（PRD 与 规范）**：在技术可行性小节，强调 Design Tokens 是连接设计师与 AI 工程师的通用语言（Ubiquitous Language）。没有 Token，AI 生成的代码就是一次性的垃圾代码。
*   **第 6 章（生成式 UI）**：
    *   **RAG 策略**：详细描述如何检索相关的 Token 片段注入 Context。不必一次性注入整个 Design System，而是根据用户请求（如画一个登录框）检索 `input.*`, `button.*`, `spacing.*` 等相关 Token。
    *   **Token 约束**：展示一个 Prompt 案例，要求 LLM 仅使用提供的 Token 键名填充 CSS 属性，并展示这如何消除了视觉不一致。
*   **第 8 章（前端工程）**：介绍设计系统即代码（Design System as Code）的工作流。AI 不仅是消费者，也可以是维护者——让 AI 扫描旧代码中的硬编码颜色，自动重构为 Token 引用。
