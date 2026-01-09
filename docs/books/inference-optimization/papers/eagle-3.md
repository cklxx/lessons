# EAGLE-3：训练时测试驱动的投机解码加速

原文链接： [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://arxiv.org/abs/2503.01840) [1]

## 论文信息
- 年份：2025 [1]
- 作者：Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang [1]
- 作者背景（研究领域）：投机解码/推理加速/系统优化 [1]
- 前后血缘关系（同主题）：前序：[Speculative Sampling](speculative-sampling.md)、[Medusa](medusa.md)；后续：无 [1]

## 主旨
EAGLE-3 的主旨是打破特征预测瓶颈，把投机解码草稿阶段改为直接 token 预测，并通过 training-time test 融合多层特征，提高接受率与加速上限。[1]

## 背景与问题定义
投机解码的收益高度依赖草稿接受率，传统 EAGLE 依赖特征预测导致数据规模提升难以转化为更高加速。[1]
论文将问题定义为：如何让草稿模型真正受益于数据扩展，并把算法收益体现在真实吞吐指标上。[1]

## 方法与机制
EAGLE-3 放弃特征预测，转向直接 token 预测，同时引入 training-time test 来融合多层表示并抑制误差累积。[1]
在解码阶段保留投机验证流程，确保输出分布一致性与速度收益同时成立。[1]

## 实验与结果
作者在五个任务上评测，包括聊天与推理模型，EAGLE-3 的 speedup 与接受长度显著提升。[1]
系统层实验显示其在 SGLang 服役框架中可带来吞吐提升，证明算法收益能传导到服务端指标。[1]

## 关键数据结果
- speedup ratio 最高达 6.5×，较 EAGLE-2 提升约 1.4×。[1]
- 在 SGLang 中，batch size=64 时吞吐提升 1.38×。[1]
- 评测覆盖 5 个任务，包含聊天与推理场景。[1]

## 工程启示（优化点）
- 将草稿阶段从特征预测转为 token 预测，降低误差累积。[1]
- 通过多层特征融合提高接受率，扩大加速上限。[1]
- 用吞吐指标验证真实收益，而非只看 speedup。[1]
- 扩大草稿训练数据规模时同步优化草稿结构与验证策略。[1]

## 局限与延伸
EAGLE-3 依赖 training-time test 与多层融合机制，增加训练与实现复杂度，且速度提升仍受接受率与硬件并行度影响。[1]
后续可探索与不同解码策略、硬件平台和长上下文场景的组合，以检验其普适性与稳定性。[1]
