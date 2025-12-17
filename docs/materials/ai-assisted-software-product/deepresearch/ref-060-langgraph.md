# Deep Research: [60] LangGraph：把 Agent 变成可控的工作流

- Source: https://docs.langchain.com/oss/python/langgraph/overview/
- Note: ../notes/ref-060-langgraph.md
- Snapshot: ../sources/md/docs-langchain-com-oss-python-langgraph-overview-38f4f5c73818.md
I will create the deep research summary for LangGraph in the specified format.

# [60] LangGraph：把 Agent 变成可控的工作流

- 资料类型：官方文档
- 原始来源：https://docs.langchain.com/oss/python/langgraph/overview/
- 对应章节：第 7 章（Agent）

## TL;DR
LangGraph 是一个用于构建有状态、长运行 Agent 的低级编排框架，它通过“图”（Graph）结构替代线性的“链”（Chain），让开发者能通过循环、持久化和状态管理，精确控制 Agent 的决策流程与边界。

## 核心观点
1.  **图胜于链**：复杂的 Agent 交互往往包含循环（Loop）和分支，DAG（有向无环图）不足以描述，需要状态机（State Machine）模型。
2.  **状态即核心**：Agent 的本质是“状态”的演进。LangGraph 强制开发者显式定义状态（Schema），确保每一步流转都有迹可循。
3.  **持久化执行（Durable Execution）**：通过 Checkpointer 机制，Agent 可以随时暂停、保存状态、从故障中恢复，甚至“时间旅行”回滚到之前的步骤。
4.  **人机回环（Human-in-the-loop）**：原生支持在图的任意节点“中断”，等待人类审批或修改状态后再继续，这是企业级 Agent 安全落地的关键。
5.  **低级编排**：它不预设 Prompt 或模型，专注于底层的控制流（Orchestration），可与 LangChain 组件配合，也可独立使用。
6.  **可观测性**：与 LangSmith 深度集成，可视化展示图的执行路径和状态变更，解决“黑盒”调试难题。

## 可落地做法
**面向工程团队的实施步骤：**
1.  **定义状态（State Schema）**：使用 `TypedDict` 或 Pydantic 定义 Agent 在生命周期内需要维护的所有数据字段（如 `messages`, `context`, `tool_outputs`）。
2.  **原子化节点（Nodes）**：将业务逻辑拆解为独立的纯函数（Node），例如 `call_model`、`execute_tool`、`human_review`。
3.  **编排边与条件（Edges）**：
    *   **普通边**：`call_model` -> `execute_tool`。
    *   **条件边**：根据 LLM 输出决定是“结束”还是“调用工具”。
4.  **配置持久化**：接入数据库（如 Postgres, Redis）作为 Checkpointer，为每个会话生成 `thread_id`。
5.  **埋入干预点**：在敏感操作节点前设置 `interrupt_before`，强行暂停等待 API 触发继续指令。

## 检查清单：LangGraph 架构设计
- [ ] **状态边界**：是否清晰定义了 State 中哪些是追加（Append）数据，哪些是覆盖（Overwrite）数据？
- [ ] **循环控制**：是否为图的循环设置了 `recursion_limit`（最大递归次数）以防止死循环？
- [ ] **人机交互**：关键的写操作（如数据库修改、API 调用）前是否有 Human-in-the-loop 检查？
- [ ] **容错机制**：单个节点失败时，是否有重试策略或错误处理分支，而不是让整个图崩溃？
- [ ] **状态精简**：是否定期清理 State 中不必要的历史上下文，防止 Token 消耗过大？

## 常见坑与对策
- **坑**：把简单的线性流程强行用 Graph 实现，导致代码复杂度无谓增加。
    - **对策**：如果流程是 A -> B -> C，直接用 LangChain Expression Language (LCEL)；只有涉及到循环（Loop）或复杂分支时才上 LangGraph。
- **坑**：忽视 State 的并发问题。
    - **对策**：LangGraph 的状态更新是顺序的，但如果 Web 服务并发请求同一个 `thread_id`，可能会导致状态竞争，需利用其内置的锁机制或队列。
- **坑**：认为“持久化”就是“存数据库”。
    - **对策**：持久化不仅仅是存储，更重要的是序列化与反序列化能力（Pickle/JSON），确保 Python 对象能完整还原。

## 可用于丰富《AI 辅助软件产品》的写作点
- **第 7 章（Agent 架构）**：
    - 用 LangGraph 对比传统的 "ReAct Loop"，说明为什么企业级应用需要更显式的状态机控制。
    - 引用“图”的概念解释 Agent 怎么从“玩具”变成“工具”：通过给不可控的 LLM 加上可控的“边”和“节点”。
- **第 19 章（迭代与运维）**：
    - 介绍“时间旅行”调试法：利用持久化状态，修改历史步骤中的某个参数，重新运行后续流程，这是调试复杂 Agent 的杀手级功能。
- **第 20 章（治理与合规）**：
    - 强调 Human-in-the-loop 不仅仅是功能，更是合规要求（Risk Control）。LangGraph 的 `interrupt` 机制是实现这一点的技术底座。
