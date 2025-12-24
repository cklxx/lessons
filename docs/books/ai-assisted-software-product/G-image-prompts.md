# 附录 G：图片 Prompt 与插图规范（无文字底图）

你可以接受“配图只是装饰”的自我安慰，但读者不会原谅你浪费他们的注意力。更糟的是，带文字的 AI 配图几乎必然演变成返工：改一个词就得重画整张图，风格漂移、构图崩坏、乱码字符轮番上演。

这份附录的目标很简单：把插图当作**可版本控制的视觉资产**，把图片 Prompt 当作**可复用的配置**，让“生成底图 → 叠字 → 验收门禁”成为默认流程。

![章节插图占位（示例）](../../assets/books/ai-assisted-software-product/chapter-hero.svg)

## 1) 为什么必须“无文字底图”

带文字的 AI 配图是事故制造机，原因很硬：

1. **不可维护**：文字是最常变的东西，你把它烧进像素里就是在自毁维护性。
2. **不可翻译**：多语言版本不是“再跑一次”，而是“再赌一次”。
3. **不可检索**：图片里的字对站内检索与 RAG 来说就是黑洞。
4. **不可一致**：字体、字重、对齐、留白是排版问题，不是图片模型的强项。

正确做法：先生成**干净底图**，关键文字后期用 SVG/排版工具叠加，风格统一、改字不重画、可回归。

## 2) 全书统一的 Prompt 基准（复制即用）

把下面三段当成“风格底座”。每次写图，只改主体变量，底座不要漂移。

### style_base

```text
flat 2D vector art, minimalist tech diagram, blue and white palette, solid white background, clean composition, high contrast, crisp edges, no text
```

### negative_prompt_base

```text
text, letters, numbers, watermark, signature, handwriting, logo, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces
```

### params_base

```text
aspect_ratio=16:9, quality=high
```

## 3) 图片验收门禁（不通过就别提交）

1. **零文字**：不得出现可识别字符、伪文字、水印、签名。
2. **可叠字**：必须预留大块纯色留白；留白位置要稳定，方便统一叠标题与标签。
3. **风格一致**：扁平向量、蓝白配色、干净背景、线条粗细一致；禁止混入写实与强材质。
4. **信息增益**：图必须表达结构隐喻（分层/流向/闭环/门禁），而不是装饰背景。
5. **可维护**：同类图用同一套构图规则；不要每张图都重新发明风格。

![占位图（用于叠字演示）](../../assets/books/ai-assisted-software-product/placeholder-diagram.svg)

## 4) 资产命名与归档规范

把图片当资产，就别让它散落成垃圾堆。

- **目录**：`docs/assets/books/ai-assisted-software-product/`（按章节主题建子目录或统一 `generated/`）。
- **文件名**：`ch<chapter>_<topic>_<concept>.png`（示例：`ch12_billing_loop.png`）。
- **alt 文本**：必须描述“图证明什么”，不是“image”。

引用示例（注意路径与 alt）：

```markdown
![计费闭环：计量-账本-对账-止损的循环底图](../../assets/books/ai-assisted-software-product/generated/ch12_billing_loop.png)
```

## 5) 生成流程（两种方式）

### 方式 A：只产出 Prompt 文本（工具无关，推荐）

你只需要交付 `image_prompt/negative_prompt/params` 三段文本。至于用什么生图工具，交给你自己。

### 方式 B：用仓库脚本生成图片（可选）

仓库已有 `skills/genimage.py` 可直接生成插图并输出 Markdown 引用（图片生成依赖你本地的 Gemini Cookie 配置，详见仓库 `skills/index.md` 的说明）。

示例：为第 7 章生成一张 CI/CD 管道的无文字底图，并输出可粘贴的 Markdown：

```bash
python3 skills/genimage.py \
  --prompt "flat 2D vector illustration of a CI/CD pipeline with nodes and arrows, blue and white palette, solid white background, high contrast, no text" \
  --style "negative constraints: text, letters, numbers, watermark, signature" \
  --max-images 1 \
  --name ch07_cicd_pipeline \
  --out docs/assets/books/ai-assisted-software-product/generated \
  --print-md \
  --md-from docs/books/ai-assisted-software-product/07-engineering.md
```

注意：`skills/genimage.py` 不会替你自动“继承风格底座”，你必须在 prompt 里显式写清 `style_base` 的关键约束，尤其是 `no text` 与负向约束。

## 6) 常用配方库（无文字底图）

用法：`image_prompt` 叠加 `style_base`；`negative_prompt` 至少包含 `negative_prompt_base`；`params` 基于 `params_base` 微调。

### 6.1 需求验证闭环（Demand Validation Loop）

#### 用途
表达“想法 → 验证 → 反馈 → 迭代”的闭环。

#### 构图要点
- 三段或四段环形箭头；中心留白用于叠字。

#### image_prompt
```text
circular iteration loop made of three smooth arrows, minimal cycle diagram, clean whitespace in the center, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, complex machinery, messy background
```

#### params
```text
aspect_ratio=1:1, quality=high
```

#### 推荐放置位置
[02-discovery.md](02-discovery.md)

### 6.2 PRD 合同隐喻（PRD Contract）

#### 用途
表达“PRD 是契约”：对齐目标、范围、验收与回滚。

#### 构图要点
- 文档图标 + 印章/握手的抽象形状；左右对称留白。

#### image_prompt
```text
minimal document icon with a simple stamp or handshake shape above it, agreement contract metaphor, clean composition, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, realistic hands, skin texture, illegible writing
```

#### params
```text
aspect_ratio=3:2, quality=high
```

#### 推荐放置位置
[03-prd.md](03-prd.md)

### 6.3 原型到状态矩阵（Prototype State Matrix）

#### 用途
表达 UI 状态覆盖：加载/空/错/无权限等。

#### 构图要点
- 网格布局；多个屏幕框；内部用几何形状表达不同状态。

#### image_prompt
```text
grid of abstract mobile screen wireframes showing different states using geometric shapes, minimalist UI state matrix, clean layout, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, app icons, realistic phone bezel, detailed UI with typography
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[04-prototype.md](04-prototype.md)

### 6.4 数据流管道（Data Pipeline）

#### 用途
表达“采集 → 清洗 → 存储 → 消费”的线性流动。

#### 构图要点
- 左入右出；节点统一形状；箭头清晰。

#### image_prompt
```text
horizontal data pipeline with processing nodes and arrows left to right, abstract data packets, clean whitespace, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, realistic plumbing, complex machinery, messy background
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[13-data.md](13-data.md)

### 6.5 前后端边界（Frontend/Backend Boundary）

#### 用途
表达 API 作为边界：前端与后端分工清晰。

#### 构图要点
- 左右分屏；中间用接口/插槽/关口隐喻连接。

#### image_prompt
```text
split-screen architecture, left side abstract UI blocks, right side server and database blocks, clean connector in the middle, minimalist diagram, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, code snippets, terminal screens, photorealistic
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[07-engineering.md](07-engineering.md)

### 6.6 RAG 架构（RAG Architecture）

#### 用途
表达“检索挂载知识库”：LLM 旁接索引/文档块。

#### 构图要点
- 核心处理单元 + 文档块/索引卡片 + 放大镜隐喻。

#### image_prompt
```text
central model chip icon connected to a stack of organized document blocks and a simple magnifier symbol, retrieval augmented generation concept, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, realistic brain anatomy, messy papers, cluttered background
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[10-agent-rag.md](10-agent-rag.md)

### 6.7 Agent 工具编排（Agent Tool Orchestration）

#### 用途
表达 Agent 调用多个工具并在中心汇聚结果。

#### 构图要点
- Hub-and-spoke；工具节点用齿轮/地球/表格等抽象形状表达。

#### image_prompt
```text
central agent core node connecting to multiple utility tool nodes (gear, globe, chart) in a hub-and-spoke layout, clean network, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, humanoid robot, realistic face, chaotic lines
```

#### params
```text
aspect_ratio=1:1, quality=high
```

#### 推荐放置位置
[10-agent-rag-agent.md](10-agent-rag-agent.md)

### 6.8 评测门禁（Evaluation Gate）

#### 用途
表达“质量门禁拦截”：不达标不放行。

#### 构图要点
- 关卡过滤；合格通过、不合格回炉；用颜色区分但不刺眼。

#### image_prompt
```text
checkpoint gate filtering geometric blocks, approved blue blocks pass through, rejected blocks redirected, quality gate metaphor, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, police imagery, photorealistic, messy background
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[18-evaluation.md](18-evaluation.md)

### 6.9 部署灰度（Canary Deployment）

#### 用途
表达“流量渐进切换”：小流量试水再放量。

#### 构图要点
- 两组节点；流量箭头一大一小；强调可回滚。

#### image_prompt
```text
two server clusters with split traffic arrows, small arrow to canary cluster and large arrow to stable cluster, traffic shifting concept, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, weather clouds, rain, photorealistic
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[17-deployment.md](17-deployment.md)

### 6.10 计费闭环（Billing Cycle）

#### 用途
表达计量/账本/对账/止损的闭环。

#### 构图要点
- 环形四节点；节点留白；符号化表达含义。

#### image_prompt
```text
circular billing loop with four abstract nodes, metering ledger reconciliation stop-loss represented by simple geometric icons, arrows forming a closed cycle, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, currency symbols, realistic money, credit cards
```

#### params
```text
aspect_ratio=1:1, quality=high
```

#### 推荐放置位置
[12-billing.md](12-billing.md)

### 6.11 治理盾牌（Governance Shield）

#### 用途
表达安全与合规防护的闭环。

#### 构图要点
- 盾牌 + 外圈流程节点；克制，不要军事化。

#### image_prompt
```text
large minimalist shield icon surrounded by a circular governance loop of small nodes and arrows, clean security metaphor, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, weapons, blood, photorealistic, messy background
```

#### params
```text
aspect_ratio=4:3, quality=high
```

#### 推荐放置位置
[20-governance.md](20-governance.md)

### 6.12 指标与告警（Metrics & Alerts）

#### 用途
表达可观测性：趋势 + 告警触发。

#### 构图要点
- 折线趋势 + 告警图标（用几何形状抽象表达）。

#### image_prompt
```text
minimal dashboard showing a rising trend line and a simple alert icon as geometric shape, monitoring concept, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, detailed spreadsheets, axes with numbers, photorealistic
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[F-metrics-alerts.md](F-metrics-alerts.md)

### 6.13 证据包归档（Evidence Archiving）

#### 用途
表达“证据落盘”：版本组合、报告与回滚指针的归档。

#### 构图要点
- 文件夹/档案盒 + 勾选标记；简洁。

#### image_prompt
```text
neatly organized archive box and folder icons with a simple checkmark shape, evidence pack metaphor, clean composition, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, dusty old books, realistic cardboard texture
```

#### params
```text
aspect_ratio=1:1, quality=high
```

#### 推荐放置位置
[D-evidence-pack.md](D-evidence-pack.md)

### 6.14 复盘时间线（Postmortem Timeline）

#### 用途
表达“分钟级时间线”：发生 → 止血 → 恢复 → 验证。

#### 构图要点
- 水平时间轴 + 关键节点；留白用于叠字。

#### image_prompt
```text
horizontal timeline with three to five milestone nodes, clean spacing, incident response timeline metaphor, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, dates, years, calendar pages, photorealistic
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[19-iteration.md](19-iteration.md)

### 6.15 路线图（Roadmap）

#### 用途
表达“未来路径”：阶段推进与里程碑。

#### 构图要点
- 向右上方的路径 + 节点；终点用星形/旗帜形状抽象表达。

#### image_prompt
```text
path leading upward to a simple star or flag shape, milestone nodes along the path, roadmap metaphor, clean whitespace for labels, no text
```

#### negative_prompt
```text
text, letters, numbers, watermark, signature, asphalt road texture, cars, photorealistic
```

#### params
```text
aspect_ratio=16:9, quality=high
```

#### 推荐放置位置
[01-method.md](01-method.md)

