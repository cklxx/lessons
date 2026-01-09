# PagedAttention / vLLM：KV 缓存的分页管理

原文链接： [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) [10]

## 论文信息
- 年份：2023 [10]
- 作者：Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica [10]
- 作者背景（研究领域）：LLM Serving/内存管理/系统优化 [10]
- 前后血缘关系（同主题）：前序：[FlashAttention-2](flashattention-2.md)；后续：无 [10]

## 主旨
PagedAttention/vLLM 的主旨是用操作系统式分页管理 KV 缓存，减少碎片与冗余，从而提升服务吞吐。[10]

## 背景与问题定义
高吞吐服务依赖大批量请求，但 KV 缓存随序列动态增长、收缩，导致碎片与冗余浪费，限制 batch 大小。[10]
论文的问题是：如何把 KV 缓存管理变成可扩展的系统机制，使吞吐提升不以延迟为代价。[10]

## 方法与机制
PagedAttention 采用虚拟内存分页思想，把 KV 缓存分块管理并支持共享，避免连续内存分配带来的浪费。[10]
vLLM 在此基础上实现灵活 batching 与缓存复用，使系统层面能更高效地利用显存。[10]

## 实验与结果
评测显示 vLLM 在保持相同延迟的前提下，实现 2–4× 吞吐提升，且对长序列与复杂解码更显著。[10]
结果强调推理优化不仅是内核问题，还需要系统级内存与调度机制。[10]

## 关键数据结果
- 与 FasterTransformer、Orca 相比，吞吐提升 2–4×，延迟水平保持一致。[10]

## 工程启示（优化点）
- 用分页方式管理 KV 缓存，降低碎片与复制开销。[10]
- 支持 KV 共享与复用，提升批量推理效率。[10]
- 把吞吐/延迟指标放在服务层整体评估，而非仅模型内核。[10]

## 局限与延伸
PagedAttention 的收益依赖请求分布与序列长度，且系统集成成本较高。[10]
未来可以结合更多解码策略与模型并行机制，形成端到端 serving 优化链路。[10]
