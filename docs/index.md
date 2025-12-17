# 我的数字书架

<div class="hero">
  <div>
    <p class="eyebrow">AI 辅助软件产品 · 工程手册</p>
    <h1>把经验沉淀成可验收的资产</h1>
    <p class="subtitle">模板 / 清单 / 失败模式 / 门禁阈值 / 回滚策略。</p>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="books/ai-assisted-software-product/">开始阅读：AI 辅助完成软件产品</a>
      <a class="md-button" href="books/ai-assisted-software-product/A-templates/">模板库</a>
      <a class="md-button" href="materials/ai-assisted-software-product/filtered/top-resources/">精选资料</a>
    </div>
  </div>
  <div class="hero-card">
    <p class="eyebrow">你会得到</p>
    <ul class="checklist">
      <li>✅ 端到端路径：从需求到上线/回滚</li>
      <li>✅ 可复制资产：模板/清单/门禁</li>
      <li>✅ 可复现方法：指标、失败判定、回归</li>
    </ul>
    <p class="meta">面向：独立开发者 / 全栈 / 技术产品 / 需要工程闭环的团队。</p>
  </div>
</div>

## 入口

<div class="grid">
  <div class="glass-card">
    <p class="eyebrow">主线</p>
    <h3>AI 全栈产品开发实战</h3>
    <p>从需求到上线与治理的全链路；每章给出可验收的交付物与门禁。</p>
    <a class="text-link" href="books/ai-assisted-software-product/">进入目录 →</a>
  </div>
  <div class="glass-card">
    <p class="eyebrow">可复制资产</p>
    <h3>模板库 / 清单 / 写作 SOP</h3>
    <p>可直接落到仓库与流程：写作、评审、验收、回归。</p>
    <p class="meta">
      <a class="text-link" href="books/ai-assisted-software-product/A-templates/">模板库 →</a>
      · <a class="text-link" href="books/ai-assisted-software-product/quality-checklist/">质量清单 →</a>
      · <a class="text-link" href="books/ai-assisted-software-product/ai-editor-sop/">AI 辅助写作 SOP →</a>
    </p>
  </div>
  <div class="glass-card">
    <p class="eyebrow">资料池</p>
    <h3>精选资料（按章可直接用）</h3>
    <p>从参考文献与标准中筛出优先读的部分，并按主题归类。</p>
    <a class="text-link" href="materials/ai-assisted-software-product/filtered/top-resources/">打开精选资料 →</a>
  </div>
</div>

<a id="guide-path"></a>
## 阅读路径（按目标）

| 你的目标 | 建议先读 | 读完你应该得到的产物 |
|---|---|---|
| 产品落地 | [第 2 章：需求挖掘](books/ai-assisted-software-product/02-discovery.md) → [第 3 章：PRD](books/ai-assisted-software-product/03-prd.md) → [第 4 章：原型](books/ai-assisted-software-product/04-prototype.md) → [第 5 章：验证与打磨](books/ai-assisted-software-product/05-validation.md) → [第 6 章：UI](books/ai-assisted-software-product/06-ui.md) | PRD + 原型验证记录 + 迭代卡片 + 验收清单 |
| 流程化开发 | [第 7 章：工程化](books/ai-assisted-software-product/07-engineering.md) → [模板库](books/ai-assisted-software-product/A-templates.md) | 质量门禁 + 回归/回滚协议 |
| RAG / Agent | [第 10 章：总览](books/ai-assisted-software-product/10-agent-rag.md) → [RAG 深入](books/ai-assisted-software-product/10-agent-rag-rag.md) → [Agent 深入](books/ai-assisted-software-product/10-agent-rag-agent.md) | 证据链 + 工具边界 + 回归基线 |
| 训练 / 推理 | [第 13 章：数据](books/ai-assisted-software-product/13-data.md) → [第 14 章：预训练](books/ai-assisted-software-product/14-pretrain.md) → [第 15 章：后训练](books/ai-assisted-software-product/15-posttrain-rl.md) → [第 16 章：推理](books/ai-assisted-software-product/16-inference.md) | 数据/模型资产 + 对比表 + 回滚策略 |
| 线上治理 | [第 17 章：部署与运维](books/ai-assisted-software-product/17-deployment.md) → [第 18 章：评测](books/ai-assisted-software-product/18-evaluation.md) → [第 20 章：合规](books/ai-assisted-software-product/20-governance.md) | 灰度/回滚 Runbook + 评测门禁 + 审计边界 |

## 快捷入口

- [模板库：写作/评审/验收标准块](books/ai-assisted-software-product/A-templates.md)
- [质量清单：从 PRD 到上线的自检门槛](books/ai-assisted-software-product/quality-checklist.md)
- [AI 辅助写作 SOP：如何用模型做校对与补强](books/ai-assisted-software-product/ai-editor-sop.md)
- [路线图（Roadmap）：后续更新计划](books/ai-assisted-software-product/writing-backlog.md)

<div class="fineprint">
  <p><strong>提示</strong>：支持全文搜索与目录大纲，适合“随用随查”。</p>
  <p><strong>本地预览</strong>：<code>pip install -r requirements.txt</code> → <code>mkdocs serve</code>（<code>http://127.0.0.1:8000</code>）。</p>
  <p><strong>发布</strong>：推送 <code>main</code> 由 GitHub Actions 自动构建；发布前自检可跑 <code>mkdocs build --strict</code>。</p>
  <p><strong>章节结构</strong>：定位 → 最小路径 → 验收/门禁 → 失败模式 → 回归/回滚。</p>
</div>
