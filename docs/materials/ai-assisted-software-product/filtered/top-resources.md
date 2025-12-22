# AI 辅助软件产品：精选资料（可直接用）

> 本页从全书参考文献与工程常用标准中，提取“最值得优先读/最能直接落地”的资料，并按章节主题归类。目标是让你在需要补背景、补方法或补门禁时，能快速找到权威出处与可执行做法。

## P0：先读这些（覆盖全书，优先级最高）

- **产品与交付（决策与节奏）**
  - *The Lean Startup*（Eric Ries）https://theleanstartup.com/ （对应第 1–2 章：证据与实验门槛；笔记：[笔记](../notes/ref-004-lean-startup.md)）
  - Continuous Discovery Habits（Teresa Torres）https://www.producttalk.org/continuous-discovery-habits/ （对应第 2/5/19 章：持续发现与实验节奏；笔记：[笔记](../notes/ref-073-continuous-discovery-habits.md)）
  - *Accelerate*（Forsgren/Humble/Kim）https://itrevolution.com/product/accelerate/ （对应第 7/17/18 章：门禁、回归与交付表现；笔记：[笔记](../notes/ref-006-accelerate.md)）
  - *Continuous Delivery*（Humble/Farley）https://martinfowler.com/books/continuousDelivery.html （对应第 7/17 章：发布门禁与回滚；笔记：[笔记](../notes/ref-005-continuous-delivery.md)）
- **AI 体验与信任（把不确定性写成可验收）**
  - Guidelines for Human-AI Interaction（Microsoft）https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ （对应第 4–6/11 章：提示、纠错、回退与解释；笔记：[笔记](../notes/ref-071-human-ai-interaction.md)）
  - People + AI Guidebook（Google PAIR）https://pair.withgoogle.com/guidebook/ （对应第 2/4–6/18/20 章：人机协作、反馈回路与评测闭环；笔记：[笔记](../notes/ref-072-pair-guidebook.md)）
- **安全底线（上线必备）**
  - OWASP ASVS https://owasp.org/www-project-application-security-verification-standard/ （对应第 11/20 章：可验收的安全检查项；笔记：[笔记](../notes/ref-068-owasp-asvs.md)）
- **可靠性门槛（别用‘努力’当承诺）**
  - SRE：Service Level Objectives（SLO）https://sre.google/sre-book/service-level-objectives/ （对应第 9/17/18 章：SLO 与错误预算；笔记：[笔记](../notes/ref-076-sre-slo.md)）
- **API 标准（契约与协作）**
  - OpenAPI Specification https://spec.openapis.org/oas/latest.html （对应第 9/10 章：契约、工具调用与协作；笔记：[笔记](../notes/ref-067-openapi-spec.md)）
  - Spectral（OpenAPI linter）https://github.com/stoplightio/spectral （对应第 3/7/9/10 章：把契约变成 CI 门禁；笔记：[笔记](../notes/ref-065-spectral.md)）
- **身份与令牌（产品边界的底座）**
  - OAuth 2.0（RFC 6749）https://www.rfc-editor.org/rfc/rfc6749 （对应第 11 章：认证/授权边界；笔记：[笔记](../notes/ref-022-oauth2.md)）
  - OpenID Connect Core 1.0 https://openid.net/specs/openid-connect-core-1_0.html （对应第 11 章：登录互操作；笔记：[笔记](../notes/ref-069-oidc-core.md)）
  - JWT（RFC 7519）https://www.rfc-editor.org/rfc/rfc7519 （对应第 11 章：令牌契约与审计；笔记：[笔记](../notes/ref-070-jwt.md)）
- **支付与合规（别等上线才补）**
  - PCI DSS v4.0 https://www.pcisecuritystandards.org/document_library/?category=pcidss&document=pci_dss （对应第 12/20 章：支付边界与合规；笔记：[笔记](../notes/ref-023-pci-dss.md)）
  - Usage-based Billing（Stripe）https://docs.stripe.com/billing/subscriptions/usage-based （对应第 12/19 章：计量口径、幂等与对账；笔记：[笔记](../notes/ref-075-stripe-usage-based-billing.md)）

## 第 2 章：需求挖掘与机会判断（Discovery）

- *The Lean Startup* https://theleanstartup.com/ （笔记：[笔记](../notes/ref-004-lean-startup.md)）
- Continuous Discovery Habits https://www.producttalk.org/continuous-discovery-habits/ （笔记：[笔记](../notes/ref-073-continuous-discovery-habits.md)）
- People + AI Guidebook https://pair.withgoogle.com/guidebook/ （笔记：[笔记](../notes/ref-072-pair-guidebook.md)）

## 第 3 章：PRD 与工程合同（Definition）

- RFC 2119（MUST/SHOULD/MAY 语义）https://www.rfc-editor.org/rfc/rfc2119 （笔记：[笔记](../notes/ref-074-rfc2119.md)）
- OpenAPI Specification https://spec.openapis.org/oas/latest.html （笔记：[笔记](../notes/ref-067-openapi-spec.md)）
- Spectral（OpenAPI linter）https://github.com/stoplightio/spectral （笔记：[笔记](../notes/ref-065-spectral.md)）
- ISO/IEC/IEEE 29148（需求工程标准）与 UML（用例建模）属于“写合同”的底层参考：建议后续补充可公开获取的摘要/导读链接，并写成可复用的 PRD 模板（见本仓库 `A-templates.md`）。

## 第 4 章：原型与信息架构（Prototyping）

- WCAG 2.2 https://www.w3.org/TR/WCAG22/ （笔记：[笔记](../notes/ref-017-wcag-2-2.md)）
- Guidelines for Human-AI Interaction（Microsoft）https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ （笔记：[笔记](../notes/ref-071-human-ai-interaction.md)）
- People + AI Guidebook https://pair.withgoogle.com/guidebook/ （笔记：[笔记](../notes/ref-072-pair-guidebook.md)）

## 第 6 章：UI 设计：把体验做成可维护资产

- Design Tokens 格式 https://www.designtokens.org/TR/drafts/format/ （笔记：[笔记](../notes/ref-053-design-tokens.md)）
- axe-core https://github.com/dequelabs/axe-core （笔记：[笔记](../notes/ref-054-axe-core.md)）
- Lighthouse https://developer.chrome.com/docs/lighthouse/ （笔记：[笔记](../notes/ref-055-lighthouse.md)）
- Playwright https://playwright.dev/ （笔记：[笔记](../notes/ref-057-playwright.md)）
- Storybook Test Runner https://storybook.js.org/docs/writing-tests/integrations/test-runner （笔记：[笔记](../notes/ref-056-storybook-test-runner.md)）

## 第 7 章：工程化与编码（Engineering）

- *Accelerate* https://itrevolution.com/product/accelerate/ （笔记：[笔记](../notes/ref-006-accelerate.md)）
- *Continuous Delivery* https://martinfowler.com/books/continuousDelivery.html （笔记：[笔记](../notes/ref-005-continuous-delivery.md)）
- OpenAPI Specification https://spec.openapis.org/oas/latest.html （笔记：[笔记](../notes/ref-067-openapi-spec.md)）
- Spectral（OpenAPI linter）https://github.com/stoplightio/spectral （笔记：[笔记](../notes/ref-065-spectral.md)）

## 第 9 章：后端架构（契约/错误语义/可靠性）

- HTTP Semantics（RFC 9110）https://www.rfc-editor.org/rfc/rfc9110 （笔记：[笔记](../notes/ref-078-http-semantics.md)）
- Problem Details for HTTP APIs（RFC 9457）https://www.rfc-editor.org/rfc/rfc9457 （笔记：[笔记](../notes/ref-079-problem-details.md)）
- SRE：Service Level Objectives（SLO）https://sre.google/sre-book/service-level-objectives/ （笔记：[笔记](../notes/ref-076-sre-slo.md)）

## 第 10 章：Agent 架构与 RAG（智能层）

- RAG 原始论文（Lewis et al., 2020）https://arxiv.org/abs/2005.11401 （笔记：[笔记](../notes/ref-024-rag-paper.md)）
- BM25 综述（Robertson & Zaragoza, 2009）https://www.nowpublishers.com/article/Details/INR-019 （笔记：[笔记](../notes/ref-027-bm25.md)）
- FAISS（Johnson et al., 2019）https://arxiv.org/abs/1702.08734 （笔记：[笔记](../notes/ref-025-faiss.md)）
- RAGAS（Shahul et al., 2023）https://arxiv.org/abs/2309.15217 （笔记：[笔记](../notes/ref-028-ragas.md)）
- ReAct（Yao et al., 2023）https://arxiv.org/abs/2210.03629 （笔记：[笔记](../notes/ref-029-react.md)）
- LangGraph 文档 https://docs.langchain.com/oss/python/langgraph/overview/ （笔记：[笔记](../notes/ref-060-langgraph.md)）
- AutoGen（Wu et al., 2023）https://arxiv.org/abs/2308.08155 （笔记：[笔记](../notes/ref-030-autogen.md)）
- OpenAI Tool Use / Function Calling（文档入口）https://platform.openai.com/docs/ （笔记：[笔记](../notes/ref-031-openai-tool-use.md)）

## 第 11 章：用户模块（AuthN/AuthZ/审计）

- OAuth 2.0（RFC 6749）https://www.rfc-editor.org/rfc/rfc6749 （笔记：[笔记](../notes/ref-022-oauth2.md)）
- OpenID Connect Core 1.0 https://openid.net/specs/openid-connect-core-1_0.html （笔记：[笔记](../notes/ref-069-oidc-core.md)）
- JWT（RFC 7519）https://www.rfc-editor.org/rfc/rfc7519 （笔记：[笔记](../notes/ref-070-jwt.md)）
- OWASP ASVS https://owasp.org/www-project-application-security-verification-standard/ （笔记：[笔记](../notes/ref-068-owasp-asvs.md)）

## 第 12 章：付费模块（计量/账本/对账/风控）

- PCI DSS v4.0 https://www.pcisecuritystandards.org/document_library/?category=pcidss&document=pci_dss （笔记：[笔记](../notes/ref-023-pci-dss.md)）
- Usage-based Billing（Stripe）https://docs.stripe.com/billing/subscriptions/usage-based （笔记：[笔记](../notes/ref-075-stripe-usage-based-billing.md)）

## 第 13 章：数据收集与清洗（Data）

- Datasheets for Datasets（Gebru et al., 2021）https://arxiv.org/abs/1803.09010 （笔记：[笔记](../notes/ref-034-datasheets.md)）
- LLM 数据去重（Lee et al., 2021）https://arxiv.org/abs/2107.06499 （笔记：[笔记](../notes/ref-035-llm-dedup.md)）

## 第 15 章：后训练与对齐（Post-train / Alignment）

- LoRA（Hu et al., 2021/2022）https://arxiv.org/abs/2106.09685 （笔记：[笔记](../notes/ref-040-lora.md)）
- Self-Instruct（Wang et al., 2023）https://arxiv.org/abs/2212.10560 （笔记：[笔记](../notes/ref-036-self-instruct.md)）
- WizardLM / Evol-Instruct（Xu et al., 2023）https://arxiv.org/abs/2304.12244 （笔记：[笔记](../notes/ref-066-wizardlm.md)）
- QLoRA（Dettmers et al., 2023）https://arxiv.org/abs/2305.14314 （笔记：[笔记](../notes/ref-047-qlora.md)）
- RLHF（Ouyang et al., 2022）https://arxiv.org/abs/2203.02155 （笔记：[笔记](../notes/ref-041-rlhf.md)）
- DPO（Rafailov et al., 2023）https://arxiv.org/abs/2305.18290 （笔记：[笔记](../notes/ref-042-dpo.md)）
- PPO（Schulman et al., 2017）https://arxiv.org/abs/1707.06347 （笔记：[笔记](../notes/ref-085-ppo.md)）
- Deep RL from Human Preferences（Christiano et al., 2017）https://arxiv.org/abs/1706.03741 （笔记：[笔记](../notes/ref-086-rl-from-human-preferences.md)）
- Learning to Summarize from Human Feedback（Stiennon et al., 2020）https://arxiv.org/abs/2009.01325 （笔记：[笔记](../notes/ref-088-learning-to-summarize-from-human-feedback.md)）
- Constitutional AI（Bai et al., 2022）https://arxiv.org/abs/2212.08073 （笔记：[笔记](../notes/ref-089-constitutional-ai.md)）

## 第 16 章：推理优化（Inference）

- vLLM（Kwon et al., 2023）https://arxiv.org/abs/2309.06180 （笔记：[笔记](../notes/ref-045-vllm.md)）
- TensorRT-LLM（官方资料入口）https://github.com/NVIDIA/TensorRT-LLM （笔记：[笔记](../notes/ref-046-tensorrt-llm.md)）
- GPTQ（Frantar et al., 2024）https://arxiv.org/abs/2210.17323 （笔记：[笔记](../notes/ref-048-gptq.md)）
- AWQ（Lin et al., 2023）https://arxiv.org/abs/2306.00978 （笔记：[笔记](../notes/ref-059-awq.md)）
- Text Generation Inference（TGI）https://github.com/huggingface/text-generation-inference （笔记：[笔记](../notes/ref-049-tgi.md)）
- KServe（推理服务编排）https://kserve.github.io/website/ （笔记：[笔记](../notes/ref-063-kserve.md)）

## 第 17–18 章：部署/运维与评测（Ops & Evaluation）

- OpenTelemetry https://opentelemetry.io/docs/ （笔记：[笔记](../notes/ref-061-opentelemetry.md)）
- LLM-as-a-Judge（Zheng et al., 2023）https://arxiv.org/abs/2306.05685 （笔记：[笔记](../notes/ref-050-llm-as-a-judge.md)）
- Prometheus https://prometheus.io/docs/introduction/overview/ （笔记：[笔记](../notes/ref-062-prometheus.md)）
- Grafana https://grafana.com/docs/grafana/latest/ （笔记：[笔记](../notes/ref-064-grafana.md)）
- SRE：Service Level Objectives（SLO）https://sre.google/sre-book/service-level-objectives/ （笔记：[笔记](../notes/ref-076-sre-slo.md)）
- Guardrails（Building Guardrails for LLMs, 2024）https://arxiv.org/abs/2402.01822 （笔记：[笔记](../notes/ref-051-guardrails.md)）

## 第 19 章：迭代与增长（路线图/实验/定价）

- Continuous Discovery Habits https://www.producttalk.org/continuous-discovery-habits/ （笔记：[笔记](../notes/ref-073-continuous-discovery-habits.md)）
- Usage-based Billing（Stripe）https://docs.stripe.com/billing/subscriptions/usage-based （笔记：[笔记](../notes/ref-075-stripe-usage-based-billing.md)）

## 第 20 章：合规与伦理（风险/隐私/安全/治理）

- NIST AI RMF https://www.nist.gov/itl/ai-risk-management-framework （笔记：[笔记](../notes/ref-077-nist-ai-rmf.md)）
- Concrete Problems in AI Safety（Amodei et al., 2016）https://arxiv.org/abs/1606.06565 （笔记：[笔记](../notes/ref-090-concrete-problems-in-ai-safety.md)）

## 说明：如何“查找与补充”更多材料

- 想按章节找：先看 `../indexes.md` 的“按章节适配”分组，再回到对应 `notes/` 和 `deepresearch/`。
- 想补某一章：优先补“权威标准/协议/论文的入口页”，其次补“可执行的工程手册”，最后再补“观点型文章”。
- 如果你发现某一章资料少：先补“底层标准”（例如 Auth 的 RFC、支付的合规标准），再补“可操作实践”（例如 runbook、回归策略、对账流程）。
