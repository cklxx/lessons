# Graph of Thoughts：图结构推理

原文链接： [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687) [91]

## 论文信息
- 年份：2023 [91]
- 作者：Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michal Podstawski, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, Torsten Hoefler [91]
- 作者背景（研究领域）：高性能计算/结构化推理 [91]
- 前后血缘关系（同主题）：前序：[Tree of Thoughts](tree-of-thoughts.md)；后续：无（图式推理方向代表）

## 主旨
Graph of Thoughts 的主旨是把推理结构从树扩展为图，让多个推理分支共享子问题与中间结论，从而减少重复推理并提高复杂任务的效率。[91]

## 背景与问题定义
论文认为树结构容易产生重复子问题，导致推理冗余。随着任务复杂度提升，需要更灵活的结构来复用中间结果。图结构能够表达合并与重用关系，更适合复杂推理与组合任务。[91]

## 方法与机制
Graph of Thoughts 将推理步骤视为图中的节点，边表示推理依赖。模型可以在图中扩展新节点，也可以复用已有节点作为后续推理的输入。该框架允许多条推理路径共享相同子结论，提升整体效率。[91]

## 实验与结果
论文在多步推理与规划任务上验证图结构的优势，显示在相同预算下，图式推理比树式推理更容易得到高质量解答，尤其在存在共享子问题的场景中收益明显。[91]

## 关键数据结果
- 图式推理在多步复杂任务上提升了解题效率与稳定性。[91]

## 工程启示（优化点）
- 显式建模子问题依赖，减少重复推理。
- 将关键中间结论写入共享记忆，便于复用。
- 用节点级评分控制图扩展，避免图爆炸。
- 结合搜索预算与合并策略平衡质量与成本。

## 局限与延伸
Graph of Thoughts 需要更复杂的状态管理与节点合并策略，系统实现成本高于树结构。若节点评估不可靠，图也会膨胀失控。延伸方向包括：自动化节点合并策略、与工具调用协同的图搜索，以及在多代理场景下的共享推理图。[91]
