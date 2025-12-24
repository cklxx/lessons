# 第 13 章：数据收集与清洗：从语料到可训练数据集
![第 13 章封面](../../assets/chapter_13_header_1766035711036.png)

> 数据不是原材料，而是你的核心产品资产。它决定你能训练什么、能评测什么、能否合规上线，以及你能否在同一个问题上持续变强。[34]

在 AI 产品中，数据有两张脸：一张是面向用户的**事实**（用户的输入、报错、反馈、失败样本），另一张是面向系统的**燃料**（训练集、评测集、RAG 语料）。做得好，你积累的是护城河；做得烂，你积累的是技术债务、法律风险和无法解释的偏差。

## 章节定位
本章连接了“产品定义”与“系统训练”。你的任务是把零散的语料、日志、文档，整理成可复用的**数据资产**：
- 有范围（Boundaries）
- 有许可（License）
- 有字段定义（Schema）
- 有清洗报告（Cleaning Report）
- 有版本快照（Snapshot）
- 可回滚（Rollback）

这样，你在后续的训练、RAG、评测与治理中，才能引用同一个“事实源”。[34][35]

## 你将收获什么
- **一套资产化流程**：从边界定义到快照归档的 6 步法。[34]
- **三个强制模板**：数据卡（Datasheet）、清洗报告、快照清单（Manifest）。[34]
- **一条红线**：先合规后增长，先可追溯后训练。[35]

## 核心逻辑：数据工作的价值不在“大”，在“可用”

### 1. 读者目标
你要交付的是一个**可训练、可评测、可治理**的数据集。
- **可复现**：别人（或未来的你）能从源头复跑出同样的数据。
- **可解释**：为什么删了这条？为什么留了那条？
- **可回滚**：新版数据把模型练崩了，能一键切回旧版。

### 2. 论证链条
数据变资产的链条是刚性的：
**边界与许可** $\rightarrow$ **字段与口径** $\rightarrow$ **清洗与过滤** $\rightarrow$ **标注与一致性** $\rightarrow$ **版本化与审计** $\rightarrow$ **回归与迭代**
缺了许可，后面全是法律风险；缺了版本号，后面全是玄学。[34][35]

### 3. 验收标准
验收不是看你抓了多少 TB 数据，而是看：
1.  **来源清晰**：能说清每一行数据从哪来、授权链条是什么。
2.  **清洗透明**：有对应的清洗报告，列明了删除率和例外清单。
3.  **结果稳定**：复跑处理流程，能得到指纹一致的结果。[34]

---

![图 13-1：数据资产化流水线](../../assets/figure_13_1_1765971297073.png)

## 关键流程：数据资产化流水线
不要依赖口头约定，要把每个阶段的**输入/输出**与**最低门禁（Quality Gate）** 写死在流水线里。

| 阶段 | 输入 | 输出 | 质量门禁（最低要求） |
| :--- | :--- | :--- | :--- |
| **1. 边界与许可** | 数据卡草稿 | 可用范围声明 | 许可明确、目的明确、留存期明确 |
| **2. 采集** | 埋点、日志、工单 | 原始区 (Raw) | Schema 固定、来源可追溯、ID 唯一 |
| **3. 清洗与脱敏** | Raw | 清洗版 (Cleaned) | 去重率达标、PII 扫描 0 命中、有例外清单 |
| **4. 标注与一致性** | Cleaned | 标注版 (Labeled) | 抽检通过、IAA (一致性) 指标达标 |
| **5. 版本化** | Labeled | 快照 (Snapshot) | 生成数据指纹 (Hash)、锁定代码版本 |
| **6. 回归** | Snapshot | 评测报告 | 核心指标未倒退，才可推送到 Training/Index |

---

## 可执行示例：最小清洗报告 + 快照 Manifest

**目标**：用一个 Python 脚本演示“清洗不是随便删”，必须留下证据：输入统计、规则逻辑、例外记录、输出指纹。

**前置条件**：Python 3 环境。

**步骤**：
1.  复制并运行下方脚本。它会模拟从 `raw` 到 `cleaned` 的过程，并生成审计所需的 `cleaning_report.md` 和 `manifest.json`。

```python
"""
data_pipeline_demo.py
演示：可审计的数据清洗流水线
"""
import hashlib
import json
import shutil
from pathlib import Path
from datetime import datetime, timezone

# 配置路径
ROOT_DIR = Path("tmp/data-snapshot-demo")
RAW_DIR = ROOT_DIR / "raw"
CLEANED_DIR = ROOT_DIR / "cleaned"
REPORT_PATH = ROOT_DIR / "cleaning_report.md"
MANIFEST_PATH = ROOT_DIR / "manifest.json"

# 初始化目录
if ROOT_DIR.exists():
    shutil.rmtree(ROOT_DIR)
RAW_DIR.mkdir(parents=True, exist_ok=True)
CLEANED_DIR.mkdir(parents=True, exist_ok=True)

# 1. 模拟原始数据 (Raw Data)
# 注意：包含一条 PII 数据和一条低质量数据
raw_samples = [
    {"id": "s_001", "text": "为什么我的 API 调用失败了？", "pii": False, "quality": "high"},
    {"id": "s_002", "text": "我的邮箱是 admin@example.com，请重置密码", "pii": True, "quality": "high"},
    {"id": "s_003", "text": "啊啊啊啊啊测试测试", "pii": False, "quality": "low"},
    {"id": "s_004", "text": "如何导出 PDF 报表？", "pii": False, "quality": "high"},
]
raw_file = RAW_DIR / "sample.jsonl"
with open(raw_file, "w", encoding="utf-8") as f:
    for item in raw_samples:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# 2. 清洗逻辑 (Cleaning Logic)
# 规则：过滤 PII=True 或 Quality=low 的样本
total_count = 0
dropped_pii = 0
dropped_low_quality = 0
kept_samples = []

with open(raw_file, "r", encoding="utf-8") as fin:
    for line in fin:
        total_count += 1
        obj = json.loads(line)
        
        # 规则 1: PII 阻断
        if obj.get("pii") is True:
            dropped_pii += 1
            continue
            
        # 规则 2: 低质量过滤
        if obj.get("quality") == "low":
            dropped_low_quality += 1
            continue
            
        kept_samples.append(obj)

# 3. 写入清洗后数据 (Cleaned Data)
cleaned_file = CLEANED_DIR / "sample.cleaned.jsonl"
with open(cleaned_file, "w", encoding="utf-8") as fout:
    for item in kept_samples:
        fout.write(json.dumps(item, ensure_ascii=False) + "\n")

# 4. 生成指纹 (Fingerprinting)
sha256_hash = hashlib.sha256()
with open(cleaned_file, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)
file_fingerprint = sha256_hash.hexdigest()

# 5. 生成清洗报告 (Cleaning Report)
report_content = f"""# 清洗报告
- **时间**: {datetime.now(timezone.utc).isoformat()}
- **输入**: {raw_file} (Total: {total_count})
- **输出**: {cleaned_file} (Kept: {len(kept_samples)})
- **指纹 (SHA256)**: `{file_fingerprint}`

## 过滤统计
| 原因 | 数量 | 占比 |
| :--- | :--- | :--- |
| PII 敏感信息 | {dropped_pii} | {dropped_pii/total_count:.1%} |
| 低质量内容 | {dropped_low_quality} | {dropped_low_quality/total_count:.1%} |

## 规则说明
1. `pii == True`: 涉及用户隐私，直接丢弃。
2. `quality == 'low'`: 无意义字符或乱码，过滤。
"""
REPORT_PATH.write_text(report_content, encoding="utf-8")

# 6. 生成快照 Manifest (机器可读)
manifest = {
    "snapshot_id": "snap_demo_v1",
    "schema_version": "1.0.0",
    "created_at": datetime.now(timezone.utc).isoformat(),
    "input": {"path": str(raw_file), "lines": total_count},
    "output": {
        "path": str(cleaned_file), 
        "lines": len(kept_samples), 
        "sha256": file_fingerprint
    },
    "metrics": {
        "dropped_pii": dropped_pii,
        "dropped_quality": dropped_low_quality
    }
}
MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"✅ 清洗完成。报告已生成: {REPORT_PATH}")
print(f"🔒 快照 Manifest: {MANIFEST_PATH}")
```

2.  **验证结果**：
    检查 `tmp/data-snapshot-demo/cleaning_report.md`，确认它解释了为什么 4 条变 2 条。
    检查 `tmp/data-snapshot-demo/manifest.json`，确认它记录了 SHA256 指纹。

**失败判定**：
- 如果没有生成 `manifest.json`，视为流程失败。
- 如果输出数据中仍包含 `"pii": true`，视为严重安全事故（阻断上线）。

---

## 第一步：先写数据边界（不要先抓再说）
数据边界决定了两件事：你**能不能**用，以及你**该不该**用。
不要把所有抓来的东西都倒进模型里。建议先写一份**数据卡（Data Card）**。

### 合规行动指南（落地版）
在采集代码写下第一行之前，必须回答：
- **授权链条**：用户同意协议了吗？开源协议兼容商用吗？谁签的字？
- **最小化原则**：一定要存身份证号吗？一定要存用户 IP 吗？能否只存去标识化后的 ID？[35]
- **退出机制**：用户要求删除时，你能从数亿条数据里把他的痕迹物理擦除吗？（如果不能，用去标识化替代）。
- **红线**：密钥、支付信息、医疗记录、合同机密——这些永远不进训练集，必须在入口处配置硬编码拦截。

### 模板 1：数据卡 (Datasheet)
每个数据集（Dataset）必须配一张卡，哪怕只有 100 行。

| 字段 | 填写说明 |
| :--- | :--- |
| **名称与版本** | 数据集唯一标识 + 语义化版本号 (e.g., `cust-support-v1.2`) |
| **用途 (Purpose)** | 仅用于训练 / 仅用于评测 / 仅用于 RAG 索引 / 仅用于红队测试 |
| **来源 (Provenance)** | 具体来源（生产库表名、开源项目 URL、采购方名称） |
| **许可 (License)** | CC-BY-SA 4.0 / 内部私有 / 用户协议条款 3.1 |
| **包含内容** | 覆盖的人群、场景、语言、时间跨度 |
| **排除内容 (Out of Scope)** | 明确不包含的场景（如：不包含金融建议、不包含代码生成） |
| **已知偏差** | 哪里数据偏多？哪里偏少？（如：中文样本仅占 5%） |
| **止损策略** | 发现严重问题（如泄露）时，如何紧急下线？ |

---

## 第二步：采集策略（失败样本优先）
0 $\rightarrow$ 1 阶段，不要痴迷于堆量。**失败样本的价值是成功样本的 10 倍**。
- **高价值**：用户修改了 AI 的回答（Direct Correction）。
- **高风险**：用户尝试注入 Prompt，或 AI 输出了乱码。
- **高频长尾**：用户搜了但没结果的 Query。

这些样本是训练集和评测集的“种子”。

### 最小数据事件 Schema
把日志打成结构化数据，而不是一堆 grep 不动的字符串。建议在 Log 或埋点中包含以下字段：

| 字段名 | 必填 | 说明 |
| :--- | :--- | :--- |
| `event_id` | Yes | 全局唯一 ID (UUID)，用于去重 |
| `trace_id` | Yes | 关联全链路，定位上下文 |
| `dataset_route` | Yes | 数据流向：`train` / `eval` / `redteam` / `drop` |
| `input_snapshot` | Yes | 用户的原始输入 |
| `output_snapshot` | Yes | AI 的原始输出 |
| `user_feedback` | No | `thumb_up`, `thumb_down`, `rewrite` |
| `safety_flags` | No | 风险标签列表 (`["pii_suspected", "toxic"]`) |
| `consent_state` | Yes | 合规标记 (`allowed`, `denied`, `revoked`) |

---

## 第三步：清洗与过滤（必须有报告）
清洗是一个**决策过程**，不是单纯的删除。
每一次 `drop` 操作，都必须在报告里解释原因。

### 模板 2：清洗报告 (Cleaning Report)
每次清洗作业结束，自动生成此 Markdown 文件，并存档。

```markdown
# 数据清洗执行报告
- **Batch ID**: 20240520-Batch-A
- **执行人/脚本**: script_v3.2.py

## 1. 概览
| 指标 | 数值 | 变化 |
| :--- | :--- | :--- |
| 原始行数 | 100,000 | - |
| 清洗后行数 | 85,400 | -14.6% |
| 处理耗时 | 12m 30s | - |

## 2. 过滤详情 (Why we dropped)
| 规则 ID | 规则描述 | 删除数量 | 示例 (已脱敏) |
| :--- | :--- | :--- | :--- |
| `FILTER_PII` | 包含手机号/邮箱 | 2,100 | "联系我 138****（已打码）" |
| `FILTER_LEN` | 长度 < 5 字符 | 5,000 | "hi", "test" |
| `FILTER_DUP` | 完全重复去重 | 7,500 | - |

## 3. 例外清单 (Exceptions)
以下样本命中规则但被**强制保留**（白名单）：
- ID: `s_9921` (命中 PII 但为虚拟示例数据)
- ID: `s_8823` (过短但为核心指令)

## 4. 门禁结果
- [x] PII 扫描通过 (0 命中)
- [x] Schema 校验通过
- [x] 分布偏移检测 (< 5% 变化)
- **结论**: ✅ 允许生成快照
```

### 清洗门禁：RB-10 止损
清洗流水线必须有**阻断能力**。如果脏数据进了 `snapshot_id`，你后面所有的“调优”都是在给垃圾堆喷香水。
请参阅 [E-runbooks.md](E-runbooks.md) 中的 **RB-10 (Data Contamination)**，配置以下红线：

1.  **PII 零容忍**：清洗后若扫描出 1 条真实 PII，整个 Batch 拒收。
2.  **Schema 强校验**：字段缺失率 > 1%（示例），拒收。
3.  **分布突变**：数据平均长度暴跌 50%，或者某类标签消失，暂停并报警。

---

## 第四步：标注与一致性（让标签可信）
标注最贵的成本不是钱，是**不一致**。
如果标注员 A 说“这个好”，标注员 B 说“这个坏”，模型就会学成精神分裂。

**策略**：
1.  **先定标准，再开工**：写一份标注指南（Guideline），包含正例、反例、模糊地带的仲裁规则。
2.  **小样本试标**：先标 100 条，计算 **IAA (Inter-Annotator Agreement)**。如果一致率低于 80%，停下来修指南，别继续标。[34]
3.  **金标准集 (Gold Set)**：维护一份专家确认过的“标准答案”，混入日常标注任务中进行“盲测”质检。

---

## 第五步：版本化与审计（Snapshot ID）
不要用 `data_final_v2_updated.json` 这种文件名。
**数据版本化的最低要求**：
- **不可变 (Immutable)**：一旦生成快照，内容绝不修改。要改就发新版。
- **可寻址 (Addressable)**：每个版本都有唯一的 `snapshot_id`（如 hash 值）。
- **可追溯 (Traceable)**：能查到这个快照是由哪份代码 (`code_revision`) 和哪份配置 (`config_hash`) 生成的。[34]

### 最小实现：S3 + Manifest
你不需要复杂的 Data Lake，只需要一个严谨的目录结构：

```text
/datasets
  /v1.0.0 (tag) -> snapshots/sha256_abc123_<...>
  /snapshots
    /sha256_abc123_<...>/
      data.jsonl      (只读)
      manifest.json   (元数据)
      cleaning_report.md
      provenance.log  (来源记录)
```

当模型出现问题时，你可以说：“模型 `model-v3` 是在 `snapshot-abc123` 上训练的，让我们回滚到 `snapshot-xyz789`。”

---

## 常见陷阱（Failures）

1.  **陷阱：只管进不管出**
    *   **现象**：数据越积越多，训练效果越来越差，因为早期的垃圾数据一直在库里。
    *   **修复**：给数据设置“有效期”或“权重衰减”。定期执行“大扫除”，废弃旧的、低质量的快照。

2.  **陷阱：脱敏自欺欺人**
    *   **现象**：以为把名字打码就安全了，结果模型通过上下文反推出了身份。
    *   **修复**：红队测试（Red Teaming）。专门尝试攻击脱敏后的数据集，看能否还原敏感信息。[35]

3.  **陷阱：回滚无门**
    *   **现象**：新清洗规则上线删错数据了，但旧数据已经被覆盖。
    *   **修复**：永远不要覆盖原始数据（Raw）。清洗是生成新文件，不是修改旧文件。始终保留上一版快照指针。

## 交付物清单
- [ ] **数据卡 (Datasheet)**：明确边界与许可。[34][35]
- [ ] **清洗报告 (Cleaning Report)**：包含过滤统计与例外清单。[34]
- [ ] **快照 Manifest**：包含数据指纹与溯源信息。[34]
- [ ] **标注指南**：如果涉及人工标注，必须有文档。

## 下一章
数据准备好了，接下来是烧钱的环节——预训练。
怎么算算力账？怎么决定是重训还是微调？请看 [14-pretrain.md](14-pretrain.md)。

## 参考
详见 [references.md](references.md)。
