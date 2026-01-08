# Enabling Claude Code to work more autonomously

- URL: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
- Retrieved: 2026-01-08T05:11:39.017249+00:00

----

[Skip to main content][Skip to footer]
(https://www.anthropic.com/)
  * [Research](https://www.anthropic.com/research)
  * [Economic Futures](https://www.anthropic.com/economic-futures)
  * Commitments
  * Learn
  * [News](https://www.anthropic.com/news)


[Try Claude](https://claude.ai/)
Product
# Enabling Claude Code to work more autonomously
Sep 29, 2025
We’re introducing several upgrades to Claude Code: a native VS Code extension, version 2.0 of our terminal interface, and checkpoints for autonomous operation. Powered by [Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5), Claude Code now handles longer, more complex development tasks in your terminal and IDE.
## Claude Code on more surfaces
****
**VS Code extension**
We’re introducing a [native VS Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) in beta that brings Claude Code directly into your IDE. You can now see Claude’s changes in real-time through a dedicated sidebar panel with inline diffs. The extension provides a richer, graphical Claude Code experience for users who prefer to work in IDEs over terminals.
****
**Enhanced terminal experience**
We’ve also refreshed Claude Code’s terminal interface. The updated interface features improved status visibility and searchable prompt history (Ctrl+r), making it easier to reuse or edit previous prompts.
**Claude Agent SDK**
For teams who want to create custom agentic experiences, the Claude Agent SDK (formerly the Claude Code SDK) gives access to the same core tools, context management systems, and permissions frameworks that power Claude Code. We’ve also released SDK support for subagents and hooks, making it more customizable for building agents for your specific workflows.
Developers are [already building agents](https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) for a broad range use cases with the SDK, including financial compliance agents, cybersecurity agents, and code debugging agents.
## Execute long-running tasks with confidence
As Claude Code takes on increasingly complex tasks, we're releasing a checkpointing feature to help delegate tasks to Claude Code with confidence while maintaining control. Combined with recent feature releases, Claude Code is now more capable of handling sophisticated tasks.
**Checkpoints**
Complex development often involves exploration and iteration. Our new checkpoint system automatically saves your code state before each change, and you can instantly rewind to previous versions by tapping Esc twice or using the /rewind command. Checkpoints let you pursue more ambitious and wide-scale tasks knowing you can always return to a prior code state.
When you rewind to a checkpoint, you can choose to restore the code, the conversation, or both to the prior state. Checkpoints apply to Claude’s edits and not user edits or bash commands, and we recommend using them in combination with version control.
**Subagents, hooks, and background tasks**
Checkpoints are especially useful when combined with Claude Code’s latest features that power autonomous work:
  * **Subagents** delegate specialized tasks—like spinning up a backend API while the main agent builds the frontend—allowing parallel development workflows
  * **Hooks** automatically trigger actions at specific points, such as running your test suite after code changes or linting before commits
  * **Background** **tasks** keep long-running processes like dev servers active without blocking Claude Code’s progress on other work


Together, these capabilities let you confidently delegate broad tasks like extensive refactors or feature exploration to Claude Code.
## Getting started
These updates are available now for Claude Code users.
  * **Claude Sonnet 4.5** is the new default model in Claude Code. Run /model to switch models
  * **VS Code extension**(beta)**:** Download from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) to get started
  * **Terminal updates** , including the visual refresh and checkpoints, are available to all Claude Code users—just update your local installation
  * **Claude Agent SDK:**[See the docs](https://docs.claude.com/en/api/agent-sdk/overview) to get started


(https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)(https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)
## Related content
### Sharing our compliance framework for California's Transparency in Frontier AI Act
[Read more](https://www.anthropic.com/news/compliance-framework-SB53)
### Working with the US Department of Energy to unlock the next era of scientific discovery
[Read more](https://www.anthropic.com/news/genesis-mission-partnership)
### Protecting the well-being of our users
[Read more](https://www.anthropic.com/news/protecting-well-being-of-users)
(https://www.anthropic.com/)
### Products
  * [Claude](https://claude.com/product/overview)
  * [Claude Code](https://claude.com/product/claude-code)
  * [Claude in Chrome](https://claude.com/chrome)
  * [Claude in Excel](https://claude.com/claude-in-excel)
  * [Claude in Slack](https://claude.com/claude-in-slack)
  * [Skills](https://www.claude.com/skills)
  * [Max plan](https://claude.com/pricing/max)
  * [Team plan](https://claude.com/pricing/team)
  * [Enterprise plan](https://claude.com/pricing/enterprise)
  * [Download app](https://claude.ai/download)
  * [Pricing](https://claude.com/pricing)
  * [Log in to Claude](https://claude.ai/)


### Models
  * [Opus](https://www.anthropic.com/claude/opus)
  * [Sonnet](https://www.anthropic.com/claude/sonnet)
  * [Haiku](https://www.anthropic.com/claude/haiku)


### Solutions
  * [AI agents](https://claude.com/solutions/agents)
  * [Code modernization](https://claude.com/solutions/code-modernization)
  * [Coding](https://claude.com/solutions/coding)
  * [Customer support](https://claude.com/solutions/customer-support)
  * [Education](https://claude.com/solutions/education)
  * [Financial services](https://claude.com/solutions/financial-services)
  * [Government](https://claude.com/solutions/government)
  * [Life sciences](https://claude.com/solutions/life-sciences)
  * [Nonprofits](https://claude.com/solutions/nonprofits)


### Claude Developer Platform
  * [Overview](https://claude.com/platform/api)
  * [Developer docs](https://platform.claude.com/docs)
  * [Pricing](https://claude.com/pricing#api)
  * [Regional Compliance](https://claude.com/regional-compliance)
  * [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
  * [Google Cloud’s Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)
  * [Console login](http://console.anthropic.com/)


### Learn
  * [Blog](https://claude.com/blog)
  * [Claude partner network](https://claude.com/partners)
  * [Connectors](https://claude.com/connectors)
  * [Courses](https://www.anthropic.com/learn)
  * [Customer stories](https://claude.com/customers)
  * [Engineering at Anthropic](https://www.anthropic.com/engineering)
  * [Events](https://www.anthropic.com/events)
  * [Powered by Claude](https://claude.com/partners/powered-by-claude)
  * [Service partners](https://claude.com/partners/services)
  * [Startups program](https://claude.com/programs/startups)
  * [Tutorials](https://claude.com/resources/tutorials)
  * [Use cases](https://claude.com/resources/use-cases)


### Company
  * [Anthropic](https://www.anthropic.com/company)
  * [Careers](https://www.anthropic.com/careers)
  * [Economic Futures](https://www.anthropic.com/economic-index)
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
  * [Security and compliance](https://trust.anthropic.com/)
  * [Transparency](https://www.anthropic.com/transparency)


### Help and security
  * [Availability](https://www.anthropic.com/supported-countries)
  * [Status](https://status.anthropic.com/)
  * [Support center](https://support.claude.com/en/)


### Terms and policies
  * [Privacy policy](https://www.anthropic.com/legal/privacy)
  * [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
  * [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
  * [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
  * [Usage policy](https://www.anthropic.com/legal/aup)


© 2025 Anthropic PBC
  * (https://www.linkedin.com/company/anthropicresearch)
  * (https://x.com/AnthropicAI)
  * (https://www.youtube.com/@anthropic-ai)


Enabling Claude Code to work more autonomously
