# 第 10 章（Agent 深入）：让模型在边界内会做事
![第 10 章封面（Agent 深入）](../../assets/chapter_10_header_1766035645245.png)

> Agent 的核心不是让模型更勤奋，而是划定行动边界：能做什么、何时停止、如何回滚。越权与不可追溯，是 Agent 系统的原罪。[29][6]

Agent 失败的主因往往不是模型能力不足，而是系统设计失控：工具任意调用、参数缺乏校验、预算无上限、失败无熔断。这种系统看似智能，实则是自动化事故制造机。

## 章节定位
本章聚焦 Agent 的行动闭环与风控：工具白名单、权限边界、预算熔断、审计与回滚，以及如何将这些约束写入评测门禁。这是构建通用 Agent 骨架的核心。[29]

## 你将收获什么
- **Agent 最小骨架**：任务定义 → 状态机 → 工具边界 → 停止条件 → 审计落盘。
- **工具合同模板**：明确定义每个工具的输入、输出、权限、副作用与预算。
- **回归门禁机制**：将越权、注入、死循环、成本失控拦截在上线前。[6][29]

![图 10-3：Agent 骨架（状态机 + 工具合同 + 预算/审计/回滚）示意](../../assets/figure_10_3_1765971191769.png)

## 关键流程图（纯文本）：一次任务的可控行动闭环

```text
用户请求（不可信输入）
  ↓
任务边界判定
  - 不需要行动：直接答复（带证据/拒答）
  - 需要行动：进入状态机
  ↓
状态机循环（每一步都可审计/可停止）
  1) 收集信息（追问/澄清）
  2) 计划（列步骤 + 标注所需工具）
  3) 执行（工具调用只能走“闸门”）
      validate_tool_call:
        - allowlist 检查（工具名）
        - schema 校验（必填/格式/白名单/长度/范围）
        - 权限校验（user/tenant/resource）
        - 预算校验（调用次数/成本/时间）
      - 失败：aborted_reason 记录 → 停止/降级/请求确认
      - 成功：写审计字段 → 更新状态 → 继续下一步
  4) 总结（解释 + 证据 + 下一步）
  ↓
副作用治理
  - 任何写操作：必须有补偿/回滚（同 action_id 可追溯）
  - 退化/事故：回滚 → 留证据 → 失败样本入回归 → 阻断发布
```

## 示例（可复制）：工具闸门 + 最小回归样本（越权/预算）

**目标：** 为“有副作用”的工具建立统一闸门，并将越权与预算越界固化为阻断级回归样本。

**前置条件：**
- Python 3 环境

**步骤：**
1. 运行验证脚本：确保 1 条合法调用通过，2 条非法调用（越权/格式错误）被拒绝。
```bash
python3 - <<'PY'
from __future__ import annotations

class Reject(Exception):
    pass

def validate_tool_call(call: dict, actor: dict, budget: dict, contracts: dict) -> None:
    tool = call.get("tool")
    if tool not in contracts:
        raise Reject("tool_not_allowlisted")

    contract = contracts[tool]
    required_role = contract["permission_scope"]["role"]
    if required_role not in actor.get("roles", []):
        raise Reject("rbac_denied")

    if call.get("tenant_id") != actor.get("tenant_id"):
        raise Reject("tenant_mismatch")

    amount_cents = int(call.get("amount_cents", -1))
    if not (1 <= amount_cents <= contract["input_validation"]["amount_cents_max"]):
        raise Reject("amount_out_of_range")

    if call.get("currency") not in contract["input_validation"]["allowed_currencies"]:
        raise Reject("currency_not_allowed")

    customer_id = str(call.get("customer_id", ""))
    if not (1 <= len(customer_id) <= contract["input_validation"]["customer_id_max_len"]):
        raise Reject("customer_id_invalid")

    if budget["calls_used"] + 1 > budget["max_calls_per_task"]:
        raise Reject("budget_calls_exceeded")

def must_pass(case: dict) -> None:
    try:
        validate_tool_call(case["call"], case["actor"], case["budget"], case["contracts"])
    except Reject as e:
        raise SystemExit(f"UNEXPECTED REJECT: {e}")

def must_reject(case: dict, expect: str) -> None:
    try:
        validate_tool_call(case["call"], case["actor"], case["budget"], case["contracts"])
        raise SystemExit("UNEXPECTED PASS")
    except Reject as e:
        if str(e) != expect:
            raise SystemExit(f"WRONG REJECT: got={e} expect={expect}")

contracts = {
    "create_invoice": {
        "permission_scope": {"role": "billing_admin"},
        "input_validation": {
            "allowed_currencies": ["CNY", "USD"],
            "amount_cents_max": 5_000_000,
            "customer_id_max_len": 64,
        },
    }
}
actor_ok = {"tenant_id": "t_001", "roles": ["billing_admin"]}
budget_ok = {"calls_used": 0, "max_calls_per_task": 1}

case_ok = {
    "contracts": contracts,
    "actor": actor_ok,
    "budget": budget_ok,
    "call": {
        "tool": "create_invoice",
        "tenant_id": "t_001",
        "currency": "CNY",
        "amount_cents": 1200,
        "customer_id": "c_123",
    },
}
must_pass(case_ok)

case_unauthorized_tenant = {**case_ok, "call": {**case_ok["call"], "tenant_id": "t_999"}}
must_reject(case_unauthorized_tenant, "tenant_mismatch")

case_budget_exceeded = {**case_ok, "budget": {"calls_used": 1, "max_calls_per_task": 1}}
must_reject(case_budget_exceeded, "budget_calls_exceeded")

print("ok")
PY
```
2. **迁移逻辑**：将 `validate_tool_call` 集成至统一工具入口，确保拒绝原因写入审计字段（如 `aborted_reason`）。
3. **固化样本**：将 `tenant_mismatch`（越权）、`schema_invalid`（非法输入）、`budget_exceeded`（成本/次数越界）加入回归集，命中即阻断发布。

**验证命令：**
- 脚本输出 `ok` 且退出码为 0；工程回归任务稳定通过。

**失败判定：**
- 非法用例被放行（`UNEXPECTED PASS`），或拒绝原因不一致（`WRONG REJECT`）。

**回滚：**
- 立即禁用问题工具或回滚至稳定版本；将触发事故的输入写入阻断级样本，复跑通过后方可解禁。

## 三层思考：Agent 的关键矛盾
### 第 1 层：读者目标
交付可托付的行动者：不仅能完成任务，更知晓边界（不该做什么）、止损（做不下去怎么办）与回滚（做错了怎么撤回）。

### 第 2 层：论证链条
Agent 的可控链条：
任务边界 → 工具合同 → 状态机与停止条件 → 零信任输入处理 → 审计与回滚 → 评测回归。
缺乏工具合同与停止条件，系统将陷入不可预测的漂移。[29][6]

### 第 3 层：落地与验收
- **工具合规**：调用严守白名单与权限；越权即阻断。[29]
- **预算熔断**：具备成本/步数上限；死循环或过度调用即失败。[6]
- **操作可逆**：关键行动可追溯、可撤回；不可回滚则不予自动化。

## 第一步：先问真的需要 Agent 吗
**需求甄别**：
- 用户仅需答案 → RAG。
- 系统必须执行连续动作 → Agent。
优先优化产品流程（拆解任务、规范输入）与后端接口，而非依赖模型“自我发挥”。[6]

## 第二步：写工具合同（工具是风险源，不是能力源）
将每个工具视为有副作用的外部系统，合同需明确：
- **边界**：做什么、不做什么。
- **权限**：所需最小权限与范围。
- **I/O**：输入输出结构与校验。
- **熔断**：预算上限与停止条件。
- **回滚**：副作用的撤回/补偿机制。[29]

### 工具合同（工具白名单）

| 字段 | 说明 |
| --- | --- |
| 工具名 | 唯一标识 |
| 目的 | 用途简述 |
| 允许动作 | 最小化操作（读/写/删/支付） |
| 权限范围 | 用户/租户/资源级隔离 |
| 输入校验 | 必填项、格式、长度、白名单 |
| 输出语义 | 成功/失败原因，重试标识 |
| 预算与停止 | 最大次数/成本/超时阈值 |
| 副作用 | 变更范围；撤回/补偿策略 |
| 审计字段 | 追责所需信息 |

下述代码展示了一个最小工具合同实现，包含输入校验与权限边界：

```text
tool: create_invoice
purpose: 为某租户创建一张草稿账单（只允许草稿）
allowed_actions: write
permission_scope:
  tenant_id: 必须等于当前会话 tenant_id
  role: billing_admin
input_validation:
  currency: 仅允许 CNY/USD
  amount_cents: 1..5000000
  customer_id: 必填，长度<=64
budget:
  max_calls_per_task: 1
  timeout_ms: 3000
side_effect:
  writes: invoices(draft)
  rollback: delete_draft_invoice（同 action_id）
audit_fields:
  action_id, request_id, user_id, tenant_id, tool, params_hash, result, latency_ms
```

## 第三步：做一个可解释的状态机
Agent 不应是黑盒，应设计为显式状态机：明确每一步的输入、输出与流转条件。

### Agent 状态机（最小可控版）

| 状态 | 进入条件 | 行为 | 成功退出 | 失败退出（必须有） |
| --- | --- | --- | --- | --- |
| 收集信息 | 信息缺失 | 追问/补齐 | 信息完备 | 超时/拒答 |
| 计划 | 任务明确 | 生成步骤 | 计划可行 | 计划含越权动作 |
| 执行 | 计划确认 | 调用工具 | 结果返回 | 工具失败/预算越界 |
| 总结 | 执行完毕 | 解释+证据+后续 | 交付完成 | 不确定则追问 |

**审计日志**：状态流转必须留痕，记录原因、预算消耗与关键输入。

| 字段 | 作用 |
| --- | --- |
| action_id / trace_id | 全链路追踪 |
| state | 当前状态 |
| event | enter/exit/fail |
| reason | 流转/失败原因 |
| tool | 调用的工具名 |
| budget_remaining | 剩余预算（步数/成本/时间） |

## 第四步：预算与停止条件（防止勤奋导致破产）
Agent 最危险的缺陷是“过度勤奋”：反复思考、检索或调用工具。必须设立硬性止损：
- **步数/次数上限**：防止死循环。
- **成本/时间上限**：控制资源消耗。
- **熔断机制**：触达阈值强制停止，并输出下一步建议。[6]

### 预算与停止条件

| 维度 | 阈值 | 触发动作 |
| --- | --- | --- |
| 工具调用次数 | ≤ N | 停止并解释 |
| 总成本 | ≤ X | 降级/确认/停止 |
| 总时长 | ≤ T | 返回中间结果 + 建议 |
| 连续失败 | ≤ M | 切换策略或停止 |

## 第五步：审计与回滚（让自动化可追责）
每一次行动必须可追溯：谁触发、对象是谁、操作内容、结果、参数。
涉及副作用（写/删/支付）的操作，必须设计撤回/补偿机制（Compensating Transaction）。[29]

**审计最低原则**：
- 工具调用全记录（输入/输出/结果/原因）。
- 关键资源操作记录权限上下文。
- 敏感操作（计费/删除/提权）需强审计与强回滚策略，必要时引入人工确认。[6]

## 安全：把输入当作不可信，把工具当作高风险
Agent 两大风险：
- **输入注入**：诱导越权或泄露。
- **工具滥用**：参数注入导致越界访问。[29]

**防护策略**：
- **代码层校验**：在工具入口实施权限与 Schema 校验，严禁仅依赖 Prompt 约束。
- **阻断记录**：越权尝试必须阻断、记录并告警，纳入回归集。[6][29]

```text
validate_tool_call(tool, params, actor, budget):
  if tool not in allowlist: reject
  if not schema_validate(params, tool.input_schema): reject
  if not rbac_allow(actor, tool, params): reject
  if budget_exceeded(budget): reject
  return ok
```

## 评测与回归：Agent 的门禁比 RAG 更硬
Agent 评测核心在于安全性与可控性：
- **越权率**：必须为 0。
- **预算越界率**：严控在阈值内。
- **可回滚率**：关键副作用必须可撤回。
- **失败恢复**：异常时能否安全停止并建议。[6]

**监控指标**：`steps_used`, `tool_calls`, `token_cost`, `latency_ms`, `aborted_reason`。越界与阻断应触发告警。

## 复现检查清单（本章最低门槛）
- [ ] **工具合同**：权限、输入校验、预算、副作用、审计、回滚定义完备。[29]
- [ ] **状态机观测**：死循环、越界、失败能被拦截并记录 `aborted_reason`。[6]
- [ ] **回归门禁**：越权、注入、预算越界样本纳入回归，命中即阻断发布。[6][29]
- [ ] **变更对比**：监控越权率、预算越界率、任务成功率，退化即回滚。[6]

## 常见陷阱（失败样本）
1.  **危险操作不可解释**
    *   **根因**：安全约束仅写在 Prompt 中，缺乏工具层物理闸门。[29]
    *   **复现**：绕过前端/Prompt，直接构造越权参数调用工具。
    *   **修复**：实施统一工具闸门（Allowlist + Schema + RBAC + Budget）。[29][6]
    *   **门禁**：非法调用必被拒绝，审计日志详尽。

2.  **成本失控与死循环**
    *   **根因**：缺乏预算与硬性停止条件。[6]
    *   **复现**：输入开放式任务，观察工具调用与时长是否无限增长。
    *   **修复**：设定任务级预算（步数/成本/时间），触达阈值强制熔断并解释。[6]
    *   **门禁**：最坏情况下的资源消耗在阈值内。

3.  **事故无法复盘**
    *   **根因**：缺乏结构化审计字段，状态与参数不可追溯。[29]
    *   **复现**：发生错误后，无法凭日志还原“谁、为何、如何”操作。
    *   **修复**：补全 `trace_id`, `state`, `tool_params`, `result` 等审计字段，支持链路重放。
    *   **门禁**：随机抽样任务可完整还原执行轨迹。

4.  **回滚失效**
    *   **根因**：无补偿机制，或缺乏 `action_id` 导致无法精准撤回。
    *   **复现**：执行写操作失败或重试时，出现重复扣费或数据不一致。
    *   **修复**：引入幂等键与补偿事务，遵循“先草稿、后确认”模式。
    *   **门禁**：故障注入下副作用不重复，回滚后状态一致。

## 交付物清单与验收标准
- **工具合同库**：覆盖至少 5 个关键工具，包含完整元数据。[29]
- **状态机文档**：明确流转逻辑、停止条件与降级策略。[6]
- **阻断级回归集**：包含越权、注入、预算越界样本，100% 拦截。[6][29]

## 下一章
Agent 解决了行动能力，接下来必须夯实地基：身份与权限。这是所有边界与审计的基石。下一章见：[11-user.md](11-user.md)。

## 参考
详见本书统一参考文献列表：[references.md](references.md)。
