# MCP-Bench：MCP 工具评测基准

原文链接： [MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers](https://arxiv.org/abs/2508.20453) [99]

## 论文信息
- 年份：2025 [99]
- 作者：Zhenting Wang, Qi Chang, Hemani Patel, Shashank Biju, Cheng-En Wu, Quan Liu, Aolin Ding, Alireza Rezazadeh, Ankit Shah, Yujia Bao, Eugene Siow [99]
- 作者背景（研究领域）：工具调用评测/MCP 生态 [99]
- 前后血缘关系（同主题）：前序：[ToolLLM](toollm.md)、[StableToolBench](stable-toolbench.md)；后续：无（MCP 工具评测方向代表）

## 主旨
MCP-Bench 的主旨是通过 MCP server 组织真实工具任务，评估代理在复杂工具生态中的规划、调用与执行闭环能力。[99]

## 背景与问题定义
论文指出传统工具评测往往忽略真实工具集成、权限管理与执行反馈，导致结果与工程实践脱节。MCP-Bench 旨在将工具调用放到可复现的 MCP 生态中进行衡量。[99]

## 方法与机制
MCP-Bench 提供基于 MCP 的工具集合与任务脚本，评测记录完整调用链、权限校验与执行反馈。评估指标不仅包括成功率，还包括调用稳定性与错误类型分布。[99]

## 实验与结果
实验显示，代理在 MCP 任务中常见失败源于权限与参数格式问题，表明工具协议对代理表现具有决定性影响。[99]

## 关键数据结果
- MCP 任务评测揭示了工具调用闭环中的主要失败模式，为工程优化提供诊断线索。[99]

## 工程启示（优化点）
- 构建可复现的 MCP 工具集与任务清单。
- 记录调用链与执行反馈，便于诊断失败模式。
- 对权限失败与参数错误分别统计与治理。
- 将工具评测纳入持续回归流程。

## 局限与延伸
MCP-Bench 仍受工具覆盖范围限制，且真实工具的权限与成本问题需要进一步治理。未来方向包括：扩展更多领域的 MCP 任务、引入安全与合规维度评测，以及与在线工具生态的持续同步。[99]
