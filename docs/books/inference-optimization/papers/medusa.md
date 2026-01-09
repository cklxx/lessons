# Medusa：多解码头投机加速框架

原文链接： [Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads](https://arxiv.org/abs/2401.10774) [7]

## 论文信息
- 年份：2024 [7]
- 作者：Tianle Cai, Yuhong Li, Zhengyang Geng, Hongwu Peng, Jason D. Lee, Deming Chen, Tri Dao [7]
- 作者背景（研究领域）：多头解码/推理加速/系统优化 [7]
- 前后血缘关系（同主题）：前序：[Speculative Sampling](speculative-sampling.md)；后续：[EAGLE-3](eagle-3.md) [7]

## 主旨
Medusa 的主旨是把“草稿模型”内嵌为多个解码头，在单模型内并行预测多个 token，从而减少解码步数。[7]

## 背景与问题定义
投机解码通常需要额外 drafter 模型，维护与部署成本高，且 drafter 与目标模型易发生分布差异。[7]
论文提出：能否在不引入独立草稿模型的前提下，实现多 token 预测并保持输出质量。[7]

## 方法与机制
Medusa 在主模型上添加多个解码头，通过树状注意力生成候选 continuation，并在同一步完成验证。[7]
给出了 Medusa-1（冻结主干）与 Medusa-2（联合微调）两种训练策略，以及接受率提升的验证机制。[7]

## 实验与结果
实验显示 Medusa-1 在保持质量的情况下实现 >2.2× speedup，Medusa-2 进一步提升到 2.3–3.6×。[7]
结果证明多头预测可以在单模型内获得可观的推理加速收益。[7]

## 关键数据结果
- Medusa-1 实现超过 2.2× speedup（lossless）。[7]
- Medusa-2 speedup 达 2.3–3.6×。[7]

## 工程启示（优化点）
- 用多解码头替代独立 drafter，降低系统复杂度。[7]
- 根据质量/速度需求选择 Medusa-1 或 Medusa-2。[7]
- 采用树状验证提升接受率。[7]
- 结合自蒸馏解决缺少训练数据的问题。[7]

## 局限与延伸
多头结构带来额外参数与训练开销，且速度收益依赖 head 预测质量与任务分布。[7]
后续可探索更轻量的多头结构与与其他投机策略的组合。[7]
