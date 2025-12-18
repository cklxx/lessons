# 写作工作流与 Gemini 脚本指南（本仓库）

本目录把仓库里与“资料→笔记→Deep Research→章节写作→发布”的流程串起来，并说明 `tools/` 下 Gemini 脚本的使用方式与输入/输出。

## 0. 约定与前置条件

### Python 环境（跑所有 `tools/*.py`）

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

### Gemini CLI（跑所有 `tools/gemini_*.py` / `tools/generate_book_edition.py`）

这些脚本通过子进程调用 `gemini`，因此你需要：

- `gemini` 在 `PATH` 中可执行；
- 你的 `gemini` 版本支持脚本用到的参数（至少包含 `gemini -p <prompt>`；部分脚本需要 `--output-format json` / `--allowed-tools read_file`）。

快速自检：

```bash
command -v gemini
gemini --help | head
```

### Gemini WebAPI（仅 `skills/genimage.py` 需要）

图片生成脚本使用 `gemini-webapi`，需要在仓库根目录提供 `.env`（参考 `.env.example`）。

## 1) 资料池流水线（推荐顺序）

目标：把“外部链接”变成可写作、可复用、可追溯的本地 Markdown 资料库，并产出 Deep Research 扩展笔记。

### Step A：批量捞链接（可选）

入口：`tools/link_harvester.py`

- 输出：`docs/materials/ai-assisted-software-product/raw/link-index-*.csv`
- 适用：需要快速扩充候选资料面时使用（支持 Bing / DuckDuckGo / HN）

示例：

```bash
python3 tools/link_harvester.py --provider duckduckgo \
  --out docs/materials/ai-assisted-software-product/raw/link-index-batchX.csv
```

### Step B：人工筛选成“优先读清单”

入口：`docs/materials/ai-assisted-software-product/filtered/top-resources.md`

建议做法：

- 只保留你“愿意在章节里引用”的内容（标准/论文/官方文档优先）。
- 每条链接写清楚：**为什么值得读**、**适配哪章**、**是否需要二次核验**。

### Step C：把链接快照成可提交的 Markdown（sources）

入口：`tools/materials_to_markdown.py`

- 输入：扫描 `docs/materials/**/*.md` 里的 URL（默认排除 `raw/`、`sources/`、`gemini/`、`deepresearch/` 等生成目录）
- 输出：
  - `docs/materials/ai-assisted-software-product/sources/md/*.md`（快照正文，可提交）
  - `docs/materials/ai-assisted-software-product/sources/index.jsonl`（索引，可提交）

示例：

```bash
python3 tools/materials_to_markdown.py \
  --out docs/materials/ai-assisted-software-product/sources/md
```

如果只是想看会抓哪些 URL：

```bash
python3 tools/materials_to_markdown.py --dry-run | head
```

### Step D：用 Gemini 给资料打标签/评分，并生成索引页

入口：`tools/gemini_build_material_indexes.py`

- 输入：`docs/materials/ai-assisted-software-product/sources/index.jsonl`
- 输出：
  - `docs/materials/ai-assisted-software-product/gemini/index.jsonl`（每条资料的分类/标签/打分结果）
  - `docs/materials/ai-assisted-software-product/indexes.md`（索引页，MkDocs 会展示）

示例：

```bash
python3 tools/gemini_build_material_indexes.py --resume
```

建议：

- 首次跑可以先加 `--max 20` 验证 prompt/输出结构是否稳定。
- 用 `--resume` 断点续跑（JSONL 追加写入）。

### Step E：写“资料笔记”（notes）

入口：`docs/materials/ai-assisted-software-product/notes/ref-*.md`

建议做法：

- 每份资料一个 `ref-XXX-*.md`，保留“原始来源：<url>”行（后续脚本会用它关联 source）。
- 只写你会在章节里复用的内容：定义、边界、清单、落地步骤、常见坑。

### Step F：用 Gemini 生成 Deep Research 扩展笔记

入口：`tools/gemini_deepresearch_materials.py`

- 输入：
  - `notes/`（你的可复用笔记）
  - `sources/index.jsonl`（快照索引，用于找到对应快照内容）
  - `gemini/index.jsonl`（分类/评分，用于按类汇总 index）
- 输出：
  - `docs/materials/ai-assisted-software-product/deepresearch/ref-*.md`
  - `docs/materials/ai-assisted-software-product/deepresearch/index.md`

示例：

```bash
python3 tools/gemini_deepresearch_materials.py
```

建议：

- 默认会跳过已存在的文件；需要重跑用 `--force`。
- 单条卡住可用 `--timeout` 调大，或用 `--max-chars` 限制输入快照长度。

## 2) 章节写作：把 Deep Research “提炼进正文”

Deep Research 的目标不是替代写作，而是把“可落地做法/清单/常见坑”这类高密度内容补进章节正文，让读者能复用。

推荐的“提炼”方式（先轻后重）：

1. **补门槛**：把 Deep Research 的检查清单变成章节的验收门槛（DoD/Gate）。
2. **补步骤**：把“可落地做法”改写成章节里的步骤与模板（表格/清单）。
3. **补反例**：把“常见坑与对策”变成失败样本（发生→代价→修复→回归）。
4. **补引用**：在正文里用引用编号（如 `[53]`）挂到 `docs/books/ai-assisted-software-product/references.md`。

实践建议：

- 先在章节里加一个 “最小 SOP/门禁” 小节，把清单落成“可执行的发布规则”，再扩写解释为什么这样做。
- 同一主题尽量只保留一个“唯一入口”的清单，避免在多个章节重复但不一致。

## 3) 写作辅助脚本（Gemini）

### 草稿讲义 → 书籍版章节（可选）

入口：`tools/generate_book_edition.py`

- 输入：你指定的一个或多个章节 Markdown
- 输出：改写后的章节 Markdown（写到 `--out-dir`）

示例：

```bash
python3 tools/generate_book_edition.py \
  --out-dir docs/books/ai-assisted-software-product/book-edition \
  docs/books/ai-assisted-software-product/07-engineering.md
```

注意：这个脚本会在 prompt 中限制可用的外部来源（只允许它自己搜索到的“延伸阅读”链接列表），但仍建议你在合并前做事实核验与风格统一。

## 5) 快速入口

- 脚本参数与输入输出对齐：[`flow/scripts.md`](scripts.md)
- 章节提炼配方（把 Deep Research 变正文）：[`flow/recipes.md`](recipes.md)
- 可运行示例（推理网关/评测脚本/Tokens 出码）：`docs/examples/`

## 4) 质量与发布

### 引用编号一致性检查

入口：`tools/check_citations.py`

```bash
python3 tools/check_citations.py
```

### 本地预览 / 严格构建

```bash
mkdocs serve
mkdocs build --strict
```
