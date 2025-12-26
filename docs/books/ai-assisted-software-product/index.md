# 写给未来的超级个体：AI 全栈产品开发实战

> 面向超级个体的实战手册，覆盖从机会发现、工程交付到模型训练与商业闭环的全链路。本书强调可裁决性，关键论点尽量给出权威来源或验收标准，让你能用证据推进决策，用门槛管理风险。[1][2][5][18]

![总览插图占位：价值/交付/治理三层闭环（无文字底图）](../../assets/books/ai-assisted-software-product/chapter-hero.svg)

## 你读这本书为了什么（先说人话）

你想要更快裁决，也想要更稳交付。更快裁决意味着这事值不值得做，今天就能证明或否掉。更稳交付意味着改动能验收、能留档，退化能回滚，上线不靠运气。

如果你读完后能做到“每次迭代都能拿出证据包，说清楚改了什么、好在哪里、差在哪里、失败怎么退”，这本书就算完成任务了。

## 你将得到什么

你会得到一套可跳读的路线图，把不同阶段的重点任务讲清楚。你会学会把“好、快、专业、稳定”这类形容词改写成阈值、窗口、触发条件和失败判定。你会建立一条可复跑的证据链，用决策日志、对比结果、评测集版本和回滚指针，把每次迭代的得失记清楚。你还会拿到一组可复制的模板与配方，用在 PRD 合同、证据包、Runbook、指标字典、提示词和图片配置上。

## 范围与前置假设

本书主要写给个人开发者和小团队，适合希望用 AI 提升验证速度、工程交付与模型能力，并最终跑通商业闭环的人。默认你能独立开发并部署一个小型 Web 产品，能阅读并修改 Python 或 TypeScript 代码，对抽样、偏差、显著性这类基础统计概念不陌生。[4][18] 训练与推理章节默认你具备租用 GPU 的能力。如果你只有 CPU 或轻量 GPU，可以优先走量化、LoRA 或 QLoRA、蒸馏或托管推理等低成本路径，先把闭环跑通，再谈更重的方案。[44][47]

## 可复现性与断言的定义

可复现指的是在明确输入、环境与随机性控制的前提下，读者能够复跑并得到同级别结论，例如同趋势、同阈值判断，而不要求逐 bit 相同输出。[1][5] 断言需要可被证伪。如果无法通过实验、日志或评测指标验证，需要明确标注为经验性建议或开放问题，并给出验证方法。[18]

## 工具链与命令约定（读之前先对齐）
本仓库是方法论文档仓库。你会看到一些可复制的示例与脚手架，它们用于表达门禁与证据链的结构，不承诺某个框架开箱即用。

读之前建议先把自检和入口命名对齐。自检方面，严格构建和引用检查需要能跑通。入口命名方面，把门禁、证据归档、发布和回滚做成固定入口，避免跨章节出现多套口径。AI 审稿流程见 [ai-editor-sop.md](ai-editor-sop.md)，里面不会绑定某个具体模型或工具。

证据包结构与字段模板详见：[附录 D：证据包与门禁速查](D-evidence-pack.md)。
常见线上事故的 10 分钟止损动作库详见：[附录 E：10 分钟止损 Runbook 库](E-runbooks.md)。
指标字典、阈值三段式与告警到动作映射详见：[附录 F：指标字典与告警门禁速查](F-metrics-alerts.md)。
插图规范与图片 Prompt 配方详见：[附录 G：图片 Prompt 与插图规范](G-image-prompts.md)。

## 配图建议（占位图 + 图片 Prompt 文本）

这本书的配图追求可维护，强调风格统一、无文字底图、留白可叠字。占位图可以先用下面这张，等你确定需要再生成正式图。

![占位图：结构/对比/关系示意（无文字底图）](../../assets/books/ai-assisted-software-product/placeholder-diagram.svg)

用于生成“总览三层闭环”配图的图片 Prompt 文本（输出给你的生图工具）：

```text
image_prompt:
flat 2D vector illustration, three concentric loops made of clean arrows representing value, delivery, governance, minimalist tech diagram,
blue and teal palette, solid white background, high contrast, ample whitespace for later typography, no text

negative_prompt:
text, letters, numbers, watermark, signature, handwriting, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces

params:
aspect_ratio=16:9, quality=high
```

## 本书的写法（你会看到的风格）
我尽量把这本书写成可长期复用的作战手册。写法上先讲可迁移的方法与结构，再把工具放在可选实现路径里，避免把某个版本当成结论。[2][24][29] 各章尽量以裁决为终点，把门槛写清，把证据留档，让退化可回滚。[5][18] 模板尽量集中在附录，正文更关注为什么和怎么想，方便你裁剪和版本化。[18] 更完整的写作约定见 [写作风格与格式约定](style-guide.md)。

## 导航与阅读路径
建议从序言开始读，先把三重责任对齐，见 [一人即是一支队伍](preface.md)。如果你正在做 0 到 1，优先读 [02-discovery.md](02-discovery.md)、[03-prd.md](03-prd.md)、[04-prototype.md](04-prototype.md)、[05-validation.md](05-validation.md)、[06-ui.md](06-ui.md) 把最短闭环先跑通。工程设施与评测体系可以先看 [07-engineering.md](07-engineering.md) 与 [18-evaluation.md](18-evaluation.md)。需要构建 RAG 或 Agent 时读 [10-agent-rag.md](10-agent-rag.md) 及两个补充章节 [10-agent-rag-rag.md](10-agent-rag-rag.md) 与 [10-agent-rag-agent.md](10-agent-rag-agent.md)。术语表与参考文献分别在 [glossary.md](glossary.md) 与 [references.md](references.md)，全书质量门槛在 [quality-checklist.md](quality-checklist.md)。

## 使用方式与质量门槛
阅读时建议把验证闭环放在第一位。每章都会给出验证方法与可复现证据的形态，例如日志、评测集、基准对比或截图，并说明怎样把检查自动化进 CI。[5][28][44] 当你改动检索、训练、部署等关键配置时，尽量做改动前后的指标对比，覆盖延迟、质量、成本与风险面。缺少证据支撑的优化，最好回到假设与实验设计层面重做。[5][28][44] 数据快照、评测集、Notebook、配置与报告建议一起版本化，形成可审计的个人资产。[1][34]

## 致读者
本书旨在帮助个人开发者与小团队，以最少的资源完成从需求验证、全栈实现到模型训练与部署的闭环。请在阅读时结合自身约束（时间、算力、预算），灵活采纳各章节的低成本路径。
