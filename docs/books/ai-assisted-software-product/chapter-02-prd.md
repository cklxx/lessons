# 第 2 章：PRD 自动化与架构蓝图

> 通过对话生成标准化 PRD、流程图和数据库 Schema，减少沟通歧义并提前暴露性能瓶颈。[11][12]

!!! note "关于复现、目录与 CI"
    本章中出现的 `make ...`、`CI`、以及示例目录/文件路径（例如 `path/to/file`）均为落地约定，用于说明如何把方法落实到你自己的工程仓库中。本仓库仅提供文档，读者需自行实现或用等价工具链替代。

## 章节定位
从“需求”到“可执行设计”的桥梁。你将让 AI 生成可机读的 PRD、自动渲染流程/时序图，并产出具备容量估算的数据库设计，确保后续编码无歧义、无遗漏。[11][12][13]

## 你将收获什么
- 一套可复用的 PRD Prompt 模板与 JSON Schema 校验器，确保字段完整且可机器解析。[11]
- 自动生成流程/时序图并覆盖异常路径，降低沟通成本。[12]
- 基于 DDD 的数据库 Schema 与索引策略，提前估算延迟与吞吐瓶颈。[13][20]

## 方法论速览
1. **对话即文档：** 以 YAML/JSON 定义 PRD 结构，LLM 生成后立即用模式校验，避免“口语化”丢字段。[11]
2. **流程与时序：** 先写文字用例，再自动转 Mermaid/PlantUML；必须包含失败/补偿路径。[12]
3. **数据建模：** 从领域事件推导聚合与边界上下文，生成 SQL/NoSQL 对照方案，明确索引与容量预算。[13]

## 典型场景
- **MVP 规划：** 两小时内完成登录、支付、内容推荐的全链路 PRD 草稿并自动校验必填字段。
- **性能先行：** 针对高并发接口，提前给出分区键、限流策略和幂等设计，避免上线后返工。

## 实战路径
### 1. PRD 模板与校验
```python
import yaml, jsonschema, pathlib
schema = {
  "type": "object",
  "required": ["features", "non_functional", "tracking", "api"],
  "properties": {
    "features": {"type": "array"},
    "non_functional": {"type": "object"},
    "tracking": {"type": "object"},
    "api": {"type": "array"}
  }
}
for path in pathlib.Path("prd").glob("*.yml"):
    data = yaml.safe_load(path.read_text())
    jsonschema.validate(instance=data, schema=schema)
```
- CI 运行失败阻断合并，强制补齐字段。

### 2. 时序图生成
- 用 Prompt 生成 Mermaid 时序图，落地文件 `diagrams/*.mmd`，再用 `mmdc` 渲染 PNG，渲染失败即视为文档缺失。[12]
- 强制在图中标记超时、重试、补偿逻辑，避免“只画成功路径”。

### 3. 数据库 Schema 验证
- 依据访问模式生成 SQL 表：主键、二级索引、分区键；同时给出 NoSQL（如 Dynamo/RedisJSON）等价设计，附容量与延迟估算。[13]
- 用 Faker 生成 10 万条合成数据，跑读写基准，记录 P50/P95 延迟，超过预算即回滚设计。

### 4. API 合约与监测
- 生成 OpenAPI 规范，自动导出客户端 SDK，确保前后端并行开发。[20]
- 在 PRD 中写清埋点需求，生成事件名、属性与采样率，接入监控后回流到假设验证。

## 复现检查（落地建议）
- `make prd-validate`：校验 YAML/JSON 结构、渲染 Mermaid、生成 OpenAPI。
- `make schema-benchmark`：自动基准测试 SQL/NoSQL 方案并输出 CSV 报告。
- PRD 与图表均需在 CI 产出 PDF 供审稿人下载。

## 常见陷阱
- **遗漏异常流：** 退款、超时、幂等未描述，后端实现容易分叉。
- **索引过度：** 未结合读写比例，索引过多导致写入放大，需用基准数据说话。
- **文档漂移：** 代码与 PRD 不一致时，以 OpenAPI 生成的客户端测试为准，CI 对比差异。

## 延伸练习
- 让 LLM 根据埋点自动生成可视化仪表盘配置（如 Grafana JSON），上线后直接复用。
- 对比两种不同的分区策略（按用户 vs 按时间），测算成本与查询延迟差异。

## 交付物与验收（落地建议）
- `prd/*.yml`：可机读 PRD，CI 校验通过。
- `diagrams/*.mmd` 与渲染 PNG：包含异常/补偿路径。
- `schemas/`：SQL/NoSQL DDL、基准报告与容量估算表。

## 正文扩展稿（用于成书排版）
1. **对话到架构的一致性**：先让 LLM 生成“领域词汇表”，再用这些词汇驱动 PRD、时序图、API 合约与 Schema，避免不同文档使用不同名词导致歧义。所有文档引用同一份词汇表文件 `prd/vocabulary.yml`，CI 校验引用一致。[11][18]
2. **PRD 可信度与变更记录**：每个功能块附“证据来源、样本量、实验计划、决策编号”，变更时在 YAML 中递增 `revision` 并链接到决策记录，保证读者能追踪“为何修改”。[4]
3. **流水线化生成**：示例：用 `make prd` 自动生成 Markdown/HTML PRD、Mermaid 图、OpenAPI 草案与 PDF；用 `make prd-check` 运行 OpenAPI lint（例如 Spectral）、Mermaid 渲染和字段必填校验。失败即阻止合并，确保文档可视、可编译、可消费。[5][65]
4. **容量与性能假设显式化**：Schema 文件内以注释注明预估 QPS、热键分布、索引覆盖率；附基准脚本与结果 CSV。若实测 P95 超出预算则强制回到设计环节重新评审。[13]
5. **指标与埋点闭环**：在 PRD 中为注册、登录、支付、核心留存行为定义事件名与校验 SQL；建议提供一个“埋点契约测试”（示例路径：`tests/metrics/test_metrics_contract.py`）检查字段存在、类型正确，并将其设为发布门禁以避免“上线无数据”。[6]

## 参考
详见本书统一参考文献列表：[`references.md`](references.md)。
