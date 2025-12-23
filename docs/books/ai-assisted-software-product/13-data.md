# 第 13 章：数据收集与清洗：从语料到可训练数据集
![第 13 章封面](../../assets/chapter_13_header_1766035711036.png)

> 数据不是原材料，而是你的产品资产：它决定你能训练什么、能评测什么、能否合规上线，以及你能否在同一问题上持续变强。[34]

在 AI 产品里，数据有两张脸：一张是面向用户的事实（他们的输入、反馈、失败样本），另一张是面向系统的燃料（训练集、评测集、检索语料）。做得好，你积累的是护城河；做得坏，你积累的是风险与偏差。

## 章节定位
本章连接产品与系统到训练与评测。你会把零散的语料与日志，整理成可复用的数据资产：有范围、有许可、有字段、有清洗报告、有版本、有回滚。这样你才能在后续训练、RAG、评测与治理里建立同一个事实源。[34][35]

## 你将收获什么
- 一套数据资产化流程：范围 → 许可 → 采集 → 清洗 → 标注 → 版本化 → 评测回归。[34]
- 三个可复用模板：数据卡（Datasheet）、标注指南、清洗报告（含阈值与例外）。[34]
- 一条底线：先合规后增长；先可追溯后训练。[35]

## 三层思考：数据工作的价值不在量，在可用
### 第 1 层：读者目标
你要交付的是可训练、可评测、可治理的数据集：别人（或未来的你）能理解它、复现它、质疑它、回滚它。

### 第 2 层：论证链条
数据变成资产的链条是：

数据边界与许可 → 字段与口径 → 清洗与过滤 → 标注与一致性 → 版本化与审计 → 回归与迭代

缺许可与边界，后面都是风险；缺版本化与审计，后面都是不可复现。[34][35]

### 第 3 层：落地与验收
验收不靠我收集了很多，而靠：
- 你能解释数据从哪里来、能不能用、能用到什么范围；
- 你能给出清洗报告与例外（为什么删、为什么留）；
- 你能复跑一遍处理流程并得到同级别结论（趋势一致）。[34]

![图 13-1：数据资产化流水线（边界→清洗→标注→版本→回归）示意](../../assets/figure_13_1_1765971297073.png)

## 关键流程图（纯文本）：数据资产化流水线（边界→清洗→标注→快照→回归）
不依赖图片也能执行：把每个阶段的输入/输出与最低门禁写清楚，你才能做审计、做回滚、做复跑。

| 阶段 | 输入 | 输出 | 质量门禁（最低要求） |
| --- | --- | --- | --- |
| 边界与许可 | 数据卡草稿 | 可用范围声明 | 许可明确、目的明确、留存明确 |
| 采集 | 产品埋点、日志、工单 | 原始区 raw | schema 固定、可追溯到来源 |
| 清洗与脱敏 | raw | 清洗版 cleaned | 去重率、PII 扫描、例外清单 |
| 标注与一致性 | cleaned | 标注版 labeled | 抽检、仲裁、IAA 指标 |
| 版本化与审计 | labeled | 快照 snapshot | 数据指纹、处理配置、可回滚 |
| 回归与迭代 | snapshot | 评测报告 | 指标达标才进入训练或索引 |

## 示例（可复制）：一份最小清洗报告 + 快照 manifest（可回滚）

**目标：** 用 1 个最小脚本把“清洗不是随便删”落成可复跑证据：输入/规则/例外/输出统计 + 快照指纹。

**前置条件：**
- Python 3 可用

**步骤：**
1. 复制并运行下面脚本：它会生成一份 `raw` 样本，按 `pii=true` 规则过滤，输出 `cleaned`、`cleaning_report.md` 与 `manifest.json`。
```bash
python3 - <<'PY'
from __future__ import annotations

import hashlib
import json
from pathlib import Path

root = Path("tmp/data-snapshot-demo")
raw_path = root / "raw" / "sample.jsonl"
cleaned_path = root / "cleaned" / "sample.cleaned.jsonl"
report_path = root / "cleaning_report.md"
manifest_path = root / "manifest.json"

root.mkdir(parents=True, exist_ok=True)
raw_path.parent.mkdir(parents=True, exist_ok=True)
cleaned_path.parent.mkdir(parents=True, exist_ok=True)

raw_samples = [
    {"id": "s_001", "text": "为什么我被扣费了？", "pii": False},
    {"id": "s_002", "text": "我的邮箱是 a@example.com，帮我改密码", "pii": True},
    {"id": "s_003", "text": "如何导出账单明细？", "pii": False},
]
raw_path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in raw_samples), encoding="utf-8")

total = 0
removed_pii = 0
kept = []
for line in raw_path.read_text(encoding="utf-8").splitlines():
    total += 1
    obj = json.loads(line)
    if obj.get("pii") is True:
        removed_pii += 1
        continue
    kept.append(obj)

cleaned_path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in kept), encoding="utf-8")

h = hashlib.sha256()
h.update(cleaned_path.read_bytes())
sha256 = h.hexdigest()

report_path.write_text(
    "\n".join(
        [
            "# 清洗报告（示例）",
            "",
            "## 输入与规则",
            "- 输入：raw/sample.jsonl",
            "- 规则：过滤 pii=true 的样本（可用于训练/索引之前的最小门禁示例）",
            "",
            "## 输出统计",
            f"- total={total}",
            f"- removed_pii={removed_pii}",
            f"- kept={len(kept)}",
            "",
            "## 回滚指针",
            "- rollback_to：上一快照 snapshot_id（示例留空，由你的数据注册表提供）",
            "",
        ]
    ),
    encoding="utf-8",
)

manifest = {
    "snapshot_id": "snapshot_demo_001",
    "schema_version": "v1",
    "input": {"path": str(raw_path), "lines": total},
    "output": {"path": str(cleaned_path), "lines": len(kept), "sha256": sha256},
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert removed_pii == 1
assert '"pii": true' not in cleaned_path.read_text(encoding="utf-8").lower()
print("ok")
PY
```
2. 把这个形态迁移到你的真实流水线：固定 `schema_version`、记录 `code_revision/config_hash`、输出 `manifest` 与 `cleaning_report`，并把 `snapshot_id` 写进训练/评测/RAG 的版本组合。

**验证命令：**
- 上面脚本输出 `ok` 且退出码为 0；并生成 `tmp/data-snapshot-demo/manifest.json` 与 `tmp/data-snapshot-demo/cleaning_report.md`。

**失败判定：**
- 清洗规则不可解释（没有报告/没有例外），或风险样本仍混入输出（PII 未被过滤），或快照无指纹（无法比较/无法回滚）。

**回滚：**
- 立即回滚到上一 `snapshot_id`（训练/评测/RAG 同步回退到对应版本组合），并把触发问题的样本写入清洗回归（命中即阻断）。

## 第一步：先写数据边界（不要先抓再说）
数据边界决定两件事：你能不能用，以及你该不该用。建议你先写清楚：
- 数据来源（用户输入、客服对话、公开资料、内部文档等）
- 使用目的（训练/评测/RAG/分析）
- 敏感性（是否含个人信息、机密、版权风险）
- 留存与删除（保留多久、如何删除、如何审计）[35]

### 合规行动指南（别只写原则，要能落地）
把下面问题写进数据卡，能显著降低你未来的返工概率：
- 这份数据的授权链条是什么（用户同意、合同授权、开源许可、内部权限）？谁能签字负责？
- 是否涉及个人信息或敏感个人信息（例如身份证号、地址、未成年人信息）？能否做数据最小化？[35]
- 是否存在跨境传输或第三方共享？数据处理者与接收方的责任边界是什么？
- 用户能否请求导出、删除、撤回同意？删除后对会计/审计留存如何处理（去标识化替代直接 PII）？
- 哪些数据永远不进入训练与索引（密钥、支付、医疗、合同机密等）？如何强制门禁？

## 模板 1：数据卡（Datasheet）
用法：每个数据集都先写一张卡，哪怕很短。[34]

| 字段 | 说明 |
| --- | --- |
| 名称与版本 | 数据集名 + 版本号 |
| 目的 | 用于训练/评测/RAG/分析 |
| 来源 | 从哪里来；是否可复现 |
| 许可与合规 | 授权、隐私、版权边界 |
| 覆盖范围 | 适用人群/任务类型/语言 |
| 不覆盖范围 | 明确不保证的部分 |
| 字段与口径 | 关键字段定义与计算口径 |
| 已知偏差 | 采样偏差、标签偏差、分布偏差 |
| 风险与止损 | 发现问题如何停用/回滚 |

## 第二步：采集策略（宁可少，但要干净）
0→1 阶段常见误区是先把量堆上去。更聪明的做法是先建立失败样本优先的采集：
- 记录用户无法完成闭环的案例（失败的输入、失败的输出、用户的纠正）。
- 记录高风险案例（越权尝试、注入、敏感内容）。
- 记录高价值案例（用户明确标注有用/采纳的输出）。[34]

这些样本会直接变成你的评测集与训练集的种子，价值远高于随机大规模抓取。

### 失败样本优先的最小采集机制（0→1 可直接照做）
- 产品侧：在关键输出旁放反馈入口（有用/无用、原因、改写建议），并允许用户一键把更正内容提交为样本。
- 工程侧：把错误与失败变成结构化事件，而不是一堆字符串日志（error_code、stage、retry_count、fallback）。
- 风险侧：把越权、注入、敏感内容命中也当作样本资产，进入红队评测与回归，而不是一删了之。[35]
- 运营侧：把客服工单与争议样本串起来，形成从投诉到数据回写的闭环。

### 最小数据事件 schema（建议从日志里长出来）

| 字段 | 用途 |
| --- | --- |
| event_id | 去重与追溯 |
| tenant_id / user_id | 归属与权限边界 |
| timestamp | 时间窗与回放 |
| entrypoint | 入口（页面/接口/批处理） |
| capability | 能力点（对话、检索、导入等） |
| request_id / trace_id | 证据定位 |
| input_summary / output_summary | 训练与评测摘要（避免落原文） |
| feedback_label | 用户反馈（有用/无用/纠正） |
| error_code / failure_stage | 失败分桶 |
| safety_flags / pii_flags | 风险标记与门禁 |
| consent_state | 是否允许用于训练/评测 |
| dataset_route | 进入哪个数据流（train/eval/redteam/none） |

## 第三步：清洗与过滤（必须有报告）
清洗不是随便删，而是可解释的决策。每一次清洗都要回答：
- 你删掉了什么（规则与阈值）？
- 你为什么删（风险或质量理由）？
- 你删掉后会损失什么（覆盖面/多样性）？
- 你保留了哪些例外（为什么保留）？[34]

**模板 2：清洗报告（最小集合）**

| 项 | 写法 |
| --- | --- |
| 输入范围 | 原始数据量、时间范围、来源 |
| 去重策略 | 重复判定规则与比例 |
| 脱敏策略 | 哪些字段脱敏/删除；验证方式（抽样人工、PII 扫描、脱敏前后统计对比） |
| 过滤规则 | 低质量、垃圾、注入、敏感内容规则 |
| 例外清单 | 为什么保留；风险如何控制 |
| 输出统计 | 清洗后数据量、分布变化、抽样示例 |
| 回滚策略 | 如何回到上一版数据集 |

### 脱敏与验证：别把自己骗了
脱敏不是把邮箱打星号就算赢。你需要能证明它真的生效：
- 抽样人工复核：对高风险字段做分层抽样，验证是否仍可反推个人身份。
- 自动化扫描：用规则与模型对 PII 做扫描，产出命中率与漏报样本。
- 统计对比：脱敏前后做长度分布、字符集分布、实体类型分布对比，防止规则失效。
- 红队回归：对脱敏后的数据做反推测试，把可逆脱敏当作缺陷回写到规则。

### 清洗门禁：把污染拦在训练/索引之前（RB-10）
清洗不是为了“跑通流程”，而是为了**拒收批次**。一旦脏数据进入 `snapshot_id` 并污染训练集或索引，你后面所有“效果优化”都可能变成把风险做得更稳定。因此清洗流水线的出口必须有强制门禁：不达标就不产出快照、不允许进入训练与索引。

阈值不要拍脑袋，按三段式写（基线分位数 + 倍数 + 绝对红线），并强制按 `batch_id/snapshot_id/version_set` 对齐口径。指标与阈值的统一写法见：[F-metrics-alerts.md](F-metrics-alerts.md)。数据污染的 10 分钟止损动作见：[E-runbooks.md](E-runbooks.md)（RB-10）。合规边界与处置建议见：[20-governance.md](20-governance.md)。

| 门禁/信号（Gate） | 三段式阈值（示例） | 首要止血动作（先断源） | 证据要求（必须可审计） | Runbook |
| --- | --- | --- | --- | --- |
| PII 命中 | `risk.pii_detected_count > 0`（绝对红线） | 立刻隔离批次 + 暂停摄入/训练/索引 | `samples/pii_hits.jsonl`（脱敏）+ `signals/pii_scan_report.json` | [E-runbooks.md](E-runbooks.md)（RB-10） |
| Schema/字段校验失败 | `fail_rate > baseline_p99×1.5` 或 `> 5%`（红线示例） | 拒收批次（不产出快照）+ 回滚到上一快照 | `signals/schema_validation.json` + `diffs/schema.diff` | [E-runbooks.md](E-runbooks.md)（RB-10） |
| 分布突变（长度/语言/标签比例） | `drift_score > baseline_p95×2` 或 `> 0.05`（绝对红线示例） | 冻结下游使用（训练/索引指针不前移）+ 人工抽检 | `signals/distribution_diff.csv` + `samples/shift_samples.jsonl` | [E-runbooks.md](E-runbooks.md)（RB-10） |
| 训练/评测泄露（数据混流） | `leak_count > 0`（绝对红线） | 立刻隔离批次 + 下线污染快照/索引 | `signals/leak_check.json` + `samples/leak_pairs.jsonl` | [E-runbooks.md](E-runbooks.md)（RB-10） |
| 注入指令/命令式句子混入（可选但强烈建议） | `hit_rate > baseline_p95×1.5` 或 `> 1%`（绝对红线示例） | 暂停摄入 + 启用更严格过滤；若已进入索引需回滚 | `signals/injection_hits.json` + `samples/injection_hits.jsonl` | [E-runbooks.md](E-runbooks.md)（RB-10/RB-05/RB-06） |
| 审计与血缘缺口（不可追溯） | `risk.audit_gap_count > 0`（绝对红线） | 禁止产出/发布该快照（先补齐元数据） | `meta.json` + `version_set.json` + `registry_snapshot.json` | [E-runbooks.md](E-runbooks.md)（RB-10） |

```text
清洗作业完成
  → 计算门禁指标（按 batch_id/snapshot_id/version_set 分桶）
  → 通过：产出新 snapshot_id + 写入数据注册表
  → 失败（任一红线命中）：
      1) 隔离批次（tainted，禁止进入训练/索引）
      2) 暂停摄入/训练/索引构建（先断源）
      3) 回滚指针到上一 snapshot_id（训练/索引）
      4) 清理污染（按 batch_id 删除/回滚）
      5) 复跑校验（PII 扫描 + schema 校验必须全绿）
      6) 恢复（逐步放开下游；把触发样本回写到门禁）
```

最小证据包（落到 `reports/YYYY-MM-DD/<change-id>/`，参照 [D-evidence-pack.md](D-evidence-pack.md)）：
- `meta.json`：批次信息、时间窗、来源、定级、负责人。
- `version_set.json`：本次处理的 `code_revision/config_hash/schema_version`（用于回滚与复跑）。
- `manifest.json`：输入/输出文件列表、校验和、行数与统计摘要（快照指纹）。
- `signals/pii_scan_report.json`：PII 扫描报告（命中率、规则版本、漏报样本 id）。
- `signals/schema_validation.json`：字段/Schema 校验结果（通过率、错误类型分布）。
- `signals/distribution_diff.csv`：清洗前后关键分布对比（长度/语言/标签等）。
- `samples/pii_hits.jsonl`：污染样本抽样（必须脱敏），用于复盘与回归门禁。
- `action_log.md`：隔离/回滚/清理动作日志 + 回滚指针。

## 第四步：标注与一致性（让标签可被信任）
标注最贵的不是人工成本，而是不一致：同一个问题，不同标注者给出不同标准，训练出来的模型会学会矛盾。

**模板 3：标注指南（让一致性可回归）**

| 模块 | 说明 |
| --- | --- |
| 任务定义 | 什么算一个样本；输入/输出边界 |
| 标签集合 | 标签名、含义、正反例 |
| 判定规则 | 评分尺度与判定优先级 |
| 冲突处理 | 标注冲突如何仲裁 |
| 质量抽检 | 抽检比例与返工规则 |

0→1 的建议：先做小规模标注，先把一致性跑通，再扩量。

## 第五步：版本化与审计（让数据可复现）
数据版本化的目标不是存档，而是可追溯：任何一次训练、评测、RAG 索引都能指向一个明确的数据快照。[34]

最低要求：
- 每次数据变更都能说明变了什么、为什么变、影响了什么；
- 能回滚到上一版本；
- 能复跑处理流程得到同级别结果（趋势一致）。

### 最小实现：先把可追溯做出来
0→1 阶段你不需要一口吃成湖仓，但至少要把下面三件事钉死：
- 数据快照：每次产出一个不可变快照（snapshot_id），并保存 manifest（文件列表、校验和、行数、统计摘要）。
- 处理可复现：记录处理流水线的 code_revision（git commit）、config_hash、schema_version、运行参数与时间窗。
- 元数据可查询：有一个数据注册表（dataset registry），能查到某次训练或索引到底用了哪个 snapshot。[34]

### 常见工具与选型方向（给你一个可走的路）
- 小团队：对象存储 + manifest + dataset registry（自建最小实现）
- 数据版本：DVC（更接近代码工作流）
- 湖仓快照：Delta Lake / Iceberg（更接近数据平台）
- 追溯与血缘：元数据系统（例如数据目录与血缘追踪）

### 数据版本记录最小字段

| 字段 | 说明 |
| --- | --- |
| dataset_id / dataset_version | 数据集标识 |
| snapshot_id | 不可变快照 |
| source_range | 来源时间窗与范围 |
| schema_version | 字段口径 |
| code_revision | 处理代码版本 |
| config_hash | 清洗与过滤配置 |
| stats_summary | 样本数、分布、命中率 |
| approval | 合规与质量审批记录 |
| rollback_to | 回滚指针 |

## 复现检查清单（本章最低门槛）
- 数据卡齐全：目的、来源、许可、风险、止损与删除策略写清；无许可或边界不清视为阻断。[34][35]
- 清洗报告可复跑：规则、阈值、例外、抽检样例与回滚指针齐全；处理可追溯 code_revision/config_hash。[34]
- 标注与抽检可回归：指南、抽检策略与一致性口径明确；争议样本回写指南与回归集。
- 数据快照可追溯：训练/评测/RAG 都能指向明确数据快照，并能查到来源时间窗与统计摘要。[34]

## 常见陷阱（失败样本）
1. **现象：** 训练或 RAG 越做越乱，表现波动难解释；同样问题今天好、明天坏。  
   **根因：** 数据版本不可追溯；每次清洗都像重新洗牌，且缺少清洗报告与指纹。[34]  
   **复现：** 同一时间窗的数据用不同清洗配置重跑两次，发现样本数/分布差异明显，但你说不清差异来自哪条规则。  
   **修复：** 强制数据卡 + 清洗报告 + 快照 manifest；没有证据与回滚指针的数据不得进入训练/索引。[34]  
   **回归验证：** 固定 `snapshot_id` 复跑三次结果一致；清洗规则与例外可解释，且快照指纹可用于对比与回滚。

2. **现象：** 模型学会了危险行为（泄露、越权、注入），而你以为自己做了安全。  
   **根因：** 把风险样本当噪声删掉；或未先写合规边界，导致敏感数据混入训练/索引。[35]  
   **复现：** 抽检训练/RAG 语料，发现含敏感字段或越权指令；或红队样本在数据流里被“清洗掉”。  
   **修复：** 高风险失败样本当资产：单独分流进 redteam/回归集；合规边界与 `consent_state` 先行，命中即阻断。[35]  
   **回归验证：** PII/敏感内容扫描与越权/注入样本回归稳定复跑：命中即阻断，且审计记录能追溯到来源与处理动作。

3. **现象：** 数据量很大，但训练收益很小；越扩量越像噪声。  
   **根因：** 数据与任务不匹配；噪声比例高；标注不一致导致模型学会矛盾。[34]  
   **复现：** 抽检 50 条样本：大量与目标任务无关，或同一类型样本标签互相矛盾；IAA 指标低且无仲裁机制。  
   **修复：** 回到数据卡的覆盖范围与“不覆盖范围”；先提升一致性与密度（标注指南/仲裁/抽检），再扩量。[34]  
   **回归验证：** 抽检与一致性指标稳定（或明确达标阈值）；训练/评测对比能解释收益来自哪些数据分桶，而不是“感觉更好”。

## 交付物清单与验收标准
- 数据卡（Datasheet）与合规边界说明。[34][35]
- 清洗报告（含阈值、例外、回滚）。[34]
- 标注指南与抽检记录（一致性可复核）。
- 数据版本与快照策略（训练/评测/RAG 可追溯）。[34]

## 下一章
数据资产准备好后，才轮到训练与适配。下一章进入预训练：你该追求什么目标、怎么核算成本、什么时候不做。见：[14-pretrain.md](14-pretrain.md)。

## 参考
详见本书统一参考文献列表：[references.md](references.md)。
