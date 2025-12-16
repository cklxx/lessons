# 欢迎来到我的数字书架

这是一套用 Markdown 编写的书籍合集，通过 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 以博客式的优雅界面呈现。每本书都放在独立的文件夹中，方便维护和扩展。

## 结构约定

- `docs/books/<书名>/index.md`：书籍的封面页，包含简介、目录与快速链接。
- `docs/books/<书名>/chapter-x.md`：具体章节内容，命名随意但建议保留章节顺序编号。
- `mkdocs.yml`：站点配置和导航定义，新增书籍后只需在这里添加条目即可。

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

## 设计风格

- **简洁导航**：左侧目录按书籍展开，章节层级清晰。
- **阅读体验**：主题色选用靛蓝与青色，配合留白与等宽代码块，营造安静的阅读氛围。
- **代码友好**：内置复制按钮与语法高亮，适合讲解 Python 示例。

准备好开始写作了吗？可以先从下面的示例书开始，复制一份作为模板即可。
