# Speculative Sampling：投机采样加速大模型解码

原文链接： [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318) [2]

## 论文信息
- 年份：2023 [2]
- 作者：Charlie Chen, Sebastian Borgeaud, Geoffrey Irving, Jean-Baptiste Lespiau, Laurent Sifre, John Jumper [2]
- 作者背景（研究领域）：投机解码/采样算法/推理系统 [2]
- 前后血缘关系（同主题）：前序：[SpecDec](speculative-decoding.md)；后续：[Online Speculative Decoding](online-speculative-decoding.md)、[Staged Speculative Decoding](staged-speculative-decoding.md)、[ParallelSpec](parallelspec.md) [2]

## 主旨
论文提出 speculative sampling，通过草稿模型生成短续写并用目标模型并行验证，实现多 token 生成同时保持目标分布一致性。[2]

## 背景与问题定义
自回归解码每步都要访问大模型参数，导致推理延迟高；而直接并行生成会破坏目标分布。[2]
作者将问题表述为：如何在不修改目标模型的前提下，用更快的草稿模型生成候选并保持分布一致性。[2]

## 方法与机制
草稿模型生成候选 token 序列，目标模型在一次前向中评估这些候选，并通过改造的拒绝采样决定接受长度。[2]
若任一步被拒绝，则回退到目标模型采样，保证最终输出严格匹配目标分布。[2]

## 实验与结果
论文以 Chinchilla 70B 为目标模型进行基准测试，在分布式设置下获得显著速度提升且样本质量保持一致。[2]
实验强调：草稿与目标模型分布接近度直接决定接受率，是 speedup 的核心驱动因素。[2]

## 关键数据结果
- 在 Chinchilla 70B 上实现 2–2.5× 解码速度提升（分布式设置）。[2]
- 速度提升在不修改目标模型的前提下获得，样本质量未下降。[2]

## 工程启示（优化点）
- 草稿模型质量与接受率是 speedup 的主要杠杆。[2]
- 并行验证减少目标模型调用次数，提升整体吞吐。[2]
- 用拒绝采样维持分布一致性，避免速度—质量二选一。[2]
- 部署时评估“速度-接受率曲线”而非单点 speedup。[2]

## 局限与延伸
速度收益依赖草稿与目标模型的能力差距，差距过大时接受率下降导致收益消失。[2]
后续研究围绕“草稿更聪明”和“验证更轻量”展开，如在线蒸馏与并行草稿等方向。[2]
