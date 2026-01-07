# Claude Agent 文档合订本（官方文档与博客汇总）

> 目标：把 Claude/Anthropic 与 Agent 相关的官方文档与博客要点整理为一份可直接落地的手册，帮助你把 Agent 设计成**可控、可测、可回滚**的工作流。

## 读者与使用方式
- **适合谁**：产品/架构/工程负责人，负责落地 Agent、工具调用与自动化流程。
- **怎么用**：先看“文档地图”快速定位能力，再按章节使用“落地要点”和“检查清单”实施。

## 内容获取说明
- 本书以“摘要 + 实施要点”为主，保留原文链接以便核查。
- 原文通常受版权保护，因此此处只保留简短摘要，不复制完整正文。

---

## 文档地图（按能力）

### 1) Agent 基础与工作流能力
- **Agents & Tools 总览**：统一理解 Agent 的能力边界、可控性与安全门禁。
- **Agent Skills（overview/quickstart/best practices）**：如何把任务拆成阶段、定义终止条件、设置检查点与评估。

### 2) 工具调用与执行环境
- **Tool use（overview/implement/programmatic）**：工具输入输出契约、错误语义、重试与幂等。
- **Computer use tool**：让 Agent 操作真实环境时的权限控制、审计、风险限制。
- **专用工具**：Web search / Web fetch / Memory / Code execution / Bash / Text editor。

### 3) 连接外部系统的标准协议
- **MCP connector + Remote MCP servers**：通过统一协议接入外部能力，集中治理权限与数据边界。

### 4) 官方博客（Agent 生态与策略）
- **MCP 基金会与生态治理**：官方对 Agent 生态、协议与治理的公开定位。
- **Claude Code 相关公告**：从工程实践角度理解 Agent 的“落地载体”。

---

## 核心原则（从文档中提炼的共同规律）

### 1) 可控性优先
- 每个 Agent 任务都要有明确的开始、终止条件与失败回退，避免无限循环。
- 把“模型能力”拆成**可度量的任务阶段**，阶段之间有检查点与验收。

### 2) 工具契约即门禁
- 工具调用必须有结构化输入、输出、错误语义和权限边界。
- 避免在提示词里“包打天下”，把操作落实到工具契约和执行策略。

### 3) 把 Agent 设计成工作流
- 用任务分解、状态管理、检查点与审计日志替代“长提示词”。
- 对关键动作引入人工确认或自动验收，防止不可控扩散。

### 4) 真实环境访问最小化
- 让 Agent 进入真实环境必须有最小权限原则与审计日志。
- 高风险动作（支付、权限变更、删除）必须人工确认或分级审批。

---

## 能力块落地指南

### A. Agent 设计与工作流拆解
1. **明确目标与终止条件**：确保任务可停、可回滚。
2. **拆分阶段与检查点**：每一阶段有输入/输出契约。
3. **内置失败路径**：设计“失败就退回上一步”或“转人工”的策略。
4. **输出结构化结果**：让评估与回归可自动化。

### B. Tool Use（工具调用）
1. **定义工具契约**：输入 schema、输出 schema、错误语义。
2. **设计幂等策略**：能安全重试，避免重复副作用。
3. **限制权限与范围**：确保工具只做“最小动作”。
4. **保留审计日志**：输入、输出、失败原因可追溯。

### C. Computer Use（真实环境操作）
1. **最小权限**：只开放必要的系统或浏览器能力。
2. **敏感操作门禁**：关键动作必须确认或审批。
3. **回放与审计**：日志可回溯，出现问题可复盘。

### D. MCP（Model Context Protocol）
1. **统一接入外部能力**：用协议而非“私有脚本”。
2. **权限集中管理**：服务端统一治理权限与数据边界。
3. **可审计、可替换**：工具服务可替换，能力可扩展。

---

## 常见误用（踩坑清单）
- **把所有步骤塞进一条提示**：不可测、不可回归、不可复盘。
- **工具无边界**：将生产系统暴露为“全能工具”，风险不可控。
- **无终止条件**：Agent 自主决定结束时间，导致成本暴涨。
- **忽略审计**：真实环境操作无日志，出问题难追责。

---

## 来源摘要（按模块）

### Agent Skills 与工作流设计
- **Agents & Tools 总览**：强调 Agent 的职责边界、可控性与安全门禁，避免“一条长链”。
- **Agent Skills（overview/quickstart/best practices）**：强调拆分任务、检查点、终止条件与可回归的评估流程。

### Tool Use 与执行环境
- **Tool use（overview/implement/programmatic）**：明确工具输入输出契约、错误语义与幂等策略。
- **Fine-grained tool streaming**：强调工具调用的阶段化输出与可观测性。
- **Tool search tool**：强调在可控范围内为 Agent 搜索可用工具。
- **Computer use tool**：强调真实环境操作的最小权限、审计与风险限制。
- **Web search / Web fetch**：强调信息获取与检索边界的可控性。
- **Memory tool**：强调可追溯的记忆与上下文管理。
- **Code execution / Bash / Text editor**：强调用专用工具完成窄任务并记录操作轨迹。

### MCP 生态与外部能力接入
- **MCP connector / Remote MCP servers**：强调用统一协议治理权限、边界与审计。

### 官方博客（Agent 生态与工程落地）
- **MCP 基金会公告**：强调协议开放与生态治理方向。
- **Building Effective Agents**：强调用任务分解、工具契约与评估闭环提升 Agent 可控性。
- **Claude Code 相关公告**：强调把 Agent 能力落地为可复用的工程化工具。
- **Snowflake × Anthropic**：强调企业级场景的 agentic AI 落地与协作模式。

---

## 落地检查清单（可复制）

**目标与边界**
- [ ] 有清晰的目标定义与停止条件。
- [ ] 高风险动作有人工确认或审批流程。

**工作流与阶段拆分**
- [ ] 每一阶段有输入/输出与验收标准。
- [ ] 失败路径定义清晰（重试/回退/转人工）。

**工具契约与权限**
- [ ] 工具输入输出为结构化协议。
- [ ] 权限边界明确，最小权限原则落实。

**审计与复盘**
- [ ] 有完整日志与可回放记录。
- [ ] 关键错误能追踪到工具调用链路。

---

## 原文索引（官方文档）
- https://platform.claude.com/docs/en/agents-and-tools
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool
- https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers

## 原文索引（官方博客与生态）
- https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- https://www.anthropic.com/research/building-effective-agents
- https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone
- https://www.anthropic.com/news/snowflake-anthropic-expanded-partnership
- https://modelcontextprotocol.io/

## 其他 Research Blog 索引（仅链接）
- https://www.anthropic.com/research/alignment-faking
- https://www.anthropic.com/research/anthropic-interviewer
- https://www.anthropic.com/research/bloom
- https://www.anthropic.com/research/constitutional-classifiers
- https://www.anthropic.com/research/deprecation-commitments
- https://www.anthropic.com/research/emergent-misalignment-reward-hacking
- https://www.anthropic.com/research/estimating-productivity-gains
- https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- https://www.anthropic.com/research/introspection
- https://www.anthropic.com/research/project-fetch-robot-dog
- https://www.anthropic.com/research/project-vend-2
- https://www.anthropic.com/research/prompt-injection-defenses
- https://www.anthropic.com/research/tracing-thoughts-language-model
- https://www.anthropic.com/research/team/alignment
- https://www.anthropic.com/research/team/economic-research
- https://www.anthropic.com/research/team/interpretability
- https://www.anthropic.com/research/team/societal-impacts
