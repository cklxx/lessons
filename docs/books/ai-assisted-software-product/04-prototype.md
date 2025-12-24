# 第 4 章：原型与信息架构：用最小成本验证路径
![第 4 章封面](../../assets/chapter_04_header_1766035396981.png)

> 原型的价值不是看起来像，而是用最小成本验证关键路径、信息架构与错误恢复：用户能不能走到价值、走错了能不能回来。[4][16]

在 0→1 阶段，你最稀缺的资源不是设计技巧，而是用户的注意力。原型的唯一任务，是把团队的注意力从“想象的完美功能”拉回“真实的崎岖路径”：用户从哪里进来、要做什么、在哪一步犹豫、失败后怎么自救。

不要在这个阶段画高保真 UI，那是掩盖逻辑漏洞的化妆品。

## 章节定位
上一章你已经把 PRD 写成了最小合同（Scope）。这一章我们要用原型（Prototype）验证这个合同能不能执行。

如果你发现关键路径走不通，最划算的修复方式不是写代码，而是改纸上的图：入口、层级、状态与恢复机制。[16][17]

## 你将收获什么
*   **一套“三张纸”原型法**：页面树（地图）、用户流（路径+坑）、状态清单（安全网）。
*   **一份走查脚本**：用“完成任务”替代“审美争论”，让反馈变成可修复的断点。
*   **一个验证门槛**：什么情况下可以进入开发，什么情况下必须撕了重画。

## 三层思考：原型到底在验证什么

### 第 1 层：读者目标
读完本章，你手里不应该只有几张图，而应该有一套能跑通的**逻辑闭环**。
*   **不仅是顺境**：用户不看说明书，能完成任务吗？
*   **更是逆境**：AI 瞎说、超时、拒答时，用户是被困死，还是能退一步海阔天空？

### 第 2 层：论证链条
验证逻辑非常冷酷，缺一不可：

`页面树（定骨架）` -> `用户流（定血肉+排雷）` -> `状态清单（兜底）` -> `走查脚本（实战）` -> `断点列表（修补）`

只要有一环是空的（比如缺异常流），你的原型就是一张这就画皮，开发阶段一定会爆雷。[16][17]

### 第 3 层：落地与验收
原型不是艺术品，是工程图纸。它的验收标准只有一条：**断点是否闭合**。所有在这个阶段发现的逻辑死胡同，必须在进入下一章前打通，否则就得回滚到 PRD。[4]

---

## 方法论：三张纸 + 一次走查

![图 4-1：三张纸（页面树/用户流/状态清单）关系示意](../../assets/figure_04_1_1765970865282.png)

!!! quote "图 4-1 生成参数"
    *   **image_prompt**: A minimalist abstract diagram showing three layers of UI design artifacts. Top layer: A simple tree structure (Information Architecture). Middle layer: A linear flow chart with branching paths (User Flow). Bottom layer: A grid of state cards (State Matrix). The three layers are connected by vertical lines indicating dependency. Technical drawing style, blueprint aesthetic, white background, black lines. No text.
    *   **negative_prompt**: text, realistic UI, complex shading, 3d, color.
    *   **params**: --ar 16:9 --v 6.0

### AI 产品的生死线：在原型里画出“不确定性”
传统软件的原型验证“功能有没有”；AI 产品的原型必须验证“出错怎么办”。

**必须刻在脑子里的事实**：AI 一定会出错（幻觉、罗嗦、听不懂）。
如果你的原型里只有 Happy Path（快乐路径），那你做的不是 AI 产品，是科幻片。[71][72]

我们把 AI 交互切分为三个**关键时刻（Moments of Truth）**，每个时刻都要在原型里有对应画面：

1.  **首次接触（First Contact）**：
    *   用户进来了，但他知道这玩意儿能干嘛吗？
    *   **必须有**：示例、引导、边界声明（我不能做什么）。
2.  **正在执行（Execution）**：
    *   AI 在思考（转圈），用户能干嘛？傻等吗？
    *   **必须有**：取消按钮、进度反馈、甚至是在生成过程中修正指令的能力。
3.  **结果交付（Delivery）**：
    *   AI 给了一坨字，用户怎么验证对错？错了怎么改？
    *   **必须有**：引用来源、不确定性标记、纠错入口（重试/编辑/降级）。[71]

![图 4-1b：AI 关键时刻地图（首次接触/执行中/结果交付）示意](../../assets/figure_04_1b_ai_moments_map_1766374209852.png)

!!! quote "图 4-1b 生成参数"
    *   **image_prompt**: A three-stage timeline visualization. Stage 1: "Entry", depicted as a door or search bar. Stage 2: "Processing", depicted as a waveform or gears turning. Stage 3: "Result", depicted as a document or card. Under each stage, icons represent user actions (question mark for Entry, pause/stop for Processing, edit/check for Result). Risk points highlighted with abstract warning shapes. Minimalist flat design. No text.
    *   **params**: --ar 3:1 --v 6.0

把这三个时刻填进下面的表，填不出来就别画图：

| 关键时刻 | 系统必须交代什么 | 用户手边必须有什么武器 | 失败了往哪儿跑（恢复） |
| :--- | :--- | :--- | :--- |
| **首次接触** | 我能写代码/画图；但我不会算命 | 点击示例 / 粘贴模板 | 看演示视频 / 回首页 |
| **正在执行** | 正在联网搜索；预计 10 秒 | 取消生成 / 补充条件 | 停止并保留已生成内容 |
| **结果交付** | 这是基于 <文档A> 的回答；置信度低 | 复制 / 只有这一段有用 / 重新生成 | 手动编辑 / 回退到上一步 |

---

### 第一张纸：页面树（IA）—— 先定骨架
不要一上来就画聊天窗口。先画层级。
AI 产品往往页面很少（Chat-first），但**功能节点**很多。

**页面树检查表**：
*   **入口唯一性**：同一个功能，不要让用户在三个地方都能找着，也不要让用户在哪儿都找不着。
*   **层级深度**：核心功能（如“开始对话”）必须在 1 点击之内。
*   **设置与控制**：模型切换、插件开关、Key 管理，这些是 AI 产品的“下水道”，必须画出来，否则合规和风控没法做。

### 第二张纸：用户流（User Flow）—— 强制画出异常
这是本章最硬的约束：**每一条主流程，必须配至少 3 条异常流。**
不要假装异常不存在。

**模板：AI 交互流程表**

| 步骤 | 用户动作 | 系统反馈（Happy Path） | **AI 抽风了（异常流）** | **用户如何自救（恢复）** |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 输入指令 | 解析意图，开始执行 | 提示“涉及敏感词”或“看不懂” | 修改指令 / 查看合规指南 |
| 2 | 等待生成 | 流式吐字，展示进度 | 卡在 99% / 吐字乱码 / 报错 | 点击“重试” / 切换模型 |
| 3 | 结果确认 | 展示结果 + 引用来源 | 产生幻觉 / 引用不存在 | 点击“溯源” / 手动修正 |

### 第三张纸：状态清单（State Matrix）—— 填补真空
原型最好看的时候是有数据的时候。
但用户最恐慌的时候是**没数据（Empty）、坏了（Error）、不让看（Permission）**的时候。
把这些状态当成一级需求来做。[17]

**模板：状态检查清单**

| 页面/组件 | 空状态（Empty） | 加载中（Loading） | 成功（Success） | 失败（Error） | 无权限（No Auth） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 历史记录 | 显示“暂无记录，发起新对话” | 骨架屏占位 | 列表展示 | 显示“加载失败，点击重试” | 隐藏或显示锁图标 |
| 生成区域 | 显示“输入以开始”+ 3个示例 | 动态波纹/打字机效果 | Markdown 渲染 | **保留用户输入** + 红色报错 | N/A |

---

### 走查脚本：用任务代替审美
不要把原型发到群里问“大家觉得怎么样”。大家会告诉你颜色不好看、字体太小——这些都是噪音。
你要做的是**任务走查（Task Walkthrough）**。

找 5 个人（同事、朋友、甚至是你自己过几天再看），给他们一个任务，然后闭嘴，观察。

**走查脚本示例**：

| 任务 ID | 任务描述 | 观察点（Pass/Fail） | 失败判定（断点） |
| :--- | :--- | :--- | :--- |
| T-01 | “请用这个工具写一个贪吃蛇游戏” | 能找到入口吗？知道怎么描述吗？ | 犹豫超过 10 秒 / 乱点菜单 |
| T-02 | “AI 写错了，请让它把蛇改成蓝色” | 能找到纠错/追问入口吗？ | 只能刷新重来 / 找不到对话框 |
| T-03 | “断网了，请找回刚才生成的代码” | 刷新后数据还在吗？ | 数据丢失 / 页面空白 |

![图 4-2：走查记录与断点标注](../../assets/figure_04_2_walkthrough_breakpoints_1766373755019.png)

!!! quote "图 4-2 生成参数"
    *   **image_prompt**: A wireframe screenshot of a chat interface overlayed with red numbered circles (breakpoints). To the right, a sidebar list corresponding to the numbers. Item 1: "User hesitated here". Item 2: "Clicked wrong button". Item 3: "Error message unclear". Red annotations on the wireframe highlight specific UI elements. Technical review style.
    *   **params**: --ar 4:3 --v 6.0

---

## 落地：把反馈变成“断点列表”

走查完，不要只留下一堆“体验不好”的抱怨。要把它们翻译成**断点（Breakpoints）**：
**断点 = 触发条件 + 预期行为 + 实际灾难 + 修复方案**

只有写成这样，工程才能认。

### 示例：断点列表

| 断点 ID | 触发条件 | 实际灾难 | 修复方案（Action Item） | 验收标准 |
| :--- | :--- | :--- | :--- | :--- |
| BP-01 | 首次进入首页 | 屏幕一片白，用户不知道点哪 | 增加“热门 Prompt”示例区 | 用户能在 5 秒内发起第一次对话 |
| BP-02 | 生成代码时断网 | 之前生成的 500 行代码全没了 | 增加本地缓存（LocalStorage） | 断网刷新后，内容可恢复 |
| BP-03 | AI 拒绝回答 | 只显示“Error”，用户以为坏了 | 区分“拒绝”和“故障”，给出拒答理由 | 错误提示明确告知由于安全策略拦截 |

---

## 可执行示例：用脚本验证你的原型完备度

不要肉眼检查。写个脚本来验证你的文档结构是否齐全，断点是否已经记录在案。

**验证脚本：`check_prototype_readiness.py`**

```python
import os
import re

def check_file_exists(path):
    if not os.path.exists(path):
        print(f"[FAIL] Missing file: {path}")
        return False
    return True

def check_content_pattern(path, pattern, min_count, error_msg):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = re.findall(pattern, content, re.MULTILINE)
        if len(matches) < min_count:
            print(f"[FAIL] {path}: {error_msg} (Found {len(matches)}, Need {min_count})")
            return False
        print(f"[PASS] {path}: Found {len(matches)} items matching '{pattern}'")
        return True
    except Exception as e:
        print(f"[ERROR] Could not read {path}: {e}")
        return False

def main():
    print("--- Starting Prototype Gate Check ---")
    all_pass = True
    
    # 1. 检查核心文档是否存在
    required_docs = [
        'docs/prototype/ia.md',
        'docs/prototype/user-flow.md',
        'docs/prototype/state-matrix.md',
        'docs/prototype/breakpoints.md'
    ]
    for doc in required_docs:
        if not check_file_exists(doc):
            all_pass = False

    # 2. 检查断点列表是否包含具体行动项
    # 假设断点格式为 "| BP-xx |"
    if not check_content_pattern(
        'docs/prototype/breakpoints.md', 
        r'\|\s*BP-\d+\s*\|', 
        5, 
        "Need at least 5 logged breakpoints (BP-xx)"
    ):
        all_pass = False

    # 3. 检查用户流是否包含异常流
    # 假设异常流在表格中标记为 "异常" 或 "Exception"
    if not check_content_pattern(
        'docs/prototype/user-flow.md', 
        r'(异常|Exception|Fail)', 
        3, 
        "User flow must document at least 3 exception paths"
    ):
        all_pass = False

    if all_pass:
        print("\n>>> GATE PASSED: Prototype artifacts are structured and ready for review.")
    else:
        print("\n>>> GATE FAILED: Please fix missing artifacts or details.")
        exit(1)

if __name__ == "__main__":
    main()
```

### 进阶：用 AI 帮你找茬（生成边缘案例）

如果你想不出异常流，让 AI 帮你做“红队攻击”。

**命令示例**：
```bash
gemini -m gemini-3-pro-preview -p "我是产品经理。我的功能是'用户上传 PDF，AI 总结全文'。请列出 10 个可能导致失败或体验糟糕的边缘案例（Edge Cases），包括恶意输入、文件问题、模型限制等。输出为 Markdown 表格。" > out/edge_cases.md
```

**预期输出（示例）**：
*   用户上传了加密的 PDF。
*   PDF 全是扫描图片，没有文字层。
*   PDF 超过 500 页，超出 Token 限制。
*   用户上传了 executable 伪装的 PDF。
*   总结结果包含原文中没有的虚假数据（幻觉）。
*   <...>

---

## 交付物清单与验收标准

### 1. 必须有的文件
*   `ia.md`：页面树，明确唯一入口。
*   `user-flow.md`：包含 Happy Path + 至少 3 条异常路径。
*   `state-matrix.md`：核心页面的 5 态（空/载/成/败/禁）。
*   `breakpoints.md`：至少 5 个经过走查发现的断点及修复方案。

### 2. 必须过的门槛（Exit Criteria）
*   **死胡同清零**：没有一个异常状态是“用户无路可退”的（必须有重试、回退或人工介入入口）。
*   **第一眼可用**：空状态必须包含“怎么开始”的引导，不能只是空白。
*   **断点闭环**：所有 BP-xx 开头的问题都有了 Owner 和 Action Item。

## 常见陷阱（Pre-mortem）
1.  **沉迷高保真**：花 3 天调按钮圆角，结果发现流程根本走不通。**修正**：用黑白线框图，禁止上色。
2.  **遗忘“不知情用户”**：自己测得很顺，因为你知道怎么用。**修正**：找个完全不懂项目的人来走查 T-01 任务。
3.  **把报错当借口**：认为“报错了就是系统问题，提示一下就行”。**修正**：报错是产品体验的一部分，必须设计“如何恢复”。

## 下一章
原型跑通了，不仅意味着逻辑通了，更意味着你拿到了第一批“虽然简陋但真实”的用户反馈。下一步，我们要把这些反馈量化，建立指标体系。
下一章见：[05-validation.md](05-validation.md)。

## 参考
详见本书统一参考文献列表：[references.md](references.md)。
