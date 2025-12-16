# 全书质量控制与复现清单（QCR）

> 用于审稿与自检的统一“守门”文件，覆盖需求验证到部署运维的所有章节。所有门槛均须有日志、报告或指标截图为证。

## 总则
- **可运行性：** 每项检查对应 `make` 任务或脚本，要求生成可追溯的日志/报告。
- **可审计性：** 关键数据、模型与配置需有 datasheet / model card，引用来源写明许可证。
- **可回滚：** 任何指标退化必须有回滚路径与版本记录（Git tag + artifact 路径）。

---

## 第一篇 指挥官
- **需求验证（Ch01）：** `make demand-benchmark`
  - 主题覆盖度、情感混淆矩阵 F1 ≥ 0.8；数据源与采集时间记录于 datasheet。
  - 生成《决策白板》：假设/证据/反例/风险/下周实验。
- **PRD/架构（Ch02）：** `make prd-validate`
  - PRD 模板字段齐全（愿景、用户故事、埋点、异常路径、SLO）。
  - Mermaid 流程/时序图在 CI 通过渲染校验；SQL Schema 通过约束检查（索引、租户隔离、审计字段）。
- **UI/UX（Ch03）：** `make ui-regression`
  - 视觉回归对比基线差异 < 0.5%；可访问性（a11y）检查通过；多设备截图归档。

## 第二篇 工程师
- **编码工作流（Ch04）：** `make test`
  - 覆盖率阈值（例如 80%）达标；pre-commit、SAST、依赖漏洞扫描无阻塞。
- **后端模块（Ch05）：** `make backend-check`
  - 身份验证、RBAC、速率限制与 Webhook 幂等性单测通过；开放接口生成最新 OpenAPI 文档。

## 第三篇 架构师
- **RAG（Ch06）：** `make rag-benchmark`
  - RAGAS `Context Precision`、`Answer Relevance` ≥ 基线；嵌入/检索/重排序参数记录。
- **Agent（Ch07）：** `make agent-e2e`
  - ReAct/流程编排用例通过；工具调用白名单与速率限制日志齐全；长链路超时与重试策略验证。

## 第四篇 造物主
- **数据工程（Ch08）：** `make data-audit`
  - 去重、去毒、PII 过滤报告；合成数据与真实数据分层质量评分。
- **预训练/增量（Ch09）：** `make pretrain-smoke`
  - Tokenizer/语料采样报告；显存/吞吐/成本估算表与实验日志。
- **后训练（Ch10）：** `make sft-train && make dpo-train`
  - Loss/偏好胜率曲线归档；安全红队命中率下降趋势记录；模型卡更新。

## 第五篇 运维专家
- **推理部署（Ch11）：** `make infer-benchmark`
  - 吞吐/延迟与量化精度对比表；限流、熔断、灰度发布日志。
- **LLMOps（Ch12）：** `make llmops-audit`
  - 观测（LangSmith/日志）与评估（RAGAS/MT-Bench）报告；成本与缓存命中率趋势图。

---

## 发布与版本
- **版本标签：** 每轮大更新以 `book-vX.Y` 打 tag，附变更日志与关键指标对比。
- **档案目录：** `reports/` 下存放各章节 CI 输出、图表与 PDF；确保 MkDocs 可引用。
- **审核流程：** 章节作者自测 → 同行审查对照本清单 → 维护者签字发布。

## 使用建议
- 将本清单添加到团队/个人的 CI pipeline，确保每次提交都有自动化证据。
- 阅读时可对照各章节的“实操与验证”小节，确认已覆盖对应的 QCR 条款。
- 如需扩展指标或定制阈值，请在每章目录下添加 `local-checklist.md` 并更新引用。
