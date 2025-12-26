# 第 16 章：推理优化：延迟、吞吐与成本的三角形
![第 16 章封面](../../assets/chapter_16_header_1766035949233.png)

> **Image Prompt:** abstract 3D visualization of a triangular balance scale, metallic texture, three vertices labeled with glowing nodes (but no text), representing Quality, Latency, and Cost. One corner is being pulled down, causing the others to shift. Dark technical background, blue and orange accent lighting. High contrast, clean lines.
> **Negative Prompt:** text, letters, words, messy wires, cartoon, low resolution, blurry.

> 推理优化的本质不是跑得更快，而是在质量、延迟、成本之间建立可裁决的取舍：你知道为了哪一点牺牲哪一点，并且退化时能回滚。[6][44]

在 AI 产品里，推理是现金流的闸门。它决定了你每一次交互的成本上限，也决定了用户是否愿意把它纳入日常工作流。你可以允许它偶尔不够聪明，但绝不能允许它经常很慢，或者贵到让你破产。[6]

## 章节定位
本章承接后训练，讨论上线推理的优化策略与治理方式。我们不讨论如何从零写一个 CUDA 核函数，而是讨论如何建立基线、如何定位瓶颈、如何用预算与降级守住底线。无论你是自部署模型还是使用 API，这些治理逻辑是通用的。[44]

## 你将收获什么
- **一张推理三角形**：质量/延迟/成本的取舍框架与守门指标。[6]
- **一套优化顺序**：先做最便宜的（Prompt/缓存），再做最昂贵的（引擎/量化），避免盲目上重武器。
- **一份预算与降级策略**：让你在尖峰与退化时有退路，而不是直接挂掉。[6]
- **一个可执行的网关原型**：用 Python 实现最小化的预算控制与并发保护。

## 三层思考：推理优化是一门治理学

### 第 1 层：读者目标
你要获得可预测的体验与成本：用户等待时间可控，账单可解释，服务退化可回滚。

### 第 2 层：论证链条
推理优化的链条是：
**基线与口径** → **瓶颈定位** → **低成本优化**（Prompt/缓存） → **高成本优化**（引擎/硬件） → **预算与降级** → **灰度与回滚**

没有基线与口径，任何优化都是盲人摸象。你必须先知道现在的 P95 是多少，才能谈优化。[6]

### 第 3 层：落地与验收
验收必须包含对比表：
1.  **质量是否达标**（且不退化）；
2.  **P95 延迟是否达标**；
3.  **单次成本是否在预算内**；
4.  **守门指标是否越界**（错误率、超时率）。[6]

## 关键流程：从优化到回滚的闭环

不要指望一次优化就能解决所有问题。这是一个闭环过程：

1.  **写取舍卡**：明确质量、延迟、成本的目标，以及守门指标（如错误率 < 0.1%）。
2.  **建立基线**：用同一批样本、同一个 Prompt、同一个模型版本，跑出当前指标。
3.  **选择优化**：按成本从低到高选择策略（Prompt 裁剪 -> 缓存 -> 并发控制 -> 引擎优化）。
4.  **跑对比表**：对比优化前后的指标。如果守门指标越界（如错误率飙升），直接不发布。
5.  **灰度发布**：小流量验证。如果线上守门指标越界，自动触发降级或回滚。
6.  **回流与迭代**：把超时、高成本、坏体验的样本抓回来，加入回归集。

## 推理三角形：先把取舍写清楚

![图 16-1：质量/延迟/成本三角形与守门指标示意](../../assets/figure_16_1_1765971418977.png)

> **Image Prompt:** isometric diagram of a triangle structure. Three corners represent distinct concepts (visualized as icons: a diamond for quality, a stopwatch for latency, a coin stack for cost). Tension lines connect them. Around the triangle is a dashed circle representing "Guardrails" or "Gatekeepers". Minimalist tech style, white background, precise vector art style.
> **Negative Prompt:** text, labels, messy, sketch, hand-drawn.

文字版推理三角形与守门指标（不依赖图片也能裁决）：

| 你想优化 | 常见动作 | 你必须守住（守门指标） | 常见代价 |
| :--- | :--- | :--- | :--- |
| **质量** | 更强模型、长上下文、多路检索、复杂工具链 | 成本预算、延迟 P95、超时率 | 单次成本飙升，响应变慢 |
| **延迟** | 缩短上下文、减少工具、流式优先、推测采样 | 质量底线、拒答率 | 回答变短、准确率下降、幻觉增加 |
| **成本** | 缓存、摘要、模型降级、量化、便宜后端 | 质量门槛、合规审计 | 智商下降，可能无法处理复杂指令 |

**守门指标**是围住三角形的边：错误率、超时率、拒答率、预算耗尽率。一旦这些指标越界，优化必须停止或回滚。不要在守门指标报警时谈“平均体验变好了”。

### 模板 16-1：推理取舍卡

| 维度 | 填写说明 | 示例 |
| :--- | :--- | :--- |
| **质量目标** | 哪些任务必须 100% 准确？哪些可以模糊？ | 代码生成必须准确，闲聊可以宽容 |
| **延迟目标** | 首字延迟 (TTFT) 和 总延迟 (E2E) 的 P95 线 | TTFT < 1s, E2E P95 < 10s |
| **成本目标** | 单次调用预算，每日总预算 | 单次 < $0.01, 每日 < $50 |
| **守门指标** | 绝对不可逾越的红线 | 错误率 < 0.5%, 超时率 < 1% |
| **回滚策略** | 失败时切回哪个版本？ | 切回 v1.2 Prompt + GPT-3.5 |

## 基线与口径：先回答三件事

在做任何优化之前，先回答三个问题。如果回答不上来，请停止优化，先去装监控。

1.  **用户到底在等什么？**
    *   如果是流式输出，用户在意的是**首字延迟 (TTFT)**。
    *   如果是任务型（如生成报表），用户在意的是**总耗时**和**成功率**。
    *   **口径**：TTFT（从请求到第一个 Token）、E2E Latency（从请求到结束）、TPOT（每个 Token 的生成时间）。[6]

2.  **钱到底花在哪了？**
    *   不要只看总账单。拆开看：输入 Token 多少？输出 Token 多少？工具调用几次？
    *   **口径**：`tokens_in`、`tokens_out`、`tool_calls_count`、`cache_hit_rate`。[6]

3.  **退化到底算什么？**
    *   不仅仅是报错。更慢、更贵、废话更多、工具调用死循环，都叫退化。
    *   **口径**：超时次数、降级触发次数、重试次数、用户取消率。[6]

### 一个可落地的口径清单

| 指标类 | 关键字段 | 说明 |
| :--- | :--- | :--- |
| **延迟** | `ttft_ms`, `e2e_ms`, `queue_ms` | 区分排队时间和生成时间 |
| **量** | `tokens_in`, `tokens_out` | 成本的主要来源 |
| **工具** | `tool_name`, `tool_duration_ms` | 工具往往是延迟大户 |
| **状态** | `status_code`, `finish_reason` | 区分正常结束还是被截断/超时 |
| **复用** | `cache_hit` (bool) | 缓存是最大的省钱手段 |
| **版本** | `model_id`, `prompt_ver` | 归因分析的基础 |

## 优化顺序：先做最便宜的

不要一上来就搞模型量化或换推理引擎。按 ROI 排序，先做容易的。

### 1. 输入与上下文：剪掉废话

很多成本是自己塞进去的。
*   **滑动窗口**：只保留最近 N 轮对话，在这个窗口之前的概括成摘要。
*   **Prompt 瘦身**：去掉只有礼貌作用的废话，合并重复指令。
*   **按需检索**：不要每次都把整个知识库塞进去，判断需要证据时再 RAG。[6]

### 2. 缓存与复用：最大的红利

对于重复性高的问题（如“如何重置密码”），缓存就是 0 延迟、0 成本。
*   **精确匹配**：Key = `hash(prompt + model_version)`。
*   **语义缓存**：用 Embedding 找相似问题（慎用，有误伤风险）。
*   **工具缓存**：如果工具查询的是静态数据（如汇率、天气），必须缓存。[6]

### 3. 并发与降级：保命手段

尖峰时刻，活下来比答得好更重要。
*   **并发限制**：设定最大 Inflight 请求数，超了直接 429 或排队。
*   **降级策略**：队列太长时，自动切换到短 Context 模式，或禁用耗时工具。
*   **熔断**：错误率过高，直接停止服务，避免雪崩。[6]

### 4. 模型与引擎：最后的重武器

只有当前面都做完了，才考虑换模型、做量化、换推理引擎（如 vLLM, TensorRT-LLM）。这些改动工程量大，风险高，必须有完整的回归测试。[44]

## 示例：一个最小化的预算网关

我们提供了一个 Python 实现的最小网关，它不依赖任何重型框架，只做四件事：**预算控制**、**并发限制**、**缓存**、**指标暴露**。

### 1. 代码位置
`docs/examples/inference/budgeted_gateway.py`

### 2. 核心逻辑（伪代码）

```python
def handle_chat(req):
    # 1. 并发检查
    if current_inflight > MAX_CONCURRENCY:
        return 429_Too_Many_Requests

    # 2. 缓存检查
    cache_key = make_key(req.prompt, req.model)
    if cache_key in cache:
        return cache[cache_key]

    # 3. 预算执行
    try:
        with time_limit(req.budget_ms):
            response = model.generate(req.prompt)
    except Timeout:
        # 4. 降级或报错
        return fallback_response()

    # 5. 写入缓存与指标
    cache[cache_key] = response
    record_metrics(latency, tokens, status="success")
    return response
```

### 3. 如何运行

先用 mock 模式跑起来，验证你的限流和缓存逻辑是否生效：

```bash
# 启动网关，使用模拟 Provider
python3 docs/examples/inference/budgeted_gateway.py --provider mock --port 8787
```

发送一个带预算的请求：

```bash
python3 - <<'PY' > /tmp/payload.json
import json
print(json.dumps({
    "user_id": "test_user",
    "prompt": "给我写个快排算法",
    "budget_ms": 500  # 设置一个很紧的预算
}))
PY

curl -X POST http://127.0.0.1:8787/chat \
  -H "Content-Type: application/json" \
  -d @/tmp/payload.json
```

如果你把 `budget_ms` 设得很小，应该能看到超时或降级响应。这就是**可测试的治理**。

### 4. 接入真实模型

你可以用一个外部 CLI 来做后端：

```bash
python3 docs/examples/inference/budgeted_gateway.py \
  --provider cli \
  --cli-cmd <LLM_CLI> \
  --cli-model <MODEL>
```

## 推理引擎选型：把吞吐当工程题

当你的并发上来后，显存管理就是吞吐量。

![图 16-2：推理可控闭环](../../assets/figure_16_2_inference_control_loop.svg)

> **Image Prompt:** flowchart diagram showing a feedback loop. Steps: "Budget Check" -> "Concurrency Gate" -> "Cache Lookup" -> "Inference Engine" -> "Metrics Collector". Arrows flow back from Metrics to Budget/Gate. Modern, clean, tech schematic style.
> **Negative Prompt:** hand-drawn, messy, blurry, text-heavy.

### 常见引擎对比

| 引擎 | 核心优势 | 适用场景 | 代价 |
| :--- | :--- | :--- | :--- |
| **vLLM** | PagedAttention，显存利用率极高 | 高并发、长 Context 场景 | 需要较新的 GPU，部署稍复杂 |
| **TensorRT-LLM** | 极致性能，算子融合 | 确定性极高的生产环境，N卡 | 构建极慢，灵活性差，版本绑定死 |
| **TGI (HuggingFace)** | 开箱即用，功能全 | 快速上线，中小规模 | 性能不是最极致的，但够用 |
| **Llama.cpp** | CPU/Apple Silicon 支持好 | 端侧、低成本部署 | 吞吐量有限，不适合高并发服务 |

## 预算与降级：把止损写成默认行为

不要害怕降级。**降级是系统成熟的标志**。与其让用户在白屏中等待 60 秒然后报错，不如在第 5 秒就告诉他“系统繁忙，请稍后再试”或者给一个简略版的答案。[6]

### 模板 16-2：降级梯度表

| 阶段 | 触发信号 | 执行动作 | 用户感知 |
| :--- | :--- | :--- | :--- |
| **Level 0 (正常)** | P95 < 1s, 错误率 < 0.1% | 全功能开启 | 丝滑 |
| **Level 1 (轻度)** | P95 > 2s | 禁用非核心工具，缩短 Max Tokens | 回答变短，稍微变笨 |
| **Level 2 (中度)** | P95 > 5s 或 显存紧张 | 开启强力缓存，跳过 RAG | 可能拿到旧数据，但能用 |
| **Level 3 (重度)** | 队列爆满 或 错误率 > 5% | 拒绝新请求 (429)，只服务 VIP | "系统繁忙" |
| **熔断** | 下游服务挂死 | 直接返回静态兜底文案 | "服务维护中" |

## 复现检查清单

- [ ] **取舍卡已填**：明确了质量、延迟、成本的红线。[6]
- [ ] **基线已测**：知道当前的 P95 和单位成本。[6]
- [ ] **网关已立**：至少有一层代码能拦截请求、记录指标、控制并发。[6]
- [ ] **降级可测**：手动触发降级阈值（如调低预算），系统能按预期降级，而不是崩溃。[6]
- [ ] **回归集完备**：优化后跑一遍回归集，确保没有为了速度牺牲太多质量。

## 常见陷阱（避坑指南）

1.  **只看平均值，不看 P95**：平均延迟 500ms 看起来很美，但 P95 可能是 10s。用户只会记得那次卡了 10s 的体验。**永远看长尾**。
2.  **为了省钱疯狂量化**：量化（如 4-bit）确实省显存，但可能导致模型变笨。一定要在**回归集**上验证质量退化。[48][59]
3.  **缓存不分租户**：把 A 用户的私人数据缓存了，B 用户问的时候直接吐出来。**这是安全事故**。缓存 Key 必须包含 `tenant_id` 或 `user_id`。[6]
4.  **没有预算上限**：一个死循环的 Prompt（比如让模型无限续写）能把你的 Token 预算跑光。必须设置 `max_tokens` 和 `timeout`。[6]

## 交付物清单与验收标准
- **推理取舍卡**：包含具体的数字指标。
- **基线报告**：优化前的性能快照。
- **降级策略代码**：在网关或业务逻辑中实现的降级分支。
- **压测报告**：证明在高并发下系统会降级而不是崩溃。

## 下一章
系统跑起来了，如何把它安全地发布到线上，并持续监控它的健康状态？
请阅读 [第 17 章：部署与运维：灰度、回滚与观测](17-deployment.md)。

## 参考
详见 [references.md](references.md)。
