# GitHub Pages 部署故障排查

本页仅覆盖本仓库的 GitHub Actions 工作流 `.github/workflows/pages.yml`（使用官方 `actions/configure-pages` / `actions/deploy-pages`）。  
如果你走的是本地 `mkdocs gh-deploy` 发布，请以 MkDocs 官方文档为准，本页的权限/配置项不一定适用。

## 报错：`Resource not accessible by integration` / `Not Found`

### 典型日志

`actions/configure-pages` 会调用 Pages REST API 创建或更新站点；当工作流令牌无法访问该 API 时，常见报错类似：

```text
Warning: Get Pages site failed. Error: Not Found - https://docs.github.com/rest/pages/pages#get-a-apiname-pages-site
Error: Create Pages site failed. Error: Resource not accessible by integration - https://docs.github.com/rest/pages/pages#create-a-apiname-pages-site
```

### 根因分类（按出现概率排序）

1. **Pages 未启用或未允许**：仓库/组织/企业策略禁用了 GitHub Pages，导致 `GITHUB_TOKEN` 无法创建站点。
2. **令牌权限不足**：工作流运行时的 `GITHUB_TOKEN` 不具备 `pages:write` 或 `id-token:write`。
3. **触发来源受限（Fork PR）**：来自 fork 的 PR/workflow 触发通常会把 `GITHUB_TOKEN` 降级为只读，无法部署 Pages。

### 逐项排查（建议按顺序执行）

1. **确认 Pages 发布来源**
   - 进入仓库 Settings → Pages → **Source**，选择 “GitHub Actions”。
   - 若页面提示 Pages 被组织/企业策略禁用，需要先在组织/企业侧放开（此时工作流侧怎么改都无效）。

2. **确认工作流触发上下文**
   - 本仓库工作流默认只在 `push` 到 `main` 或手动 `workflow_dispatch` 触发；确保不是从 fork PR 触发的部署。
   - 如果你确实需要 PR 预览部署，建议使用独立的预览站点/分支策略，不要直接复用生产 Pages（否则权限与安全边界会很复杂）。

3. **确认工作流权限声明**
   - 检查 `.github/workflows/pages.yml` 是否包含：
     - `pages: write`
     - `id-token: write`
     - `contents: read`
   - 如果文件已声明但仍失败，优先怀疑**组织策略**或**仓库设置把权限强行收紧**。

4. **确认仓库 Actions 权限设置（有些组织会强制）**
   - Settings → Actions → General → Workflow permissions：
     - 若被设置为只读并且组织策略不允许覆盖，可能导致 Pages API 无法调用。
   - 同页的 “Allow GitHub Actions to create and approve pull requests” 与 Pages 无直接关系，但在一些组织模板里会被一起锁定；以组织策略为准。

5. **修正后重跑**
   - 回到 Actions 页面，重新运行失败的 workflow（Re-run jobs）。

### 如果你不打算启用 Pages，但又希望 CI 通过

最简单的做法是删除 `.github/workflows/pages.yml`。  
如果需要保留文件但在特定场景不执行，可以给 `jobs.deploy` 加条件（示例）：

```yaml
if: github.ref == 'refs/heads/main' && github.event_name != 'pull_request'
```
