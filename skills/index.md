# skills

这里放一些可复用的小工具脚本。

## genimage：生成文章内插图

位置：`skills/genimage.py`

### 依赖

脚本使用 `gemini-webapi`：

```bash
pip install gemini-webapi
```

### 配置 Cookie（放到 env / .env）

把 Gemini（<https://gemini.google.com>）的 Cookie 写到环境变量里：

- `Secure_1PSID`（必填）
- `Secure_1PSIDTS`（可空）

推荐：复制仓库根目录的 `.env.example` 为 `.env`，填好后即可；脚本会自动从仓库根目录读取 `.env`。

### 使用

先验证 `.env` 是否能被正确加载（不触发网络请求）：

```bash
python3 skills/genimage.py --dry-run --prompt "test"
```

生成图片并输出可直接粘贴到 Markdown 的引用（`--md-from` 会按「当前文章」自动算相对路径）：

```bash
python3 skills/genimage.py \
  --prompt "为《第 1 章：需求挖掘与市场验证》生成一张扁平风、干净、抽象的插图，不要文字" \
  --max-images 2 \
  --name chapter-01-hero \
  --print-md \
  --md-from docs/books/ai-assisted-software-product/chapter-01-demand.md
```

默认输出目录：`docs/assets/skills/generated/<name>/`。

参考实现与更多说明：<https://github.com/HanaokaYuzu/Gemini-API>

## gemini_md：用 Gemini 批量扩写/改写 Markdown（带门禁）

位置：`skills/gemini_md.py`

这个脚本解决两个重复劳动：

1) 用 `gemini -m gemini-3-pro-preview -p` 对现有 Markdown 进行扩写/改写（stdin 输入原文，prompt 负责规则与目标）。  
2) 输出前做硬门禁，避免触发仓库的 citation 检查规则（例如方括号纯数字的 `[12]` 会被当成缺失引用）。

### 配套 prompt 模板

位置：`skills/prompts/flawless-expression-enrich.txt`

模板默认约束：不外链、相对链接带 `.md`、保持尖锐批判、补模板/示例/失败判定/回滚、并插入占位图与图片 Prompt 文本。

### 用法

单文件输出到 stdout（推荐先审再覆盖）：

```bash
python3 skills/gemini_md.py \
  --prompt-file skills/prompts/flawless-expression-enrich.txt \
  docs/books/flawless-expression/01-mindset.md > /tmp/01-mindset.new.md
```

批量生成到目录（保留相对路径，并在文件名后追加 `.gemini.md`）：

```bash
python3 skills/gemini_md.py \
  --prompt-file skills/prompts/flawless-expression-enrich.txt \
  --out-dir /tmp/gemini-out \
  docs/books/flawless-expression
```

确认无误后再原地覆盖（会先跑门禁，失败直接退出）：

```bash
python3 skills/gemini_md.py \
  --prompt-file skills/prompts/flawless-expression-enrich.txt \
  --in-place \
  docs/books/flawless-expression/02-facts.md
```

## check_docs：一键跑文档门禁

位置：`skills/check_docs.sh`

```bash
bash skills/check_docs.sh
```
