# AI 辅助软件产品：精选资料（可直接用）

> 本页从全书参考文献与工程常用标准中，提取“最值得优先读/最能直接落地”的资料，并按章节主题归类。目标是让你在需要补背景、补方法或补门禁时，能快速找到权威出处与可执行做法。

## P0：先读这些（覆盖全书）

- **产品与交付（决策与节奏）**
  - *The Lean Startup*（Eric Ries）https://theleanstartup.com/ （对应第 1–2 章：证据与实验门槛；笔记：[笔记](../notes/ref-004-lean-startup.md)）
  - *Accelerate*（Forsgren/Humble/Kim）https://itrevolution.com/product/accelerate/ （对应第 4/12 章：门禁、回归与交付表现；笔记：[笔记](../notes/ref-006-accelerate.md)）
  - *Continuous Delivery*（Humble/Farley）https://martinfowler.com/books/continuousDelivery.html （对应第 4/11/12 章：发布门禁与回滚；笔记：[笔记](../notes/ref-005-continuous-delivery.md)）
- **安全底线（上线必备）**
  - OWASP ASVS https://owasp.org/www-project-application-security-verification-standard/ （对应第 5/11/12 章：可验收的安全检查项；笔记：[笔记](../notes/ref-068-owasp-asvs.md)）
- **API 标准（契约与协作）**
  - OpenAPI Specification https://spec.openapis.org/oas/latest.html （对应第 2/5/7 章：契约、工具调用与协作；笔记：[笔记](../notes/ref-067-openapi-spec.md)）

## 第 6 章：RAG（检索增强生成）

- RAG 原始论文（Lewis et al., 2020）https://arxiv.org/abs/2005.11401 （笔记：[笔记](../notes/ref-024-rag-paper.md)）
- BM25 综述（Robertson & Zaragoza, 2009）https://www.nowpublishers.com/article/Details/INR-019 （笔记：[笔记](../notes/ref-027-bm25.md)）
- FAISS（Johnson et al., 2019）https://arxiv.org/abs/1702.08734 （笔记：[笔记](../notes/ref-025-faiss.md)）
- RAGAS（Shahul et al., 2023）https://arxiv.org/abs/2309.15217 （笔记：[笔记](../notes/ref-028-ragas.md)）

## 第 7 章：Agent（智能体）

- ReAct（Yao et al., 2023）https://arxiv.org/abs/2210.03629 （笔记：[笔记](../notes/ref-029-react.md)）
- LangGraph 文档 https://docs.langchain.com/oss/python/langgraph/overview/ （笔记：[笔记](../notes/ref-060-langgraph.md)）
- AutoGen（Wu et al., 2023）https://arxiv.org/abs/2308.08155 （笔记：[笔记](../notes/ref-030-autogen.md)）
- OpenAI Tool Use / Function Calling（文档入口）https://platform.openai.com/docs/ （笔记：[笔记](../notes/ref-031-openai-tool-use.md)）

## 第 8–10 章：数据工程与后训练

- Datasheets for Datasets（Gebru et al., 2021）https://arxiv.org/abs/1803.09010 （笔记：[笔记](../notes/ref-034-datasheets.md)）
- LLM 数据去重（Lee et al., 2021）https://arxiv.org/abs/2107.06499 （笔记：[笔记](../notes/ref-035-llm-dedup.md)）
- LoRA（Hu et al., 2021/2022）https://arxiv.org/abs/2106.09685 （笔记：[笔记](../notes/ref-040-lora.md)）
- Self-Instruct（Wang et al., 2023）https://arxiv.org/abs/2212.10560 （笔记：[笔记](../notes/ref-036-self-instruct.md)）
- WizardLM / Evol-Instruct（Xu et al., 2023）https://arxiv.org/abs/2304.12244 （笔记：[笔记](../notes/ref-066-wizardlm.md)）
- QLoRA（Dettmers et al., 2023）https://arxiv.org/abs/2305.14314 （笔记：[笔记](../notes/ref-047-qlora.md)）
- RLHF（Ouyang et al., 2022）https://arxiv.org/abs/2203.02155 （笔记：[笔记](../notes/ref-041-rlhf.md)）
- DPO（Rafailov et al., 2023）https://arxiv.org/abs/2305.18290 （笔记：[笔记](../notes/ref-042-dpo.md)）

## 第 11 章：推理加速与部署

- vLLM（Kwon et al., 2023）https://arxiv.org/abs/2309.06180 （笔记：[笔记](../notes/ref-045-vllm.md)）
- TensorRT-LLM（官方资料入口）https://github.com/NVIDIA/TensorRT-LLM （笔记：[笔记](../notes/ref-046-tensorrt-llm.md)）
- GPTQ（Frantar et al., 2024）https://arxiv.org/abs/2210.17323 （笔记：[笔记](../notes/ref-048-gptq.md)）
- AWQ（Lin et al., 2023）https://arxiv.org/abs/2306.00978 （笔记：[笔记](../notes/ref-059-awq.md)）
- Text Generation Inference（TGI）https://github.com/huggingface/text-generation-inference （笔记：[笔记](../notes/ref-049-tgi.md)）
- KServe（推理服务编排）https://kserve.github.io/website/ （笔记：[笔记](../notes/ref-063-kserve.md)）

## 第 12 章：LLMOps（监控与评估）

- OpenTelemetry https://opentelemetry.io/docs/ （笔记：[笔记](../notes/ref-061-opentelemetry.md)）
- LLM-as-a-Judge（Zheng et al., 2023）https://arxiv.org/abs/2306.05685 （笔记：[笔记](../notes/ref-050-llm-as-a-judge.md)）
- Prometheus https://prometheus.io/docs/introduction/overview/ （笔记：[笔记](../notes/ref-062-prometheus.md)）
- Grafana https://grafana.com/docs/grafana/latest/ （笔记：[笔记](../notes/ref-064-grafana.md)）
- Guardrails（Building Guardrails for LLMs, 2024）https://arxiv.org/abs/2402.01822 （笔记：[笔记](../notes/ref-051-guardrails.md)）

## 前端与体验（第 3–4 章常用）

- WCAG 2.2 https://www.w3.org/TR/WCAG22/ （笔记：[笔记](../notes/ref-017-wcag-2-2.md)）
- Design Tokens 格式 https://www.designtokens.org/TR/drafts/format/ （笔记：[笔记](../notes/ref-053-design-tokens.md)）
- axe-core https://github.com/dequelabs/axe-core （笔记：[笔记](../notes/ref-054-axe-core.md)）
- Lighthouse https://developer.chrome.com/docs/lighthouse/ （笔记：[笔记](../notes/ref-055-lighthouse.md)）
- Playwright https://playwright.dev/ （笔记：[笔记](../notes/ref-057-playwright.md)）
- Storybook Test Runner https://storybook.js.org/docs/writing-tests/integrations/test-runner （笔记：[笔记](../notes/ref-056-storybook-test-runner.md)）
