# Deep Research Index

> 本目录为每篇资料生成一份更深入的可落地扩展笔记，用于补充/强化《AI 辅助软件产品》。

## 怎么用这份索引（建议）
把它当成写作/做产品时的外挂记忆，而不是单纯的资料堆：

1. **先带着问题来**：你是在写 PRD、做原型、上线回归，还是在处理一次线上事故？先选章节，再打开 1–3 篇 Deep Research。
2. **只抄能落地的部分**：优先提取每篇里的检查清单 / 常见坑 / 最小可行做法，把它们改写成你项目里的门禁、模板或回归集样本。
3. **用对比代替感觉**：读到一个方法论时，顺手问一句：它如何进入发布门禁？退化时我怎么回滚？（否则很快又会变成鸡汤）
4. **深浅配合**：notes 目录更像速记，适合快速定位；deepresearch 目录更像扩展笔记，适合把一个点写成可复用的流程。

> 备注：条目后的括号分数是资料的综合评分（用于排序参考），不是正确性保证。遇到关键结论，仍建议回到原文核对。

## 从 Deep Research 写回正文（一个最省力的流程）
这份索引最有用的时刻，是你准备把一个观点写进正文，或者准备把一个风险做成门禁的时候。建议用一个很土但很稳的三步走：

1. 先定裁判：这次你要裁决什么？写清楚一句话断言 + 一个可被证伪的验收口径（指标/对比表/回归集样本）。如果你连验收都写不出来，先别扩写正文。
2. 再抄结构，不抄句子：打开 1 篇 Deep Research，只提取关键门槛、常见坑、最小可行做法、回滚策略。把它们改写成你项目里的检查清单，或者改写成书里一个可执行的小节。
3. 最后落到制品：把结论落到可版本化的东西上，比如 PRD 条款、OpenAPI、lint 规则、评测集、回归用例、监控告警、运行手册。只写解释但没有落点，后面一定会忘。

## 快速路径（只读 6 篇也能开工）
- 想把做什么变成可裁决：先读 [4](ref-004-lean-startup.md)，再读 [73](ref-073-continuous-discovery-habits.md)
- 想把怎么交付变成可回滚：先读 [6](ref-006-accelerate.md)，再读 [5](ref-005-continuous-delivery.md)
- 想把AI 体验写成可验收：先读 [71](ref-071-human-ai-interaction.md)，再读 [72](ref-072-pair-guidebook.md)
- 想把智能层做得可解释可治理：先读 [24](ref-024-rag-paper.md)，再读 [29](ref-029-react.md)

## 第 1 章：全流程方法论
这一组更像全书的骨架。建议先把能做事的接口与工作流（Tool Use / ReAct / LangGraph）读顺，再把证据门槛读透（Lean Startup / Continuous Discovery），你会更容易写出能裁决、能回滚的推进节奏。

- [[30] AutoGen：多智能体协作不是为了热闹](ref-030-autogen.md)（9.55） · Agents & Tool Use
- [[31] Tool Use / Function Calling：让模型能做事的标准接口](ref-031-openai-tool-use.md)（9.55） · General References
- [[73] Continuous Discovery Habits（Teresa Torres）：把需求挖掘变成可持续的习惯](ref-073-continuous-discovery-habits.md)（9.55） · Discovery & Product Strategy
- [[60] LangGraph：把 Agent 变成可控的工作流](ref-060-langgraph.md)（9.40） · Agents & Tool Use
- [[29] ReAct：Agent 的推理—行动循环](ref-029-react.md)（9.25） · Agents & Tool Use
- [[4] 精益创业（The Lean Startup）：最小实验与证据门槛](ref-004-lean-startup.md)（8.60） · Discovery & Product Strategy

## 第 2 章：需求挖掘与机会判断
这一章的关键不是想法多，而是能用证据淘汰想法。建议把持续发现当作节拍器：每一轮都要能写下反例、门槛与止损线，别让调研停留在大家都说需要。

- [[73] Continuous Discovery Habits（Teresa Torres）：把需求挖掘变成可持续的习惯](ref-073-continuous-discovery-habits.md)（9.55） · Discovery & Product Strategy
- [[4] 精益创业（The Lean Startup）：最小实验与证据门槛](ref-004-lean-startup.md)（8.60） · Discovery & Product Strategy

## 第 3 章：PRD 与工程合同
如果你只想从这一章带走一件事：把口头约定变成可执行契约。OpenAPI 负责把接口说清楚，Spectral 负责把它变成门禁，RFC 2119 负责让需求语言在团队里没有歧义。

- [[67] OpenAPI Specification：把接口变成可执行契约](ref-067-openapi-spec.md)（9.70） · PRD & Specs
- [[65] Spectral（OpenAPI linter）：把接口契约变成可自动验收的门禁](ref-065-spectral.md)（9.55） · PRD & Specs
- [[74] RFC 2119：把必须/应该/可以写成团队一致的合同语言](ref-074-rfc2119.md)（8.80） · PRD & Specs

## 第 4 章：原型与信息架构
AI 产品的原型往往死在用户不知道发生了什么。这组资料的共同点是：把可理解、可恢复、可预期写成检查项——先守住可访问性底线，再谈高级交互。

- [[17] WCAG 2.2：可访问性底线与可验收检查项](ref-017-wcag-2-2.md)（9.85） · UX / UI & Design Systems
- [[72] People + AI Guidebook（Google PAIR）：把以人为本写成可执行的工作流](ref-072-pair-guidebook.md)（9.40） · UX / UI & Design Systems
- [[71] Guidelines for Human-AI Interaction（Microsoft）：把AI 体验写成可验收的交互合同](ref-071-human-ai-interaction.md)（9.25） · UX / UI & Design Systems
- [[53] Design Tokens：让设计和代码说同一种话](ref-053-design-tokens.md)（9.20） · UX / UI & Design Systems
- [[54] axe-core：可访问性自动化检查的最低成本方案](ref-054-axe-core.md)（9.20） · UX / UI & Design Systems

## 第 5 章：产品验证与打磨
验证阶段最常见的陷阱是做完才想起来怎么验收。建议把 a11y、交互合同与证据门槛当作默认门禁：你不是在打磨 UI，你是在打磨用户能否闭环的确定性。

- [[17] WCAG 2.2：可访问性底线与可验收检查项](ref-017-wcag-2-2.md)（9.85） · UX / UI & Design Systems
- [[73] Continuous Discovery Habits（Teresa Torres）：把需求挖掘变成可持续的习惯](ref-073-continuous-discovery-habits.md)（9.55） · Discovery & Product Strategy
- [[72] People + AI Guidebook（Google PAIR）：把以人为本写成可执行的工作流](ref-072-pair-guidebook.md)（9.40） · UX / UI & Design Systems
- [[71] Guidelines for Human-AI Interaction（Microsoft）：把AI 体验写成可验收的交互合同](ref-071-human-ai-interaction.md)（9.25） · UX / UI & Design Systems
- [[53] Design Tokens：让设计和代码说同一种话](ref-053-design-tokens.md)（9.20） · UX / UI & Design Systems
- [[54] axe-core：可访问性自动化检查的最低成本方案](ref-054-axe-core.md)（9.20） · UX / UI & Design Systems
- [[4] 精益创业（The Lean Startup）：最小实验与证据门槛](ref-004-lean-startup.md)（8.60） · Discovery & Product Strategy

## 第 6 章：UI 设计与资产化
这章更偏把体验做成资产。如果你经常遇到每次改 UI 都像重写，那就优先读 Design Tokens；如果你更常遇到看起来没问题但有人用不了，先把 WCAG + axe-core 变成流水线门禁。

- [[17] WCAG 2.2：可访问性底线与可验收检查项](ref-017-wcag-2-2.md)（9.85） · UX / UI & Design Systems
- [[72] People + AI Guidebook（Google PAIR）：把以人为本写成可执行的工作流](ref-072-pair-guidebook.md)（9.40） · UX / UI & Design Systems
- [[71] Guidelines for Human-AI Interaction（Microsoft）：把AI 体验写成可验收的交互合同](ref-071-human-ai-interaction.md)（9.25） · UX / UI & Design Systems
- [[53] Design Tokens：让设计和代码说同一种话](ref-053-design-tokens.md)（9.20） · UX / UI & Design Systems
- [[54] axe-core：可访问性自动化检查的最低成本方案](ref-054-axe-core.md)（9.20） · UX / UI & Design Systems

## 第 7 章：工程化与编码
这一章的底色是：别让 AI 的快变成债务的快。建议把契约（OpenAPI/RFC）和门禁（Spectral/Accelerate）当作底座，再用可观测性把每次变更的证据留下来——否则你会很快失去敢改的能力。

- [[67] OpenAPI Specification：把接口变成可执行契约](ref-067-openapi-spec.md)（9.70） · PRD & Specs
- [[30] AutoGen：多智能体协作不是为了热闹](ref-030-autogen.md)（9.55） · Agents & Tool Use
- [[45] vLLM：推理吞吐为什么能上去](ref-045-vllm.md)（9.55） · Inference & Optimization
- [[65] Spectral（OpenAPI linter）：把接口契约变成可自动验收的门禁](ref-065-spectral.md)（9.55） · PRD & Specs
- [[69] OpenID Connect Core 1.0：把登录做成可互操作的协议](ref-069-oidc-core.md)（9.55） · User / Auth / Audit
- [[76] SRE：Service Level Objectives（SLO）：把可靠性写成可交易的预算](ref-076-sre-slo.md)（9.55） · Deployment & Operations
- [[64] Grafana：让指标能被人看懂的最后一公里](ref-064-grafana.md)（9.50） · Deployment & Operations
- [[46] TensorRT-LLM：把推理性能当作工程问题来解](ref-046-tensorrt-llm.md)（9.40） · Inference & Optimization
- [[48] GPTQ：后训练量化（PTQ）不是白嫖](ref-048-gptq.md)（9.40） · Inference & Optimization
- [[50] MT-Bench/Chatbot Arena：LLM-as-a-Judge 的边界](ref-050-llm-as-a-judge.md)（9.40） · Evaluation
- [[60] LangGraph：把 Agent 变成可控的工作流](ref-060-langgraph.md)（9.40） · Agents & Tool Use
- [[63] KServe：把推理服务当成可运维的工作负载](ref-063-kserve.md)（9.40） · Inference & Optimization
- [[61] OpenTelemetry：观测性三件套（logs/metrics/traces）](ref-061-opentelemetry.md)（9.35） · Deployment & Operations
- [[68] OWASP ASVS：把安全从口号变成验收项](ref-068-owasp-asvs.md)（9.35） · Engineering Workflow
- [[29] ReAct：Agent 的推理—行动循环](ref-029-react.md)（9.25） · Agents & Tool Use
- [[49] TGI（Text Generation Inference）：把推理服务当成产品在运营](ref-049-tgi.md)（9.25） · Inference & Optimization
- [[70] JWT（RFC 7519）：令牌不是字符串，是可审计的契约](ref-070-jwt.md)（9.25） · User / Auth / Audit
- [[28] RAGAS：RAG 自动评估指标与落地方式](ref-028-ragas.md)（9.20） · Evaluation
- [[55] Lighthouse：把网页质量变成客观分数](ref-055-lighthouse.md)（9.20） · Evaluation
- [[56] Storybook Test Runner：组件级回归比页面级更省钱](ref-056-storybook-test-runner.md)（9.20） · Engineering Workflow
- [[57] Playwright：端到端测试的最后一道门禁](ref-057-playwright.md)（9.20） · Engineering Workflow
- [[79] Problem Details for HTTP APIs（RFC 9457）：把错误变成可解释、可对账、可回归的合同](ref-079-problem-details.md)（9.20） · Backend & Reliability
- [[22] OAuth 2.0（RFC 6749）：认证授权的最小事实源](ref-022-oauth2.md)（9.10） · User / Auth / Audit
- [[24] RAG 原始论文（Lewis et al., 2020）：为什么检索 + 生成能提高可靠性](ref-024-rag-paper.md)（9.10） · RAG
- [[25] FAISS：向量相似检索的工业级底座](ref-025-faiss.md)（8.95） · RAG
- [[59] AWQ：量化的目标是够用且更便宜](ref-059-awq.md)（8.90） · Inference & Optimization
- [[78] HTTP Semantics（RFC 9110）：把请求/重试/状态码写成可推理的契约](ref-078-http-semantics.md)（8.90） · Backend & Reliability
- [[74] RFC 2119：把必须/应该/可以写成团队一致的合同语言](ref-074-rfc2119.md)（8.80） · PRD & Specs
- [[6] Accelerate：交付表现与门禁怎么量化](ref-006-accelerate.md)（8.75） · Engineering Workflow
- [[27] BM25：关键词检索的底盘（以及它为什么仍然重要）](ref-027-bm25.md)（8.45） · RAG
- [[5] 持续交付（Continuous Delivery）：把发布做成可回滚的流水线](ref-005-continuous-delivery.md)（8.45） · Deployment & Operations
- [[62] Prometheus：指标监控的事实标准（但别滥用标签）](ref-062-prometheus.md)（8.40） · Deployment & Operations

## 第 8 章：前端实现
前端在 AI 产品里是驾驶舱。建议先读 a11y 与交互合同，确保状态/错误恢复/反馈入口不漏；再读 Storybook/Playwright，把体验变成能回归的系统，而不是靠人肉点。

- [[17] WCAG 2.2：可访问性底线与可验收检查项](ref-017-wcag-2-2.md)（9.85） · UX / UI & Design Systems
- [[72] People + AI Guidebook（Google PAIR）：把以人为本写成可执行的工作流](ref-072-pair-guidebook.md)（9.40） · UX / UI & Design Systems
- [[68] OWASP ASVS：把安全从口号变成验收项](ref-068-owasp-asvs.md)（9.35） · Engineering Workflow
- [[71] Guidelines for Human-AI Interaction（Microsoft）：把AI 体验写成可验收的交互合同](ref-071-human-ai-interaction.md)（9.25） · UX / UI & Design Systems
- [[53] Design Tokens：让设计和代码说同一种话](ref-053-design-tokens.md)（9.20） · UX / UI & Design Systems
- [[54] axe-core：可访问性自动化检查的最低成本方案](ref-054-axe-core.md)（9.20） · UX / UI & Design Systems
- [[56] Storybook Test Runner：组件级回归比页面级更省钱](ref-056-storybook-test-runner.md)（9.20） · Engineering Workflow
- [[57] Playwright：端到端测试的最后一道门禁](ref-057-playwright.md)（9.20） · Engineering Workflow
- [[6] Accelerate：交付表现与门禁怎么量化](ref-006-accelerate.md)（8.75） · Engineering Workflow

## 第 9 章：后端架构
后端的核心是把风险关在笼子里。建议把错误语义与协议契约（RFC 9110/9457）先统一，再把身份与安全底线（OIDC/JWT/ASVS）补齐；这些会直接决定你的系统能不能做幂等、能不能审计、能不能复盘。

- [[67] OpenAPI Specification：把接口变成可执行契约](ref-067-openapi-spec.md)（9.70） · PRD & Specs
- [[65] Spectral（OpenAPI linter）：把接口契约变成可自动验收的门禁](ref-065-spectral.md)（9.55） · PRD & Specs
- [[69] OpenID Connect Core 1.0：把登录做成可互操作的协议](ref-069-oidc-core.md)（9.55） · User / Auth / Audit
- [[68] OWASP ASVS：把安全从口号变成验收项](ref-068-owasp-asvs.md)（9.35） · Engineering Workflow
- [[70] JWT（RFC 7519）：令牌不是字符串，是可审计的契约](ref-070-jwt.md)（9.25） · User / Auth / Audit
- [[75] Usage-based Billing（Stripe）：把计量口径写成能对账的产品合同](ref-075-stripe-usage-based-billing.md)（9.25） · Billing & Pricing
- [[23] PCI DSS v4.0：把支付合规当作产品边界](ref-023-pci-dss.md)（9.20） · Billing & Pricing
- [[56] Storybook Test Runner：组件级回归比页面级更省钱](ref-056-storybook-test-runner.md)（9.20） · Engineering Workflow
- [[57] Playwright：端到端测试的最后一道门禁](ref-057-playwright.md)（9.20） · Engineering Workflow
- [[79] Problem Details for HTTP APIs（RFC 9457）：把错误变成可解释、可对账、可回归的合同](ref-079-problem-details.md)（9.20） · Backend & Reliability
- [[22] OAuth 2.0（RFC 6749）：认证授权的最小事实源](ref-022-oauth2.md)（9.10） · User / Auth / Audit
- [[78] HTTP Semantics（RFC 9110）：把请求/重试/状态码写成可推理的契约](ref-078-http-semantics.md)（8.90） · Backend & Reliability
- [[74] RFC 2119：把必须/应该/可以写成团队一致的合同语言](ref-074-rfc2119.md)（8.80） · PRD & Specs
- [[6] Accelerate：交付表现与门禁怎么量化](ref-006-accelerate.md)（8.75） · Engineering Workflow

## 第 10 章：RAG & Agent
当你开始做智能层，最常见的翻车点就三个：无证据、越边界、不可回归。这组资料分别解决证据链（RAG/BM25/FAISS），行动边界（ReAct/LangGraph/Tool Use），以及怎么裁决（RAGAS/Judge）。

- [[67] OpenAPI Specification：把接口变成可执行契约](ref-067-openapi-spec.md)（9.70） · PRD & Specs
- [[30] AutoGen：多智能体协作不是为了热闹](ref-030-autogen.md)（9.55） · Agents & Tool Use
- [[65] Spectral（OpenAPI linter）：把接口契约变成可自动验收的门禁](ref-065-spectral.md)（9.55） · PRD & Specs
- [[50] MT-Bench/Chatbot Arena：LLM-as-a-Judge 的边界](ref-050-llm-as-a-judge.md)（9.40） · Evaluation
- [[60] LangGraph：把 Agent 变成可控的工作流](ref-060-langgraph.md)（9.40） · Agents & Tool Use
- [[29] ReAct：Agent 的推理—行动循环](ref-029-react.md)（9.25） · Agents & Tool Use
- [[34] Datasheets for Datasets：数据集要像产品说明书一样可追溯](ref-034-datasheets.md)（9.25） · Data
- [[28] RAGAS：RAG 自动评估指标与落地方式](ref-028-ragas.md)（9.20） · Evaluation
- [[55] Lighthouse：把网页质量变成客观分数](ref-055-lighthouse.md)（9.20） · Evaluation
- [[24] RAG 原始论文（Lewis et al., 2020）：为什么检索 + 生成能提高可靠性](ref-024-rag-paper.md)（9.10） · RAG
- [[25] FAISS：向量相似检索的工业级底座](ref-025-faiss.md)（8.95） · RAG
- [[74] RFC 2119：把必须/应该/可以写成团队一致的合同语言](ref-074-rfc2119.md)（8.80） · PRD & Specs
- [[35] LLM 数据去重：为什么重复会伤模型（以及怎么测）](ref-035-llm-dedup.md)（8.75） · Data
- [[27] BM25：关键词检索的底盘（以及它为什么仍然重要）](ref-027-bm25.md)（8.45） · RAG

## 第 11 章：用户与权限
这一章更像边界工程。先把登录/令牌/授权写成可互操作协议（OAuth/OIDC/JWT），再谈治理框架与护栏：你要守住的是谁能代表谁做事，以及系统在越界时能否留下证据、能否阻断。

- [[69] OpenID Connect Core 1.0：把登录做成可互操作的协议](ref-069-oidc-core.md)（9.55） · User / Auth / Audit
- [[77] NIST AI RMF：把AI 风险从口号变成可审计的治理框架](ref-077-nist-ai-rmf.md)（9.55） · Governance & Security
- [[70] JWT（RFC 7519）：令牌不是字符串，是可审计的契约](ref-070-jwt.md)（9.25） · User / Auth / Audit
- [[22] OAuth 2.0（RFC 6749）：认证授权的最小事实源](ref-022-oauth2.md)（9.10） · User / Auth / Audit
- [[51] Guardrails：给生成式系统加护栏，不是加枷锁](ref-051-guardrails.md)（8.90） · Governance & Security

## 第 12 章：付费与风控
计费最难的从来不是收多少钱，而是口径一致、可对账、可止损。建议先把用量口径与幂等写清楚（Stripe），再把合规当作边界条件（PCI DSS），最后把风控策略写成能进门禁的规则（别只靠运营兜底）。

- [[77] NIST AI RMF：把AI 风险从口号变成可审计的治理框架](ref-077-nist-ai-rmf.md)（9.55） · Governance & Security
- [[75] Usage-based Billing（Stripe）：把计量口径写成能对账的产品合同](ref-075-stripe-usage-based-billing.md)（9.25） · Billing & Pricing
- [[23] PCI DSS v4.0：把支付合规当作产品边界](ref-023-pci-dss.md)（9.20） · Billing & Pricing
- [[51] Guardrails：给生成式系统加护栏，不是加枷锁](ref-051-guardrails.md)（8.90） · Governance & Security

## 第 13 章：数据收集与清洗
数据阶段最容易忙到最后只剩一堆垃圾。建议把 Datasheets 当作数据的合同，把去重当作质量底线，把合成数据当作补洞工具——所有数据策略都要能回到评测与回归里裁决，而不是靠感觉更好。

- [[42] DPO：无需显式奖励模型的偏好优化](ref-042-dpo.md)（9.70） · Training & Alignment
- [[40] LoRA：低成本微调的核心思路](ref-040-lora.md)（9.55） · Training & Alignment
- [[47] QLoRA：把微调从奢侈品变成日用品](ref-047-qlora.md)（9.55） · Training & Alignment
- [[77] NIST AI RMF：把AI 风险从口号变成可审计的治理框架](ref-077-nist-ai-rmf.md)（9.55） · Governance & Security
- [[36] Self-Instruct：低成本生成指令数据的起手式](ref-036-self-instruct.md)（9.40） · Training & Alignment
- [[34] Datasheets for Datasets：数据集要像产品说明书一样可追溯](ref-034-datasheets.md)（9.25） · Data
- [[24] RAG 原始论文（Lewis et al., 2020）：为什么检索 + 生成能提高可靠性](ref-024-rag-paper.md)（9.10） · RAG
- [[41] RLHF：对齐不是更听话，而是可控且可回归](ref-041-rlhf.md)（9.10） · Training & Alignment
- [[25] FAISS：向量相似检索的工业级底座](ref-025-faiss.md)（8.95） · RAG
- [[51] Guardrails：给生成式系统加护栏，不是加枷锁](ref-051-guardrails.md)（8.90） · Governance & Security
- [[35] LLM 数据去重：为什么重复会伤模型（以及怎么测）](ref-035-llm-dedup.md)（8.75） · Data
- [[27] BM25：关键词检索的底盘（以及它为什么仍然重要）](ref-027-bm25.md)（8.45） · RAG
- [[66] WizardLM / Evol-Instruct：让合成指令更难一点](ref-066-wizardlm.md)（8.40） · Training & Alignment

## 第 14 章：预训练
这一章建议带着先不训练也能解决吗的心态来读：大多数 0→1 的最短路径仍然是数据边界 + RAG + 评测回归。预训练的价值在于长期复利，但前提是你能写清楚成本、门槛与止损线。

- [[42] DPO：无需显式奖励模型的偏好优化](ref-042-dpo.md)（9.70） · Training & Alignment
- [[40] LoRA：低成本微调的核心思路](ref-040-lora.md)（9.55） · Training & Alignment
- [[47] QLoRA：把微调从奢侈品变成日用品](ref-047-qlora.md)（9.55） · Training & Alignment
- [[36] Self-Instruct：低成本生成指令数据的起手式](ref-036-self-instruct.md)（9.40） · Training & Alignment
- [[41] RLHF：对齐不是更听话，而是可控且可回归](ref-041-rlhf.md)（9.10） · Training & Alignment
- [[66] WizardLM / Evol-Instruct：让合成指令更难一点](ref-066-wizardlm.md)（8.40） · Training & Alignment

## 第 15 章：后训练与对齐
后训练的关键词是可控且可回归。别急着堆花活，先把行为目标写成可评测的口径，再选 SFT/DPO/RLHF 等路径；否则你会得到一个更像它自己、而不像你产品的模型。

- [[42] DPO：无需显式奖励模型的偏好优化](ref-042-dpo.md)（9.70） · Training & Alignment
- [[40] LoRA：低成本微调的核心思路](ref-040-lora.md)（9.55） · Training & Alignment
- [[47] QLoRA：把微调从奢侈品变成日用品](ref-047-qlora.md)（9.55） · Training & Alignment
- [[36] Self-Instruct：低成本生成指令数据的起手式](ref-036-self-instruct.md)（9.40） · Training & Alignment
- [[41] RLHF：对齐不是更听话，而是可控且可回归](ref-041-rlhf.md)（9.10） · Training & Alignment
- [[66] WizardLM / Evol-Instruct：让合成指令更难一点](ref-066-wizardlm.md)（8.40） · Training & Alignment

## 第 16 章：推理优化
推理优化的主线是质量—延迟—成本三角：你不可能只涨质量不付账，也不可能只降成本不伤体验。建议先读 vLLM/量化建立直觉，再看 TensorRT-LLM 这类极致工程派，最后把它们接回部署与门禁（否则只是跑得快而已）。

- [[45] vLLM：推理吞吐为什么能上去](ref-045-vllm.md)（9.55） · Inference & Optimization
- [[46] TensorRT-LLM：把推理性能当作工程问题来解](ref-046-tensorrt-llm.md)（9.40） · Inference & Optimization
- [[48] GPTQ：后训练量化（PTQ）不是白嫖](ref-048-gptq.md)（9.40） · Inference & Optimization
- [[63] KServe：把推理服务当成可运维的工作负载](ref-063-kserve.md)（9.40） · Inference & Optimization
- [[49] TGI（Text Generation Inference）：把推理服务当成产品在运营](ref-049-tgi.md)（9.25） · Inference & Optimization
- [[59] AWQ：量化的目标是够用且更便宜](ref-059-awq.md)（8.90） · Inference & Optimization

## 第 17 章：部署与运维
部署与运维关注的是出了事能不能解释、能不能止损、能不能恢复。建议先把 SLO 写成预算，再用 Grafana/OTel/Prometheus 把证据链串起来；同时把安全验收项（ASVS）当作发布门禁的一部分，而不是上线后的排雷。

- [[45] vLLM：推理吞吐为什么能上去](ref-045-vllm.md)（9.55） · Inference & Optimization
- [[76] SRE：Service Level Objectives（SLO）：把可靠性写成可交易的预算](ref-076-sre-slo.md)（9.55） · Deployment & Operations
- [[64] Grafana：让指标能被人看懂的最后一公里](ref-064-grafana.md)（9.50） · Deployment & Operations
- [[46] TensorRT-LLM：把推理性能当作工程问题来解](ref-046-tensorrt-llm.md)（9.40） · Inference & Optimization
- [[48] GPTQ：后训练量化（PTQ）不是白嫖](ref-048-gptq.md)（9.40） · Inference & Optimization
- [[50] MT-Bench/Chatbot Arena：LLM-as-a-Judge 的边界](ref-050-llm-as-a-judge.md)（9.40） · Evaluation
- [[63] KServe：把推理服务当成可运维的工作负载](ref-063-kserve.md)（9.40） · Inference & Optimization
- [[61] OpenTelemetry：观测性三件套（logs/metrics/traces）](ref-061-opentelemetry.md)（9.35） · Deployment & Operations
- [[68] OWASP ASVS：把安全从口号变成验收项](ref-068-owasp-asvs.md)（9.35） · Engineering Workflow
- [[49] TGI（Text Generation Inference）：把推理服务当成产品在运营](ref-049-tgi.md)（9.25） · Inference & Optimization
- [[28] RAGAS：RAG 自动评估指标与落地方式](ref-028-ragas.md)（9.20） · Evaluation
- [[55] Lighthouse：把网页质量变成客观分数](ref-055-lighthouse.md)（9.20） · Evaluation
- [[56] Storybook Test Runner：组件级回归比页面级更省钱](ref-056-storybook-test-runner.md)（9.20） · Engineering Workflow
- [[57] Playwright：端到端测试的最后一道门禁](ref-057-playwright.md)（9.20） · Engineering Workflow
- [[79] Problem Details for HTTP APIs（RFC 9457）：把错误变成可解释、可对账、可回归的合同](ref-079-problem-details.md)（9.20） · Backend & Reliability
- [[59] AWQ：量化的目标是够用且更便宜](ref-059-awq.md)（8.90） · Inference & Optimization
- [[78] HTTP Semantics（RFC 9110）：把请求/重试/状态码写成可推理的契约](ref-078-http-semantics.md)（8.90） · Backend & Reliability
- [[6] Accelerate：交付表现与门禁怎么量化](ref-006-accelerate.md)（8.75） · Engineering Workflow
- [[5] 持续交付（Continuous Delivery）：把发布做成可回滚的流水线](ref-005-continuous-delivery.md)（8.45） · Deployment & Operations
- [[62] Prometheus：指标监控的事实标准（但别滥用标签）](ref-062-prometheus.md)（8.40） · Deployment & Operations

## 第 18 章：评测体系
评测不是上线前做一次，而是你持续迭代时的裁判系统。建议先把 LLM-as-a-Judge 的偏差与去偏策略读明白，再用 RAGAS 把 RAG 链路拆开评分；最后把这些指标接到发布门禁与回滚策略里，别让评测停留在报告。

- [[42] DPO：无需显式奖励模型的偏好优化](ref-042-dpo.md)（9.70） · Training & Alignment
- [[30] AutoGen：多智能体协作不是为了热闹](ref-030-autogen.md)（9.55） · Agents & Tool Use
- [[40] LoRA：低成本微调的核心思路](ref-040-lora.md)（9.55） · Training & Alignment
- [[45] vLLM：推理吞吐为什么能上去](ref-045-vllm.md)（9.55） · Inference & Optimization
- [[47] QLoRA：把微调从奢侈品变成日用品](ref-047-qlora.md)（9.55） · Training & Alignment
- [[76] SRE：Service Level Objectives（SLO）：把可靠性写成可交易的预算](ref-076-sre-slo.md)（9.55） · Deployment & Operations
- [[64] Grafana：让指标能被人看懂的最后一公里](ref-064-grafana.md)（9.50） · Deployment & Operations
- [[36] Self-Instruct：低成本生成指令数据的起手式](ref-036-self-instruct.md)（9.40） · Training & Alignment
- [[46] TensorRT-LLM：把推理性能当作工程问题来解](ref-046-tensorrt-llm.md)（9.40） · Inference & Optimization
- [[48] GPTQ：后训练量化（PTQ）不是白嫖](ref-048-gptq.md)（9.40） · Inference & Optimization
- [[50] MT-Bench/Chatbot Arena：LLM-as-a-Judge 的边界](ref-050-llm-as-a-judge.md)（9.40） · Evaluation
- [[60] LangGraph：把 Agent 变成可控的工作流](ref-060-langgraph.md)（9.40） · Agents & Tool Use
- [[63] KServe：把推理服务当成可运维的工作负载](ref-063-kserve.md)（9.40） · Inference & Optimization
- [[61] OpenTelemetry：观测性三件套（logs/metrics/traces）](ref-061-opentelemetry.md)（9.35） · Deployment & Operations
- [[29] ReAct：Agent 的推理—行动循环](ref-029-react.md)（9.25） · Agents & Tool Use
- [[34] Datasheets for Datasets：数据集要像产品说明书一样可追溯](ref-034-datasheets.md)（9.25） · Data
- [[49] TGI（Text Generation Inference）：把推理服务当成产品在运营](ref-049-tgi.md)（9.25） · Inference & Optimization
- [[28] RAGAS：RAG 自动评估指标与落地方式](ref-028-ragas.md)（9.20） · Evaluation
- [[55] Lighthouse：把网页质量变成客观分数](ref-055-lighthouse.md)（9.20） · Evaluation
- [[79] Problem Details for HTTP APIs（RFC 9457）：把错误变成可解释、可对账、可回归的合同](ref-079-problem-details.md)（9.20） · Backend & Reliability
- [[24] RAG 原始论文（Lewis et al., 2020）：为什么检索 + 生成能提高可靠性](ref-024-rag-paper.md)（9.10） · RAG
- [[41] RLHF：对齐不是更听话，而是可控且可回归](ref-041-rlhf.md)（9.10） · Training & Alignment
- [[25] FAISS：向量相似检索的工业级底座](ref-025-faiss.md)（8.95） · RAG
- [[59] AWQ：量化的目标是够用且更便宜](ref-059-awq.md)（8.90） · Inference & Optimization
- [[78] HTTP Semantics（RFC 9110）：把请求/重试/状态码写成可推理的契约](ref-078-http-semantics.md)（8.90） · Backend & Reliability
- [[35] LLM 数据去重：为什么重复会伤模型（以及怎么测）](ref-035-llm-dedup.md)（8.75） · Data
- [[27] BM25：关键词检索的底盘（以及它为什么仍然重要）](ref-027-bm25.md)（8.45） · RAG
- [[5] 持续交付（Continuous Delivery）：把发布做成可回滚的流水线](ref-005-continuous-delivery.md)（8.45） · Deployment & Operations
- [[62] Prometheus：指标监控的事实标准（但别滥用标签）](ref-062-prometheus.md)（8.40） · Deployment & Operations
- [[66] WizardLM / Evol-Instruct：让合成指令更难一点](ref-066-wizardlm.md)（8.40） · Training & Alignment

## 第 19 章：迭代与增长
增长并不神秘，难的是建立一个能反复跑的节拍：发现 → 实验 → 裁决 → 归档 → 回归更新。建议把持续发现当作输入端，把计费口径当作约束端，你会更容易做出既敢试错又不失控的迭代。

- [[73] Continuous Discovery Habits（Teresa Torres）：把需求挖掘变成可持续的习惯](ref-073-continuous-discovery-habits.md)（9.55） · Discovery & Product Strategy
- [[75] Usage-based Billing（Stripe）：把计量口径写成能对账的产品合同](ref-075-stripe-usage-based-billing.md)（9.25） · Billing & Pricing
- [[23] PCI DSS v4.0：把支付合规当作产品边界](ref-023-pci-dss.md)（9.20） · Billing & Pricing
- [[4] 精益创业（The Lean Startup）：最小实验与证据门槛](ref-004-lean-startup.md)（8.60） · Discovery & Product Strategy

## 第 20 章：合规与伦理
这章的底层逻辑是：合规不是上线前的检查表，而是系统的默认属性。建议把治理框架（NIST）当作总账，把数据与观测当作凭证，把护栏与发布门禁当作执行层——这样你才不需要靠祈祷来运营 AI。

- [[69] OpenID Connect Core 1.0：把登录做成可互操作的协议](ref-069-oidc-core.md)（9.55） · User / Auth / Audit
- [[76] SRE：Service Level Objectives（SLO）：把可靠性写成可交易的预算](ref-076-sre-slo.md)（9.55） · Deployment & Operations
- [[77] NIST AI RMF：把AI 风险从口号变成可审计的治理框架](ref-077-nist-ai-rmf.md)（9.55） · Governance & Security
- [[64] Grafana：让指标能被人看懂的最后一公里](ref-064-grafana.md)（9.50） · Deployment & Operations
- [[61] OpenTelemetry：观测性三件套（logs/metrics/traces）](ref-061-opentelemetry.md)（9.35） · Deployment & Operations
- [[34] Datasheets for Datasets：数据集要像产品说明书一样可追溯](ref-034-datasheets.md)（9.25） · Data
- [[70] JWT（RFC 7519）：令牌不是字符串，是可审计的契约](ref-070-jwt.md)（9.25） · User / Auth / Audit
- [[75] Usage-based Billing（Stripe）：把计量口径写成能对账的产品合同](ref-075-stripe-usage-based-billing.md)（9.25） · Billing & Pricing
- [[23] PCI DSS v4.0：把支付合规当作产品边界](ref-023-pci-dss.md)（9.20） · Billing & Pricing
- [[22] OAuth 2.0（RFC 6749）：认证授权的最小事实源](ref-022-oauth2.md)（9.10） · User / Auth / Audit
- [[51] Guardrails：给生成式系统加护栏，不是加枷锁](ref-051-guardrails.md)（8.90） · Governance & Security
- [[35] LLM 数据去重：为什么重复会伤模型（以及怎么测）](ref-035-llm-dedup.md)（8.75） · Data
- [[5] 持续交付（Continuous Delivery）：把发布做成可回滚的流水线](ref-005-continuous-delivery.md)（8.45） · Deployment & Operations
- [[62] Prometheus：指标监控的事实标准（但别滥用标签）](ref-062-prometheus.md)（8.40） · Deployment & Operations
