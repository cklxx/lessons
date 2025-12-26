# 附录 D：证据包与门禁速查（可复制）

> 目标：把“质量控制”落成默认动作：每次改动都有证据包（可复跑、可裁决、可回滚）；每条门禁都有入口、判定、证据与回滚。
>
> 说明：本书仓库是文档仓库；本附录描述的是你在**产品/服务代码库**里落地的结构与模板。命令均为示例，请按你的技术栈替换。

## D.1 推荐的“可裁决”仓库骨架

把质量基础设施（评测/证据/Runbook）和源代码（`src/`）并列，保证它们不仅存在，而且“可见、可复跑、可审计”。

```text
project-root/
├── src/                      # 源代码
├── docs/                     # 项目文档与设计规范（可选）
├── eval/                     # [核心] 评估体系（回归/红队/对比）
│   ├── sets/                 # 评测集与失败样本（版本化）
│   ├── scorers/              # 评分器/裁判 (Gatekeeper Judge)
│   └── configs/              # 评测参数配置 (Admission Policy)
├── reports/                  # [核心] 证据包归档 (Evidence Pack)
│   └── 2025-12-23/
│       └── fix-rag-topk-a1b2c/
├── runbooks/                 # [核心] 10 分钟止损手册 (Rollback Triggers)
│   ├── release.md
│   └── rollback.md
├── schemas/                  # 结构化输出契约
├── tools/                    # 门禁哨兵 (Gatekeeper Scripts)
├── tests/                    # 单元/集成测试
└── Makefile                  # 入口：gate / evidence / release
```

## D.2 证据包标准（Evidence Package）

每次变更（Feature/Fix/Hotfix）上线前，生成一个独立的证据目录；让任何人都能回答四个问题：
1) 我改了什么？2) 用的什么版本组合？3) 怎么验证的？4) 失败怎么回滚？

### 目录结构与命名规范

- **路径格式**：`reports/YYYY-MM-DD/<change-id>/`
- **命名建议**：`<type>-<short-desc>-<short-sha>`，例如 `feat-search-rerank-a1b2c`
- **敏感信息**：证据包默认应作为 CI artifact/对象存储归档；若要提交到代码仓库，先确保已脱敏（不得包含密钥与用户 PII）。

```text
<change-id>/
├── manifest.json             # [必须] 版本组合 + 环境指纹 + 门禁结论（模板见下）
├── diffs/                    # [必须] 关键变更快照（可读 diff）
│   ├── prompts.diff
│   ├── config.diff
│   ├── schemas.diff
│   └── infra.diff
├── gates/                    # [必须] 门禁执行输出（原始日志 + 汇总）
│   ├── unit_test_report.*
│   ├── eval_summary.*
│   └── security_scan.*
├── samples/                  # [建议] 本次新增/命中的失败样本（最小复现条件）
├── media/                    # [可选] 人工验收证据（截图/录屏/trace）
└── rollback.md               # [可选] 回滚记录（若发生回滚）
```

### `manifest.json` 模板（建议最小字段）

```json
{
  "meta": {
    "timestamp": "2025-12-23T14:30:00Z",
    "change_id": "feat-search-rerank-a1b2c",
    "builder": "ci-runner-01",
    "operator": "dev_alias"
  },
  "version_set": {
    "code": { "git_commit": "a1b2c3d4" },
    "config": { "config_hash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef" },
    "data": { "dataset_snapshot_id": "ds_2025_12_23_01" },
    "index": { "index_id": "kb_v17" },
    "model": { "model_id": "model_v4", "checkpoint": "ckpt_0123" },
    "prompt": { "prompt_id": "prompt_v12" }
  },
  "gates": {
    "unit_tests": { "level": "L0", "status": "PASS", "evidence": "gates/unit_test_report.*" },
    "ai_regression": { "level": "L0", "status": "PASS", "evidence": "gates/eval_summary.*" },
    "security": { "level": "L0", "status": "PASS", "evidence": "gates/security_scan.*" }
  },
  "verdict": { "decision": "SHIP", "reason": "score_up+cost_flat", "reviewer": "reviewer_alias" },
  "rollback": { "trigger": "any L0 FAIL", "target_change_id": "previous_version_set_id" }
}
```

## D.3 变更类型与门禁矩阵（最低门槛）

不同类型的变更，对应不同的“最低留档证据”和“默认回滚动作”。你不需要一次性做全，但建议先把最常改的 3–5 类落到 L0。

| 变更类型 | 必须留档证据（示例） | 最低门禁（示例） | 失败判定（示例） | 默认回滚动作 |
| :--- | :--- | :--- | :--- | :--- |
| **Prompt/策略** | Prompt Diff + 回归报告 | 关键用例通过率 ≥ 阈值 | 核心语义漂移/拒答失控/成本飙升 | 回退到上一版 prompt |
| **RAG 索引/语料** | Chunk/索引快照 + 召回评测 | Top-K 召回不低于基线 | 关键知识点召回失败/过期引用 | 切回旧 index alias |
| **模型版本** | 对比评测 + 压测报告 | 质量不退化且守门指标达标 | 质量退化/超时率越界 | 配置指回旧模型 |
| **工具/Schema** | 契约 Diff + Mock 调用日志 | 向后兼容检查通过 | 必填字段缺失/类型不匹配 | 回退代码与契约 |
| **前端交互** | 关键流程截图/录屏 | 核心路径可用且无阻断错误 | 白屏/交互死循环/误导文案 | 回退前端构建产物 |
| **后端接口** | 契约测试 + 迁移脚本 | 集成测试全绿 | 5xx 激增/鉴权失败 | 回退服务版本 |
| **数据快照** | 分布统计 + Schema 校验 | 异常值/漂移检查通过 | 空值率激增/主键冲突 | 停止注入/回退快照 |
| **训练/微调** | 曲线 + held-out 评测 | 主指标达标且守门不过线 | 过拟合/灾难性遗忘 | 丢弃 checkpoint |
| **推理配置** | 采样参数 diff + 格式检查 | 输出合同满足率 ≥ 阈值 | 空输出/重复死循环 | 回退配置 |
| **部署/基础设施** | IaC Diff + dry-run | 预发健康检查通过 | 资源不足/启动失败 | 一键回滚到上一版 |

## D.4 “一条命令入口”：门禁与证据的统一动词

目标不是迷信 `Makefile`，而是把验证逻辑收敛为简单动词，让本地与 CI 复用同一入口：`gate`（跑门禁）→ `evidence`（产证据）→ `release`（发灰度）。

```makefile
.PHONY: gate evidence release

TIMESTAMP := $(shell date +%Y-%m-%d)
COMMIT := $(shell git rev-parse --short HEAD)
CHANGE_ID ?= $(shell git branch --show-current | sed 's/\\//-/g')-$(COMMIT)
REPORT_DIR := reports/$(TIMESTAMP)/$(CHANGE_ID)

# 你只需要把下面三条替换成自己项目的命令入口
UNIT_TEST_CMD ?= <your_unit_test_cmd>
AI_EVAL_CMD ?= <your_ai_eval_cmd>
SECURITY_CMD ?= <your_security_scan_cmd>

gate:
	@mkdir -p $(REPORT_DIR)/gates
	@echo "[gate] unit tests" && $(UNIT_TEST_CMD)
	@echo "[gate] ai eval" && $(AI_EVAL_CMD)
	@echo "[gate] security" && $(SECURITY_CMD)

evidence: gate
	@mkdir -p $(REPORT_DIR)/diffs
	@git diff HEAD^..HEAD > $(REPORT_DIR)/diffs/changes.diff
	@echo "Replace this line: write $(REPORT_DIR)/manifest.json (version_set + gate results)"

release: evidence
	@echo "Replace this line: deploy (canary) + verify + rollback on breach"
```

**落地要点：**
- `gate` 失败必须以**非 0 退出码**结束（否则 CI 无法阻断）。
- `evidence` 只做两件事：归档“原始输出”和“可读摘要”；不要只留截图不留源数据。
- `release` 必须绑定 Runbook：任何指标越界都有“立即动作 + 验证动作 + 证据留档”。

## D.5 发布与回滚 Runbook 速查（10 分钟止损）

### 发布检查单（Pre-flight）
1) **版本组合可追溯**：能说清本次 `version_set`（代码/配置/数据/索引/模型/prompt）。
2) **门禁可复跑**：跑通 `gate`，并能定位证据输出路径。
3) **证据可归档**：证据包已上传/留档（artifact/对象存储），且已脱敏。
4) **灰度可止损**：Feature Flag/分桶策略可一键关闭；回滚目标版本组合已写清。
5) **上线后验证**：至少跑 1 次端到端关键任务（含异常流），并把输出落进证据包。

### 回滚矩阵（Rollback Matrix）

| 触发场景 | 阈值/信号（示例） | 立即动作 | 验证动作 | 证据留档 |
| :--- | :--- | :--- | :--- | :--- |
| **致命崩溃** | 5xx 错误率 > 阈值 | 立即回滚到上一版 | 健康检查恢复 + 关键用例可用 | 错误日志 + 回滚记录 |
| **严重幻觉** | Bad case 激增/用户投诉集中 | 关闭特性开关或降级能力 | 抽样复测关键 Query | Bad case JSON + 截图 |
| **性能恶化** | P99 延迟 > 阈值 | 降级并发/缓存/模型，必要时回滚 | 观测曲线回落到基线 | 延迟指标导出 |
| **成本激增** | Token/调用量 > 预算线 | 限流 + 降级到更便宜路径 | 单位成本恢复到阈值内 | 用量报表 |
| **安全合规** | PII 泄露/越权/注入命中 | 紧急阻断入口 + 下线能力 | 红队复现并固定回归 | 攻击样本 + 审计日志 |

## D.6 最常见 12 个工程坑（现象→根因→复现→修复→回归）

1. **Prompt 漂移**
   - **现象**：场景 A 变好，但场景 B 彻底失效。
   - **根因**：Prompt 隐式耦合，且缺乏全局回归。
   - **最小复现**：只跑场景 A 的用例通过；一跑场景 B 回归集就失败。
   - **修复**：把“跨场景关键用例”固定进 L0 回归，并建立版本化评测集。
   - **回归验证**：全量回归通过率恢复到阈值，且失败样本已入库。

2. **上下文溢出**
   - **现象**：长对话/长文档触发 `context_length_exceeded` 或隐式截断导致答非所问。
   - **根因**：没做 token 预算与截断策略；检索/工具输出不受控。
   - **最小复现**：构造超长输入（或拼接多个长文档），观察报错或质量崩坏。
   - **修复**：上游做 token 计数 + 分段/滑窗；下游做摘要与引用合同。
   - **回归验证**：超长输入不崩溃，且能稳定产出“截断说明 + 可用答案”。

3. **结构化输出解析失败**
   - **现象**：看似输出了 JSON，但包含 Markdown 包裹/注释，解析直接崩溃。
   - **根因**：契约不硬（schema 不校验）或缺少重试/修复策略。
   - **最小复现**：让模型输出 ```` ```json {"ok": true} ``` ````，观察解析失败。
   - **修复**：启用严格模式（如 JSON-only）+ schema 校验；失败走“修复/重试/降级”分支。
   - **回归验证**：给一批脏输出样本，解析与校验能稳定产出结构化结果或明确失败。

4. **RAG 引用幻觉**
   - **现象**：回答很像真的，但引用的文档 ID 不存在或内容不匹配。
   - **根因**：引用标记由模型自由生成，未做后置校验。
   - **最小复现**：问只有文档 A 有答案的问题，模型却引用文档 B。
   - **修复**：引用必须来自检索上下文集合；生成后校验引用有效性，无效则重试或拒答。
   - **回归验证**：引用校验通过率达标；无效引用会被拦截并形成失败样本。

5. **密钥泄露**
   - **现象**：密钥/凭据被提交到仓库或写进日志。
   - **根因**：缺乏 pre-commit/CI secret scan；日志策略不脱敏。
   - **最小复现**：在代码/日志中可检索到疑似密钥模式（例如 `rg -n \"API_KEY|BEGIN PRIVATE|sk-\"`）。
   - **修复**：加 secret scan + 轮换密钥；日志脱敏与最小化。
   - **回归验证**：提交包含伪造密钥的改动被拦截；线上日志不再出现敏感字段。

6. **环境配置漂移**
   - **现象**：本地与线上行为不一致（例如线上仍指向旧模型/旧索引）。
   - **根因**：配置没纳入版本管理；生产环境靠手工改。
   - **最小复现**：本地 `MODEL_ID=model_v4`，线上仍是 `model_v3`。
   - **修复**：配置代码化并进入版本组合；每次发布输出配置 diff 进入证据包。
   - **回归验证**：对比运行环境与 `manifest.json` 一致；差异直接阻断发布。

7. **超时/重试不匹配**
   - **现象**：长输出被默认超时截断；重试导致重复扣费或重复写入。
   - **根因**：把 LLM 当普通 HTTP；缺少幂等键与预算熔断。
   - **最小复现**：生成长文本或故障注入，观察超时与重复副作用。
   - **修复**：区分流式/异步；写操作要求幂等；重试要受预算与次数约束。
   - **回归验证**：故障注入下不重复写入/扣费，且能在阈值内自动止损。

8. **测试集污染**
   - **现象**：离线分数极高，上线效果却很差。
   - **根因**：评测集泄漏进训练/RAG 索引；或样本与线上分布脱节。
   - **最小复现**：检索评测题，命中“答案原文”就在索引中。
   - **修复**：物理隔离数据；评测集版本化与访问控制；上线后用真实失败样本补齐。
   - **回归验证**：评测题在索引中不可直接命中；离线/线上指标相关性提升。

9. **非确定性导致的 Flaky Gate**
   - **现象**：同样代码，门禁有时过有时挂。
   - **根因**：采样温度不为 0；并发竞态；评测集/裁判漂移。
   - **最小复现**：同一门禁连续跑 10 次，结果不一致。
   - **修复**：门禁默认确定性（低温/固定种子）；对非确定评测用 N 次聚合判定。
   - **回归验证**：连续多次运行结论稳定；漂移会被记录为 L1 事件而非静默通过。

10. **流式渲染乱码/闪烁**
    - **现象**：Markdown 标记被切分导致渲染闪烁或乱码。
    - **根因**：前端把 chunk 当完整文本渲染，未做 buffer/增量解析。
    - **最小复现**：Mock 把 `**bold**` 拆成多个 chunk 返回，观察渲染问题。
    - **修复**：增量 buffer + 语法边界处理；必要时降级为纯文本。
    - **回归验证**：在弱网与大输出下渲染稳定，且不会破坏结构化区块。

11. **Schema/迁移不兼容**
    - **现象**：新代码依赖新字段，但数据库/索引迁移未完成，导致线上报错。
    - **根因**：迁移与部署时序错乱；缺少向后兼容策略。
    - **最小复现**：在旧 schema 上运行新版本触发 `Column not found`。
    - **修复**：遵循“先兼容、后切换”；迁移进入发布门禁并产证据。
    - **回归验证**：旧 schema + 新代码可运行；迁移完成后再打开新能力。

12. **错误吞没（Silent Failure）**
    - **现象**：调用失败但 UI 显示“成功”，用户拿到空内容或错误结果。
    - **根因**：过度 try/catch + 无日志/无用户提示；缺少失败分支设计。
    - **最小复现**：让调用失败（断网/无权限/预算越界），观察 UI 与日志是否能解释。
    - **修复**：失败必须可见：日志 + 埋点 + 用户可恢复入口（重试/降级/反馈）。
    - **回归验证**：故障注入下能稳定产出“失败原因 + 下一步动作 + 证据记录”。
