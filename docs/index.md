# 欢迎来到我的数字书架

<div class="hero">
  <div>
    <p class="eyebrow">AI 辅助软件工程 · 实战手册</p>
    <h1>把知识写成「可复用的工程资产」</h1>
    <p class="subtitle">不仅是教程，更是一套可直接拷贝复用的资产：需求模板、验收清单、失败模式库、门禁阈值与回滚策略。</p>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="books/ai-assisted-software-product/">开始阅读：AI 辅助完成软件产品</a>
      <a class="md-button" href="#guide-path">按角色选路径</a>
      <a class="md-button" href="#quickstart">本地构建</a>
    </div>
  </div>
  <div class="hero-card">
    <p class="eyebrow">你会在这里得到什么</p>
    <ul class="checklist">
      <li>✅ 章节化的“端到端”实践：从需求到上线与回滚</li>
      <li>✅ 可复制的模板与清单：能直接放进你的仓库做门禁</li>
      <li>✅ 图文并茂的流程示意：用来对齐团队与复盘迭代</li>
    </ul>
    <p class="meta">适用人群：独立开发者 / 全栈工程师 / 技术产品经理 / 需要把 AI 能力“落到工程闭环”的团队。</p>
  </div>
</div>

## 这座书架的写作约定

为了确保内容可复用、可验收，本书采用“工程文档”结构：

- **每章必有**：定位/收获/方法论速览/实战路径/复现检查/常见陷阱（现象→根因→复现→修复→回归验证）/交付物与验收。
- **示例（可复制）优先**：尽量把“怎么做”写成可以直接拷贝到你项目里的骨架（目录、字段、门禁与报告）。
- **图文并茂**：重要闭环优先用图或表表达；你可以把图替换成真实截图或你的架构图。

![图：写作结构与验收闭环（占位）](assets/fig-placeholder.svg)

*图 0-1：写作结构与验收闭环——方法论→模板→示例→验证→回归（示意）*
<!-- TODO: replace with a real diagram (e.g., my writing workflow / review loop) -->

## 目录总览（当前重点）

<div class="grid">
  <div class="glass-card">
    <p class="eyebrow">AI 产品方法论 · 主线</p>
    <h3>如何在 AI 的辅助下完成一个软件产品</h3>
    <p>从需求、PRD、原型、工程实现、RAG/Agent 到训练、推理、LLMOps 的全链路实践。每章都有可复制示例与验收门槛。</p>
    <a class="text-link" href="books/ai-assisted-software-product/">进入目录 →</a>
  </div>
  <div class="glass-card">
    <p class="eyebrow">写作模板 · 附录</p>
    <h3>模板库 / 清单 / 写作 SOP</h3>
    <p>把“怎么写、怎么验收、怎么复盘”变成标准块：你可以直接在团队里复用。</p>
    <p class="meta">
      <a class="text-link" href="books/ai-assisted-software-product/A-templates/">模板库 →</a>
      · <a class="text-link" href="books/ai-assisted-software-product/quality-checklist/">质量清单 →</a>
      · <a class="text-link" href="books/ai-assisted-software-product/ai-editor-sop/">AI 辅助写作 SOP →</a>
    </p>
  </div>
  <div class="glass-card">
    <p class="eyebrow">教程 · 站点模板</p>
    <h3>示例书（模板）</h3>
    <p>最小可用的书籍结构（封面/章节/导航），适合作为“新书起点”。</p>
    <a class="text-link" href="books/example-book/">快速浏览 →</a>
  </div>
</div>

> 提示：站点支持全文搜索与目录大纲，适合长篇沉浸阅读，也适合当“工程手册”随用随查。

<a id="guide-path"></a>
## 角色与路径

如果你第一次来，可以按自己的目标选择一条“最短路径”：

| 你的目标 | 建议先读 | 读完你应该得到的产物 |
|---|---|---|
| 我想把想法落地为产品 | [第 1 章：需求](books/ai-assisted-software-product/chapter-01-demand.md) → [第 2 章：PRD](books/ai-assisted-software-product/chapter-02-prd.md) → [第 3 章：UI](books/ai-assisted-software-product/chapter-03-ui.md) | 一份可评审 PRD + 原型 + 验收清单 |
| 我想把 AI 辅助开发变成流程 | [第 4 章：工作流](books/ai-assisted-software-product/chapter-04-workflow.md) → [附录：模板库](books/ai-assisted-software-product/A-templates.md) | 一套可复用的 Prompt/任务模板与回归门禁 |
| 我正在做 RAG/Agent | [第 6 章：RAG](books/ai-assisted-software-product/chapter-06-rag.md) → [第 7 章：Agent](books/ai-assisted-software-product/chapter-07-agent.md) | 一份检索评估 + 失败模式库 + 回滚策略 |
| 我在训练或部署模型 | [第 8 章：数据](books/ai-assisted-software-product/chapter-08-data.md) → [第 9 章：预训练](books/ai-assisted-software-product/chapter-09-pretrain.md) → [第 10 章：后训练](books/ai-assisted-software-product/chapter-10-posttrain.md) | 数据卡片/模型卡 + 门禁阈值 + 训练/发布审计链 |
| 我在做线上稳定性与治理 | [第 11 章：推理](books/ai-assisted-software-product/chapter-11-inference.md) → [第 12 章：LLMOps](books/ai-assisted-software-product/chapter-12-llmops.md) | 灰度发布/回滚 Runbook + 监控与告警口径 |

## 内容预览（图文示例）

下面是本书里最常用的三类“图”：你可以把它们替换为你的真实架构图、报表截图或监控面板。

![图：RAG 端到端流水线（占位）](assets/ch06-rag-pipeline.png)

*图 0-2：RAG 数据流转全景：从切分（Chunking）到索引、检索、重排与生成*
<!-- TODO: replace with a real diagram from my own stack -->

![图：切分策略对效果的影响（占位）](assets/ch06-chunking-strategy.png)

*图 0-3：切分策略影响：过长引入噪声、过短割裂上下文，混合策略通常更稳*
<!-- TODO: replace with real evaluation results -->

![图：结构化输出与引用（占位）](assets/ch06-structured-output.png)

*图 0-4：结构化输出：答案与引用拆分，便于审计、溯源与回归评测*
<!-- TODO: replace with product screenshot -->

## 快捷入口：可复制资产

- [模板库：写作/评审/验收标准块](books/ai-assisted-software-product/A-templates.md)
- [质量清单：从 PRD 到上线的自检门槛](books/ai-assisted-software-product/quality-checklist.md)
- [AI 辅助写作 SOP：如何用模型做校对与补强](books/ai-assisted-software-product/ai-editor-sop.md)
- [路线图（Roadmap）：后续更新计划](books/ai-assisted-software-product/writing-backlog.md)

<a id="quickstart"></a>
## 快速开始（本地预览）

1. 安装依赖（本地预览需要 Python 3.8+）：

   ```bash
   pip install -r requirements.txt
   ```

2. 启动本地预览：

   ```bash
   mkdocs serve
   ```

   浏览器访问 <http://127.0.0.1:8000>，即可看到实时更新的页面。

3. 部署到 GitHub Pages：

   ```bash
   mkdocs gh-deploy
   ```

   默认推送到 `gh-pages` 分支，可在仓库设置中绑定为 Pages 来源。

4. CI/CD 自动发布：

   推送到 `main` 后，GitHub Actions 会自动构建并发布静态页面，失败信息会在 Actions 日志中给出。

<details>
<summary>给维护者：发布前自检与站点约定（可折叠）</summary>

- 运行 `mkdocs build --strict`，确保构建阶段没有警告/错误（例如链接与元数据问题）。
- 确认首页卡片链接可正常跳转（原始 HTML 中的链接不会被 MkDocs 自动改写，需手动保持与实际 URL 一致）。

### 结构约定

- `docs/books/<书名>/index.md`：书籍的封面页，包含简介、目录与快速链接。
- `docs/books/<书名>/chapter-x.md`：具体章节内容，命名随意但建议保留章节顺序编号。
- `mkdocs.yml`：站点配置和导航定义，新增书籍后只需在这里添加条目即可。

### 设计风格

- **简洁导航**：左侧目录按书籍展开，章节层级清晰。
- **阅读体验**：主题色选用靛蓝与青色，配合留白与等宽代码块，营造安静的阅读氛围。
- **代码友好**：内置复制按钮与语法高亮，适合讲解 Python 示例。

</details>

准备好开始写作了吗？你可以从“阅读路径”里选一条开始，也可以直接打开模板库，把它们拷贝到自己的项目里作为起点。
