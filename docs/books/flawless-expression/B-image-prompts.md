# 附录 B：图片 Prompt 配方库（无文字底图）

如果你还在让图片模型“把图画出来顺便把字也写对”，你不是在做内容生产，你是在制造返工与事故。带文字的 AI 配图有三个硬伤：

1. **改一个字要重做整张图**：维护成本爆炸，且每次重做都会引入构图漂移。
2. **多语言版本是地狱**：中文能凑合，英文更容易乱码；要出多语种基本等于重跑。
3. **小屏幕可读性为零**：伪文字、字符粘连、对比不足，读者放大也看不清。

正确做法只有一种：**先生成无文字底图，再用矢量/排版工具叠加真实文字**。这不仅更专业，而且可复用、可版本化、可回归（见 [06-feedback.md](06-feedback.md)）。

![配图占位：示意图底图](../../assets/books/flawless-expression/placeholder-diagram.svg)

## 全局基准（全书统一）

把它当成“风格底座”，每张图只改主体变量，禁止每次临时换风格。

### style_base（所有配方共享）

```text
flat 2D vector art, minimalist tech diagram style, blue and white palette, solid white background, clean composition, high contrast, crisp edges
```

### negative_prompt_base（所有配方共享）

```text
text, letters, numbers, watermark, signature, handwriting, logo, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces
```

### params_base（按你的生图工具填写）

```text
aspect_ratio=16:9, quality=high
```

---

## 配方 01：系统架构层次图（分层底图）

### 用途
表现“下层基础设施 → 中层平台 → 上层应用”的堆叠关系，留白用于后期叠字。

### 构图要点
- 三层必须可分辨（形状或高度区分），但不要画具体产品 logo。
- 箭头只表达方向与依赖，不表达文字语义。

### image_prompt
```text
flat 2D vector illustration, three horizontal layers stacked vertically, abstract blocks representing client/platform/database,
thin arrows connecting layers, generous whitespace for later labels, blue and white palette, solid white background, clean composition, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, logo, photorealistic, 3d render, gradients, shadows, messy background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 02：数据流管道（左入右出）

### 用途
表现“采集 → 处理 → 存储 → 消费”的线性流程，适合做章节插图底图。

### 构图要点
- 横向构图，左到右明确。
- 节点用统一几何图标（圆角矩形、圆形、圆柱），不要细节过密。

### image_prompt
```text
flat 2D vector diagram, horizontal data pipeline from left to right, simple processing nodes as rounded rectangles, arrows indicating flow,
abstract data packets as small squares, blue and white palette, solid white background, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, gradients, shadows, cluttered layout, messy background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 03：闭环循环（反馈回路）

### 用途
表现“写 Prompt → 跑回归 → 评审 → 发布门禁”的闭环（或任何 PDCA 类循环）。

### 构图要点
- 圆环或四段环，中心留白。
- 只画节点与箭头，文字后期叠加。

### image_prompt
```text
flat 2D vector illustration, circular feedback loop with four abstract nodes connected by arrows, minimal tech style,
blue and white palette, solid white background, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 04：三圈交集（交集即甜点区）

### 用途
表达“价值/交付/治理”等三要素的交集，适合做概念框架图底图。

### 构图要点
- 三个圆透明叠加，交集区域对比明显。
- 不要在图里放任何文字。

### image_prompt
```text
flat 2D vector illustration, three overlapping translucent circles, distinct intersection areas with subtle blending,
blue and green and orange palette, solid white background, minimalist composition, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, gradients, heavy shadows, blur, cluttered background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 05：盾牌治理闭环（防护与门禁）

### 用途
表达“治理/审计/门禁/红队”的保护性闭环，适合安全与合规主题。

### 构图要点
- 中心主体是盾牌或锁的隐喻，外围环形节点表达流程。
- 风格必须克制，避免“军事化武器感”。

### image_prompt
```text
flat 2D vector illustration, central shield icon made of simple geometric shapes, surrounding circular loop with small abstract nodes and arrows,
blue and white palette, solid white background, clean composition, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, weapons, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 06：三阶台阶（成熟度/进阶）

### 用途
表达“草稿 → 协作 → 机器执行”的进阶路线或成熟度模型。

### 构图要点
- 台阶表面留白用于叠加短标签。
- 不要画人物爬楼梯，避免喧宾夺主。

### image_prompt
```text
flat 2D vector illustration, three-step staircase made of simple blocks, subtle upward arrow, minimalist tech style,
blue and white palette, solid white background, clean composition, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, people, faces, photorealistic, 3d render, gradients, shadows, blur, messy background
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 07：对比卡片（Before vs After）

### 用途
表达“混乱 vs 结构化”“聊天 vs 交付”的对比，适合序章与总览。

### 构图要点
- 一分为二，左右对称，中央有分隔。
- 左侧更杂乱但仍保持审美克制，避免脏。

### image_prompt
```text
flat 2D vector illustration, split-screen composition, left side chaotic abstract shapes and noisy lines, right side clean structured blocks and checklists,
blue and white palette, solid white background, high contrast, minimalist style, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, gradients, heavy shadows, blur, messy background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 08：告警与门禁（阻断点）

### 用途
表达“质量门禁阻断”“不通过就不能发布”的概念。

### 构图要点
- 以“关卡/栅栏/闸门”作隐喻，搭配少量警示色点缀。
- 不要画车祸、火灾等戏剧化场景。

### image_prompt
```text
flat 2D vector illustration, minimalist gate or barrier blocking a flow line, small warning accent in orange,
clean tech style, blue and white palette, solid white background, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, gradients, heavy shadows, blur, disaster scene, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 09：资料池索引（知识库与索引）

### 用途
表达“资料池/索引/检索”的结构化存储隐喻，适合资料池页面或 RAG 相关章节。

### 构图要点
- 画整齐排列的立方体或书脊抽象形状，留白充足。
- 避免密集细节，避免“赛博电路板噪声”。

### image_prompt
```text
flat 2D vector illustration, organized grid of abstract data cubes and file cards, subtle depth but minimalist,
blue and white palette, solid white background, clean composition, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, photorealistic, 3d render, gradients, heavy shadows, blur, cluttered layout, messy background, humans, faces
```

### params
```text
aspect_ratio=16:9, quality=high
```

---

## 配方 10：章节封面分隔图（宽屏留白）

### 用途
用作章节首页题图：视觉重心在右侧，左侧留白用于叠加章节标题。

### 构图要点
- 右侧有轻量几何波纹或网格，左侧近乎纯白。
- 绝不承载关键信息，避免“图胜于文”的误导。

### image_prompt
```text
flat 2D vector wide banner, subtle abstract tech wave or mesh pattern on the far right, fading into pure white space on the left,
blue and white palette, clean minimalist composition, high contrast, no text
```

### negative_prompt
```text
text, letters, numbers, watermark, signature, centered subject, cluttered left side, photorealistic, 3d render, gradients, heavy shadows, messy background, humans, faces
```

### params
```text
aspect_ratio=21:9, quality=high
```

---

更多“图文混排与载体选择”规则见 [05-medium.md](05-medium.md)。记住：底图是容器，文字才是定义。
