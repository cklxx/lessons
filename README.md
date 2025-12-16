# lessons

基于 MkDocs Material 的个人数字书架。每本书放在 `docs/books/<书名>` 下，用 Markdown 编写，自动生成优雅的网页阅读体验。

## 快速开始

```bash
pip install -r requirements.txt
mkdocs serve
```

浏览器打开 <http://127.0.0.1:8000> 查看效果。新增书籍后在 `mkdocs.yml` 的 `nav` 中补充导航即可。

## 部署到 GitHub Pages

```bash
mkdocs gh-deploy
```

命令会构建并推送到 `gh-pages` 分支，然后在仓库设置中将其绑定为 Pages 来源。

或直接依赖仓库内的 GitHub Actions 工作流（`.github/workflows/pages.yml`）：

- 推送到 `main` 分支或手动触发会自动构建并发布站点到 GitHub Pages。
- 首次使用时在仓库 Settings → Pages 中选择 “GitHub Actions” 作为部署来源。

## 目录示例

- `docs/index.md`：首页与说明
- `docs/books/example-book/`：示例书，包含 `index.md` 和章节文件
- `docs/styles/overrides.css`：自定义配色与排版样式
