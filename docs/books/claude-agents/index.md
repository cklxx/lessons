# Claude Agent 文档合订本（官方文档与博客汇总）

> 目标：把 Claude/Anthropic 与 Agent 相关的官方文档与博客要点整理为一份可落地手册，帮助你把 Agent 设计成**可控、可测、可回滚**的工作流。

## 读者与使用方式
- **适合谁**：产品/架构/工程负责人，负责落地 Agent、工具调用、自动化流程与安全治理。
- **怎么用**：先看“文档地图”定位能力，再按“官方要点”和“落地流程”实施，最后用“检查清单”收尾。

## 内容获取说明
- 覆盖范围：Claude 官方文档（Agents & Tools + Agent SDK）与 Anthropic 官方博客/研究。
- 原文受版权保护，因此只保留摘要与可落地要点，完整内容请查看“原文索引”。
- 本文按“设计 → 实现 → 安全 → 运营”顺序组织，避免只堆链接。

---

## 文档地图（按能力）

| 能力 | 关键文档 | 落地关注点 |
| --- | --- | --- |
| Agent 定义与工作流 | Building Effective Agents（研究） | 何时用 workflow / 何时用 agent，任务拆解与验收 |
| Agent Skills | Agent Skills（overview/quickstart/best practices） | Skill 结构、触发条件、写作规范与安全审计 |
| Tool Use 基础 | Tool use overview / implement / programmatic | 工具契约、schema、幂等与错误处理 |
| 内建工具 | Web search / Web fetch / Memory / Code execution / Bash / Text editor / Computer use / Tool search | 能力边界、风险与参数限制 |
| MCP 协议 | MCP connector / Remote MCP servers + modelcontextprotocol.io | 统一接入外部工具、集中权限治理 |
| Agent SDK（Claude Code 运行时） | Agent SDK overview / quickstart / python / typescript | 运行时、权限、hooks、sessions、subagents |
| 安全与部署 | permissions / secure-deployment / computer-use | 最小权限、隔离、审计与防注入 |
| 运维与可观测 | cost-tracking / structured-outputs / checkpointing | 费用、可追踪输出、可回滚文件变更 |

---

## 核心概念速览（先统一词汇）
- **Agent vs Workflow**：Workflow 是预定义流程编排；Agent 是由模型动态决定步骤与工具调用。
- **Tool Use**：基于 `name/description/input_schema` 的工具契约，让模型在结构化输入下调用工具。
- **Agent Skills**：可复用的 `SKILL.md` 指令包，按需加载并自动触发。
- **Programmatic Tool Calling**：允许在 code execution 容器内再调用工具，支持更复杂的数据流。
- **MCP（Model Context Protocol）**：统一接入外部系统与工具的协议层。
- **Agent SDK**：把 Claude Code 的 agent loop、工具和上下文管理作为库提供。
- **Sessions / Subagents**：会话续航与子代理分工机制。
- **Hooks / Permissions**：在工具调用前后进行拦截、审批、审计与安全控制。

---

## 官方文档要点（可直接落地）

### 1) Agent Skills（API + SDK）
- **Skill 结构**：必须包含 `SKILL.md` + YAML frontmatter（`name`/`description`），名称需小写、短、可读。  
  `description` 要写清“做什么”和“什么时候用”，否则模型不会触发。
- **加载机制**：只预加载元信息；真正执行时才读取正文，因此要简洁，避免占用上下文。
- **安全建议**：仅使用可信来源 Skill；不可信 Skill 必须人工审计。
- **SDK 中的存放位置**：项目技能 `.claude/skills/`，用户技能 `~/.claude/skills/`；通过 `setting_sources`/`settingSources` 启用。
- **工具限制**：SDK 中工具权限由 `allowedTools` 控制，`SKILL.md` 的 `allowed-tools` 仅对 Claude Code CLI 生效。
- **预置能力**：官方提供 Office/PDF 等预置 Skills（PPTX/XLSX/DOCX）用于文档类任务。

### 2) Tool Use（基础契约 + 编排）
- **工具定义**：`name`、`description`、`input_schema` 是最小必需；复杂工具可加 `input_examples`。
- **描述越详细越好**：明确“何时用/何时不用/边界条件”，否则模型难以稳定调用。
- **严格 schema**：配合 Structured Outputs / `strict` 工具定义，避免参数漂移。
- **执行链路**：`tool_use` → 你执行工具 → `tool_result` 回传；所有错误语义要结构化。
- **Programmatic Tool Calling**：可在 code execution 容器内调用工具；用 `allowed_callers` 限制调用来源，并留意容器超时与复用。
- **Fine-grained Tool Streaming**：适用于长耗时工具；需要处理无效 JSON、分段输出与缓冲重试。

### 3) 内建工具速查（能力 + 风险）
| 工具 | 适合场景 | 风险/限制 | 关键控制项 |
| --- | --- | --- | --- |
| Web search | 获取最新事实 | 结果可能含注入指令 | 缓存、批量限制 |
| Web fetch | 抓取网页内容 | 内容不可信 | `allowed_domains`、`max_uses` |
| Memory | 跨会话记忆 | 隐私与漂移 | 保存/删除策略 |
| Code execution | 代码运行/数据处理 | 容器有效期 | 容器复用/超时 |
| Bash | 系统命令/脚本 | 破坏性操作 | 沙箱、命令白名单 |
| Text editor | 精准编辑文件 | 误改范围 | 只开放必要目录 |
| Computer use | UI/桌面自动化 | 高风险、可扩散 | 最小权限、审计 |
| Tool search | 大量工具筛选 | 误选工具 | Regex/BM25 策略 |

### 4) MCP（Model Context Protocol）
- **MCP Connector**：通过 API 直接接入 MCP 服务器，无需自建客户端。
- **配置粒度**：支持工具 allowlist/denylist、OAuth Bearer、单请求多服务器。
- **Remote MCP servers**：推荐把外部系统统一成 MCP 服务，便于权限治理与替换。

### 5) Agent SDK（Claude Code 作为库）
- **运行时**：依赖 Claude Code CLI；Python/TypeScript 均可使用。
- **能力面板**：Read/Write/Edit/Bash/Glob/Grep/WebSearch/WebFetch 等内建工具；支持 hooks、plugins、自定义工具与 MCP。
- **权限模型（四层）**：Permission modes → `canUseTool` → Hooks → `settings.json` 规则。
- **Sessions**：自动生成 `session_id`，支持续航与 fork 分支实验。
- **Subagents**：可按 `.claude/agents/` 或参数定义子代理，限定工具范围。
- **Structured outputs**：用 Zod/Pydantic 定义 schema，强制输出 JSON 结构。
- **Cost tracking**：`usage` 中包含 token 与 `total_cost_usd`，适合做计费与限额。
- **Checkpointing**：追踪 Write/Edit/NotebookEdit 文件变更，支持一键回滚（Bash 修改不在内）。
- **安全部署**：最小权限、隔离、沙箱、静态分析与 Web 搜索摘要降低注入风险。

---

## 官方博客与研究要点（策略层补充）

### Agent 设计方法论
- **Building Effective Agents**：强调简单可组合模式优先，区分 workflow 与 agent，避免过度框架化。
- **When not to use agents**：高确定性、低复杂度任务优先走 workflow，减少不可控性。

### 安全与治理
- **Safe & trustworthy agents 框架**：强调人类可控、行为透明、隐私保护与安全边界。
- **Agentic misalignment / Sleeper agents**：研究提示需要对代理行为进行审计与隔离，避免“隐性目标”风险。

### Computer Use 与 Agent 运行时
- **Developing computer use**：强调能力提升与安全设计并行推进。
- **Introducing computer use**：展示模型可通过 UI 执行任务，但必须强化权限控制与审计。

### Claude Code 与组织级落地
- **Claude Code 自主性增强**：新增 VS Code extension、长任务与 checkpoints，适合任务型代理。
- **团队/企业控制**：引入管理控制与合规模块，强调成本与权限治理。

### MCP 生态
- **Introducing MCP / Donating MCP to AAIF**：MCP 正式开源并进入基金会治理，生态可预期。

---

## 落地流程（目标 → 前置 → 步骤 → 验证 → 失败标准 → 回滚）

**目标**
- 明确 Agent 要完成的“结果”而不是“过程”，写入一页任务定义文档。

**前置**
- 账号/权限：Anthropic 账号、API key、Claude Code CLI（如使用 Agent SDK）。
- 系统/工具：可调用的工具清单、访问边界、数据分类等级。

**步骤**
1. 任务拆解为 workflow + agent 组合，定义终止条件与人工介入点。
2. 设计工具契约（schema + 说明 + 错误语义），必要时启用 strict。
3. 最小权限接入工具与数据源（allowlist/denylist）。
4. 加入 hooks 与 permissions，落地审批与审计日志。
5. 设置成本与行为监控（usage、tool 调用链路、错误率）。
6. 在 staging 跑基准场景，记录输出与失败案例。

**验证**
- 工具调用命中率与失败率在预设阈值内（证据：日志/报表）。
- 关键任务输出可回放、可复现（证据：审计记录与输出存档）。

**失败标准**
- 超过成本/延迟上限，或出现未授权工具调用。
- 无法复现关键输出或出现不可解释的偏差。

**回滚**
- 停用对应 Skill/Tool 配置，恢复到上一个版本。
- 恢复文件 checkpoint 或 git revert，关闭外部工具权限。

---

## 常见误用（踩坑清单）
- **把所有步骤塞进一条提示**：不可测、不可回归、不可复盘。
- **工具无边界**：将生产系统暴露为“全能工具”，风险不可控。
- **无终止条件**：Agent 自主决定结束时间，导致成本暴涨。
- **忽略审计**：真实环境操作无日志，出问题难追责。

---

## 落地检查清单（含证据）

**目标与边界**
- [ ] 目标、终止条件、人工介入点已记录（证据：需求文档/Runbook 链接）。
- [ ] 风险动作有审批或确认机制（证据：权限规则或审核记录）。

**工具契约与权限**
- [ ] 所有工具具备 schema 与详细描述（证据：工具定义 JSON）。
- [ ] `allowedTools`/allowlist/denylist 配置生效（证据：配置文件或日志）。
- [ ] `canUseTool` 或 hooks 已记录阻断策略（证据：hook 代码与触发日志）。

**安全与隔离**
- [ ] 沙箱或最小权限策略已启用（证据：settings.json 或部署说明）。
- [ ] 对外部网页内容有输入过滤/摘要策略（证据：处理逻辑说明）。

**可观测与成本**
- [ ] 记录 usage 与成本字段（证据：日志样本）。
- [ ] 工具调用链路可追踪（证据：链路日志或审计记录）。

**发布与回滚**
- [ ] staging 场景跑通并归档结果（证据：测试报告）。
- [ ] rollback 策略可执行（证据：checkpoint 记录或回滚演练记录）。

---

## 原文索引（官方文档）

### Agent Skills
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart.md
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md

### Tool Use
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool.md
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.md

### MCP
- https://platform.claude.com/docs/en/agents-and-tools/mcp-connector.md
- https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers.md
- https://modelcontextprotocol.io/

### Agent SDK
- https://platform.claude.com/docs/en/agent-sdk/overview.md
- https://platform.claude.com/docs/en/agent-sdk/quickstart.md
- https://platform.claude.com/docs/en/agent-sdk/python.md
- https://platform.claude.com/docs/en/agent-sdk/typescript.md
- https://platform.claude.com/docs/en/agent-sdk/typescript-v2-preview.md
- https://platform.claude.com/docs/en/agent-sdk/skills.md
- https://platform.claude.com/docs/en/agent-sdk/subagents.md
- https://platform.claude.com/docs/en/agent-sdk/hooks.md
- https://platform.claude.com/docs/en/agent-sdk/permissions.md
- https://platform.claude.com/docs/en/agent-sdk/custom-tools.md
- https://platform.claude.com/docs/en/agent-sdk/mcp.md
- https://platform.claude.com/docs/en/agent-sdk/structured-outputs.md
- https://platform.claude.com/docs/en/agent-sdk/cost-tracking.md
- https://platform.claude.com/docs/en/agent-sdk/file-checkpointing.md
- https://platform.claude.com/docs/en/agent-sdk/streaming-vs-single-mode.md
- https://platform.claude.com/docs/en/agent-sdk/sessions.md
- https://platform.claude.com/docs/en/agent-sdk/slash-commands.md
- https://platform.claude.com/docs/en/agent-sdk/plugins.md
- https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts.md
- https://platform.claude.com/docs/en/agent-sdk/hosting.md
- https://platform.claude.com/docs/en/agent-sdk/secure-deployment.md
- https://platform.claude.com/docs/en/agent-sdk/migration-guide.md
- https://platform.claude.com/docs/en/agent-sdk/todo-tracking.md

## 原文索引（官方博客与研究）
- https://www.anthropic.com/research/building-effective-agents
- https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents
- https://www.anthropic.com/news/model-context-protocol
- https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- https://www.anthropic.com/news/developing-computer-use
- https://www.anthropic.com/news/3-5-models-and-computer-use
- https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
- https://www.anthropic.com/news/claude-code-on-team-and-enterprise
- https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone
- https://www.anthropic.com/research/agentic-misalignment
- https://www.anthropic.com/research/probes-catch-sleeper-agents
- https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training
