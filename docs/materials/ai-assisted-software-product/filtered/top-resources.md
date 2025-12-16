# AI 辅助软件产品：精选资料（可直接用）

> 本页从全书参考文献与工程常用标准中，提取“最值得优先读/最能直接落地”的资料，并按章节主题归类。目标是让你在需要补背景、补方法或补门禁时，能快速找到权威出处与可执行做法。

## P0：先读这些（覆盖全书）

- **产品与交付（决策与节奏）**
  - *The Lean Startup*（Eric Ries）https://theleanstartup.com/ （对应第 1–2 章：证据与实验门槛）
  - *Accelerate*（Forsgren/Humble/Kim）https://itrevolution.com/product/accelerate/ （对应第 4/12 章：门禁、回归与交付表现）
  - *Continuous Delivery*（Humble/Farley）https://martinfowler.com/books/continuousDelivery.html （对应第 4/11/12 章：发布门禁与回滚）
- **安全底线（上线必备）**
  - OWASP ASVS https://owasp.org/www-project-application-security-verification-standard/ （对应第 5/11/12 章：可验收的安全检查项）

## 第 6 章：RAG（检索增强生成）

- RAG 原始论文（Lewis et al., 2020）https://arxiv.org/abs/2005.11401
- BM25 综述（Robertson & Zaragoza, 2009）https://www.nowpublishers.com/article/Details/INR-019
- FAISS（Johnson et al., 2019）https://arxiv.org/abs/1702.08734
- RAGAS（Li et al., 2024）https://arxiv.org/abs/2402.01761

## 第 7 章：Agent（智能体）

- ReAct（Yao et al., 2023）https://arxiv.org/abs/2210.03629
- AutoGen（Wu et al., 2023）https://arxiv.org/abs/2308.08155
- LangGraph 文档 https://langchain-ai.github.io/langgraph/
- OpenAI Tool Use / Function Calling（文档入口）https://platform.openai.com/docs/

## 第 8–10 章：数据工程与后训练

- Datasheets for Datasets（Gebru et al., 2021）https://arxiv.org/abs/1803.09010
- LLM 数据去重（Mouli et al., 2023）https://arxiv.org/abs/2307.03195
- Self-Instruct（Wang et al., 2023）https://arxiv.org/abs/2212.10560
- WizardLM / Evol-Instruct（Xu et al., 2023）https://arxiv.org/abs/2304.12244
- LoRA（Hu et al., 2021/2022）https://arxiv.org/abs/2106.09685
- QLoRA（Dettmers et al., 2023）https://arxiv.org/abs/2305.14314
- RLHF（Ouyang et al., 2022）https://arxiv.org/abs/2203.02155
- DPO（Rafailov et al., 2023）https://arxiv.org/abs/2305.18290

## 第 11 章：推理加速与部署

- vLLM（Kwon et al., 2023）https://arxiv.org/abs/2309.06180
- TensorRT-LLM（官方资料入口）https://github.com/NVIDIA/TensorRT-LLM
- GPTQ（Frantar et al., 2024）https://arxiv.org/abs/2210.17323
- AWQ（Lin et al., 2023）https://arxiv.org/abs/2306.00978
- Text Generation Inference（TGI）https://github.com/huggingface/text-generation-inference
- KServe（推理服务编排）https://kserve.github.io/website/

## 第 12 章：LLMOps（监控与评估）

- OpenTelemetry https://opentelemetry.io/docs/
- Prometheus https://prometheus.io/docs/introduction/overview/
- Grafana https://grafana.com/docs/grafana/latest/
- LLM-as-a-Judge（Zheng et al., 2023）https://arxiv.org/abs/2306.05685
- Guardrails 综述（Rawte et al., 2023）https://arxiv.org/abs/2307.08715

## 前端与体验（第 3–4 章常用）

- WCAG 2.2 https://www.w3.org/TR/WCAG22/
- Design Tokens 格式 https://www.designtokens.org/TR/drafts/format/
- axe-core https://github.com/dequelabs/axe-core
- Lighthouse https://developer.chrome.com/docs/lighthouse/
- Playwright https://playwright.dev/
- Storybook Test Runner https://storybook.js.org/docs/writing-tests/integrations/test-runner

