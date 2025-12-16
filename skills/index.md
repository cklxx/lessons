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

