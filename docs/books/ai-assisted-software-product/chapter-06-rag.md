# 第 6 章：RAG（检索增强生成）—— 赋予 AI 记忆

> 通过向量检索 + 重排序 + 过滤策略，让模型回答始终“有出处、有证据、有稳定延迟”。[24][25][27][28]

!!! note "关于复现、目录与 CI"
    本章中出现的 `make ...`、`CI`、以及示例目录/文件路径（例如 `path/to/file`）均为落地约定，用于说明如何把方法落实到你自己的工程仓库中。本仓库仅提供文档，读者需自行实现或用等价工具链替代。

## 章节定位
本章解决“模型记不住/答不准”的问题。你将搭建完整的 RAG 管线：数据清洗、切分、索引、检索、重排序与引用追踪，并用自动化评估量化改动收益。[24][28]

## 你将收获什么
- 可切换的向量数据库方案（Milvus/Pinecone/pgvector），附性能与成本对比。[25]
- 语义分块、BM25 + 向量混合检索、重排序的组合策略与可复现脚本。[24][27]
- RAGAS/LLM-as-a-Judge 评测流水线，量化准确率、引用率与延迟。[28]

## 方法论速览
1. **数据处理：** PDF/Markdown 清洗、语义分块、元数据对齐，确保来源可追踪。[24]
2. **检索策略：** 混合检索（BM25 + 向量）、查询重写、重排序，兼顾召回与精度。[27]
3. **评估闭环：** 构建问答对与引用检查，RAGAS 自动评分，失败则回滚配置。[28]

## 实战路径
### 1. 数据清洗与分块
- 使用 `langchain`/`llamaindex` 解析 PDF/Markdown，去除页眉页脚与目录噪声。
- 采用语义分块（按主题/标题）+ 固定长度混合策略，块内保留来源页码。

### 2. 索引与检索
```python
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores import MilvusVectorStore

index = VectorStoreIndex.from_documents(docs, vector_store=MilvusVectorStore())
query_engine = index.as_query_engine(similarity_top_k=5)
print(query_engine.query("How to handle retries?"))
```
- 对比 Pinecone/Milvus/pgvector：记录建库时间、QPS、P95 延迟、存储成本。[25]
- 结合 BM25/keyword 检索做混合召回，减少语义漂移。

### 3. 重排序与引用
- 使用 Cross-Encoder（如 `cross-encoder/ms-marco-MiniLM-L-6-v2`）重排序 top-K 结果。
- 在生成阶段强制输出引用（原文片段与页码），引用缺失即判定失败。

### 4. 自动评估
- 构造 100–200 对问答基准，标注参考答案与允许的引用片段。
- 运行 RAGAS/LLM-as-a-Judge，指标包含 Faithfulness、Answer Correctness、Context Precision。[28][50]

## 复现检查（落地建议）
- `make rag-build`：清洗、切分、索引与基准数据生成。
- `make rag-eval`：执行 RAGAS 评估并输出 CSV；低于阈值自动退回上一个版本。
- CI 存档检索延迟与成本对比表，便于决策。

## 常见陷阱
- **块过长/过短：** 过长导致噪声，过短导致上下文断裂，需结合语义与长度混合。
- **引用缺失：** 生成模型未携带来源，需在模板中强制格式，并在评测中处罚。
- **数据漂移：** 文档更新未重建索引，需设定增量刷新与一致性校验。

## 延伸练习
- 对比 Dense Retriever（E5/ColBERT）与 Sparse（BM25）在你数据集上的指标差异。
- 尝试基于 rerank 模型蒸馏一个轻量 Cross-Encoder，验证延迟下降幅度。

## 交付物与验收（落地建议）
- 清洗脚本、切分配置与索引构建脚本；所有步骤可重放。
- 评估报告（RAGAS + 真实用户问答）；性能与成本对比表。
- 生成提示模板与引用格式说明，缺失引用的响应在 CI 中视为失败。

## 参考
详见本书统一参考文献列表：[`references.md`](references.md)。
