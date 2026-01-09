# SayCan：语言规划与可行性分离

原文链接： [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) [71]

## 论文信息
- 年份：2022 [71]
- 作者：Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Omar Cortes, Byron David, Chelsea Finn, Chuyuan Fu, Keerthana Gopalakrishnan, Karol Hausman, Alex Herzog, Daniel Ho, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Eric Jang, Rosario Jauregui Ruano, Kyle Jeffrey, Sally Jesmonth, Nikhil J Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Kuang-Huei Lee, Sergey Levine, Yao Lu, Linda Luu, Carolina Parada, Peter Pastor, Jornell Quiambao, Kanishka Rao, Jarek Rettinghouse, Diego Reyes, Pierre Sermanet, Nicolas Sievers, Clayton Tan, Alexander Toshev, Vincent Vanhoucke, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Mengyuan Yan, Andy Zeng [71]
- 作者背景（研究领域）：机器人/具身智能规划 [71]
- 前后血缘关系（同主题）：前序：[ALFWorld](alfworld.md)；后续：[Voyager](voyager.md)

## 主旨
SayCan 的主旨是把高层语言规划与低层可行性判断分离。LLM 负责提出“能做什么”的计划，而机器人或环境模型负责判断“是否可做”，从而让规划既有灵活性又具可执行性。[71]

## 背景与问题定义
论文针对机器人任务中的常见问题：语言模型能生成合理计划，但缺乏对物理约束的感知，导致不可执行的动作序列。作者希望通过可行性模型约束行动选择，把安全性与实际可执行性纳入决策过程。[71]

## 方法与机制
论文提出“Say（语言规划）+ Can（可行性过滤）”的机制。LLM 生成多个候选动作或子目标，随后由可行性模型对每个候选进行评分，选择最可执行的一项。该设计避免了语言模型直接控制动作的风险，把安全性与可靠性放在外部约束层。[71]

## 实验与结果
作者在机器人任务中验证了该框架，展示了它在复杂操作上的稳定性优势。实验指出：即使语言模型的规划偶尔偏离真实环境，依靠可行性模型过滤仍能大幅提升成功率。论文核心贡献是证明“可行性约束”是具身代理可靠性的关键因素。[71]
此外，实验还表明，当可行性模型提供更精细的评分而非二元过滤时，系统能保持灵活性并减少误拒，这提示工程上应优先优化可行性评分而非硬规则。[71]

## 关键数据结果
- 在 101 个真实机器人任务上，PaLM-SayCan 在训练环境中的规划成功率 84%、执行成功率 74%；迁移到真实厨房时为 81%/60%。[71]
- 技能库包含 551 个技能，覆盖 7 个技能族与 17 个对象；实验环境使用 15 个对象与 5 个位置。[71]
- 错误来源分析显示，长任务失败中约 65% 来自 LLM 规划错误，35% 来自可行动作/执行可行性错误。[71]


## 工程启示（优化点）
- 规划阶段生成多个候选动作，而非单一路径。
- 用独立模块对候选动作进行安全与可行性打分。
- 在提示中引入环境约束，降低无效动作生成。
- 记录被过滤的动作，为后续改进提供数据。
- 将可行性评分显式回馈规划器，形成闭环。

## 局限与延伸
SayCan 依赖高质量的可行性模型，若过滤器不准可能导致过度保守或错误执行。该框架也假设动作空间可被穷举或采样，现实环境中可能难以满足。还需要处理“可行但不优”的动作排序问题，可行性模型与语言规划的分布漂移也会累积误差。延伸方向包括：用学习式可行性模型适配复杂环境、在规划阶段引入不确定性估计、以及把该范式扩展到软件工具与 API 调用场景。[71]
