# AI 校对与审稿 SOP（使用 `gemini -p`）

> 目标：让 AI 做“校对、找漏洞、补例子、查一致性”，而不是替代作者决策；所有建议必须能回到“可验收的改动”。

## 1) 最小输入原则（避免上下文过载）
- 只给与任务直接相关的段落（通常 30–120 行），附带：章节目标、读者预期、约束（术语/结构/输出格式）。
- 对代码类内容：附“验证命令/失败判定/禁止改动范围”（例如“禁止改实现，只能补测试”）。

## 2) 常用审稿任务（可直接复制）

### 2.1 结构一致性检查
```bash
target_file="docs/books/ai-assisted-software-product/chapter-01-demand.md"
excerpt=$(sed -n '1,160p' "$target_file")
prompt=$(cat <<'EOF'
你是中文技术书编辑。请检查以下章节是否缺少：章节定位/你将收获什么/方法论速览/实战路径/复现检查/常见陷阱/延伸练习/交付物与验收/深度解析：核心原则。
输出：缺失项列表 + 建议补写的 3 条要点（每条一句话，带验收标准）。

章节内容：
<<<
EOF
)
prompt+="$excerpt"
prompt+=$'\n>>>\n'
gemini -p "$prompt"
```

### 2.2 逻辑漏洞与反例补全
```bash
target_file="docs/books/ai-assisted-software-product/chapter-01-demand.md"
excerpt=$(sed -n '1,200p' "$target_file")
prompt=$(cat <<'EOF'
你是资深审稿人。请针对下面文本找出：隐含前提、可能的反例、会导致读者误用的表达，并给出“如何改写一句话就能更严谨”的修改建议（最多 8 条）。

文本：
<<<
EOF
)
prompt+="$excerpt"
prompt+=$'\n>>>\n'
gemini -p "$prompt"
```

### 2.3 给某小节补一个“可复制示例”
```bash
target_file="docs/books/ai-assisted-software-product/chapter-04-workflow.md"
excerpt=$(sed -n '20,120p' "$target_file")
prompt=$(cat <<'EOF'
你是中文技术书写作者。请基于下面的小节内容，补一个“示例（可复制）”，必须包含：目标/上下文/约束/输出格式/验证命令/失败判定/回滚。
要求：能直接粘贴进 Markdown；不要出现需要联网或依赖未声明工具的步骤。

小节内容：
<<<
EOF
)
prompt+="$excerpt"
prompt+=$'\n>>>\n'
gemini -p "$prompt"
```

## 3) 采纳规则（作者作为裁判）
- 只采纳能落到“可验收改动”的建议（新增示例、补步骤、改标题、补约束、补失败判定）。
- 对“工具/框架推荐”默认谨慎：优先保留范式与可迁移原则，工具清单放附录。
- 任何涉及安全/合规的建议：必须补一句“边界条件/前置假设”，避免被当成通用结论。

## 4) 实用提醒
- **长文本分块**：对整章审阅，优先按小节分块（`sed -n` 取 100–200 行），避免提示过长导致输出发散或命令行参数过大。
- **保存审稿结果**：需要留档时用 `| tee` 保存输出（示例：`gemini -p \"$prompt\" | tee review.md`）。
