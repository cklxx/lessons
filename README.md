# lessons

基于 MkDocs Material 的个人数字书架/笔记库：所有内容以 Markdown 维护，由 MkDocs 统一生成静态站点。

## 范围与约定

- 本仓库的“源码”主要是 `docs/` 下的 Markdown；`mkdocs.yml` 只负责站点配置与导航。
- 文档中的命令示例默认在 macOS/Linux shell 执行；Windows 可用 PowerShell/WSL 做等价替换。
- 站内链接优先使用 Markdown 相对路径（例如 `docs/books/.../chapter-1.md`），避免在原始 HTML 中硬编码构建后的 URL（MkDocs 不会自动重写 HTML）。

## 环境要求

- Python >= 3.8（推荐 3.11/3.12）
- 可用的 `pip`

## 本地预览

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
mkdocs serve
```

浏览器打开 <http://127.0.0.1:8000> 查看效果。

### 严格构建（建议用于发布前自检）

```bash
mkdocs build --strict
```

## 新增/维护内容

1. 在 `docs/books/<slug>/` 新建一本书，至少包含 `index.md`（封面/目录）与若干章节文件。
2. 在 `mkdocs.yml` 的 `nav` 中补充导航；导航顺序即侧边栏顺序。
3. 如需自定义样式，修改 `docs/styles/overrides.css`。

### 链接与命名规范（避免 404）

- 文件名一旦发布尽量不要改；MkDocs 的 URL 默认与路径强绑定。
- 在 Markdown 中使用相对链接并显式写 `.md`（MkDocs 会在构建时重写到站点 URL）。
- 不要在原始 HTML 里写 `.../index/` 这类目录 URL（很容易与 `use_directory_urls` 的真实输出不一致）。

## 部署到 GitHub Pages

仓库已包含 GitHub Actions 工作流 `.github/workflows/pages.yml`，默认在 `main` 分支推送或手动触发时自动构建并发布站点到 GitHub Pages。

首次使用需要一次性配置：

1. 仓库 Settings → Pages → Source 选择 “GitHub Actions”。
2. 若仓库/组织策略禁用了 Pages 或限制了令牌权限，请先放开。

如果你确实需要本地手动发布（不推荐与 Actions 混用）：

```bash
mkdocs gh-deploy
```

该命令会构建并推送到 `gh-pages` 分支；注意这要求你对远端仓库有写权限，并且需要自行处理分支保护/发布策略。

## 目录示例

- `mkdocs.yml`：站点配置与导航
- `docs/index.md`：站点首页
- `docs/books/`：书籍内容（每本书一个目录）
- `docs/styles/overrides.css`：自定义配色与排版样式
