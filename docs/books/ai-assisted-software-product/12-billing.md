# 第 12 章：付费模块：订阅、计费与风控
![第 12 章封面](../../assets/chapter_12_header_1766035684589.png)

> 计费系统不是“接个支付接口”，而是一份不可抵赖的工程合同：谁在何时用掉了什么、应付多少、为什么这么算、出错如何纠正。做对了，它让你能增长；做错了，它让你背锅。

AI 产品的计费比传统 SaaS 凶险得多：成本与质量强耦合（Token 越贵效果越好）、调用次数随交互波动（用户多聊几句成本就翻倍）、异常峰值容易把利润瞬间吃光（死循环调用）。因此，**风控与止损不是运营补丁，而是计费系统的第一属性**。

如果你接入银行卡支付，第一原则是**让敏感卡数据（PAN）永远别碰你的服务器**。把支付与卡信息全权交给 Stripe/Paddle 等服务商，你只处理“订单状态、订阅权益、用量事件”和“Webhook 回调”。把 PCI 合规范围压到最小，别给自己找麻烦。

但请别自欺欺人：付费合规不是只有 PCI。你的系统里依然存着敏感数据：用户身份、账单明细（含用量摘要）、税务归属。0→1 阶段你不需要造全套税务引擎，但必须把**结构**预留出来：币种、税率版本、不可变账单号、数据留存策略。否则，出海第一天你就会在 GDPR 和税务审计里翻车。

## 章节定位
本章承接“用户与权限”，把商业闭环落到代码层面：定价模型、计量口径、账本与对账、异常处理与风控。它的目标不是让你马上做出复杂的阶梯定价，而是让你从第一天起就能**算清账、能对账、能回滚**。

## 你将收获什么
*   **选择框架**：订阅、用量计费、混合计费的三种模型与避坑指南。
*   **最小闭环**：一套“计量口径 → 账本 → 对账”的工程实现，保证可重放、可纠错。
*   **止损防线**：在异常用量、退款风暴、成本尖峰击穿利润前的最后一道闸门。

---

## 三层思考：计费是系统的事实
### 第 1 层：读者目标
你要交付的是一套让自己睡得着的系统：收费逻辑可解释、账目历史可重放、异常情况可自动止损。

### 第 2 层：论证链条
计费系统的核心链条是单向且不可逆的：

**定价策略** → **计量口径**（数什么）→ **账本记录**（只增不改）→ **对账与结算**（核对一致性）→ **风控与止损**（熔断机制）→ **审计与回滚**（纠错）

只要你缺了“不可变账本”和“自动化对账”，你迟早会在用户投诉和退款争议中崩溃。

### 第 3 层：落地与验收
验收标准不是“能扣款”，而是：
1.  **幂等性**：同一笔用量（重试、回调）绝不会重复计费。
2.  **可解释性**：任何账单金额都能回溯到具体的计量事件。
3.  **安全性**：成本或风险越界时，系统能自动止血（限流、降级、暂停）。

![图 12-1：计费闭环示意](../../assets/figure_12_1_1765971267577.png)

!!! tip "图表生成提示"
    **Image Prompt:** A technical diagram showing the data flow of a billing system.
    **Key Nodes:**
    1.  **Metering Gateway** (Input): Receives raw usage events.
    2.  **Dedup/Idempotency** (Process): Filters duplicate requests.
    3.  **Immutable Ledger** (Storage): Stack of blocks, append-only.
    4.  **Reconciliation Engine** (Check): Compares Ledger vs. Payment Gateway.
    5.  **Risk Control** (Guard): A circuit breaker switch monitoring the flow.
    **Style:** High-contrast line art, engineering schematic style, no text inside shapes.
    **Caption:** 计费闭环：从计量到对账的单向数据流。

---

## 关键流程图（纯文本）：计费闭环
别画复杂的泳道图，直接把每个环节的“输入/输出/不变量”写死。这才是能写进代码的规范。

| 环节 | 输入 (Input) | 产出 (Output) | 关键不变量 (Invariant) |
| :--- | :--- | :--- | :--- |
| **定价与承诺** | Plan ID, Price Version | 权益包、限制规则 | 规则必须**版本化**，旧订单锁定旧版本 |
| **计量 (Metering)** | Request ID, Usage Data | Metering Event | **幂等 Key** 必须存在，防止重放 |
| **入账 (Ledger)** | Metering Event | Ledger Entry | **不可变 (Append-only)**，只能冲正，不能修改 |
| **汇总 (Rollup)** | Ledger Entries | Usage Rollup | **可重放**，任意时间重算结果一致 |
| **出账 (Invoicing)** | Rollup, Tax Rules | Invoice/Statement | **快照化**，币种与税率在生成瞬间锁定 |
| **收款/退款** | Invoice | Payment/Refund | 状态机流转，每一笔变动都有日志 |
| **对账 (Recon)** | Payment + Ledger | 差异清单 (Diff) | 每一分钱的差异都必须有解释（证据） |
| **争议与纠错** | User Dispute | Reversal/Credit Note | **不改历史**，通过追加负向条目修正 |
| **止损 (Stop-Loss)**| Cost Metrics | Throttle/Pause | 先止血（阻断），再复盘 |

---

## 示例（可复制）：不可变账本 + 冲正验证

**目标**：用一段脚本验证三个核心原则：计量事件幂等、账本只追加（Append-only）、纠错只能用冲正（Reversal）。

**前置条件**：Python 3 环境。

**步骤**：
1.  复制并运行以下脚本。它模拟了：一条正常用量入账 → 重复事件被自动丢弃 → 发现错误后发起冲正。

```python
import hashlib
import json

def calculate_hash(event: dict) -> str:
    """简单模拟：基于内容生成唯一指纹，实际应使用 RequestID"""
    return hashlib.md5(json.dumps(event, sort_keys=True).encode()).hexdigest()

def append_ledger(ledger: list[dict], event: dict, idempotency_keys: set[str]) -> str:
    # 1. 幂等性检查
    key = event.get("idempotency_key")
    if not key:
        raise ValueError("Event missing idempotency_key")
    
    if key in idempotency_keys:
        return "IGNORED_DUPLICATE"

    # 2. 写入账本 (Append Only)
    ledger.append(event)
    idempotency_keys.add(key)
    return "APPENDED"

def get_balance(ledger: list[dict]) -> int:
    return sum(int(e["amount_cents"]) for e in ledger)

# --- 测试环境 ---
ledger_store = []
processed_keys = set()

# 1. 正常入账：消耗 120 分
usage_evt = {
    "idempotency_key": "req_ABC123:metering_v1",
    "type": "usage",
    "amount_cents": 120,
    "user_id": "u_001"
}
status1 = append_ledger(ledger_store, usage_evt, processed_keys)
print(f"Event 1: {status1}")

# 2. 重复入账（模拟重试）：应被忽略
status2 = append_ledger(ledger_store, usage_evt, processed_keys)
print(f"Event 2 (Duplicate): {status2}")

# 3. 冲正（纠错）：发现多记了，追加一笔负数
reversal_evt = {
    "idempotency_key": "req_ABC123:reversal_01", # 新的唯一 ID
    "type": "reversal",
    "amount_cents": -120,
    "ref_event": "req_ABC123:metering_v1",
    "reason": "billing_error"
}
status3 = append_ledger(ledger_store, reversal_evt, processed_keys)
print(f"Event 3 (Reversal): {status3}")

# --- 验证 ---
assert len(ledger_store) == 2, "账本应该只有两条记录（原记录 + 冲正记录）"
assert get_balance(ledger_store) == 0, "余额应该归零"
print("\n✅ 验证通过：幂等性生效，冲正逻辑正确。")
```

**工程落地要求**：
*   **Idempotency Key**：建议格式 `request_id + action_type`（如 `req_123:deduct_token`）。
*   **Reversal**：冲正必须是单独的事件类型，**严禁**直接修改数据库里的旧行。
*   **Regression**：把“重复回调”和“冲正后重算”加入你的 CI/CD 自动化测试。

---

## 先做选择：你卖的到底是什么
AI 产品的定价模型决定了你的架构复杂度。

| 模型 | 适合场景 | 致命坑点 | 0→1 建议 |
| :--- | :--- | :--- | :--- |
| **订阅制 (Subscription)** | 工具类、价值稳定的服务 | **亏本风险**：用户 24 小时跑脚本调用你的 API，Token 成本瞬间击穿订阅费。 | **必须加额度上限 (Quota)**。不要做无限量的 "All You Can Eat"。 |
| **用量计费 (Pay-as-you-go)** | API 服务、基础设施、成本波动大的模型 | **劝退用户**：用户不知道聊一小时要花多少钱，不敢充值。 | 提供**预算护栏**和**实时估算**。 |
| **混合制 (Hybrid)** | 大多数成熟 AI SaaS | **规则爆炸**：订阅送额度 + 超额按量 + 席位费，导致账单像天书。 | **先做可解释性**，再加复杂度。 |

**定价页设计原则**：不要让用户做数学题。
*   ❌ "每 1k Token $0.03"（用户没概念）
*   ✅ "基础版：$20/月，包含 500 次对话。超出后 $0.01/次。适合个人开发者。"

---

## 计量口径：先写怎么数，再写多少钱
AI 产品的计量很容易扯皮：模型生成了一半断网了算不算钱？RAG 检索了 10 次但没找到答案算不算钱？

**通用原则**：凡是消耗了你算力的，都应该计费（除非是系统故障）。但在产品层面，你可以选择“豁免”来提升体验。

### AI 核心计量表（建议直接写入代码枚举）

| 计量单位 | 典型场景 | 争议边界 (Edge Case) | 建议口径 (Policy) |
| :--- | :--- | :--- | :--- |
| **Token In/Out** | LLM 对话 | 流式输出中断 (Stream Interruption) | **计费**。已生成的 Token 已消耗 GPU 资源。除非是 500 错误。 |
| **Request Count** | 简单 API | 参数错误 (400) / 鉴权失败 (401) | **免费**。未进入核心逻辑，不计费。 |
| **Tool Calls** | Agent 联网/画图 | 工具调用失败 / 结果为空 | **计费**。调用外部 API 或算力已发生。除非是你系统 Bug。 |
| **Storage (Vector)** | 知识库索引 | 重复上传同一文件 | **去重后计费**。按实际存储/处理量计算。 |
| **Model Load** | 专属微调模型 | 模型加载耗时 (Cold Start) | **通常免费**，或者是包含在“独占实例费”中。 |

**关键实现**：
在你的代码里，必须有一个 `BillingGateway` 或 `MeteringService`，所有的 Model/Tool 调用结束后，必须异步发送一个 `MeteringEvent`。
*   **不要**在主线程里同步等记账，会拖慢响应。
*   **一定要**确保事件不丢失（使用可靠的消息队列或发件箱模式）。

---

## 账本：把事实写成不可变记录
账本（Ledger）是你的法律底气。当用户问“为什么收我 50 块钱”时，你必须能拿出一行行不可修改的记录。

### 账本事件结构 (Schema)

```json
{
  "ledger_event_id": "lev_890XYZ",        // 全局唯一 ID
  "trace_id": "trace_abc123",             // 关联的技术链路
  "user_id": "u_007",
  "account_id": "acc_999",
  "timestamp": "2025-12-24T10:00:00Z",
  "action_type": "llm_completion",        // 业务语义
  "model_id": "gpt-4-turbo",
  "usage": {
    "input_tokens": 500,
    "output_tokens": 120
  },
  "cost_cents": 350,                      // 金额（建议用整数，分/厘）
  "currency": "USD",
  "price_snapshot_id": "plan_v2_2025",    // 关键！记录当时是按哪个价格算的
  "status": "committed"                   // committed | reverted
}
```

### 冲正与补记：如何优雅地认错
当发现算错了（比如价格配置错误），**绝对不要 SQL Update** 去改那条记录。

正确做法：
1.  **冲正 (Reversal)**：插入一条一模一样但金额为负的记录，标记 `ref_event_id` 指向原记录。
2.  **补记 (Correction)**：插入一条正确的新记录。
3.  **结果**：`SUM(原记录, 冲正, 补记)` = 正确金额。且历史痕迹完整保留。

---

## 对账：工程的自救
对账（Reconciliation）不是财务的事，是工程师的事。它是你发现 Bug（漏记、重记、价格配错）的唯一手段。

**0→1 最小对账清单**：
*   **每日汇总 (Daily Aggregation)**：
    *   `SUM(DB 里的计量记录)` vs `SUM(Stripe/支付网关的订单)`
    *   误差容忍度：**0**。哪怕差 1 分钱也是 Bug。
*   **抽样复核 (Spot Check)**：
    *   随机抽取 5 个 Request ID，手动按当前价格算一遍，看跟账本里记的是否一样。
*   **异常监控**：
    *   如果在 1 分钟内产生了超过 $100 的消耗（除非是企业大户），立刻报警。

---

## 出账与税务：别自己造轮子
*   **发票 (Invoice)**：交给支付服务商（Stripe Invoice, Paddle）。不要自己写 PDF 生成器，维护成本极高。
*   **税务 (Tax)**：SaaS 税务极为复杂（不同国家、不同州税率不同）。务必使用服务商的自动税务功能（Tax Jar, Stripe Tax）。
    *   **自建的坑**：你需要维护全球 200+ 地区的税率表，并且每个月更新。这是自杀。
*   **快照 (Snapshot)**：出账单的那一刻，把用户的地址、税号、当时的汇率**快照**下来。因为用户下个月可能会搬家，不能改历史账单的地址。

---

## 风控与止损：把“越用越亏”关掉
计费风控的本质是**熔断器**。

### 推荐的止损阈值 (Thresholds)

| 场景 | 监控指标 | 推荐阈值 (0→1 阶段) | 触发动作 |
| :--- | :--- | :--- | :--- |
| **单用户异常** | 每日消耗金额 | > 历史均值 × 3 或 > $50 (硬顶) | **暂停服务** + 发邮件确认 |
| **API Key 泄露** | 调用频率 (QPS) | > 5 QPS (非企业用户) | **限流 (429)** |
| **死循环调用** | 连续错误率 | 1 分钟内 100% 失败且高频重试 | **临时封禁 IP/Key** |
| **全局破产** | 平台总 Token 消耗 | > 预设每日预算 (如 $500) | **告警 S0** (给老板发短信) |

**实现方式**：
在网关层（Gateway）或鉴权层（Auth），每次请求前检查 Redis 里的计数器。如果超限，直接拒掉，**不进入模型调用环节**。

详细的事故处理手册见：[E-runbooks.md](E-runbooks.md) (RB-08 计费异常)。

---

## 交付物清单
1.  **定价页文案**：明确单位、价格、豁免规则。
2.  **计量代码**：含 `idempotency_key` 的埋点。
3.  **账本表结构**：支持 append-only 和 reversal。
4.  **对账脚本**：每日运行，差异报警。
5.  **风控配置**：Redis 里的限流阈值和熔断开关。

## 下一章
钱算清楚了，接下来是数据的战争。如何把用户在使用中产生的数据变成你的资产，而不是隐私地雷？
见：[13-data.md](13-data.md)。
