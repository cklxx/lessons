# Deep Research: [55] Lighthouse：把网页质量变成客观分数

- Source: https://developer.chrome.com/docs/lighthouse/
- Note: ../notes/ref-055-lighthouse.md
- Snapshot: ../sources/md/developer-chrome-com-docs-lighthouse-1b45ffb23796.md
## TL;DR
Lighthouse 是 Google 开源的自动化网页质量审计工具，它将性能、可访问性、SEO 等主观体验转化为客观评分与改进建议，是 AI 生成代码质量验证的关键自动化门禁。

## 核心观点
1.  **质量量化与客观化**：将网页加载快慢这种主观感受，转化为 LCP（最大内容绘制）、TBT（总阻塞时间）等可量化的 Core Web Vitals 指标。
2.  **多维度审计**：不仅关注性能（Performance），还强制覆盖可访问性（Accessibility）、最佳实践（Best Practices）、SEO 和 PWA，防止偏科。
3.  **开发周期的全覆盖**：支持在 Chrome DevTools（本地调试）、CLI（CI/CD 流水线）和 PageSpeed Insights（线上环境）中运行。
4.  **作为 AI 代码的质检员**：在 AI 辅助编程场景下，Lighthouse 是验证 AI 生成的前端代码是否符合工业标准的最高效自动判卷机。
5.  **行动导向**：不仅给出分数，还直接列出导致扣分的问题代码（如未压缩的图片、阻塞渲染的 JS）及修复文档。
6.  **门禁思维**：通过设定性能预算（Performance Budget），在代码合入阶段自动拦截导致性能退化的变更。

## 可落地做法

### 1. 产品经理（定义标准）
*   在 PRD 的非功能需求（NFR）中明确 Lighthouse 阈值。
    *   *示例*：所有新页面的 Lighthouse 性能评分在移动端不得低于 80 分，可访问性必须达到 100 分。

### 2. 研发工程师（开发与集成）
*   **本地自测**：开发过程中使用 Chrome DevTools 的 Lighthouse 面板（建议使用无痕模式）进行即时反馈。
*   **流水线集成**：使用 Lighthouse CI (LHCI)。
    *   *步骤 1*：安装 `@lhci/cli`。
    *   *步骤 2*：配置 `.lighthouserc.json`，设置 `assert` 规则（如 `categories:performance: ["error", {minScore: 0.9}]`）。
    *   *步骤 3*：在 GitHub Actions 或 GitLab CI 中添加审计步骤，构建失败即阻止合并。

### 3. 测试/QA（验收）
*   建立基准环境：确保测试时的网络条件（如 Throttling 到 4G）和设备性能一致，避免分数波动。
*   对比测试：定期跑竞品网站的分数，作为优化的参考坐标。

## 检查清单：Lighthouse 质量门禁

### 准备工作
- [ ] **环境纯净**：是否在 Chrome 无痕模式或通过 CLI 运行（避免浏览器插件干扰）？
- [ ] **网络模拟**：是否开启了统一的网络限速（如 Mobile 4G）？
- [ ] **构建版本**：是否针对 Production Build（生产环境构建包）进行测试（开发环境包通常性能较差）？

### 核心指标核查
- [ ] **Performance**：总分是否 > 90（或符合项目基准）？
    - [ ] LCP (Largest Contentful Paint) 是否 < 2.5s？
    - [ ] CLS (Cumulative Layout Shift) 是否 < 0.1？
- [ ] **Accessibility**：总分是否为 100？（AI 生成代码容易丢失 ARIA 标签，需重点检查）
    - [ ] 图片是否有 `alt` 属性？
    - [ ] 按钮是否有清晰的 label？
    - [ ] 颜色对比度是否达标？
- [ ] **Best Practices**：
    - [ ] 控制台是否有报错？
    - [ ] 是否使用 HTTPS？
- [ ] **SEO**：
    - [ ] 页面是否有 `<meta name="viewport">`？
    - [ ] 页面标题和描述是否完整？

## 常见坑与对策

| 常见坑 | 解释 | 对策 |
| :--- | :--- | :--- |
| **插件干扰** | 浏览器插件（如广告拦截、翻译）会注入代码，严重影响 Performance 和 Best Practices 分数。 | 强制使用**无痕模式**（Incognito）或使用 CLI 工具运行。 |
| **分数波动** | 同样的页面连跑几次分数不同，受本地 CPU/网络波动影响。 | 在 CI 中使用 Docker 容器固定环境；本地测试时运行至少 3 次取平均值（Lighthouse CLI 支持 `--runs` 参数）。 |
| **开发环境测分** | 对着 `localhost` 的热更新（HMR）版本测分，JS 包未压缩，分数极低且无意义。 | 务必执行 `npm run build` 后，对着 `dist/` 目录启动本地服务进行测试。 |
| **唯分数论** | 为了刷分采用了作弊手段（如针对 User-Agent 优化），但用户体验并未提升。 | Lighthouse 只是模拟实验数据，需结合 RUM（真实用户监控）数据综合判断。 |

## 可用于丰富《AI 辅助软件产品》的写作点

*   **第 3 章（UI/UX 设计）- 生成式 UI 的质量底线**：
    *   在讨论AI 生成 UI时，引入 Lighthouse 作为**客观审美与工程质量的仲裁者**。AI 生成的界面不仅要像样，还要好用。可以通过截图对比：一个 AI 生成的看起来很美但在 Lighthouse 只有 50 分的页面（大图未压缩、HTML 结构混乱），VS 经过优化后 95 分的页面。
*   **第 4 章（工程与质量）- 自动化门禁**：
    *   在AI 时代的 TDD（测试驱动开发）小节中，将 Lighthouse 审计作为 Frontend Ops 的一部分。强调在 AI 极速生成大量代码的背景下，人工 Review 性能已不可能，必须依赖 Lighthouse CI 这样的工具守门。
*   **第 18 章（评估与迭代）**：
    *   将 Lighthouse 分数作为评估 AI 编码能力（Coding Agent）的指标之一。例如，提示词工程的优化目标可以是：编写一个 React 组件，要求 Lighthouse 可访问性得分为 100。
