# [91] Claude Agent 文档总览：把能力拆成可复用的工作流

- 资料类型：官方文档 + 官方博客合集
- 原始来源：
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
  - https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
  - https://www.anthropic.com/research/building-effective-agents
  - https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone
  - https://www.anthropic.com/news/snowflake-anthropic-expanded-partnership
- 对应章节：第 10 章（Agent 体系）

## 一句话
Claude 的 Agent 文档核心不是“让模型更聪明”，而是把**目标拆成可观察、可验证、可回退的步骤**，并用工具调用、MCP 连接与流程编排把结果拉回可控范围。

## 文档地图（按能力）
| 能力块 | 关键文档 | 你应该关注的点 |
| --- | --- | --- |
| Agent 基础与边界 | Agents & Tools / Agent Skills | 任务拆分、终止条件、状态与工具边界、失败回退与成本控制。 |
| 工作流落地 | Agent Skills Quickstart + Best Practices | 分阶段计划、检查点、评估与安全门禁，避免“长链条黑盒”。 |
| 工具调用 | Tool use（overview/implement/programmatic） | 工具输入输出契约、错误语义、重试与幂等，确保可回归。 |
| 真实环境操作 | Computer use tool | 最小权限、审计日志、敏感动作限制与人工确认。 |
| 远程工具生态 | MCP connector + Remote MCP servers | 用标准协议接入外部系统，集中管理权限与数据边界。 |
| 代码与系统工具 | Code execution/Bash/Text editor/Web search/Web fetch/Memory | 用专门工具完成窄任务，避免在提示词里“兜底”。 |
| 生态与平台策略 | Anthropic News（MCP/Claude Code） | 官方对 Agent 生态的定位与治理取向。 |

## 你该从文档带走什么
- **可控性优先**：每个 Agent 任务都必须有明确的“开始-进行-终止”条件，不允许无限循环或自我扩张。
- **工具契约即门禁**：工具定义要包含输入校验、权限范围、失败语义与回滚策略，避免“工具当黑盒”。
- **流程化而非一条长链**：把任务拆成阶段，阶段之间有检查点，必要时引入人工审阅或自动验收。
- **MCP 是权限与数据边界的基座**：远程工具接入时，用统一协议治理连接方式、权限范围与审计。
- **真实环境访问要最小化**：Computer use 适合补位自动化，而非替代系统权限，关键操作需要审计与警戒线。

## 在本书里怎么用
- 第 10 章写作时，把“Agent 能做什么”写成**工作流图 + 门禁**，而不是“模型很强”。
- 第 7 章工程化部分可引用“工具契约”思路：把工具调用当作 API 协议，强制验收和回滚。
- 第 18 章评测体系：把 Agent 的每个阶段都接入日志/指标，确保可追踪与可复盘。
- 第 17 章部署运维：把 MCP 服务器当成“可审计的外部能力网关”，把权限收敛在服务端。

## 常见误用
- **只有一个超长提示词**：把所有步骤塞进一条提示里，导致无法拆解、无法测、不可回归。
- **工具无边界**：把数据库、支付、生产系统暴露为“无权限工具”，最后只能靠人工兜底。
- **无终止条件**：让 Agent 自主决定结束时间，结果是成本不可控、行为不可预测。
- **忽略审计**：让 Agent 在真实环境操作但不记录日志，问题出现后无法追责。
