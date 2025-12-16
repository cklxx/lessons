# 欢迎来到我的数字书架

<div class="hero">
  <div>
    <p class="eyebrow">日拱一卒 · 学习自留地</p>
    <h1>用 Markdown 写书，用优雅界面沉浸阅读</h1>
    <p class="subtitle">精心打磨的 Material 主题，支持全文搜索、章节导航与代码高亮。每一册都可以独立维护、快速发布。</p>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="books/example-book/index/">开始阅读示例书</a>
      <a class="md-button" href="#快速开始">本地构建指南</a>
    </div>
  </div>
  <div class="hero-card">
    <p class="eyebrow">站点状态</p>
    <ul class="checklist">
      <li>✅ 一键 `mkdocs build` 生成静态站点</li>
      <li>✅ GitHub Actions 自动打包并发布 Pages</li>
      <li>✅ 自定义主题与卡片式导航</li>
    </ul>
    <p class="meta">想要新增内容？复制任意书籍目录，更新 <code>mkdocs.yml</code> 即可。</p>
  </div>
</div>

## 目录总览

<div class="grid">
  <div class="glass-card">
    <p class="eyebrow">教程 · 示例书</p>
    <h3>示例书（模板）</h3>
    <p>从封面、章节到导航的最小示例，适合作为新书的起点。</p>
    <a class="text-link" href="books/example-book/index/">快速浏览 →</a>
  </div>
  <div class="glass-card">
    <p class="eyebrow">AI 产品方法论</p>
    <h3>如何在 AI 的辅助下完成一个软件产品</h3>
    <p>从需求挖掘到上线评测的全链路方法，覆盖原型、工程实现与增长治理。</p>
    <a class="text-link" href="books/ai-assisted-software-product/index/">进入目录 →</a>
  </div>
</div>

> 提示：Material 主题自带搜索和大纲导航，适合长篇阅读，也能快速跳转到代码示例。

## 快速开始

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

## 结构约定

- `docs/books/<书名>/index.md`：书籍的封面页，包含简介、目录与快速链接。
- `docs/books/<书名>/chapter-x.md`：具体章节内容，命名随意但建议保留章节顺序编号。
- `mkdocs.yml`：站点配置和导航定义，新增书籍后只需在这里添加条目即可。

## 设计风格

- **简洁导航**：左侧目录按书籍展开，章节层级清晰。
- **阅读体验**：主题色选用靛蓝与青色，配合留白与等宽代码块，营造安静的阅读氛围。
- **代码友好**：内置复制按钮与语法高亮，适合讲解 Python 示例。

准备好开始写作了吗？复制示例书作为模板，或在现有章节下继续创作。
