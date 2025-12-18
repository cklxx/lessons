# Deep Research: [29] ReAct：Agent 的推理—行动循环

- Source: https://arxiv.org/abs/2210.03629
- Note: ../notes/ref-029-react.md
- Snapshot: ../sources/md/arxiv-org-abs-2210-03629-7647307fe498.md
## TL;DR
ReAct 范式通过交替生成“推理轨迹”（Thought）与“行动”（Action），让大模型能够利用外部工具的反馈动态调整认知，有效解决了纯推理易产生幻觉、纯行动缺乏规划能力的问题。

## 核心观点
1.  **协同效应**：推理（Reasoning）用于规划目标、跟踪进度和处理异常，行动（Acting）用于从外部环境获取事实；两者交织产生“大于之和”的效果。
2.  **事实落地（Groundedness）**：相比 Chain-of-Thought (CoT)，ReAct 强依赖外部观察（Observation），大幅降低了事实性错误和幻觉。
3.  **过程可解释与可调试**：显式的 `Thought` 字段暴露了模型的决策逻辑，使得开发者可以通过检查或修改“想法”来低成本地修正 Agent 行为，而无需重训。
4.  **策略互补**：在知识密集型任务中，ReAct（擅长求真）与 CoT（擅长利用内隐知识）结合使用效果最佳（例如 ReAct 失败时回退到 CoT，或 CoT 信心不足时启动 ReAct）。
5.  **稀疏推理（Sparse Reasoning）**：在长链路决策任务（如游戏、网页导航）中，不需要每一步都推理，仅在关键决策点生成 Thought 即可保持高效。

## 可落地做法

### 1. 工程实现：构建 ReAct 循环 (The Loop)
*   **步骤一：定义动作空间 (Action Space)**
    确定 Agent 可调用的 API（如 `search(query)`, `click(id)`, `finish(answer)`）。接口需保持原子性和幂等性。
*   **步骤二：Prompt 构造**
    使用 Few-shot 样本，严格遵循格式：`Thought: [思考] \n Action: [工具名][参数] \n Observation: [工具返回结果]`。
*   **步骤三：执行主循环**
    1.  将当前上下文（History + New Question）喂给 LLM。
    2.  设置停止词（Stop Sequence）为 `Observation:`，防止 LLM 自行编造工具返回结果。
    3.  解析 LLM 输出，提取 Action。
    4.  **执行代码/调用 API**，获取真实结果。
    5.  将 `Observation: [真实结果]` 拼接到上下文。
    6.  重复上述过程，直到解析出 `Finish` 动作或达到最大步数。

### 2. 产品设计：透明化思考过程
*   在 UI 上将 `Thought` 内容通过折叠卡片或打字机效果展示给用户（参考 Perplexity 或 ChatGPT 的 "Searching..." 状态），提升用户对 AI 响应的信任度。
*   提供“人工介入”入口：允许高级用户在 Agent 卡住时编辑 `Thought` 文本，引导 Agent 走出死胡同。

## 检查清单：ReAct Agent 基础实现
若要上线一个基于 ReAct 的功能，请核对以下条目：

*   [ ] **停止词配置**：是否严格配置了 `Observation:` 作为 LLM 的生成停止词？
*   [ ] **工具解析鲁棒性**：解析器能否处理 LLM 输出的非标准格式（如多余空格、错误的括号）？建议使用 Function Calling (Tool Use) API 替代纯文本 Prompt 以提高稳定性。
*   [ ] **最大步数熔断**：是否设置了 Max Steps（如 10 步），防止 Agent 进入死循环消耗过多 Token？
*   [ ] **上下文窗口管理**：当 Observation 内容过长（如网页抓取内容）时，是否有截断或摘要机制？
*   [ ] **错误反馈回路**：当工具调用失败或参数错误时，是否将 Error Message 作为 Observation 反馈给 LLM，让其有机会自我修正？
*   [ ] **回退策略**：当 ReAct 连续多次搜索无果时，是否有机制切换回普通对话模式或寻求人工帮助？

## 常见坑与对策
*   **死循环 (Looping)**：Agent 反复执行相同的搜索或操作。
    *   *对策*：在上下文中检测重复 Action；在 System Prompt 中加入指令“如果搜索结果为空，请尝试精简关键词”；引入惩罚机制。
*   **上下文溢出**：几轮交互后 Prompt 长度爆炸。
    *   *对策*：仅保留最近 N 轮的详细 Observation，早期的 Observation 替换为简短摘要；限制工具返回的字符数（如 `grep` 只返回匹配行及前后 2 行）。
*   **能力被工具限制**：Agent 变得过度依赖工具，连简单常识也要搜索。
    *   *对策*：混合策略。先让 Agent 评估“通过内部知识回答”的置信度，只有置信度低时才调用工具。

## 可用于丰富《AI 辅助软件产品》的写作点
*   **第 7 章 (Engineering/Backend - Agent)**：
    *   使用 ReAct 的流程图替换传统的“请求-响应”图，说明 Agent 系统的核心由于“无状态”变为“有状态循环”。
    *   作为 **"Agent State Machine"** 的基础实现模式进行详细代码拆解。
*   **第 10 章 (Agentic RAG)**：
    *   对比传统 RAG（一次检索 -> 生成）与 **Agentic RAG**（ReAct 模式：检索 -> 看了不够 -> 换个词再搜 -> 生成）。ReAct 是实现复杂问题（Multi-hop QA）检索的关键。
*   **第 18 章 (Evaluation)**：
    *   新增“过程评估”指标：除了最终答案准确率，还要评估 **Trajectory Efficiency**（轨迹效率，是否走了弯路）和 **Hallucination Rate in Thoughts**（思考过程中的幻觉率）。
