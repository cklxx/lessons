# tools/ 脚本使用指南（偏“怎么跑、怎么对齐输入输出”）

本页按“输入/输出/常用参数/常见问题”总结 `tools/` 下与写作链路相关的脚本。

## `tools/materials_to_markdown.py`：URL → 可提交的 Markdown 快照

目的：把 `docs/materials/**/*.md` 里的 URL 统一快照到 `sources/md/`，并生成 `sources/index.jsonl` 供后续脚本关联。

常用：

```bash
python3 tools/materials_to_markdown.py
```

先看会处理哪些 URL：

```bash
python3 tools/materials_to_markdown.py --dry-run | head
```

关键参数：

- `--root`：扫描 URL 的根目录（默认 `docs/materials`）
- `--out`：快照输出目录（默认 `docs/materials/ai-assisted-software-product/sources/md`）
- `--max`：限制处理条数（用于先小规模验证）
- `--force`：忽略缓存，强制重抓
- `--timeout`/`--sleep-ms`：网络与节流

输出：

- `docs/materials/ai-assisted-software-product/sources/md/*.md`
- `docs/materials/ai-assisted-software-product/sources/index.jsonl`

## `tools/gemini_build_material_indexes.py`：sources → Gemini 标签/评分 → indexes

目的：对每份 `sources` 快照做分类、打分、标签，并生成 `docs/materials/.../indexes.md` 作为资料索引页。

常用（断点续跑）：

```bash
python3 tools/gemini_build_material_indexes.py --resume
```

建议先小规模验证：

```bash
python3 tools/gemini_build_material_indexes.py --max 20
```

关键参数：

- `--sources-index`：输入索引（默认 `docs/materials/ai-assisted-software-product/sources/index.jsonl`）
- `--out-jsonl`：Gemini 输出（默认 `docs/materials/ai-assisted-software-product/gemini/index.jsonl`，追加写入）
- `--out-md`：索引页（默认 `docs/materials/ai-assisted-software-product/indexes.md`）
- `--model`：覆盖 Gemini 模型名（留空则用脚本默认）
- `--resume`：跳过已处理 URL
- `--max-chars`：截断输入，避免超长快照导致失败

## `tools/gemini_deepresearch_materials.py`：notes + sources + labels → deepresearch

目的：以“你的 notes”为对齐锚点，结合 sources 快照做更深入的“可落地扩展笔记”，并生成 `deepresearch/index.md`。

常用：

```bash
python3 tools/gemini_deepresearch_materials.py
```

强制重生成：

```bash
python3 tools/gemini_deepresearch_materials.py --force
```

关键参数：

- `--notes-dir`：你的资料笔记目录（默认 `docs/materials/ai-assisted-software-product/notes`）
- `--sources-index`：sources 索引（默认 `.../sources/index.jsonl`）
- `--labels-jsonl`：Gemini 标签/评分（默认 `.../gemini/index.jsonl`）
- `--out-dir`/`--index-out`：deepresearch 输出位置
- `--timeout`/`--sleep-ms`：单条调用超时与节流
- `--max-chars`：限制快照输入长度

对齐规则（很重要）：

- notes 里需要包含一行 `原始来源：https://...`（脚本用它把 notes ↔ sources 对上）。

## `tools/check_citations.py`：引用编号一致性检查

目的：检查 `docs/books/ai-assisted-software-product/*.md` 里出现的 `[n]` 是否都在 `references.md` 中存在。

```bash
python3 tools/check_citations.py
```

## `tools/generate_figures_svg.py`：用 Python 生成书内示意图（SVG）

目的：用标准库生成轻量 SVG 图（便于版本化与复现），输出到 `docs/assets/`。

```bash
python3 tools/generate_figures_svg.py --out-dir docs/assets
```

输出示例：

- `docs/assets/figure_06_2_tokens_pipeline.svg`
- `docs/assets/figure_16_2_inference_control_loop.svg`
- `docs/assets/figure_17_2_observability_stack.svg`
- `docs/assets/figure_18_2_judge_regression_loop.svg`

## `tools/generate_book_edition.py`：章节改写（可选）

目的：把“讲义/草稿风格”的章节改写为更接近出版的版本（会做一次 DDG 搜索并把链接作为“延伸阅读”约束）。

示例：

```bash
python3 tools/generate_book_edition.py \
  --out-dir docs/books/ai-assisted-software-product/book-edition \
  docs/books/ai-assisted-software-product/07-engineering.md
```

注意：

- 这个脚本依赖 `gemini --output-format json --allowed-tools read_file` 形态的 CLI 能力。
- 输出更适合当“改写草稿”，合并回主文前仍建议做事实核验与引用编号统一。

## Gemini CLI：把“文字工作”脚本化的最小套路

你不一定要写新脚本才能“脚本化使用 gemini”。很多时候，一条可复现的命令就够了：把输入通过 stdin 喂给 gemini，再把输出重定向到文件，形成“可回滚的文字变更”。

### 1) 对单个小节做润色（推荐：先小后大）

最小套路：

```bash
cat input.md | gemini --model gemini-2.5-flash "请把 stdin 的 Markdown 小节润色得更循循善诱，但保持可执行性；只输出 Markdown，不要代码块。"
```

建议你在 prompt 里加上硬约束：

- 只改写某个小节；
- 代码块/命令行逐字不改；
- 不新增引用编号（或保持已有编号不变）；
- 不编造事实或数据（不确定就标注“待核验”）。

### 2) 把结果落到“可审查的补丁”

你可以把 gemini 的输出写到临时文件，然后用 `git diff` 审查变更范围，再决定是否合入。这比在编辑器里直接覆盖更安全。
