# External Link Index

This document records external links related to the "AI-Assisted Software Product" book. Add URLs as they are discovered; no need to download article contents. All link lists now live under `docs/materials/ai-assisted-software-product/raw/` (moved out of the book folder).

## How to use this index
- Keep links organized by the book's major areas.
- Capture lightweight metadata only (title, URL, source/domain, publication date if known).
- Rate each link on multiple dimensions to support later prioritization.
- Within each category, sort rows by the total score (highest first).

## Scoring dimensions (0.0–1.0)
- **Relevance**: How closely the link matches the book's topic.
- **Authority**: Credibility of the source (e.g., well-known orgs, academic, industry leaders).
- **Recency**: How up-to-date the content is.
- **Completeness**: Depth and coverage of key points.
- **Readability**: Clarity, structure, and signal-to-noise ratio.

Total score can be a weighted sum (e.g., 0.35·Relevance + 0.25·Authority + 0.15·Recency + 0.15·Completeness + 0.10·Readability). The CSVs also include a "Score Reason" column that explains why each dimension received its value.

## How to collect 3,000+ links quickly
Use the helper script at `tools/link_harvester.py` to bulk-fetch results from a search API (Bing Web Search or compatible endpoint). For a smaller batch (e.g., 500 links) without an API key, switch to the DuckDuckGo provider or the Hacker News provider (`--provider hn`).

1. Prepare an API key (e.g., `BING_SEARCH_KEY`) and ensure internet access is allowed. If you do not have an API key, use `--provider duckduckgo` or `--provider hn` (Hacker News Algolia API).
2. Run the script with broad + long-tail queries: `python tools/link_harvester.py --api-key "$BING_SEARCH_KEY" --out docs/materials/ai-assisted-software-product/raw/link-index-batch1.csv`.
3. For a quick 500-link pass without a key and with URL dedupe against existing batches: `python tools/link_harvester.py --provider hn --target-count 500 --pages-per-query 8 --page-size 50 --seed-file docs/materials/ai-assisted-software-product/raw/link-index-batch1.csv --out docs/materials/ai-assisted-software-product/raw/link-index-batch2.csv`.
4. For later passes, dedupe against all prior batches via the combined seed file: `python tools/link_harvester.py --provider hn --target-count 500 --pages-per-query 12 --page-size 50 --seed-file docs/materials/ai-assisted-software-product/raw/link-index-seeds.csv --out docs/materials/ai-assisted-software-product/raw/link-index-batch3.csv`.
5. The script iterates over thematic keyword bundles, requests results, deduplicates by URL (including any `--seed-file`), auto-categorizes, computes heuristic scores, writes per-dimension reasons, and saves a CSV you can sort or import back into this Markdown file.
6. If you need more coverage, increase `--pages-per-query` or add queries via `--extra-query-file queries.txt` (one query per line).

### Taxonomy (for automatic + manual tagging)
- **Discovery & Product Strategy**: market research, problem discovery, product strategy, positioning, pricing, monetization, user research.
- **Prototyping & UX**: wireframes, design systems, UX writing, usability testing, AI-first UX, prompt-based UX.
- **Engineering & Tooling**: SDLC, CI/CD, platform engineering, SDKs, frameworks, security, performance.
- **Data, RAG, and Agents**: data pipelines, feature stores, vector DBs, RAG patterns, agent frameworks, tool use, retrieval quality.
- **Deployment, MLOps, and Evaluation**: LLMOps, infra, observability, evaluation, monitoring, rollback, canary, alignment in production.
- **Governance & Ethics**: compliance, privacy, safety, fairness, risk management, policy.
- **Templates, SOPs, and Checklists**: playbooks, how-tos, runbooks, SOPs, checklists.
- **General References**: broad AI/LLM knowledge that supports the book but does not cleanly fit above.

### Heuristic scoring rules used by the script
- **Relevance**: cosine similarity of query vs. title/snippet keywords; boosted if category keywords match.
- **Authority**: domain-based prior (e.g., `.gov`, `.edu`, well-known vendors), plus penalty for low-quality domains.
- **Recency**: based on publish date if provided; otherwise a modest default.
- **Completeness**: estimated from snippet length and presence of key phrases per category.
- **Readability**: penalizes clickbait patterns and excessively long or short snippets; otherwise neutral.

Weights are configurable in the script; defaults align with the mix above.

## Link tables

### Discovery & Product Strategy
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: RouteGPT – model routing on ChatGPT aligned to user preferences | https://chromewebstore.google.com/detail/routegpt/cbnfoohelfohplngdocidckbnbamghbf | chromewebstore.google.com | 2025-07-22T17:52:01Z | 0.8 | 0.78 | 0.7986 | 0.8 | 0.6 | 0.7748 |
| Show HN: Created a nifty subscription price and market research generator | https://tier-craft.lovable.app/ | tier-craft.lovable.app | 2025-07-04T23:31:27Z | 0.9 | 0.55 | 0.774 | 0.85 | 0.6 | 0.7561 |
| Show HN: Enabling Agentic Commerce Protocol (ACP) for Shopify Stores | https://www.actory.ai/ | www.actory.ai | 2025-12-15T20:08:01Z | 0.75 | 0.55 | 0.9986 | 0.85 | 0.5 | 0.7273 |
| Show HN: Amplift – AI agent for influencer marketing, GEO, and social listening | https://amplift.ai/ | amplift.ai | 2025-12-11T20:53:09Z | 0.8 | 0.45 | 0.9932 | 0.8 | 0.6 | 0.7215 |
| Show HN: SubSparks – I built an AI to turn Reddit pain points into SaaS ideas | https://www.subsparks.com | www.subsparks.com | 2025-06-07T16:58:00Z | 0.8 | 0.55 | 0.737 | 0.8 | 0.6 | 0.7081 |
| Show HN: Lucen – AI dating coach for over-thinkers (like me) | https://lucen.app | lucen.app | 2025-11-19T23:15:22Z | 0.75 | 0.45 | 0.963 | 0.85 | 0.6 | 0.7069 |
| Show HN: Voice AI Practice Scenarios for PM Interviews | https://www.toughtongueai.com/blog/ai-practice-scenarios-product-management | www.toughtongueai.com | 2025-06-19T20:41:54Z | 0.8 | 0.55 | 0.7534 | 0.7 | 0.7 | 0.7055 |
| Show HN: Marvin, your own AI-powered game studio | https://marvin.hyve.gg/?r=hn | marvin.hyve.gg | 2025-12-04T19:36:12Z | 0.65 | 0.55 | 0.9836 | 0.8 | 0.6 | 0.6925 |
| Show HN: Uniqalc – No-code calculators for SaaS and AI pricing | https://www.uniqalc.com/ | www.uniqalc.com | 2025-09-21T00:29:32Z | 0.65 | 0.55 | 0.8808 | 0.8 | 0.7 | 0.6871 |
| Show HN: NicheTrafficKit – a multi-platform traffic tool for Google-hit websites | https://nichetraffickit.com | nichetraffickit.com | 2025-07-14T16:14:48Z | 0.75 | 0.45 | 0.7877 | 0.85 | 0.6 | 0.6807 |
| Show HN: A Call of Duty event clipper and compilation maker using Python and AI | https://github.com/karimm-ai/NiceShot_AI | github.com | 2025-12-05T21:14:42Z | 0.65 | 0.45 | 0.9849 | 0.8 | 0.7 | 0.6777 |
| Show HN: My wife and I built MagicCV.ai, a 100% free online resume builder | https://www.magiccv.ai/ | www.magiccv.ai | 2025-09-16T13:34:58Z | 0.65 | 0.55 | 0.8753 | 0.8 | 0.6 | 0.6763 |
| Show HN: A 50% Undercut | https://www.aiworkphoto.com/ | www.aiworkphoto.com | 2025-07-11T07:17:45Z | 0.65 | 0.55 | 0.7836 | 0.8 | 0.7 | 0.6725 |
| Show HN: Worthunt a unified workspace for digital professionals | https://worthunt.com/ | worthunt.com | 2025-11-02T16:54:25Z | 0.65 | 0.45 | 0.9397 | 0.8 | 0.7 | 0.671 |
| Show HN: Cardog – AI car companion for transparent ownership | https://cardog.app/waitlist | cardog.app | 2025-05-23T02:48:38Z | 0.8 | 0.45 | 0.7151 | 0.8 | 0.5 | 0.6698 |
| Show HN: Tovideo – AI Video Generator with 9 Models (Google Veo 3 etc.) | https://apps.apple.com/us/app/ai-video-generator-tovideo/id6748954744 | apps.apple.com | 2025-08-09T19:25:55Z | 0.65 | 0.55 | 0.8233 | 0.8 | 0.6 | 0.6685 |
| Show HN: Rocktangle – AI tool to automate market research–saves 10 hours/week | https://rocktangle.com | rocktangle.com | 2025-01-31T08:11:40Z | 0.8 | 0.45 | 0.563 | 0.8 | 0.7 | 0.6669 |
| Show HN: AgentMail – Email infra for AI agents | https://chat.agentmail.to/ | chat.agentmail.to | 2025-07-31T14:08:33Z | 0.65 | 0.55 | 0.811 | 0.8 | 0.6 | 0.6666 |
| Show HN: I built a tool to help freelancers find better Upwork jobs with AI | https://github.com/daniloedu/UpworkOpportunityMatcher | github.com | 2025-10-10T14:12:14Z | 0.65 | 0.45 | 0.9082 | 0.8 | 0.7 | 0.6662 |
| Show HN: The Influencer AI – consistent AI "models" for photos and talking video | https://www.theinfluencer.ai | www.theinfluencer.ai | 2025-07-22T11:48:58Z | 0.65 | 0.55 | 0.7986 | 0.8 | 0.6 | 0.6648 |
| Show HN: Datta AI – Get paid when your data trains AI models | https://www.dattaai.com | www.dattaai.com | 2025-06-03T04:26:08Z | 0.65 | 0.55 | 0.7315 | 0.8 | 0.7 | 0.6647 |
| Show HN: Reload – Pay-as-you-go wallet for AI tools (no subscriptions) | https://www.withreload.com/for-platforms | www.withreload.com | 2025-05-28T14:33:08Z | 0.65 | 0.55 | 0.7233 | 0.8 | 0.7 | 0.6635 |
| Show HN: Tapflow – Built for devs/designers with way too many docs | https://www.tapflow.ai/ | www.tapflow.ai | 2025-05-29T00:18:12Z | 0.65 | 0.55 | 0.7233 | 0.8 | 0.7 | 0.6635 |
| Show HN: Free Y2K horror image generator using Gemini prompts | https://dreamyy2k.app/ | dreamyy2k.app | 2025-11-13T13:37:26Z | 0.65 | 0.45 | 0.9548 | 0.8 | 0.6 | 0.6632 |
| Show HN: ClassroomFeed – Weekly AI Summaries of Your Google Classroom | https://www.classroomfeed.com/ | www.classroomfeed.com | 2025-07-04T17:01:10Z | 0.65 | 0.55 | 0.774 | 0.8 | 0.6 | 0.6611 |
| Show HN: Frost AI – Stop losing money on AI agents | https://www.frostai.dev/ | www.frostai.dev | 2025-06-20T16:40:15Z | 0.65 | 0.55 | 0.7548 | 0.8 | 0.6 | 0.6582 |
| Show HN: Personalized Wealth Management – Institutional Meets Consumer | https://www.fulfilledwealth.co/home | www.fulfilledwealth.co | 2025-06-15T22:58:34Z | 0.65 | 0.55 | 0.7479 | 0.8 | 0.6 | 0.6572 |
| Show HN: Daily install trends of AI coding extensions in VS Code | https://bloomberry.com/coding-tools.html | bloomberry.com | 2025-10-14T13:12:00Z | 0.65 | 0.45 | 0.9137 | 0.8 | 0.6 | 0.6571 |
| Show HN: AI Voice AudioBook – Convert ebooks to audio with your cloned voice | https://zan.chat/ai-voice-show-hn.html | zan.chat | 2025-10-10T12:59:01Z | 0.65 | 0.45 | 0.9082 | 0.8 | 0.6 | 0.6562 |
| Show HN: Zenode – an AI-powered electronic component search engine | https://zenode.ai/ | zenode.ai | 2025-09-22T14:57:46Z | 0.65 | 0.45 | 0.8836 | 0.8 | 0.6 | 0.6525 |
| Show HN: I vibe coded a word game as a game designer (no ads, just fun) | https://wordsdescrambler.com/solver/games/wordsearch/ | wordsdescrambler.com | 2025-08-01T02:19:03Z | 0.65 | 0.45 | 0.811 | 0.8 | 0.7 | 0.6516 |
| Show HN: AI Image Editor with Natural Language Commands | https://imagable.ai | imagable.ai | 2025-09-11T06:39:50Z | 0.65 | 0.45 | 0.8685 | 0.8 | 0.6 | 0.6503 |
| Show HN: Palm Trees AI – A Software Robot Network of Specialized AI Personas | https://palmtreesai.com | palmtreesai.com | 2025-10-27T21:19:21Z | 0.65 | 0.45 | 0.9315 | 0.8 | 0.5 | 0.6497 |
| Show HN: What Paid Directories Charge in 2025 | https://directoryideas.ai/pricing-benchmark-study | directoryideas.ai | 2025-12-10T05:13:36Z | 0.65 | 0.45 | 0.9918 | 0.6 | 0.7 | 0.6488 |
| Show HN: Sudo – AI monetization infrastructure for developers | https://sudoapp.dev/ | sudoapp.dev | 2025-09-02T16:43:41Z | 0.65 | 0.45 | 0.8562 | 0.8 | 0.6 | 0.6484 |
| Show HN: B2B Sales Meeting Prep | https://meetinglens.io | meetinglens.io | 2025-03-26T01:40:38Z | 0.8 | 0.45 | 0.6356 | 0.8 | 0.4 | 0.6478 |
| Show HN: We built an open source, zero webhooks payment processor | https://github.com/flowglad/flowglad | github.com | 2025-11-25T17:33:50Z | 0.65 | 0.45 | 0.9712 | 0.8 | 0.4 | 0.6457 |
| Show HN: AI Agent that lives on your website | https://www.virtuans.ai/ | www.virtuans.ai | 2025-06-02T12:07:08Z | 0.65 | 0.55 | 0.7301 | 0.8 | 0.5 | 0.6445 |
| Show HN: AI Voice Agent Cost Calculator | https://softcery.com/ai-voice-agents-calculator | softcery.com | 2025-06-25T15:00:51Z | 0.65 | 0.45 | 0.7616 | 0.8 | 0.7 | 0.6442 |
| Show HN: Miniwhips – Transform your car photo into its toy version | https://miniwhips.app | miniwhips.app | 2025-08-04T17:41:12Z | 0.65 | 0.45 | 0.8164 | 0.8 | 0.6 | 0.6425 |
| Show HN: AgentGuard – Auto-kill AI agents before they burn through your budget | https://github.com/dipampaul17/AgentGuard | github.com | 2025-07-31T05:54:04Z | 0.65 | 0.45 | 0.811 | 0.8 | 0.6 | 0.6417 |
| Show HN: PayRankJobs – AI matches your resume with the highest-paying jobs | https://payrankjobs.com | payrankjobs.com | 2025-07-28T12:47:16Z | 0.65 | 0.45 | 0.8068 | 0.8 | 0.6 | 0.641 |
| Show HN: Ending the Bot Wars: A New Protocol for AI Consent and Value Exchange | https://github.com/peacprotocol/peac | github.com | 2025-07-22T16:23:01Z | 0.65 | 0.45 | 0.7986 | 0.8 | 0.6 | 0.6398 |
| Show HN: Placecard.net – Free PDF Seating Cards with Puppeteer | https://placecard.net/place-card-maker | placecard.net | 2025-07-02T14:01:36Z | 0.65 | 0.45 | 0.7712 | 0.8 | 0.6 | 0.6357 |
| Show HN: I made an open source Idea to App WebApp | https://github.com/rohitg00/CreateMVP | github.com | 2025-04-22T14:17:22Z | 0.65 | 0.45 | 0.674 | 0.8 | 0.7 | 0.6311 |
| Show HN: AIdea – AI researches and brainstorms your startup idea | https://aidea-app.framer.website/ | aidea-app.framer.website | 2024-12-20T08:23:40Z | 0.65 | 0.55 | 0.5055 | 0.8 | 0.7 | 0.6308 |
| Show HN: AI-Powered Audio Sample Generator (VST/AU) | https://www.text-to-sample.com/ | www.text-to-sample.com | 2025-02-02T23:17:52Z | 0.65 | 0.55 | 0.5658 | 0.8 | 0.6 | 0.6299 |
| Show HN: Page Magic: Use AI to customize any web page | https://github.com/khaledh/pagemagic | github.com | 2025-06-03T00:24:42Z | 0.65 | 0.45 | 0.7301 | 0.8 | 0.6 | 0.6295 |
| Show HN: Free AI Faceswap that just works | https://faceswap.pixub.com | faceswap.pixub.com | 2024-12-13T08:56:34Z | 0.65 | 0.55 | 0.4959 | 0.8 | 0.7 | 0.6294 |
| Show HN: Noedge token, a currently WIP crypto for bets without any edge and fees | https://bsky.app/profile/anonlife.bsky.social/post/3llyq46ssps2n | bsky.app | 2025-04-04T15:34:13Z | 0.65 | 0.45 | 0.6493 | 0.8 | 0.7 | 0.6274 |
| Show HN: Mkinf – an open-source library of hosted AI agents and tools | https://hub.mkinf.io | hub.mkinf.io | 2025-02-12T17:36:33Z | 0.65 | 0.55 | 0.5795 | 0.7 | 0.7 | 0.6269 |
| Show HN: Data for AI and AI for Data | https://www.opendatabay.com/ | www.opendatabay.com | 2025-01-16T11:39:04Z | 0.65 | 0.55 | 0.5425 | 0.8 | 0.6 | 0.6264 |
| Instacart's AI-enabled pricing may bump up your grocery costs by as much as 23% | https://www.cbsnews.com/news/instacart-price-discrepancies-investigation/ | www.cbsnews.com | 2025-12-11T03:17:45Z | 0.65 | 0.55 | 0.9918 | 0.35 | 0.6 | 0.6263 |
| Instacart's AI-Enabled Pricing Experiments May Be Inflating Your Grocery Bill | https://www.consumerreports.org/money/questionable-business-practices/instacart-ai-pricing-experiment-inflating-grocery-bills-a1142182490/ | www.consumerreports.org | 2025-12-09T14:05:47Z | 0.65 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.6261 |
| Show HN: Planitly – AI Trip Planner, Now More Personalized and Powerful | https://planitly.com | planitly.com | 2025-05-14T09:50:34Z | 0.65 | 0.45 | 0.7041 | 0.8 | 0.6 | 0.6256 |
| Show HN: 30-day Slack AI trail ran out | https://catchupslack.com/ | catchupslack.com | 2025-03-17T18:14:57Z | 0.65 | 0.45 | 0.6247 | 0.8 | 0.7 | 0.6237 |
| Show HN: Lumigo – Transparent AI-Driven Product Search Engine Without Ads | https://lumigo.ai/ | lumigo.ai | 2025-03-13T18:39:16Z | 0.65 | 0.45 | 0.6192 | 0.8 | 0.7 | 0.6229 |
| Show HN: I build an AI powered content marketing assistant | https://getmarketerai.com/ | getmarketerai.com | 2024-08-11T16:03:58Z | 0.8 | 0.45 | 0.326 | 0.8 | 0.6 | 0.6214 |
| Show HN: SDK for AI Coding with Long Running Tasks | https://cloudcoding.ai/ | cloudcoding.ai | 2025-04-22T12:43:32Z | 0.65 | 0.45 | 0.674 | 0.8 | 0.6 | 0.6211 |
| Show HN: RoundtableJS – Open-source programmatic survey library | https://github.com/roundtableAI/roundtable-js | github.com | 2024-08-08T16:13:05Z | 0.8 | 0.45 | 0.3219 | 0.8 | 0.6 | 0.6208 |
| Why every AI coding tool gets pricing wrong | https://getlago.substack.com/p/why-every-ai-coding-tool-gets-pricing | getlago.substack.com | 2025-11-13T14:02:52Z | 0.65 | 0.55 | 0.9548 | 0.35 | 0.6 | 0.6207 |
| AI Pricing Tools in Senior Care: The Antitrust Risks You Need to Manage Now | https://www.jdsupra.com/legalnews/ai-pricing-tools-in-senior-care-the-4725400/ | www.jdsupra.com | 2025-11-10T06:05:42Z | 0.65 | 0.55 | 0.9507 | 0.35 | 0.6 | 0.6201 |
| PerfectPrice: Automated competitor price tracking and AI pricing recommendations | https://www.perfectprice.app/ | www.perfectprice.app | 2025-11-10T09:01:55Z | 0.65 | 0.55 | 0.9507 | 0.35 | 0.6 | 0.6201 |
| US House lawmakers probe Delta Air Lines on use of AI in ticket pricing | https://www.reuters.com/world/us/us-house-lawmakers-probe-delta-air-lines-use-ai-ticket-pricing-2025-11-05/ | www.reuters.com | 2025-11-09T20:04:56Z | 0.65 | 0.55 | 0.9493 | 0.35 | 0.6 | 0.6199 |
| The AI Monetization Playbook | https://ondeviceguy.substack.com/p/the-ai-monetization-blueprint-the | ondeviceguy.substack.com | 2025-11-02T14:03:52Z | 0.65 | 0.55 | 0.9397 | 0.35 | 0.6 | 0.6185 |
| Microsoft sued for allegedly misleading millions with its AI pricing | https://www.theguardian.com/australia-news/2025/oct/27/microsoft-sued-allegedly-misleading-millions-australians-ai-pricing-ntwnfb | www.theguardian.com | 2025-10-27T01:55:30Z | 0.65 | 0.55 | 0.9301 | 0.35 | 0.6 | 0.617 |
| AI startup Augment scraps 'unsustainable' pricing, users say new model 10x worse | https://www.theregister.com/2025/10/15/augment_pricing_model/ | www.theregister.com | 2025-10-15T13:21:00Z | 0.65 | 0.55 | 0.9151 | 0.35 | 0.6 | 0.6148 |
| Show HN: I built a non-algorithmic social network for just my family and friends | https://aponlink.com/ | aponlink.com | 2025-03-19T15:22:11Z | 0.65 | 0.45 | 0.6274 | 0.8 | 0.6 | 0.6141 |
| OpenAI to boost content owners control for Sora AI video app, plans monetization | https://www.reuters.com/business/media-telecom/openai-boost-content-owners-control-sora-ai-video-app-plans-monetization-2025-10-04/ | www.reuters.com | 2025-10-05T10:06:06Z | 0.65 | 0.55 | 0.9014 | 0.35 | 0.6 | 0.6127 |
| Show HN: FindOurView – instant user research insights your team can chat with | https://www.findourview.com | www.findourview.com | 2023-10-19T18:15:46Z | 0.8 | 0.55 | 0.1 | 0.8 | 0.6 | 0.6125 |
| Show HN: Interactive price comparison for AI models (LLMs and Speech-to-Text) | https://ai-pricing.vercel.app/ | ai-pricing.vercel.app | 2024-10-28T18:18:07Z | 0.65 | 0.55 | 0.4329 | 0.8 | 0.6 | 0.6099 |
| Show HN: Klipy – AI GIFs, Clips, GIFs, Memes and Stickers API with Monetization | https://klipy.com | klipy.com | 2025-02-17T23:47:10Z | 0.65 | 0.45 | 0.5863 | 0.8 | 0.6 | 0.6079 |
| AI pricing is currently in a state of 'pandemonium' says Gartner | https://www.theregister.com/2025/09/10/ai_software_licensing_immature/ | www.theregister.com | 2025-09-11T13:15:08Z | 0.65 | 0.55 | 0.8685 | 0.35 | 0.6 | 0.6078 |
| Apple event expected to feature a slimmer iPhone as pricing, AI questions linger | https://www.reuters.com/business/apple-event-expected-feature-slimmer-iphone-pricing-ai-questions-linger-2025-09-09/ | www.reuters.com | 2025-09-09T10:14:50Z | 0.65 | 0.55 | 0.8658 | 0.35 | 0.6 | 0.6074 |
| Netlify: New credit-based pricing for today's AI development | https://www.netlify.com/blog/new-pricing-credits/ | www.netlify.com | 2025-09-04T17:06:49Z | 0.65 | 0.55 | 0.8589 | 0.35 | 0.6 | 0.6063 |
| Researchers say AI 'deadbots' are primed for monetization | https://www.npr.org/2025/08/26/nx-s1-5508355/ai-dead-people-chatbots-videos-parkland-court | www.npr.org | 2025-08-27T17:44:47Z | 0.65 | 0.55 | 0.8479 | 0.35 | 0.6 | 0.6047 |
| AI 'deadbots' are persuasive and primed for monetization | https://text.npr.org/nx-s1-5508355 | text.npr.org | 2025-08-26T23:42:33Z | 0.65 | 0.55 | 0.8466 | 0.35 | 0.6 | 0.6045 |
| Show HN: Our first sales with our Alt-Text Generator SaaS | https://alt-generator.ai/ | alt-generator.ai | 2025-03-21T07:57:47Z | 0.65 | 0.45 | 0.6301 | 0.8 | 0.5 | 0.6045 |
| Show HN: I built an OSS abstraction over Stripe to embed any pricing model | https://github.com/johnyeocx/autumn | github.com | 2025-01-29T13:33:37Z | 0.65 | 0.45 | 0.5603 | 0.8 | 0.6 | 0.604 |
| Show HN: Onit – Source-available ChatGPT Desktop with local mode, Claude, Gemini | https://github.com/synth-inc/onit | github.com | 2025-01-24T22:15:16Z | 0.65 | 0.45 | 0.5534 | 0.8 | 0.6 | 0.603 |
| Outcome-based won't be AI's pricing model | https://getlago.substack.com/p/outcome-based-pricing-is-not-the | getlago.substack.com | 2025-08-12T15:06:57Z | 0.65 | 0.55 | 0.8274 | 0.35 | 0.6 | 0.6016 |
| The "stranded asset" in AI pricing | https://arnon.dk/the-stranded-asset-in-ai-pricing/ | arnon.dk | 2025-12-10T21:52:25Z | 0.65 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.6013 |
| Show HN: Thisorthis.ai: Compare, Share, and Vote on AI-Generated Responses | https://thisorthis.ai | thisorthis.ai | 2024-06-20T14:19:34Z | 0.75 | 0.45 | 0.2548 | 0.85 | 0.6 | 0.6007 |
| Why "Per Seat" pricing is failing for AI agents (and what's replacing it) | https://blog.paid.ai/p/why-per-seat-pricing-is-failing-for | blog.paid.ai | 2025-08-06T12:12:45Z | 0.65 | 0.55 | 0.8192 | 0.35 | 0.6 | 0.6004 |
| Show HN: A Better Log Service | https://txtlog.net/ | txtlog.net | 2025-01-11T14:34:52Z | 0.65 | 0.45 | 0.5356 | 0.8 | 0.6 | 0.6003 |
| AI Flight Pricing Can Push Travelers to the Limit of Their Ability to Pay | https://www.bloomberg.com/news/articles/2025-08-04/how-ai-can-raise-airline-ticket-prices | www.bloomberg.com | 2025-08-04T23:15:02Z | 0.65 | 0.55 | 0.8164 | 0.35 | 0.6 | 0.6 |
| AI Monetization: Turn user ideas into shared IP via AI+Human screening | https://medium.com/@zaranur848/a-new-monetization-pathway-for-ai-platforms-using-multi-layer-ai-evaluation-and-human-review-to-42b69f19f2d4 | medium.com | 2025-12-03T06:39:44Z | 0.65 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.5998 |
| Delta’s new AI-powered pricing strategy | https://blog.getjetback.com/delta-engineered-a-pricing-system-that-sorts-you-by-economic-value/ | blog.getjetback.com | 2025-07-29T19:30:40Z | 0.65 | 0.55 | 0.8082 | 0.35 | 0.6 | 0.5987 |
| Surveillance Pricing Using AI | https://www.nytimes.com/2025/07/26/business/dealbook/personalized-pricing.html | www.nytimes.com | 2025-07-26T13:49:33Z | 0.65 | 0.55 | 0.8041 | 0.35 | 0.6 | 0.5981 |
| Delta plans to use AI in ticket pricing draws fire from US lawmakers | https://www.reuters.com/sustainability/boards-policy-regulation/delta-plans-use-ai-ticket-pricing-draws-fire-us-lawmakers-2025-07-22/ | www.reuters.com | 2025-07-23T11:25:50Z | 0.65 | 0.55 | 0.8 | 0.35 | 0.6 | 0.5975 |
| Show HN: LunarLink AI, all LLMs at API pricing without inputting your API key | https://www.lunarlinkai.com/ | www.lunarlinkai.com | 2024-09-20T07:39:57Z | 0.65 | 0.55 | 0.3808 | 0.7 | 0.7 | 0.5971 |
| Salesforce's weak quarterly revenue forecast signals lagging AI monetization | https://www.reuters.com/sustainability/sustainable-finance-reporting/salesforces-weak-quarterly-revenue-forecast-signals-lagging-ai-monetization-2025-09-03/ | www.reuters.com | 2025-09-03T22:32:04Z | 0.65 | 0.55 | 0.8575 | 0.35 | 0.5 | 0.5961 |
| Show HN: Agent Papaya – Your AI Privacy Companion | https://github.com/papayaverse/agent_papaya | github.com | 2025-02-08T23:09:46Z | 0.65 | 0.45 | 0.574 | 0.8 | 0.5 | 0.5961 |
| The OpenAI Blueprint: Designing Monetization for the AI Era | https://metronome.com/blog/the-openai-blueprint-designing-monetization-for-the-ai-era | metronome.com | 2025-11-13T21:41:48Z | 0.65 | 0.45 | 0.9548 | 0.35 | 0.6 | 0.5957 |
| Show HN: Pactory – AI Agents Marketplace integrated with Flowise and Langflow | https://pactory.ai/ | pactory.ai | 2025-02-02T20:08:22Z | 0.65 | 0.45 | 0.5658 | 0.8 | 0.5 | 0.5949 |
| Show HN: Kuakua.app – Happiness Unleash Power Within by Psychology and AI | https://kuakua.app/en | kuakua.app | 2024-12-12T02:53:31Z | 0.65 | 0.45 | 0.4945 | 0.8 | 0.6 | 0.5942 |
| Show HN: Ella AI Companion – Now with a Paid Version for Sustained Support | https://ella.quicklabs.app | ella.quicklabs.app | 2024-08-05T17:55:38Z | 0.65 | 0.55 | 0.3178 | 0.8 | 0.6 | 0.5927 |
| How do you handle pricing predictability for Agentic AI? | https://blog.paid.ai/p/pricing-predictability-for-agentic | blog.paid.ai | 2025-06-24T17:33:49Z | 0.65 | 0.55 | 0.7603 | 0.35 | 0.6 | 0.5915 |
| AI Agent Pricing: Winning Strategies and Models to Drive Growth | https://www.forbes.com/councils/forbesbusinesscouncil/2025/01/28/executive-guide-to-ai-agent-pricing-winning-strategies-and-models-to-drive-growth/ | www.forbes.com | 2025-06-13T17:53:36Z | 0.65 | 0.55 | 0.7452 | 0.35 | 0.6 | 0.5893 |
| Sora API Pricing (On Azure OpenAI) | https://www.ai.moda/en/blog/sora-pricing-on-azure-openai | www.ai.moda | 2025-06-04T17:07:44Z | 0.65 | 0.55 | 0.7329 | 0.35 | 0.6 | 0.5874 |
| The Complete Guide to AI Agent Monetization | https://blog.paid.ai/p/the-complete-guide-to-ai-agent-monetization | blog.paid.ai | 2025-06-04T18:40:00Z | 0.65 | 0.55 | 0.7329 | 0.35 | 0.6 | 0.5874 |
| AI Coding Agent Pricing | https://www.nibzard.com/agent-pricing/ | www.nibzard.com | 2025-05-25T20:48:49Z | 0.65 | 0.55 | 0.7192 | 0.35 | 0.6 | 0.5854 |
| Show HN: Create a AI/Cloud Pricing Calculator | https://v0-product-launch-waitlist-sigma-sooty.vercel.app | v0-product-launch-waitlist-sigma-sooty.vercel.app | 2025-05-21T04:17:56Z | 0.65 | 0.55 | 0.7137 | 0.35 | 0.6 | 0.5846 |
| Show HN: Ouro – Collaborative monetization platform for technical creators | https://ouro.foundation | ouro.foundation | 2024-09-07T12:40:01Z | 0.65 | 0.45 | 0.363 | 0.8 | 0.7 | 0.5844 |
| AI will kill seat-based pricing (mostly) | https://getlago.substack.com/p/why-seat-based-pricing-will-slowly | getlago.substack.com | 2025-05-19T10:02:39Z | 0.65 | 0.55 | 0.711 | 0.35 | 0.6 | 0.5841 |
| Show HN: TrailDrop – Lightweight GPX sharing and monetization platform |  | traildrop.app | 2025-09-12T11:08:29Z | 0.65 | 0.45 | 0.8699 | 0.35 | 0.6 | 0.583 |
| Show HN: TrailDrop – Lightweight GPX sharing and monetization platform | https://traildrop.app/ | traildrop.app | 2025-09-12T11:08:29Z | 0.65 | 0.45 | 0.8699 | 0.35 | 0.6 | 0.583 |
| A framework for pricing AI products | https://stripe.com/blog/a-framework-for-pricing-ai-products | stripe.com | 2025-09-11T18:03:51Z | 0.65 | 0.45 | 0.8685 | 0.35 | 0.6 | 0.5828 |
| Show HN: FinetuneDB – AI fine-tuning platform to create custom LLMs | https://finetunedb.com | finetunedb.com | 2024-10-09T15:44:53Z | 0.65 | 0.45 | 0.4068 | 0.8 | 0.6 | 0.581 |
| Show HN: Built simple Startup Directory in 3 days – 300 users in 72 hours | https://maze.do/saas-directory | maze.do | 2024-10-06T18:45:44Z | 0.65 | 0.45 | 0.4027 | 0.8 | 0.6 | 0.5804 |
| How to price AI? The most disruptive pricing models | https://hellorobots.substack.com/p/comment-pricer-lia | hellorobots.substack.com | 2025-04-25T05:50:23Z | 0.65 | 0.55 | 0.6781 | 0.35 | 0.6 | 0.5792 |
| Best pricing model for AI? Work in progress, says Salesforce | https://www.theregister.com/2025/06/02/salesforce_ai_pricing/ | www.theregister.com | 2025-06-02T15:48:53Z | 0.65 | 0.55 | 0.7301 | 0.35 | 0.5 | 0.577 |
| The Issue with AI-Powered Pricing | https://time.com/7307739/issue-with-ai-powered-pricing/ | time.com | 2025-08-11T18:28:26Z | 0.65 | 0.45 | 0.826 | 0.35 | 0.6 | 0.5764 |
| We're Making Enterprise Pricing Research Cost Less Than Your Domain Name | https://askrally.com/article/enterprise-pricing-research-costs-less-than-domain-name | askrally.com | 2025-08-05T13:14:13Z | 0.65 | 0.45 | 0.8178 | 0.35 | 0.6 | 0.5752 |
| LLM Pricing Calculator | https://app.hatrio.ai/free/llm-pricing-calculator | app.hatrio.ai | 2025-12-17T00:40:54Z | 0.5 | 0.55 | 1.0 | 0.35 | 0.6 | 0.575 |
| Amazon Kiro AI IDE – Pricing Announcement | https://kiro.dev/pricing/ | kiro.dev | 2025-08-01T19:11:49Z | 0.65 | 0.45 | 0.8123 | 0.35 | 0.6 | 0.5743 |
| Pricing AI Proofs-of-Concept: free pilots will kill you | https://arnon.dk/pricing-ai-proofs-of-concept-free-pilots-will-kill-you/ | arnon.dk | 2025-07-30T12:26:54Z | 0.65 | 0.45 | 0.8096 | 0.35 | 0.6 | 0.5739 |
| Win custom pricing with AI-powered Request a Quote and Hide Product Price app | https://apps.shopify.com/request-a-quote-hide-price-sb | apps.shopify.com | 2025-03-18T11:52:02Z | 0.65 | 0.55 | 0.626 | 0.35 | 0.6 | 0.5714 |
| Will AI end cheap flights? Critics attack Delta's "predatory" AI pricing | https://arstechnica.com/tech-policy/2025/07/will-ai-end-cheap-flights-critics-attack-deltas-predatory-ai-pricing/ | arstechnica.com | 2025-07-18T02:01:49Z | 0.65 | 0.45 | 0.7918 | 0.35 | 0.6 | 0.5713 |
| Show HN: Discover 1400+ AI Tools with AI Infinity Tools Directory | https://aiinfinity-meetpatel.notion.site/AI-Infinity-AI-Tools-Directory-0da673c487124ea2b6f8ebe59b75a231 | aiinfinity-meetpatel.notion.site | 2023-04-23T12:40:06Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.7 | 0.57 |
| Show HN: Track and bill users' AI token usage through an API | https://www.tiktokenizer.dev/ | www.tiktokenizer.dev | 2023-05-11T19:35:08Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.7 | 0.57 |
| The Chatbot Monetization Problem: Can AI Chatbots Be as Profitable as Google? | https://www.vincentschmalbach.com/the-chatbot-monetization-problem-can-ai-chatbots-be-as-profitable-as-google/ | www.vincentschmalbach.com | 2025-03-05T10:46:51Z | 0.65 | 0.55 | 0.6082 | 0.35 | 0.6 | 0.5687 |
| Flexprice–Open source monetization platform for AI companies | https://github.com/flexprice/flexprice | github.com | 2025-07-03T14:30:37Z | 0.65 | 0.45 | 0.7726 | 0.35 | 0.6 | 0.5684 |
| Warp Terminal changes pricing model | https://www.warp.dev/blog/warp-new-pricing-flexibility-byok | www.warp.dev | 2025-10-31T15:02:49Z | 0.5 | 0.55 | 0.937 | 0.35 | 0.6 | 0.5655 |
| Tech firms call for zonal electricity pricing in UK to fuel AI datacentres | https://www.theguardian.com/business/2025/feb/10/tech-firms-uk-electricity-zonal-pricing-ai-datacentres | www.theguardian.com | 2025-02-10T09:17:57Z | 0.65 | 0.55 | 0.5767 | 0.35 | 0.6 | 0.564 |
| The Future of Pricing: AI, Customer Value, and Outcome Based Models | https://open.spotify.com/episode/5Cs8uqt4BMPrKAcBxMjBVY | open.spotify.com | 2025-01-27T07:51:21Z | 0.65 | 0.55 | 0.5575 | 0.35 | 0.6 | 0.5611 |
| When should AI companies think about their pricing? | https://www.togai.com/blog/pricing-strategy-ai-companies/ | www.togai.com | 2025-01-25T07:56:26Z | 0.65 | 0.55 | 0.5548 | 0.35 | 0.6 | 0.5607 |
| Show HN - tool that converts image receipts to Excel | https://share.streamlit.io/-/auth/app?redirect_uri=https%3A%2F%2Freceipts2csv.streamlit.app%2F | share.streamlit.io | 2024-02-17T18:05:29Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Show HN: AI-Native Interactive Story Entertainment | https://www.ready2play.online/ | www.ready2play.online | 2023-09-07T02:11:47Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Show HN: I've built an iOS app to create your own mobile wallpapers using AI | https://apps.apple.com/us/app/wally-create-your-wallpapers/id6473636677 | apps.apple.com | 2024-01-04T15:30:41Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Show HN: Lindy, build your own AI employees with no-code | https://www.lindy.ai/ | www.lindy.ai | 2024-02-15T17:17:19Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Show HN: Lume – automate data mappings using AI | https://www.lume.ai/ | www.lume.ai | 2023-12-06T17:37:48Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Show HN: ReadToMe (iOS) turns paper books into audio | https://www.readtome-app.com | www.readtome-app.com | 2024-02-04T23:56:47Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Show HN: Sociables: The community platform for content creators and niches | https://sociables.substack.com/p/introducing-sociables | sociables.substack.com | 2023-07-14T13:51:02Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.6 | 0.56 |
| Salesforce Updates Slack Pricing to Expand Access to AI, Agentforce, and CRM | https://slack.com/blog/news/june-2025-pricing-and-packaging-announcement?nojsmode=1 | slack.com | 2025-06-17T21:01:26Z | 0.65 | 0.45 | 0.7507 | 0.35 | 0.5 | 0.5551 |
| Salesforce updates Slack pricing to expand access to AI, Agentforce, and CRM | https://slack.com/intl/en-au/blog/news/june-2025-pricing-and-packaging-announcement?nojsmode=1 | slack.com | 2025-06-18T00:35:45Z | 0.65 | 0.45 | 0.7507 | 0.35 | 0.5 | 0.5551 |
| Show HN: Okaaaay – Simple, Affordable and Intuitive AI Copywriter | https://www.okaaaay.com/ | www.okaaaay.com | 2023-02-13T16:32:11Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.5 | 0.55 |
| Study mode and spaced repetition. Feature requests, Monetization ideas? | https://app.polymax.ai/study-mode | app.polymax.ai | 2025-08-01T12:46:02Z | 0.5 | 0.55 | 0.8123 | 0.35 | 0.6 | 0.5468 |
| Show HN: Hive – open-source Marketplace for AI | https://hivenetwork.ai/ | hivenetwork.ai | 2024-04-25T17:49:15Z | 0.65 | 0.45 | 0.1781 | 0.8 | 0.6 | 0.5467 |
| Benchmarks and comparison of LLM AI models and API hosting providers | https://artificialanalysis.ai | artificialanalysis.ai | 2024-01-16T16:11:31Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.7 | 0.545 |
| Product Strategy in the Age of AI | https://www.intercom.com/blog/videos/intercom-on-product-ep21/ | www.intercom.com | 2023-10-05T08:22:34Z | 0.8 | 0.55 | 0.1 | 0.35 | 0.6 | 0.545 |
| Show HN: I Made SaaS Pricing Optimizer (AI-Powered Pricing Optimizations) | https://ai-pricing.co/?ref=hacker-news | ai-pricing.co | 2023-11-06T08:42:35Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.7 | 0.545 |
| Not by AI Pricing | https://notbyai.fyi/pricing | notbyai.fyi | 2025-02-25T17:30:56Z | 0.65 | 0.45 | 0.5973 | 0.35 | 0.6 | 0.5421 |
| Show HN: US visa price calculator (O-1A, O-1B, EB-1A, EB-2 NIW) | https://tukki.ai/pricing | tukki.ai | 2024-10-17T12:13:59Z | 0.5 | 0.45 | 0.4178 | 0.8 | 0.7 | 0.5402 |
| Show HN: Styrate – AI-Powered Product Reviews and Recommendations | https://styrate.vercel.app/ | styrate.vercel.app | 2023-04-24T00:17:16Z | 0.65 | 0.55 | 0.1 | 0.8 | 0.4 | 0.54 |
| Show HN: An open source alternative to some of Slack AI's premium features | https://github.com/meetbryce/open-source-slack-ai | github.com | 2024-05-09T15:49:47Z | 0.65 | 0.45 | 0.1973 | 0.8 | 0.5 | 0.5396 |
| Kagi – Introducing Fair Pricing | https://kagi.com/changelog#6155 | kagi.com | 2025-02-05T07:57:51Z | 0.65 | 0.45 | 0.5699 | 0.35 | 0.6 | 0.538 |
| Show HN: AI Receptionist, Speaks 64 Languages | https://lomni.ai/ | lomni.ai | 2023-11-15T20:29:11Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.6 | 0.535 |
| Show HN: Create a GPT3-powered Chatbot from any YouTube playlist | https://addcontext.xyz/create | addcontext.xyz | 2023-01-27T19:02:35Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.6 | 0.535 |
| Show HN: PixelForge – Verticalize YouTube videos with AI for TikTok, Reels | https://pixelforge.art | pixelforge.art | 2023-03-01T12:19:10Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.6 | 0.535 |
| AI 'Surveillance Pricing' Could Use Data to Make People Pay More | https://www.scientificamerican.com/article/ai-surveillance-pricing-practices-under-federal-probe/ | www.scientificamerican.com | 2024-09-03T20:18:44Z | 0.65 | 0.55 | 0.3575 | 0.35 | 0.6 | 0.5311 |
| Hypothesis Around the Pricing of Agentic AI | https://redmonk.com/rstephens/2024/12/23/hypothesis-around-the-pricing-of-agentic-ai/ | redmonk.com | 2024-12-23T19:24:56Z | 0.65 | 0.45 | 0.5096 | 0.35 | 0.6 | 0.5289 |
| Senate: Kroger's new AI pricing scheme is 'corporate greed out of control' | https://www.rawstory.com/kroger-pricing-strategy/ | www.rawstory.com | 2024-08-12T13:20:13Z | 0.65 | 0.55 | 0.3274 | 0.35 | 0.6 | 0.5266 |
| Outcome-based pricing for AI agents | https://sierra.ai/blog/outcome-based-pricing-for-ai-agents | sierra.ai | 2024-12-10T21:16:47Z | 0.65 | 0.45 | 0.4918 | 0.35 | 0.6 | 0.5263 |
| Show HN: Sociables, A Reddit alternative that lets community owners monetize | https://sociables.com/browse/top | sociables.com | 2023-06-12T18:56:29Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.5 | 0.525 |
| Show HN: Sociables, a Discord/Reddit/Patreon hybrid community platform | https://sociables.com/browse/all | sociables.com | 2023-06-21T12:34:48Z | 0.65 | 0.45 | 0.1 | 0.8 | 0.5 | 0.525 |
| Show HN: Jira Sucks. Meet the Product Strategy Tool You Deserve | https://meetsquad.ai/ | meetsquad.ai | 2024-11-25T21:01:55Z | 0.65 | 0.45 | 0.4712 | 0.35 | 0.6 | 0.5232 |
| Why Cursor's pricing model could lead to its downfall | https://blog.kilocode.ai/p/why-cursors-flat-fee-pricing-will | blog.kilocode.ai | 2025-04-07T09:34:11Z | 0.5 | 0.55 | 0.6534 | 0.35 | 0.6 | 0.523 |
| Why Cursor's flat-fee pricing could lead to its downfall | https://blog.kilocode.ai/p/why-cursors-flat-fee-pricing-could | blog.kilocode.ai | 2025-04-03T21:16:26Z | 0.5 | 0.55 | 0.6479 | 0.35 | 0.6 | 0.5222 |
| On AI Product Strategy | https://towardsdatascience.com/defining-your-ai-product-strategy-7-areas-of-focus-2cf112c82c07 | towardsdatascience.com | 2020-03-04T16:44:11Z | 0.8 | 0.45 | 0.1 | 0.35 | 0.6 | 0.52 |
| What Generative AI Means for Product Strategy and How to Evaluate It | https://thenewstack.io/what-generative-ai-means-for-product-strategy-and-how-to-evaluate-it/ | thenewstack.io | 2023-07-26T01:15:45Z | 0.8 | 0.45 | 0.1 | 0.35 | 0.6 | 0.52 |
| Why Token Pricing for Dev Tools Is Broken(and What We're Doing About It) | https://forgecode.dev/blog/seat-based-pricing-ai-agents/ | forgecode.dev | 2025-07-22T14:10:05Z | 0.5 | 0.45 | 0.7986 | 0.35 | 0.6 | 0.5198 |
| Synthetic User Research Is a Terrible Idea | https://spin.atomicobject.com/synthetic-user-research-terrible-idea/ | spin.atomicobject.com | 2024-07-09T18:39:10Z | 0.65 | 0.55 | 0.2808 | 0.35 | 0.6 | 0.5196 |
| DeepSeek expands business scope in potential shift towards monetization | https://www.scmp.com/tech/tech-trends/article/3299123/ai-start-deepseek-expands-business-scope-potential-shift-towards-monetisation | www.scmp.com | 2025-02-18T16:31:36Z | 0.5 | 0.55 | 0.5877 | 0.35 | 0.6 | 0.5132 |
| AI, Publicity Rights, and Alternate Monetization | https://blog.withedge.com/p/ai-publicity-rights-and-alternate | blog.withedge.com | 2024-05-31T12:38:52Z | 0.65 | 0.55 | 0.2274 | 0.35 | 0.6 | 0.5116 |
| From 0 to 70k Users: 3 Key Lessons from Our AI Business's Pricing Failures | https://usagestack.com/blog/from-0-to-70-000-users-3-key-lessons-from-our-ai-business-s-pricing-failures | usagestack.com | 2024-09-05T20:39:25Z | 0.65 | 0.45 | 0.3603 | 0.35 | 0.6 | 0.5065 |
| Canadian mega landlord using AI 'pricing scheme' as it hikes rents | https://breachmedia.ca/canadian-mega-landlord-ai-pricing-scheme-hikes-rents/ | breachmedia.ca | 2024-09-05T01:59:23Z | 0.65 | 0.45 | 0.3589 | 0.35 | 0.6 | 0.5063 |
| OpenAI API pricing update FAQ |  | help.openai.com | 2022-08-22T18:34:54Z | 0.5 | 0.8 | 0.1 | 0.35 | 0.6 | 0.5025 |
| OpenAI API pricing update FAQ | https://help.openai.com/en/articles/6485334-openai-api-pricing-update-faq | help.openai.com | 2022-08-22T18:34:54Z | 0.5 | 0.8 | 0.1 | 0.35 | 0.6 | 0.5025 |
| An update to our pricing | https://windsurf.com/blog/pricing-v2 | windsurf.com | 2025-04-21T21:07:25Z | 0.5 | 0.45 | 0.6726 | 0.35 | 0.6 | 0.5009 |
| AWS pricing for Kiro dev tool dubbed 'a wallet-wrecking tragedy' | https://www.theregister.com/2025/08/18/aws_updated_kiro_pricing/ | www.theregister.com | 2025-08-18T21:08:45Z | 0.35 | 0.55 | 0.8356 | 0.35 | 0.6 | 0.4978 |
| FTC investigates AI-based pricing strategies | https://techcrunch.com/2024/07/23/ftc-is-investigating-how-companies-are-using-ai-to-base-pricing-on-consumer-behavior/ | techcrunch.com | 2024-07-24T14:39:15Z | 0.65 | 0.45 | 0.3014 | 0.35 | 0.6 | 0.4977 |
| Google PaLM Pricing matches gpt3.5 for chat | https://cloud.google.com/vertex-ai/pricing | cloud.google.com | 2023-06-05T23:03:38Z | 0.5 | 0.78 | 0.1 | 0.35 | 0.6 | 0.4975 |
| Silicon Valley is pricing academics out of AI research | https://www.washingtonpost.com/technology/2024/03/10/big-tech-companies-ai-research/ | www.washingtonpost.com | 2024-03-13T19:40:35Z | 0.65 | 0.55 | 0.1192 | 0.35 | 0.6 | 0.4954 |
| GPT-4's Hidden Cost: Is Your Language Pricing You Out of AI Innovation? (2023) | https://tomaszurbanski.substack.com/p/the-hidden-price-tag-on-gpt-4-for | tomaszurbanski.substack.com | 2024-03-02T04:24:02Z | 0.65 | 0.55 | 0.1041 | 0.35 | 0.6 | 0.4931 |
| AI Monetization and Freemium Models in the SaaS Industry | https://www.saassun.day/p/ai-monetization-freemium-models-saas-industry | www.saassun.day | 2023-02-06T12:29:04Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| AMD AI Software Solved – MI300X Pricing, Perf, PyTorch, FlashAttention, Triton | https://www.semianalysis.com/p/amd-ai-software-solved-mi300x-pricing | www.semianalysis.com | 2023-06-30T15:54:49Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Adobe increases Creative Cloud pricing, takes Firefly generative AI out of beta | https://www.dpreview.com/news/1676880155/adobe-increases-creative-cloud-pricing-takes-firefly-out-of-beta | www.dpreview.com | 2023-09-18T02:27:36Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| All new, AI-powered Creative Cloud release and pricing update | https://blog.adobe.com/en/publish/2023/09/13/ai-creative-cloud-release-pricing-update | blog.adobe.com | 2023-09-13T14:03:45Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Can AI pricing algorithms be stopped from learning to collude? (2020, pdf) | https://revistas.pucp.edu.pe/index.php/themis/article/view/24175/22938 | revistas.pucp.edu.pe | 2022-04-19T04:06:52Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Enterprise Generative AI Pricing Estimator App | https://share.streamlit.io/-/auth/app?redirect_uri=https%3A%2F%2Fgen-ai-pricing-estimator.streamlit.app%2F | share.streamlit.io | 2023-10-06T05:18:24Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| How AI Is Driving Dynamic Pricing in Online Retail | https://blog.datahut.co/how-ai-is-driving-dynamic-pricing-in-online-retail/ | blog.datahut.co | 2019-10-31T08:12:08Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Quoter: AI-powered planning, pricing, and delivery of marketing | http://quoter.doz.com | quoter.doz.com | 2016-06-07T06:33:35Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Updates to Kagi pricing plans – More searches, unrestricted AI tools | https://blog.kagi.com/plan-changes | blog.kagi.com | 2023-05-23T05:46:32Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Using AI Would Provide Greater Transfer Pricing Tax Transparency | https://news.bloombergtax.com/tax-insights-and-commentary/using-ai-would-provide-greater-transfer-pricing-tax-transparency | news.bloombergtax.com | 2024-02-06T15:03:52Z | 0.65 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Pricing AI products is an engineering nightmare | https://github.com/getlago/lago/wiki/Pricing-AI-products-is-an-engineering-nightmare | github.com | 2024-06-21T17:33:32Z | 0.65 | 0.45 | 0.2562 | 0.35 | 0.6 | 0.4909 |
| Notes on where seat-based pricing is going | https://paid.ai/blog/ai-monetization/notes-on-where-seat-based-pricing-is-going | paid.ai | 2025-10-25T14:31:41Z | 0.35 | 0.45 | 0.9288 | 0.35 | 0.6 | 0.4868 |
| Pricing AI is a unit based problem | https://github.com/getlago/lago/wiki/Pricing-AI-is-a-unit%E2%80%90based-problem | github.com | 2024-05-14T00:14:16Z | 0.65 | 0.45 | 0.2027 | 0.35 | 0.6 | 0.4829 |
| Two new Gemini models, reduced 1.5 Pro pricing, increased rate limits, and more | https://developers.googleblog.com/en/updated-production-ready-gemini-models-reduced-15-pro-pricing-increased-rate-limits-and-more/ | developers.googleblog.com | 2024-09-24T20:59:28Z | 0.5 | 0.55 | 0.3863 | 0.35 | 0.6 | 0.4829 |
| Pricing AI products is hard | https://github.com/getlago/lago/wiki/Pricing-AI-products-is-hard | github.com | 2024-05-05T02:17:07Z | 0.65 | 0.45 | 0.1904 | 0.35 | 0.6 | 0.4811 |
| Pricing AI Is Hard | https://github.com/getlago/lago/wiki/AI-pricing-is-hard | github.com | 2024-04-28T04:36:52Z | 0.65 | 0.45 | 0.1822 | 0.35 | 0.6 | 0.4798 |
| SaaS pricing is so complex | https://useautumn.com/ | useautumn.com | 2025-01-06T19:48:57Z | 0.5 | 0.45 | 0.5288 | 0.35 | 0.6 | 0.4793 |
| AI Pricing Strategies for AI Apps |  | whoisgrowing.com | 2024-12-11T23:09:24Z | 0.5 | 0.45 | 0.4932 | 0.35 | 0.6 | 0.474 |
| AI Pricing Strategies for AI Apps | https://whoisgrowing.com/p/ai-pricing-strategies-for-ai-apps | whoisgrowing.com | 2024-12-11T23:09:24Z | 0.5 | 0.45 | 0.4932 | 0.35 | 0.6 | 0.474 |
| GPT-5: Key characteristics, pricing and system card | https://simonwillison.net/2025/Aug/7/gpt-5/ | simonwillison.net | 2025-08-08T01:33:10Z | 0.35 | 0.45 | 0.8205 | 0.35 | 0.6 | 0.4706 |
| What is 'surveillance pricing,' and is it forcing some consumers to pay more? | https://www.latimes.com/business/story/2024-07-23/ftc-investigates-surveillance-pricing-ai-data-mining | www.latimes.com | 2024-07-23T23:38:58Z | 0.5 | 0.55 | 0.3 | 0.35 | 0.6 | 0.47 |
| Silicon Valley is pricing lecturers out of AI research | https://tech-gate.org/2024/03/10/silicon-valley-is-pricing-lecturers-out-of-ai-research/ | tech-gate.org | 2024-03-10T18:46:43Z | 0.65 | 0.45 | 0.1151 | 0.35 | 0.6 | 0.4698 |
| 2024 Pricing comparison of text based Commercial AI LLM models – GPT, Gemini | https://subpage.app/blog/2024-Commercial-AI-LLM-pricing-compared-in-detail-GPT-Gemini-Cohere-Mistral | subpage.app | 2024-01-02T16:27:29Z | 0.65 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4675 |
| AI Pricing Optimizer – Your Virtual CRO Expert | https://ai-pricing.co/ | ai-pricing.co | 2023-10-29T19:26:08Z | 0.65 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4675 |
| Has the generative AI pricing collapse already started? | https://arstechnica.com/gadgets/2023/03/has-the-generative-ai-pricing-collapse-already-started/ | arstechnica.com | 2023-03-11T18:42:19Z | 0.65 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4675 |
| Oversubscribed Podcast: The Future of AI, #RIPTwitter, and Content Monetization | https://soundcloud.com/oversubscribedpodcast/oversubscribed-4-the-future-of-ai-riptwitter-and-content-monetization-with-mark-johnson | soundcloud.com | 2016-02-08T22:21:53Z | 0.65 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4675 |
| Pricing AI Enabled SaaS | https://techcrunch.com/2023/06/01/factors-to-consider-before-pricing-ai-enabled-saas/ | techcrunch.com | 2023-06-03T05:50:40Z | 0.65 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4675 |
| Pricing Homes Like Agents Do: “Human-in-Charge AI” for Pricing Using Comparables | https://medium.com/compass-true-north/pricing-homes-like-agents-do-ai-for-real-estate-cma-adjustments-c3de27a7ef | medium.com | 2022-01-11T17:18:39Z | 0.65 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4675 |
| The internet lost its shit over Wendy's 'surge pricing' | https://michaelestrin.substack.com/p/the-internet-lost-its-shit-over-wendys | michaelestrin.substack.com | 2024-03-03T22:11:42Z | 0.5 | 0.55 | 0.1055 | 0.35 | 0.6 | 0.4408 |
| Had a call with Reddit to discuss pricing | https://old.reddit.com/r/apolloapp/comments/13ws4w3/had_a_call_with_reddit_to_discuss_pricing_bad/ | old.reddit.com | 2023-05-31T20:48:07Z | 0.5 | 0.55 | 0.1 | 0.35 | 0.6 | 0.44 |
| Wendy's to Add Surge Pricing | https://www.theverge.com/2024/2/27/24084527/wendys-surge-dynamic-pricing-ai-2025 | www.theverge.com | 2024-02-27T17:03:23Z | 0.5 | 0.55 | 0.1 | 0.35 | 0.6 | 0.44 |
| Artificial intelligence, algorithmic pricing, and collusion | https://voxeu.org/article/artificial-intelligence-algorithmic-pricing-and-collusion | voxeu.org | 2019-02-17T03:10:19Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Azure Pricing: What You Need to Know | https://cast.ai/blog/azure-pricing-what-you-need-to-know/ | cast.ai | 2022-05-02T13:50:29Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Cloud Pricing Comparison: AWS vs. Azure vs. Google Cloud Platform in 2022 | https://cast.ai/blog/cloud-pricing-comparison-aws-vs-azure-vs-google-cloud-platform/ | cast.ai | 2022-05-06T08:51:26Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Cloud pricing comparison: AWS vs. Azure vs. Google Cloud in 2021 | https://cast.ai/blog/ultimate-cloud-pricing-comparison-aws-vs-azure-vs-google-cloud-in-2021/ | cast.ai | 2021-08-26T14:55:03Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Copyright is not a moral right, it's a monetization strategy | https://twitter.com/Plinz/status/1740597001652461895 | twitter.com | 2023-12-29T11:55:44Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Crash course: Amazon EC2 pricing (and cutting your AWS bill) | https://cast.ai/blog/crash-course-amazon-ec2-pricing-and-cutting-your-aws-bill/ | cast.ai | 2021-04-28T15:33:44Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| How to Maximize API Monetization | https://api7.ai/blog/api7-portal-api-monetization | api7.ai | 2023-07-11T15:34:01Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Wendy's will experiment with dynamic surge pricing for food in 2025 | https://arstechnica.com/information-technology/2024/02/wendys-plans-ai-powered-menu-to-change-food-prices-based-on-demand-weather/ | arstechnica.com | 2024-02-28T14:40:49Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| What happened with the Web Monetization API? | https://chriscoyier.net/2024/01/24/what-happened-with-the-web-monetization-api/ | chriscoyier.net | 2024-02-06T18:18:36Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |

### Prototyping & UX
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: Startfa.st – A curated, fast directory of AI, dev, and product tools | https://startfa.st | startfa.st | 2025-11-18T12:00:20Z | 0.9 | 0.45 | 0.9616 | 0.85 | 0.6 | 0.7592 |
| Show HN: CodeWords – Build automations by chatting with AI | https://www.agemo.ai/codewords | www.agemo.ai | 2025-09-17T14:28:47Z | 0.8 | 0.55 | 0.8767 | 0.8 | 0.6 | 0.729 |
| Show HN: AgentCanvas: Open-source canvas-style editor for ML developers | https://github.com/Mai0313/AgentCanvas | github.com | 2025-05-09T13:25:36Z | 0.9 | 0.45 | 0.6973 | 0.85 | 0.6 | 0.7196 |
| Show HN: Beginner's Guide to Answer Engine Optimization – The Future of Search? | https://drive.google.com/file/d/15-5VOBDMLqIfEzLgIytw57cvS7kKtYLV/view?usp=drive_link | drive.google.com | 2025-07-30T16:31:09Z | 0.65 | 0.78 | 0.8096 | 0.8 | 0.5 | 0.7139 |
| Show HN: Logical (YC F25): a local-first proactive desktop AI copilot | https://trylogical.ai | trylogical.ai | 2025-11-26T20:11:05Z | 0.8 | 0.45 | 0.9726 | 0.8 | 0.5 | 0.7084 |
| Show HN: What Would Paul Graham Write? An experiment in personality extension | https://wwpgw.georgestrakhov.com/ | wwpgw.georgestrakhov.com | 2025-05-19T13:29:58Z | 0.8 | 0.55 | 0.711 | 0.8 | 0.6 | 0.7042 |
| Show HN: ChatPhotoFix – AI photo editor that works from a single prompt | https://chatphotofix.com/ | chatphotofix.com | 2025-06-23T09:14:47Z | 0.75 | 0.45 | 0.7589 | 0.85 | 0.6 | 0.6763 |
| Show HN: Build, test, and deploy your own LLM router | https://platform.mintii.ai/login | platform.mintii.ai | 2024-12-23T19:12:50Z | 0.8 | 0.55 | 0.5096 | 0.8 | 0.6 | 0.6739 |
| Show HN: Call a PM.ai – For founders & PMs that need a Product Co-Pilot / Mentor | https://callapm.ai/ | callapm.ai | 2025-03-04T18:29:43Z | 0.8 | 0.45 | 0.6068 | 0.8 | 0.7 | 0.6735 |
| Show HN: A self-reflective system that rewrites itself as it thinks | http://reflexivetotality.com:8000/view?mode=adam | reflexivetotality.com:8000 | 2025-05-28T13:21:41Z | 0.65 | 0.45 | 0.7233 | 0.8 | 0.6 | 0.6285 |
| Show HN: AI Agents to Explore, Design and Test Business Strategies | https://brainterms.ai/ | brainterms.ai | 2025-05-20T09:22:39Z | 0.65 | 0.45 | 0.7123 | 0.8 | 0.6 | 0.6268 |
| Show HN: I created an app to solve the biggest design challenge | https://www.figma.com/community/plugin/1189158575928509194/QoQo.ai---Copy%2C-personas%2C-journey-mapping%2C-and-interviews. | www.figma.com | 2023-04-17T10:57:35Z | 0.8 | 0.55 | 0.1 | 0.8 | 0.7 | 0.6225 |
| Show HN: Traibe – Your Ultimate AI Co-Founder | https://www.traibe.xyz | www.traibe.xyz | 2024-10-09T11:50:39Z | 0.65 | 0.55 | 0.4068 | 0.8 | 0.5 | 0.596 |
| Show HN: Beam – Find Better Answers with Multi-Model AI Reasoning | https://big-agi.com/blog/beam-multi-model-ai-reasoning | big-agi.com | 2024-04-01T22:54:33Z | 0.8 | 0.45 | 0.1452 | 0.8 | 0.6 | 0.5943 |
| Seeking Cofounder for First Moroccan Social Network (Reddit-Like): Rasderb.com | https://rasderb.com | rasderb.com | 2024-08-15T13:07:19Z | 0.65 | 0.45 | 0.3315 | 0.8 | 0.6 | 0.5697 |
| Show HN: Uxia: AI-powered user testing in minutes | https://www.uxia.app/ | www.uxia.app | 2025-09-07T17:11:11Z | 0.5 | 0.55 | 0.863 | 0.35 | 0.6 | 0.5544 |
| Damn Small Linux | https://www.damnsmalllinux.org/ | www.damnsmalllinux.org | 2025-12-09T11:55:07Z | 0.35 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.5211 |
| Why are anime catgirls blocking my access to the Linux kernel? | https://lock.cmpxchg8b.com/anubis.html | lock.cmpxchg8b.com | 2025-08-20T21:42:46Z | 0.35 | 0.55 | 0.8384 | 0.35 | 0.6 | 0.4983 |
| Releasing open weights for FLUX.1 Krea | https://www.krea.ai/blog/flux-krea-open-source-release | www.krea.ai | 2025-07-31T21:18:24Z | 0.35 | 0.55 | 0.811 | 0.35 | 0.6 | 0.4942 |
| FLUX.2: Frontier Visual Intelligence |  | bfl.ai | 2025-11-26T03:25:20Z | 0.35 | 0.45 | 0.9726 | 0.35 | 0.6 | 0.4934 |
| FLUX.2: Frontier Visual Intelligence | https://bfl.ai/blog/flux-2 | bfl.ai | 2025-11-26T03:25:20Z | 0.35 | 0.45 | 0.9726 | 0.35 | 0.6 | 0.4934 |
| Danish Ministry Replaces Windows and Microsoft Office with Linux and LibreOffice |  | www.heise.de | 2025-06-12T15:09:41Z | 0.35 | 0.55 | 0.7438 | 0.35 | 0.6 | 0.4841 |
| Danish Ministry Replaces Windows and Microsoft Office with Linux and LibreOffice | https://www.heise.de/en/news/From-Word-and-Excel-to-LibreOffice-Danish-ministry-says-goodbye-to-Microsoft-10438942.html | www.heise.de | 2025-06-12T15:09:41Z | 0.35 | 0.55 | 0.7438 | 0.35 | 0.6 | 0.4841 |
| 30 Years Defending Linux – Until I Called It Quits | https://ludditus.com/2025/09/21/too-much-is-too-much-and-i-cant-stand-this-shit-anymore/ | ludditus.com | 2025-09-24T06:59:35Z | 0.35 | 0.45 | 0.8863 | 0.35 | 0.6 | 0.4804 |
| TmuxAI: AI-Powered, Non-Intrusive Terminal Assistant | https://tmuxai.dev/ | tmuxai.dev | 2025-04-27T19:48:11Z | 0.35 | 0.45 | 0.6808 | 0.35 | 0.6 | 0.4496 |
| Linux, Amazon, Meta, and Microsoft want to break the Google Maps monopoly |  | arstechnica.com | 2022-12-17T20:17:49Z | 0.35 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3625 |
| Linux, Amazon, Meta, and Microsoft want to break the Google Maps monopoly | https://arstechnica.com/gadgets/2022/12/linux-amazon-meta-and-microsoft-want-to-break-the-google-maps-monopoly/ | arstechnica.com | 2022-12-17T20:17:49Z | 0.35 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3625 |

### Engineering & Tooling
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: Welcome to "Voice AI Stack" Weekly – A Home for Voice AI Builders | https://videosdkweekly.substack.com/p/welcome-to-voice-ai-stack-weekly | videosdkweekly.substack.com | 2025-08-28T15:36:15Z | 0.9 | 0.55 | 0.8493 | 0.85 | 0.6 | 0.7674 |
| Show HN: Dlog – Journaling and AI coach that learns what drives wellbeing (Mac) | https://dlog.pro/ | dlog.pro | 2025-10-27T17:14:34Z | 0.9 | 0.45 | 0.9315 | 0.85 | 0.6 | 0.7547 |
| Launch HN: Airweave (YC X25) – Let agents search any app | https://github.com/airweave-ai/airweave | github.com | 2025-09-30T16:21:09Z | 0.9 | 0.45 | 0.8945 | 0.85 | 0.6 | 0.7492 |
| Show HN: Callio – A Real-Time AI Call Coach for iOS | https://apps.apple.com/us/app/callio-ai/id6745380476 | apps.apple.com | 2025-07-15T14:55:41Z | 0.9 | 0.55 | 0.789 | 0.85 | 0.5 | 0.7484 |
| Show HN: I Made InfoBeatLive – The Operating System for Startup Success | https://www.infobeatlive.com | www.infobeatlive.com | 2025-10-23T16:03:28Z | 0.8 | 0.55 | 0.926 | 0.8 | 0.7 | 0.7464 |
| Show HN: USST – A protocol to reduce LLM context redundancy by 98.5% | https://gist.github.com/maverick069/06d6f6e89947d621b4905765245a220a | gist.github.com | 2025-12-05T08:29:25Z | 0.8 | 0.55 | 0.9849 | 0.8 | 0.6 | 0.7452 |
| Show HN: GuardiAgent – Sandboxing / permission model for MCP servers | https://www.guardiagent.com/developers | www.guardiagent.com | 2025-11-21T12:29:08Z | 0.8 | 0.55 | 0.9658 | 0.8 | 0.6 | 0.7424 |
| Show HN: Medullar, the AI-Powered Data Discovery and Insight Platform | https://www.medullar.com | www.medullar.com | 2025-04-25T08:57:01Z | 0.9 | 0.55 | 0.6781 | 0.85 | 0.5 | 0.7317 |
| Show HN: Lemonade: Run LLMs Locally with GPU and NPU Acceleration | https://github.com/lemonade-sdk/lemonade | github.com | 2025-08-19T19:35:16Z | 0.9 | 0.45 | 0.837 | 0.85 | 0.5 | 0.7306 |
| Show HN: Modern office furniture catalog built with Next.js | https://www.ofistek.com.tr/ | www.ofistek.com.tr | 2025-11-09T13:24:08Z | 0.75 | 0.55 | 0.9493 | 0.85 | 0.6 | 0.7299 |
| Show HN: Averi – The AI Marketing Workspace | https://www.averi.ai/ | www.averi.ai | 2025-11-04T13:09:04Z | 0.8 | 0.55 | 0.9425 | 0.8 | 0.5 | 0.7289 |
| Show HN: Needle – Find users, track competitors, and spot market opportunities | https://useneedle.net | useneedle.net | 2025-11-21T13:51:59Z | 0.8 | 0.45 | 0.9658 | 0.8 | 0.6 | 0.7174 |
| Show HN: QueryPanel – AI Driven Dashboards | https://querypanel.io | querypanel.io | 2025-12-08T21:30:49Z | 0.75 | 0.45 | 0.989 | 0.85 | 0.6 | 0.7108 |
| Show HN: Shaped – Fine-tuning semantic search on behavioral signal | https://play.shaped.ai/dashboard/home | play.shaped.ai | 2024-12-03T15:51:46Z | 0.9 | 0.55 | 0.4822 | 0.85 | 0.5 | 0.7023 |
| Show HN: Aude – I built this because I hate bothering other engineers in my team | https://marketplace.atlassian.com/apps/1237445/aude?tab=overview&hosting=cloud | marketplace.atlassian.com | 2025-05-06T23:38:01Z | 0.8 | 0.55 | 0.6932 | 0.8 | 0.6 | 0.7015 |
| Show HN: Get more out of your Claude Code plan with VibeBooster | https://github.com/wsun19/VibeBooster | github.com | 2025-09-02T14:43:25Z | 0.8 | 0.45 | 0.8562 | 0.8 | 0.6 | 0.7009 |
| Show HN: 1.5B LLM routing model that aligns to preferences, not leaderboards | https://huggingface.co/katanemo/Arch-Router-1.5B | huggingface.co | 2025-07-17T20:29:12Z | 0.8 | 0.45 | 0.7918 | 0.8 | 0.6 | 0.6913 |
| Show HN: Deep Research – Open-Source Customizable Reasoning Framework for Devs | https://github.com/JigsawStack/deep-research | github.com | 2025-06-01T21:34:46Z | 0.8 | 0.45 | 0.7288 | 0.8 | 0.6 | 0.6818 |
| Show HN: Requirement Linter, an AI-powered tool to improve software requirements | https://github.com/jonverrier/RequirementLinter | github.com | 2025-04-14T15:32:33Z | 0.8 | 0.45 | 0.663 | 0.8 | 0.6 | 0.672 |
| Show HN: Transform static presentations → dynamic AI-guided experiences | https://app.toughtongueai.com/library/product-design-interview-tips-5-strategies-688bb9ca8021d1a72a3d25fa/ | app.toughtongueai.com | 2025-08-01T05:19:30Z | 0.65 | 0.55 | 0.8123 | 0.8 | 0.6 | 0.6668 |
| Show HN: NetFabric – next-gen network monitoring solution | https://netfabric.ai | netfabric.ai | 2024-07-25T13:01:55Z | 0.9 | 0.45 | 0.3027 | 0.85 | 0.6 | 0.6604 |
| We fine-tuned Llama 405B on AMD GPUs | https://publish.obsidian.md/felafax/pages/Tune+Llama3+405B+on+AMD+MI300x+(our+journey) | publish.obsidian.md | 2024-09-23T21:42:26Z | 0.8 | 0.55 | 0.3849 | 0.8 | 0.6 | 0.6552 |
| Show HN: Using LLMs to build a user centric design | https://flowtest-ai.vercel.app/ | flowtest-ai.vercel.app | 2024-07-19T22:28:48Z | 0.8 | 0.55 | 0.2945 | 0.8 | 0.7 | 0.6517 |
| Show HN: Buybase – Ecom for your AI agent | https://www.buybase.ai/ | www.buybase.ai | 2025-01-02T22:08:36Z | 0.75 | 0.55 | 0.5233 | 0.85 | 0.4 | 0.646 |
| Show HN: Synthetic Data Studio for LLMs | https://www.withcoherence.com/ | www.withcoherence.com | 2025-02-14T15:20:28Z | 0.65 | 0.55 | 0.5822 | 0.8 | 0.6 | 0.6323 |
| Show HN: Pingu Unchained an Unrestricted LLM for High-Risk AI Security Research | https://pingu.audn.ai | pingu.audn.ai | 2025-11-07T21:10:56Z | 0.65 | 0.55 | 0.9466 | 0.35 | 0.6 | 0.6195 |
| Show HN: Gentrace – evaluation and observability for generative AI | https://gentrace.ai | gentrace.ai | 2023-08-23T16:38:13Z | 0.75 | 0.45 | 0.1 | 0.85 | 0.6 | 0.5775 |
| Show HN: AI Assist – SDKs to build AI-powered assistance into your product | https://www.dopt.com/ai | www.dopt.com | 2024-03-19T17:49:24Z | 0.65 | 0.55 | 0.1274 | 0.8 | 0.6 | 0.5641 |
| Sloppy AI defenses take cybersecurity back to the 1990s, researchers say | https://www.scworld.com/news/sloppy-ai-defenses-take-cybersecurity-back-to-the-1990s-researchers-say | www.scworld.com | 2025-08-12T14:07:59Z | 0.5 | 0.55 | 0.8274 | 0.35 | 0.6 | 0.5491 |
| LLM Security Guide – 100 tools and real-world attacks from 370 experts | https://github.com/requie/LLMSecurityGuide | github.com | 2025-11-03T22:37:17Z | 0.5 | 0.45 | 0.9411 | 0.35 | 0.6 | 0.5412 |
| The “S” in MCP Stands for Security | https://elenacross7.medium.com/%EF%B8%8F-the-s-in-mcp-stands-for-security-91407b33ed6b | elenacross7.medium.com | 2025-04-06T14:32:42Z | 0.35 | 0.55 | 0.6521 | 0.35 | 0.6 | 0.4703 |
| Dual RTX 5090 Beats $25,000 H100 in Real-World LLM Performance | https://www.hardware-corner.net/dual-rtx-5090-vs-h100-for-llm/ | www.hardware-corner.net | 2025-04-01T17:26:15Z | 0.35 | 0.55 | 0.6452 | 0.35 | 0.6 | 0.4693 |
| OpenAI claims gold-medal performance at IMO 2025 | https://twitter.com/alexwei_/status/1946477742855532918 | twitter.com | 2025-07-19T18:48:12Z | 0.35 | 0.45 | 0.7945 | 0.35 | 0.6 | 0.4667 |
| ChatGPT-4 significantly increased performance of business consultants | https://d3.harvard.edu/navigating-the-jagged-technological-frontier/ | d3.harvard.edu | 2023-09-30T12:43:17Z | 0.35 | 0.85 | 0.1 | 0.35 | 0.6 | 0.4625 |
| A look at Apple's technical approach to AI including core model performance etc. | https://www.interconnects.ai/p/apple-intelligence | www.interconnects.ai | 2024-06-14T12:31:11Z | 0.5 | 0.55 | 0.2466 | 0.35 | 0.6 | 0.462 |
| Google's First Tensor Processing Unit: Architecture |  | thechipletter.substack.com | 2024-03-26T15:42:04Z | 0.35 | 0.55 | 0.137 | 0.35 | 0.6 | 0.3931 |
| Google's First Tensor Processing Unit: Architecture | https://thechipletter.substack.com/p/googles-first-tpu-architecture | thechipletter.substack.com | 2024-03-26T15:42:04Z | 0.35 | 0.55 | 0.137 | 0.35 | 0.6 | 0.3931 |

### Data, RAG, and Agents
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: Intent vectors for AI search and knowledge graphs for AI analytics | https://platform.papr.ai/ | platform.papr.ai | 2025-12-15T15:35:32Z | 1.0 | 0.55 | 0.9986 | 0.9 | 0.6 | 0.8323 |
| Show HN: Story Keeper – AI agents with narrative continuity instead of memory | https://github.com/neurobloomai/pact-ax | github.com | 2025-10-23T18:50:24Z | 1.0 | 0.45 | 0.926 | 0.9 | 0.6 | 0.7964 |
| Show HN: Cognitive AI architecture prototype with identity, memory, initiative | https://ivanhonis.github.io/ai_home/ | ivanhonis.github.io | 2025-11-30T15:59:42Z | 0.9 | 0.55 | 0.9781 | 0.85 | 0.6 | 0.7867 |
| Show HN: Spine AI – Visual workspace to think across multiple AI models | https://app.getspine.ai/guest | app.getspine.ai | 2025-11-09T18:13:29Z | 0.9 | 0.55 | 0.9493 | 0.85 | 0.6 | 0.7824 |
| Show HN: Graph – turn your ChatGPT into AI-sorted RSS feeds | https://www.graph.cx | www.graph.cx | 2025-08-21T16:42:26Z | 0.9 | 0.55 | 0.8397 | 0.85 | 0.6 | 0.766 |
| Show HN: ZeroEntropy (YC W25), Advanced AI Search over Complex Documents | https://dashboard.zeroentropy.dev | dashboard.zeroentropy.dev | 2025-01-13T21:33:43Z | 1.0 | 0.55 | 0.5384 | 0.9 | 0.6 | 0.7633 |
| Top Agents – A public directory for discovering and reviewing AI agents | https://top-agents.replit.app/ | top-agents.replit.app | 2025-06-10T18:50:55Z | 0.9 | 0.55 | 0.7411 | 0.85 | 0.7 | 0.7612 |
| Show HN: An Open-Source, Local-First Agent Framework in Rust | http://github.com/liquidos-ai/autoagents | github.com | 2025-11-26T05:58:03Z | 0.9 | 0.45 | 0.9726 | 0.85 | 0.6 | 0.7609 |
| Show HN: I built a context machine both users and LLM's love | https://www.overbooked.app/ | www.overbooked.app | 2025-07-23T15:23:19Z | 0.9 | 0.55 | 0.8 | 0.85 | 0.6 | 0.76 |
| Show HN: Sim Studio – Open-Source Agent Workflow GUI | https://github.com/simstudioai/sim | github.com | 2025-04-28T16:14:31Z | 1.0 | 0.45 | 0.6822 | 0.9 | 0.6 | 0.7598 |
| Show HN: Onboarding with pre-filled workspace. Agnt and search and human-in-loop | https://get.traction.team/v/early-access | get.traction.team | 2025-07-02T11:58:41Z | 0.9 | 0.55 | 0.7712 | 0.85 | 0.6 | 0.7557 |
| Show HN: FactIQ – A Data Explorer for the US Economy | https://www.factiq.com/ | www.factiq.com | 2025-12-02T13:25:16Z | 0.8 | 0.55 | 0.9808 | 0.8 | 0.6 | 0.7446 |
| Vector search on our codebase transformed our SDLC automation | https://medium.com/@antonybrahin/grounding-ai-in-reality-how-vector-search-on-our-codebase-transformed-our-sdlc-automation-7d068b1244a8 | medium.com | 2025-09-02T13:58:27Z | 0.9 | 0.45 | 0.8562 | 0.85 | 0.6 | 0.7434 |
| Show HN: Memori – Open-Source Memory Engine for AI Agents | https://github.com/GibsonAI/memori | github.com | 2025-08-18T14:29:32Z | 0.9 | 0.45 | 0.8356 | 0.85 | 0.6 | 0.7403 |
| Show HN: Vect AI – Autonomous Marketing OS with Real-Time Market Signal Analyzer | https://blog.vect.pro/vect-ai-bible-guide | blog.vect.pro | 2025-12-16T10:36:37Z | 0.8 | 0.55 | 1.0 | 0.8 | 0.5 | 0.7375 |
| Show HN: Arch-Router – Aligning LLM Routing with Human Preferences | https://arxiv.org/abs/2506.16655 | arxiv.org | 2025-08-03T06:32:04Z | 0.9 | 0.45 | 0.8151 | 0.85 | 0.6 | 0.7373 |
| Show HN: Ubik - A new way to use AI in citation-based work and research | https://www.ubik.studio | www.ubik.studio | 2025-10-27T14:38:38Z | 0.8 | 0.55 | 0.9315 | 0.8 | 0.6 | 0.7372 |
| Show HN: Lenzy AI – Turn AI agent conversations into actionable insights | https://www.lenzy.ai/ | www.lenzy.ai | 2025-10-21T10:22:05Z | 0.8 | 0.55 | 0.9233 | 0.8 | 0.6 | 0.736 |
| Show HN: Keplar – Voice AI for qualitative research at quantitative scale | https://www.keplar.io/ | www.keplar.io | 2025-09-17T20:50:51Z | 0.8 | 0.55 | 0.8767 | 0.8 | 0.6 | 0.729 |
| Show HN: TrafficScout – Discover high-intent Reddit threads with AI agents | https://www.trafficscout.app/ | www.trafficscout.app | 2025-12-11T20:37:26Z | 0.8 | 0.55 | 0.9932 | 0.75 | 0.5 | 0.729 |
| Show HN: A Unique User-in-the-Loop Agent for Investment Research | https://vector.deepinsightlabs.ai/login | vector.deepinsightlabs.ai | 2025-07-26T17:54:34Z | 0.8 | 0.55 | 0.8041 | 0.8 | 0.6 | 0.7181 |
| Show HN: RowboatX – open-source Claude Code for everyday automations | https://github.com/rowboatlabs/rowboat | github.com | 2025-11-18T18:50:00Z | 0.8 | 0.45 | 0.9616 | 0.8 | 0.6 | 0.7167 |
| Show HN: Kinic – A Portable AI Memory Store You Own (Farewell AI Amnesia) | https://www.kinic.io/ | www.kinic.io | 2025-07-09T14:30:35Z | 0.8 | 0.55 | 0.7808 | 0.8 | 0.6 | 0.7146 |
| Show HN: Deta Surf – An open source and local-first AI notebook | https://github.com/deta/surf | github.com | 2025-10-23T12:11:27Z | 0.8 | 0.45 | 0.926 | 0.8 | 0.6 | 0.7114 |
| Show HN: FastGraphRAG – Better RAG using good old PageRank | https://github.com/circlemind-ai/fast-graphrag | github.com | 2024-11-18T17:43:13Z | 0.95 | 0.45 | 0.4616 | 0.9 | 0.6 | 0.7092 |
| Show HN: No-Code, Private AI Agents – Build and Run Locally | https://browseragent.dev | browseragent.dev | 2025-01-31T20:31:37Z | 0.9 | 0.45 | 0.563 | 0.85 | 0.6 | 0.6995 |
| Show HN: AICF – a tiny "what changed" feed for AI/RAG (v0.1 minimal core) | https://github.com/mnswdhw/AICF/blob/main/spec/AICF-v0.1.md | github.com | 2025-08-22T20:16:02Z | 0.75 | 0.45 | 0.8411 | 0.85 | 0.7 | 0.6987 |
| Show HN: AutoGather – Find your ideal social influencers by natural language | https://www.autogather.ai/ | www.autogather.ai | 2025-03-03T13:28:24Z | 0.8 | 0.55 | 0.6055 | 0.8 | 0.7 | 0.6983 |
| Show HN: MethodsAgent – Solves "I can build but can't sell" for founders | https://www.methodsagent.com/ | www.methodsagent.com | 2025-12-16T11:07:03Z | 0.65 | 0.55 | 1.0 | 0.8 | 0.6 | 0.695 |
| Show HN: Best AI Tool Finder (BATF) | https://bestaitoolfinder.com/ | bestaitoolfinder.com | 2025-07-30T03:00:04Z | 0.8 | 0.45 | 0.8082 | 0.8 | 0.6 | 0.6937 |
| Show HN: OllaMan – An Elegant GUI for Ollama AI Model Management and Chat | https://ollaman.com | ollaman.com | 2025-09-12T02:05:10Z | 0.8 | 0.45 | 0.8685 | 0.8 | 0.5 | 0.6928 |
| Show HN: Decipher SEO – Topical Maps and Auto-Linking for 10x Faster SEO | https://decipherseo-dwf2slle7a-el.a.run.app | decipherseo-dwf2slle7a-el.a.run.app | 2025-03-14T08:28:58Z | 0.8 | 0.55 | 0.6205 | 0.8 | 0.6 | 0.6906 |
| Show HN: GreenReguAI, the platform to simplify renewable energy compliance | https://greenreguai.com/ | greenreguai.com | 2025-01-16T09:23:26Z | 0.9 | 0.45 | 0.5425 | 0.85 | 0.5 | 0.6864 |
| Show HN: EnrichMCP – A Python ORM for Agents | https://github.com/featureform/enrichmcp | github.com | 2025-06-19T17:32:21Z | 0.8 | 0.45 | 0.7534 | 0.8 | 0.6 | 0.6855 |
| Show HN: A financial analysis and research tool powered by agents | https://github.com/chisasaw/zenith | github.com | 2024-12-28T10:38:31Z | 0.9 | 0.45 | 0.5164 | 0.8 | 0.6 | 0.685 |
| Show HN: BotBudget – AI Agent Cost Calculator | https://botbudget.com/calculator | botbudget.com | 2025-07-15T16:44:42Z | 0.75 | 0.45 | 0.789 | 0.85 | 0.6 | 0.6808 |
| Show HN: RooAGI's Roo-VectorDB: A New PostgreSQL Extension for Vector Search | https://github.com/RooAGI/Roo-VectorDB | github.com | 2025-07-15T15:37:00Z | 0.75 | 0.45 | 0.789 | 0.85 | 0.6 | 0.6808 |
| Show HN: Preview Your HN Post Before Posting (Because I Messed Up Mine) | https://hnpostformatter.blancotech.com | hnpostformatter.blancotech.com | 2025-02-21T16:00:46Z | 0.75 | 0.55 | 0.5918 | 0.85 | 0.6 | 0.6763 |
| Show HN: Community Ninja – Discover and Engage with Communities Using AI Agents | https://communityninja.ai/ | communityninja.ai | 2025-05-03T07:30:04Z | 0.8 | 0.45 | 0.689 | 0.8 | 0.6 | 0.6759 |
| Show HN: Chat GPT bypass GPTZero detection | https://chat.openai.com/g/g-iG8l7QwvG-gptone | chat.openai.com | 2024-02-08T11:23:51Z | 0.8 | 0.8 | 0.1 | 0.8 | 0.6 | 0.675 |
| Show HN: Agent File (.af) – A standard file format for serializing AI agents | https://github.com/letta-ai/agent-file | github.com | 2025-04-02T16:44:00Z | 0.8 | 0.45 | 0.6466 | 0.8 | 0.6 | 0.6695 |
| Show HN: AI Feed | https://www.weblist.ai/ | www.weblist.ai | 2024-10-29T03:34:02Z | 0.8 | 0.55 | 0.4329 | 0.8 | 0.6 | 0.6624 |
| Show HN: Emdash – Slack/Zoom alternative for distributed team collaboration | https://emdash.io/ | emdash.io | 2025-02-26T15:10:52Z | 0.8 | 0.45 | 0.5986 | 0.8 | 0.6 | 0.6623 |
| Show HN: Chatsguru – A Chatbase Alternative with Advanced RAG Techniques | https://chatsguru.co | chatsguru.co | 2025-02-04T13:37:41Z | 0.75 | 0.45 | 0.5685 | 0.85 | 0.7 | 0.6578 |
| Show HN: I made free versions of GPTs | https://www.mithrin.ai/experts/ | www.mithrin.ai | 2024-10-04T02:49:37Z | 0.8 | 0.55 | 0.3986 | 0.8 | 0.6 | 0.6573 |
| Show HN: R2R V2 – A open source RAG engine with prod features | https://github.com/SciPhi-AI/R2R | github.com | 2024-06-26T13:27:14Z | 0.9 | 0.45 | 0.263 | 0.85 | 0.6 | 0.6544 |
| Show HN: Search Ads Manager AI Agent | https://agents.houseware.io/agents/search-ads-manager | agents.houseware.io | 2024-08-28T14:12:27Z | 0.8 | 0.55 | 0.3493 | 0.8 | 0.6 | 0.6499 |
| Show HN: Rankai – Automated SEO with AI | https://rankai.ai/ | rankai.ai | 2024-11-13T18:55:44Z | 0.8 | 0.45 | 0.4548 | 0.8 | 0.6 | 0.6407 |
| Show HN: Biblos – Semantic Search the Church Fathers | https://biblos.app/ | biblos.app | 2023-12-07T18:08:18Z | 0.9 | 0.45 | 0.1 | 0.85 | 0.7 | 0.64 |
| Show HN: Zarathustra – AI-powered sales research in 60 seconds | https://www.zarathustra.network/ | www.zarathustra.network | 2025-03-24T15:24:12Z | 0.65 | 0.55 | 0.6342 | 0.8 | 0.5 | 0.6301 |
| Show HN: Frugal by NumexaHQ- Transparency, Control and Cost Optimisation | https://github.com/NumexaHQ/frugal | github.com | 2023-08-23T19:39:42Z | 0.9 | 0.45 | 0.1 | 0.85 | 0.6 | 0.63 |
| Show HN: RAGatouille, a simple lib to use&train top retrieval models in RAG apps | https://github.com/bclavie/RAGatouille | github.com | 2024-01-04T16:48:34Z | 0.9 | 0.45 | 0.1 | 0.85 | 0.6 | 0.63 |
| Show HN: Platle – The Better ChatGPT | https://twitter.com/platleHQ/status/1846614186258059270 | twitter.com | 2024-10-17T00:11:43Z | 0.8 | 0.45 | 0.4164 | 0.8 | 0.5 | 0.625 |
| Show HN: AI-Powered Stock Market Analyst with Global Coverage | https://decodeinvesting.com/chat | decodeinvesting.com | 2024-08-04T21:31:03Z | 0.8 | 0.45 | 0.3164 | 0.8 | 0.6 | 0.62 |
| Show HN: Wyvern – Real-time machine learning platform for marketplaces | https://github.com/Wyvern-AI/wyvern | github.com | 2023-09-13T20:06:47Z | 0.9 | 0.45 | 0.1 | 0.85 | 0.5 | 0.62 |
| Show HN: Automated, hosted UI tests with AI test discovery (octomind.dev) | https://www.octomind.dev/ | www.octomind.dev | 2023-09-25T15:25:20Z | 0.8 | 0.55 | 0.1 | 0.8 | 0.6 | 0.6125 |
| Show HN: I built a tool to capture and centralise insights from discovery calls | https://usediscovery.ai | usediscovery.ai | 2024-05-11T05:11:38Z | 0.8 | 0.45 | 0.2 | 0.8 | 0.6 | 0.6025 |
| Breaking down JetBrains' complex AI agent strategy |  | leaddev.com | 2025-10-23T11:24:01Z | 0.65 | 0.45 | 0.926 | 0.35 | 0.6 | 0.5914 |
| Breaking down JetBrains' complex AI agent strategy | https://leaddev.com/ai/breaking-down-jetbrains-complex-ai-agent-strategy | leaddev.com | 2025-10-23T11:24:01Z | 0.65 | 0.45 | 0.926 | 0.35 | 0.6 | 0.5914 |
| Show HN: Skyvern – Browser automation using LLMs and computer vision | https://github.com/Skyvern-AI/skyvern | github.com | 2024-03-14T16:31:34Z | 0.8 | 0.45 | 0.1205 | 0.8 | 0.6 | 0.5906 |
| Show HN: Apollo – An affordable brand copywriter for blog posts and articles | https://apollowrites.com | apollowrites.com | 2023-09-20T13:34:52Z | 0.8 | 0.45 | 0.1 | 0.8 | 0.6 | 0.5875 |
| Show HN: Build AI apps like pdf.ai, chatbase.co, jenni.ai with this Git Repo | https://shipgpt.ai/ | shipgpt.ai | 2023-11-22T10:17:35Z | 0.8 | 0.45 | 0.1 | 0.8 | 0.6 | 0.5875 |
| Show HN: Product discovery with AI and community input filter fake reviews | https://styrate.co/landing/ | styrate.co | 2023-05-02T18:55:28Z | 0.8 | 0.45 | 0.1 | 0.8 | 0.6 | 0.5875 |
| Show HN: CloudCruise (YC W24) – Graph-Based Workflow Builder for Web Agents | https://cloudcruise.com/ | cloudcruise.com | 2024-04-16T14:57:50Z | 0.8 | 0.45 | 0.1658 | 0.8 | 0.5 | 0.5874 |
| Show HN: I built a database of successful social media marketing case studies | https://www.thecontentmarketingblueprint.com/ | www.thecontentmarketingblueprint.com | 2024-05-16T15:29:32Z | 0.65 | 0.55 | 0.2068 | 0.8 | 0.6 | 0.576 |
| Agentic AI in Retail: How Autonomous Shopping Is Redefining the Customer Journey | https://www.bain.com/insights/agentic-ai-in-retail-how-autonomous-shopping-redefining-customer-journey/ | www.bain.com | 2025-12-13T11:39:21Z | 0.5 | 0.55 | 0.9959 | 0.35 | 0.6 | 0.5744 |
| The Risk in AI Products: Fragmented Enterprise Knowledge | https://medium.com/@ravelantunes/you-cant-build-ai-products-without-context-management-strategy-2e9d3079bf82 | medium.com | 2025-07-23T15:44:09Z | 0.65 | 0.45 | 0.8 | 0.35 | 0.6 | 0.5725 |
| Show HN: AI agents that validate your product idea by talking to real users | https://app.holyshift.ai/ai/project | app.holyshift.ai | 2025-11-30T17:07:04Z | 0.5 | 0.55 | 0.9781 | 0.35 | 0.6 | 0.5717 |
| Windows 11 adds AI agent that runs in background with access to personal folders |  | www.windowslatest.com | 2025-11-18T20:36:21Z | 0.5 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.5692 |
| Windows 11 adds AI agent that runs in background with access to personal folders | https://www.windowslatest.com/2025/11/18/windows-11-to-add-an-ai-agent-that-runs-in-background-with-access-to-personal-folders-warns-of-security-risk/ | www.windowslatest.com | 2025-11-18T20:36:21Z | 0.5 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.5692 |
| Instant Checkout and the Agentic Commerce Protocol |  | openai.com | 2025-09-29T21:15:20Z | 0.35 | 0.8 | 0.8932 | 0.35 | 0.6 | 0.569 |
| Instant Checkout and the Agentic Commerce Protocol | https://openai.com/index/buy-it-in-chatgpt/ | openai.com | 2025-09-29T21:15:20Z | 0.35 | 0.8 | 0.8932 | 0.35 | 0.6 | 0.569 |
| Show HN: ChatGPT for Your Notebook | https://xnote.ai/ | xnote.ai | 2024-08-01T21:06:56Z | 0.65 | 0.45 | 0.3123 | 0.8 | 0.6 | 0.5668 |
| ChatGPT Agent – EU Launch | https://help.openai.com/en/articles/11752874-chatgpt-agent | help.openai.com | 2025-08-09T20:47:32Z | 0.35 | 0.8 | 0.8233 | 0.35 | 0.6 | 0.5585 |
| The New Distribution Game: Building Products for Agents, Not Users |  | www.productcurious.com | 2025-07-21T06:58:34Z | 0.5 | 0.55 | 0.7973 | 0.35 | 0.6 | 0.5446 |
| The New Distribution Game: Building Products for Agents, Not Users | https://www.productcurious.com/p/the-new-distribution-game-building | www.productcurious.com | 2025-07-21T06:58:34Z | 0.5 | 0.55 | 0.7973 | 0.35 | 0.6 | 0.5446 |
| I built a toolkit for building hive minds with AI agents |  | github.com | 2025-11-16T20:52:25Z | 0.5 | 0.45 | 0.9589 | 0.35 | 0.6 | 0.5438 |
| I built a toolkit for building hive minds with AI agents | https://github.com/dileet/ecco | github.com | 2025-11-16T20:52:25Z | 0.5 | 0.45 | 0.9589 | 0.35 | 0.6 | 0.5438 |
| Amazon CEO says AI agents will soon reduce company's corporate workforce |  | www.cbsnews.com | 2025-07-13T23:25:18Z | 0.5 | 0.55 | 0.7863 | 0.35 | 0.6 | 0.5429 |
| Amazon CEO says AI agents will soon reduce company's corporate workforce | https://www.cbsnews.com/news/amazon-ceo-generative-ai-corporate-workforce/ | www.cbsnews.com | 2025-07-13T23:25:18Z | 0.5 | 0.55 | 0.7863 | 0.35 | 0.6 | 0.5429 |
| From LLM to AI Agent: What's the Real Journey Behind AI System Development? | https://www.codelink.io/blog/post/ai-system-development-llm-rag-ai-workflow-agent | www.codelink.io | 2025-06-19T18:47:23Z | 0.5 | 0.55 | 0.7534 | 0.35 | 0.6 | 0.538 |
| Legal Contracts Built for AI Agents |  | paid.ai | 2025-10-08T19:48:22Z | 0.5 | 0.45 | 0.9055 | 0.35 | 0.6 | 0.5358 |
| Legal Contracts Built for AI Agents | https://paid.ai/blog/ai-agents/paid-gitlaw-introducing-legal-contracts-built-for-ai-agents | paid.ai | 2025-10-08T19:48:22Z | 0.5 | 0.45 | 0.9055 | 0.35 | 0.6 | 0.5358 |
| New tools for building agents | https://openai.com/index/new-tools-for-building-agents/ | openai.com | 2025-03-12T09:58:58Z | 0.35 | 0.8 | 0.6178 | 0.35 | 0.6 | 0.5277 |
| Vibe Revenue – a mirage of AI success | https://paid.ai/blog/ai-monetization/vibe-revenue-a-mirage-of-ai-success | paid.ai | 2025-08-25T20:54:37Z | 0.5 | 0.45 | 0.8452 | 0.35 | 0.6 | 0.5268 |
| AI agents lose money every second they run | https://paid.ai/blog/ai-monetization/your-ai-agents-are-losing-money | paid.ai | 2025-08-20T12:54:13Z | 0.5 | 0.45 | 0.8384 | 0.35 | 0.6 | 0.5258 |
| JetBrains IDEs Go AI: Coding Agent, Smarter Assistance, Free Tier | https://blog.jetbrains.com/blog/2025/04/16/jetbrains-ides-go-ai/ | blog.jetbrains.com | 2025-04-16T13:13:14Z | 0.5 | 0.55 | 0.6658 | 0.35 | 0.6 | 0.5249 |
| AI Agent Marketplace |  | aetheragentforge.org | 2025-07-13T03:15:01Z | 0.5 | 0.45 | 0.7863 | 0.35 | 0.6 | 0.5179 |
| AI Agent Marketplace | https://aetheragentforge.org | aetheragentforge.org | 2025-07-13T03:15:01Z | 0.5 | 0.45 | 0.7863 | 0.35 | 0.6 | 0.5179 |
| Discontinuation of ARM Notebook with Snapdragon X Elite SoC |  | www.tuxedocomputers.com | 2025-11-22T13:41:06Z | 0.35 | 0.55 | 0.9671 | 0.35 | 0.6 | 0.5176 |
| Discontinuation of ARM Notebook with Snapdragon X Elite SoC | https://www.tuxedocomputers.com/en/Discontinuation-of-ARM-notebooks-with-Snapdragon-X-Elite-SoC.tuxedo | www.tuxedocomputers.com | 2025-11-22T13:41:06Z | 0.35 | 0.55 | 0.9671 | 0.35 | 0.6 | 0.5176 |
| Monetize Your AI Agents |  | pooly.ai | 2025-06-23T07:00:05Z | 0.5 | 0.45 | 0.7589 | 0.35 | 0.6 | 0.5138 |
| Monetize Your AI Agents | https://pooly.ai | pooly.ai | 2025-06-23T07:00:05Z | 0.5 | 0.45 | 0.7589 | 0.35 | 0.6 | 0.5138 |
| .agent – A YAML/Markdown file format for AI agents (open source) | https://github.com/agentbrazley/dot.agent/tree/v1.0.1 | github.com | 2025-06-23T03:39:43Z | 0.5 | 0.45 | 0.7575 | 0.35 | 0.6 | 0.5136 |
| Andrej Karpathy – It will take a decade to work through the issues with agents | https://www.dwarkesh.com/p/andrej-karpathy | www.dwarkesh.com | 2025-10-18T00:51:40Z | 0.35 | 0.55 | 0.9178 | 0.35 | 0.6 | 0.5102 |
| Why the push for Agentic when models can barely follow a simple instruction? | https://forum.cursor.com/t/why-the-push-for-agentic-when-models-can-barely-follow-a-single-simple-instruction/137154 | forum.cursor.com | 2025-10-14T12:42:04Z | 0.35 | 0.55 | 0.9137 | 0.35 | 0.6 | 0.5096 |
| Meta Superintelligence Labs' first paper is about RAG | https://paddedinputs.substack.com/p/meta-superintelligences-surprising | paddedinputs.substack.com | 2025-10-13T20:39:02Z | 0.35 | 0.55 | 0.9123 | 0.35 | 0.6 | 0.5093 |
| Agent Process Intelligence – Map work and ground agents in reality | https://www.clearwork.io/clearwork-agent-process-intelligence | www.clearwork.io | 2025-09-17T18:50:48Z | 0.35 | 0.55 | 0.8767 | 0.35 | 0.6 | 0.504 |
| Show HN: An Agentic AI assistant with 200 app connectors | https://www.incredible.one/ | www.incredible.one | 2025-09-10T17:41:06Z | 0.35 | 0.55 | 0.8671 | 0.35 | 0.6 | 0.5026 |
| Get AWS EC2 at 40% off through cloud arbitrage | https://www.cloudidr.com/ | www.cloudidr.com | 2025-10-28T17:32:51Z | 0.35 | 0.55 | 0.9329 | 0.35 | 0.5 | 0.5024 |
| Show HN: Cleverb.ee – open-source agent that writes a cited research report | https://github.com/SureScaleAI/cleverbee | github.com | 2025-04-28T08:52:28Z | 0.5 | 0.45 | 0.6822 | 0.35 | 0.6 | 0.5023 |
| The web does not need gatekeepers: Cloudflare’s new “signed agents” pitch | https://positiveblue.substack.com/p/the-web-does-not-need-gatekeepers | positiveblue.substack.com | 2025-08-29T17:23:13Z | 0.35 | 0.55 | 0.8507 | 0.35 | 0.6 | 0.5001 |
| Open Source Implementation Of Deep Research Agent | https://github.com/swirl-ai/ai-angineers-handbook/tree/main/building_agents_from_scratch/deep_research_agent | github.com | 2025-04-13T06:28:23Z | 0.5 | 0.45 | 0.6616 | 0.35 | 0.6 | 0.4992 |
| Gemini CLI Tips and Tricks for Agentic Coding | https://github.com/addyosmani/gemini-cli-tips | github.com | 2025-11-27T05:44:28Z | 0.35 | 0.45 | 0.974 | 0.35 | 0.6 | 0.4936 |
| Qwen3-Coder: Agentic coding in the world | https://qwenlm.github.io/blog/qwen3-coder/ | qwenlm.github.io | 2025-07-23T06:09:18Z | 0.35 | 0.55 | 0.8 | 0.35 | 0.6 | 0.4925 |
| Agentu: The sleekest way to build AI agents | https://pypi.org/project/agentu/ | pypi.org | 2025-11-13T18:46:35Z | 0.35 | 0.45 | 0.9548 | 0.35 | 0.6 | 0.4907 |
| You should write an agent | https://fly.io/blog/everyone-write-an-agent/ | fly.io | 2025-11-07T03:01:17Z | 0.35 | 0.45 | 0.9452 | 0.35 | 0.6 | 0.4893 |
| Monetize Your AI Agents – AI-First Ad Network | https://adsgent.com | adsgent.com | 2025-02-16T08:56:50Z | 0.5 | 0.45 | 0.5849 | 0.35 | 0.6 | 0.4877 |
| Generative AI coding tools and agents do not work for me | https://blog.miguelgrinberg.com/post/why-generative-ai-coding-tools-and-agents-do-not-work-for-me | blog.miguelgrinberg.com | 2025-06-17T04:16:49Z | 0.35 | 0.55 | 0.7507 | 0.35 | 0.6 | 0.4851 |
| Agentic Coding Recommendations |  | lucumr.pocoo.org | 2025-06-12T14:12:15Z | 0.35 | 0.55 | 0.7438 | 0.35 | 0.6 | 0.4841 |
| Agentic Coding Recommendations | https://lucumr.pocoo.org/2025/6/12/agentic-coding/ | lucumr.pocoo.org | 2025-06-12T14:12:15Z | 0.35 | 0.55 | 0.7438 | 0.35 | 0.6 | 0.4841 |
| Supporting Our AI Overlords: Redesigning Data Systems to Be Agent-First | https://arxiv.org/abs/2509.00997 | arxiv.org | 2025-09-20T14:44:39Z | 0.35 | 0.45 | 0.8808 | 0.35 | 0.6 | 0.4796 |
| Internet Search Is Not a Naive Information Retrieval Problem | https://www.gojiberries.io/internet-search-is-not-a-naive-information-retrieval-problem/ | www.gojiberries.io | 2025-05-17T19:13:13Z | 0.35 | 0.55 | 0.7082 | 0.35 | 0.6 | 0.4787 |
| Npcsh, the multi-agent shell, has now reached 50 stars on GitHub | https://github.com/NPC-Worldwide/npcsh | github.com | 2025-09-15T22:21:05Z | 0.35 | 0.45 | 0.874 | 0.35 | 0.6 | 0.4786 |
| Gemini 2.0: our new AI model for the agentic era | https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/ | blog.google | 2024-12-11T16:02:09Z | 0.5 | 0.45 | 0.4932 | 0.35 | 0.6 | 0.474 |
| New Prompt Engineering Metaheuristic – (NoA) Network of Agents | https://github.com/andres-ulloa-de-la-torre/NoA | github.com | 2025-08-15T22:31:35Z | 0.35 | 0.45 | 0.8315 | 0.35 | 0.6 | 0.4722 |
| The SaaS competitor's agent is coming | https://paid.ai/blog/ai-monetization/the-saas-competitors-agent-is-coming | paid.ai | 2025-08-15T08:56:09Z | 0.35 | 0.45 | 0.8315 | 0.35 | 0.6 | 0.4722 |
| The Agent2Agent Protocol (A2A) | https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ | developers.googleblog.com | 2025-04-09T13:45:18Z | 0.35 | 0.55 | 0.6562 | 0.35 | 0.6 | 0.4709 |
| Crush: Glamourous AI coding agent for your favourite terminal | https://github.com/charmbracelet/crush | github.com | 2025-07-30T17:16:32Z | 0.35 | 0.45 | 0.8096 | 0.35 | 0.6 | 0.4689 |
| Are you selling agents the way customers want to buy? | https://paid.ai/blog/ai-monetization/are-you-selling-agents-the-way-customers-want-to-buy | paid.ai | 2025-09-08T22:41:32Z | 0.35 | 0.45 | 0.8644 | 0.35 | 0.5 | 0.4672 |
| Show HN: Nxtscape – an open-source agentic browser |  | github.com | 2025-06-20T22:16:27Z | 0.35 | 0.45 | 0.7548 | 0.35 | 0.6 | 0.4607 |
| Show HN: Nxtscape – an open-source agentic browser | https://github.com/nxtscape/nxtscape | github.com | 2025-06-20T22:16:27Z | 0.35 | 0.45 | 0.7548 | 0.35 | 0.6 | 0.4607 |
| Show HN: A web browser agent in your Chrome side panel | https://github.com/parsaghaffari/browserbee | github.com | 2025-05-18T12:30:20Z | 0.35 | 0.45 | 0.7096 | 0.35 | 0.6 | 0.4539 |
| A Survey of AI Agent Protocols | https://arxiv.org/abs/2504.16736 | arxiv.org | 2025-05-04T05:21:46Z | 0.35 | 0.45 | 0.6904 | 0.35 | 0.6 | 0.4511 |
| Real-Time Evaluation Models for RAG: Who Detects Hallucinations Best? | https://arxiv.org/abs/2503.21157 | arxiv.org | 2025-04-08T22:50:43Z | 0.35 | 0.45 | 0.6548 | 0.35 | 0.6 | 0.4457 |
| Mayo Clinic's secret weapon against AI hallucinations: Reverse RAG in action | https://venturebeat.com/ai/mayo-clinic-secret-weapon-against-ai-hallucinations-reverse-rag-in-action/ | venturebeat.com | 2025-03-15T20:11:41Z | 0.35 | 0.45 | 0.6219 | 0.35 | 0.6 | 0.4408 |
| Show HN: AI Garage Sale – Haggle with AI to buy real products | https://www.aigaragesale.com/ | www.aigaragesale.com | 2023-11-28T04:25:00Z | 0.5 | 0.55 | 0.1 | 0.35 | 0.4 | 0.42 |
| The Tragedy of CharacterAI | https://rdrama.net/post/133435/effortpost-the-tragedy-of-characterai-coomers | rdrama.net | 2022-12-22T19:50:41Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| Google creating an AI agent to use your PC on your behalf | https://vmvirtualmachine.com/google-creating-an-ai-agent-to-use-your-pc-on-your-behalf-says-report/ | vmvirtualmachine.com | 2024-10-27T23:26:35Z | 0.35 | 0.45 | 0.4315 | 0.35 | 0.6 | 0.4122 |
| Adaptive RAG – dynamic retrieval methods adjustment | https://arxiv.org/abs/2403.14403 | arxiv.org | 2024-04-01T11:09:33Z | 0.45 | 0.45 | 0.1452 | 0.35 | 0.6 | 0.4043 |
| GitHub Copilot loses an average of $20 per user per month | https://www.thurrott.com/cloud/290661/report-github-copilot-loses-an-average-of-20-per-user-per-month | www.thurrott.com | 2023-10-11T08:05:59Z | 0.35 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3875 |
| Google Promises Unlimited Storage; Cancels; Tells Journalist Life's Work Deleted |  | www.techdirt.com | 2023-12-13T16:01:19Z | 0.35 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3875 |
| Google Promises Unlimited Storage; Cancels; Tells Journalist Life's Work Deleted | https://www.techdirt.com/2023/12/12/google-promises-unlimited-cloud-storage-then-cancels-plan-then-tells-journalist-his-lifes-work-will-be-deleted-without-enough-time-to-transfer-the-data/ | www.techdirt.com | 2023-12-13T16:01:19Z | 0.35 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3875 |
| Machine Learning Engineer Guide: Feature Store vs. Data Warehouse | https://www.logicalclocks.com/blog/feature-store-vs-data-warehouse | www.logicalclocks.com | 2020-10-08T16:10:05Z | 0.35 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3875 |
| Mundane chores are all the rage in gaming | https://www.economist.com/culture/2022/06/14/mundane-chores-are-all-the-rage-in-gaming | www.economist.com | 2022-06-15T13:46:11Z | 0.35 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3875 |
| Memary: Open-Source Longterm Memory for Autonomous Agents | https://github.com/kingjulio8238/memary | github.com | 2024-04-29T15:11:37Z | 0.35 | 0.45 | 0.1836 | 0.35 | 0.6 | 0.375 |

### Deployment, MLOps, and Evaluation
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: Epoch – build and backtest trading strategies with plain English | https://www.epoch.trade/ | www.epoch.trade | 2025-07-03T16:03:08Z | 0.8 | 0.55 | 0.7726 | 0.8 | 0.6 | 0.7134 |
| Show HN: Tenum – a serverless full‑stack Dev Plattform and Runtime | https://tenum.ai/ | tenum.ai | 2025-08-14T10:39:21Z | 0.75 | 0.45 | 0.8301 | 0.85 | 0.6 | 0.687 |
| Show HN: PromptMage – Simplify and Manage Your LLM Workflows | https://promptmage.io/ | promptmage.io | 2024-08-28T11:20:57Z | 0.9 | 0.45 | 0.3493 | 0.85 | 0.6 | 0.6674 |
| Show HN: TensorZero – open-source data and learning flywheel for LLMs | https://github.com/tensorzero/tensorzero | github.com | 2024-09-16T15:25:03Z | 0.65 | 0.45 | 0.3753 | 0.8 | 0.6 | 0.5763 |
| Condemning the Deployment of GPT-4chan | https://docs.google.com/forms/d/e/1FAIpQLSdh3Pgh0sGrYtRihBu-GPN7FSQoODBLvF7dVAFLZk2iuMgoLw/viewform?fbzx=1650213417672418119 | docs.google.com | 2022-06-27T11:35:47Z | 0.35 | 0.78 | 0.1 | 0.35 | 0.6 | 0.445 |
| OpenObserve: Observability platform for logs, metrics, traces, analytics | https://github.com/openobserve/openobserve | github.com | 2024-10-23T20:41:12Z | 0.35 | 0.45 | 0.426 | 0.35 | 0.6 | 0.4114 |

### Governance & Ethics
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: PaperDebugger – An Overleaf companion for revising LaTeX papers | https://github.com/PaperDebugger/paperdebugger | github.com | 2025-12-16T14:53:22Z | 0.9 | 0.45 | 1.0 | 0.85 | 0.6 | 0.765 |
| Show HN: Privacyforge.ai – AI privacy compliance documents that work | https://www.privacyforge.ai/ | www.privacyforge.ai | 2025-09-28T06:37:56Z | 0.85 | 0.55 | 0.8918 | 0.9 | 0.6 | 0.7638 |
| Show HN: I built "Schnippi", my dream screenshot Chrome extension | https://chromewebstore.google.com/detail/schnippi-screenshot-tool/bnihkhiedonaoadigfljpjojncpnkeln | chromewebstore.google.com | 2025-07-09T12:43:20Z | 0.8 | 0.78 | 0.7808 | 0.8 | 0.5 | 0.7621 |
| Show HN: Explanans – Personalized video lectures for any topic | https://explanans.com/ | explanans.com | 2025-11-20T15:30:10Z | 0.8 | 0.45 | 0.9644 | 0.8 | 0.6 | 0.7172 |
| Show HN: archgw: open-source, intelligent proxy for AI agents, built on Envoy | https://github.com/katanemo/archgw | github.com | 2024-11-19T19:26:28Z | 0.9 | 0.45 | 0.463 | 0.85 | 0.6 | 0.6845 |
| Show HN: I vibe coded a complex trading app | https://apps.apple.com/us/app/tradofire/id6615085924 | apps.apple.com | 2025-05-21T16:30:17Z | 0.65 | 0.55 | 0.7137 | 0.8 | 0.6 | 0.6521 |
| Updates to Consumer Terms and Privacy Policy |  | www.anthropic.com | 2025-08-29T16:06:10Z | 0.45 | 0.76 | 0.8507 | 0.35 | 0.6 | 0.5876 |
| Updates to Consumer Terms and Privacy Policy | https://www.anthropic.com/news/updates-to-our-consumer-terms | www.anthropic.com | 2025-08-29T16:06:10Z | 0.45 | 0.76 | 0.8507 | 0.35 | 0.6 | 0.5876 |
| Fighting the New York Times' invasion of user privacy |  | openai.com | 2025-11-13T13:54:25Z | 0.35 | 0.8 | 0.9548 | 0.35 | 0.6 | 0.5782 |
| Fighting the New York Times' invasion of user privacy | https://openai.com/index/fighting-nyt-user-privacy-invasion | openai.com | 2025-11-13T13:54:25Z | 0.35 | 0.8 | 0.9548 | 0.35 | 0.6 | 0.5782 |
| LLMs with user-level differential privacy | https://research.google/blog/fine-tuning-llms-with-user-level-differential-privacy/ | research.google | 2025-05-26T10:06:29Z | 0.65 | 0.45 | 0.7205 | 0.35 | 0.6 | 0.5606 |
| Purple Llama: Towards open trust and safety in generative AI |  | ai.meta.com | 2023-12-07T17:09:46Z | 0.5 | 0.76 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Purple Llama: Towards open trust and safety in generative AI | https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/ | ai.meta.com | 2023-12-07T17:09:46Z | 0.5 | 0.76 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Edward Snowden and Ben Goertzel on the AI Explosion and Data Privacy | https://www.youtube.com/watch?v=4H_iWpWG_c0 | www.youtube.com | 2023-06-06T19:12:18Z | 0.5 | 0.55 | 0.1 | 0.35 | 0.6 | 0.44 |
| Sam and Greg's response to OpenAI Safety researcher claims | https://twitter.com/gdb/status/1791869138132218351 | twitter.com | 2024-05-19T05:28:39Z | 0.5 | 0.45 | 0.211 | 0.35 | 0.6 | 0.4316 |
| Many AI safety orgs have tried to criminalize currently-existing open-source AI | https://1a3orn.com/sub/machine-learning-bans.html | 1a3orn.com | 2024-01-16T16:07:18Z | 0.5 | 0.45 | 0.1 | 0.35 | 0.6 | 0.415 |
| SB-1047 will stifle open-source AI and decrease safety | https://www.answer.ai/posts/2024-04-29-sb1047.html | www.answer.ai | 2024-04-29T15:22:10Z | 0.35 | 0.55 | 0.1836 | 0.35 | 0.6 | 0.4 |
| Privacy Sandbox on Android | https://developer.android.com/design-for-safety/ads | developer.android.com | 2022-02-16T17:17:22Z | 0.35 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3875 |

### Templates, SOPs, and Checklists
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: Playbook AI – knowledge base for using AI in product development | https://aidevplaybook.com/en | aidevplaybook.com | 2025-10-21T18:11:58Z | 0.8 | 0.45 | 0.9233 | 0.8 | 0.6 | 0.711 |
| Show HN: SaaS for analyzing Bitcoin price movements | https://www.cantor.ai | www.cantor.ai | 2022-08-29T18:19:08Z | 0.8 | 0.55 | 0.1 | 0.8 | 0.6 | 0.6125 |
| Google's Results Are Infested, Open AI Is Using Their Playbook from the 2000s |  | chuckwnelson.com | 2024-12-29T04:37:23Z | 0.5 | 0.45 | 0.5178 | 0.35 | 0.6 | 0.4777 |
| Google's Results Are Infested, Open AI Is Using Their Playbook from the 2000s | https://chuckwnelson.com/blog/google-search-results-infested-open-ai-using-google-playbook | chuckwnelson.com | 2024-12-29T04:37:23Z | 0.5 | 0.45 | 0.5178 | 0.35 | 0.6 | 0.4777 |
| The Pinball Philosophy (1975) | https://pinballnirvana.com/forums/threads/the-pinball-philosophy-john-mcphee-1975.22239/ | pinballnirvana.com | 2025-02-11T15:01:24Z | 0.35 | 0.45 | 0.5781 | 0.35 | 0.6 | 0.4342 |
| Google dusts off the Google+ playbook to fight ChatGPT |  | arstechnica.com | 2023-03-10T19:44:26Z | 0.35 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3625 |
| Google dusts off the Google+ playbook to fight ChatGPT | https://arstechnica.com/gadgets/2023/03/google-dusts-off-the-failed-google-playbook-to-fight-chatgpt/ | arstechnica.com | 2023-03-10T19:44:26Z | 0.35 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3625 |

### General References
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Show HN: Auto rename downloads by AI and with your own naming rules | https://chromewebstore.google.com/detail/cantripsai-auto-rename-do/fnaemmlnchphilapbdjejjlhoomcpblk | chromewebstore.google.com | 2025-02-12T22:48:33Z | 0.7 | 0.78 | 0.5795 | 0.75 | 0.6 | 0.6994 |
| Show HN: Tool to check risks of your startup | https://www.siqnalis.com/risk-check | www.siqnalis.com | 2025-11-18T12:30:56Z | 0.7 | 0.55 | 0.9616 | 0.75 | 0.6 | 0.6992 |
| Show HN: Prexist – AI-powered search for products (now 3x faster with Exa AI) | https://prexist.pages.dev/ | prexist.pages.dev | 2025-10-22T14:03:59Z | 0.7 | 0.55 | 0.9247 | 0.75 | 0.6 | 0.6937 |
| Show HN: I built a simulator to teach PMs why they shouldn't interrupt migration | https://apmcommunication.com | apmcommunication.com | 2025-12-15T09:04:47Z | 0.7 | 0.45 | 0.9986 | 0.75 | 0.6 | 0.6798 |
| Show HN: Evaluating LLMs on creative writing via reader usage, not benchmarks | https://www.narrator.sh/ | www.narrator.sh | 2025-08-14T17:33:58Z | 0.7 | 0.55 | 0.8301 | 0.75 | 0.6 | 0.6795 |
| Show HN: FactBomb – A fast daily trivia game with zero friction | https://www.factbomb.com/ | www.factbomb.com | 2025-08-06T04:55:24Z | 0.7 | 0.55 | 0.8192 | 0.75 | 0.6 | 0.6779 |
| Show HN: Tuned.ws – AI growth strategist for Spotify/Apple Music artists (demo) | https://tuned.ws/demo/ | tuned.ws | 2025-12-06T00:43:21Z | 0.7 | 0.45 | 0.9849 | 0.75 | 0.6 | 0.6777 |
| Taking an open model from discovery to a production-ready endpoint on Vertex AI | https://cloud.google.com/blog/products/ai-machine-learning/take-an-open-model-from-discovery-to-endpoint-on-vertex-ai | cloud.google.com | 2025-08-04T16:48:07Z | 0.7 | 0.78 | 0.8164 | 0.35 | 0.6 | 0.675 |
| Show HN: Deep Researcher Web App, Node.js-Based (Open Source; MIT) | https://serqai.com/deep-search.html | serqai.com | 2025-09-03T16:57:44Z | 0.7 | 0.45 | 0.8575 | 0.75 | 0.7 | 0.6686 |
| Show HN: Tool that backtests your strategy only from a plain English description | https://www.BacktestAI.com/ | www.BacktestAI.com | 2025-07-30T18:44:44Z | 0.7 | 0.55 | 0.8096 | 0.75 | 0.5 | 0.6664 |
| Show HN: AI that researches your B2B prospects like a human | https://www.intellisell.ai/ | www.intellisell.ai | 2025-08-13T13:39:25Z | 0.7 | 0.55 | 0.8288 | 0.75 | 0.4 | 0.6593 |
| Show HN: Recursepaper – recursive entity extraction for improved understanding | https://github.com/GabrielNakamoto/recursepaper | github.com | 2025-08-22T21:47:16Z | 0.7 | 0.45 | 0.8411 | 0.75 | 0.6 | 0.6562 |
| Show HN: AI Roaster - A feed style app for roasting the AI hype | https://airoaster.app | airoaster.app | 2025-08-12T14:49:04Z | 0.7 | 0.45 | 0.8274 | 0.75 | 0.6 | 0.6541 |
| Show HN: Magicbox – AI-powered gift shopping platform | https://magicboxgifts.com/ | magicboxgifts.com | 2025-06-20T06:14:53Z | 0.7 | 0.45 | 0.7548 | 0.75 | 0.7 | 0.6532 |
| Show HN: AI Powered Earnings Reports (Stock Analysis) | https://palmy-investing.com/stocks/company-report/MSFT/earnings-reports | palmy-investing.com | 2025-05-12T14:15:49Z | 0.7 | 0.45 | 0.7014 | 0.75 | 0.7 | 0.6452 |
| Show HN: I made SEO tool using vector embeddings | https://www.babylovegrowth.ai/ | www.babylovegrowth.ai | 2025-02-24T12:15:54Z | 0.7 | 0.55 | 0.5959 | 0.75 | 0.6 | 0.6444 |
| Think Before You Speak – Exploratory Forced Hallucination Study [pdf] | https://github.com/AutomationOptimization/tsce_demo/blob/main/docs/Think_Before_You_Speak.pdf | github.com | 2025-06-16T23:58:00Z | 0.7 | 0.45 | 0.7493 | 0.75 | 0.6 | 0.6424 |
| Show HN: Docsforge.app – generate customer help docs from your React components | https://www.docsforge.app/ | www.docsforge.app | 2025-03-14T07:04:28Z | 0.7 | 0.55 | 0.6205 | 0.75 | 0.5 | 0.6381 |
| Show HN: I built a Reddit MCP server for faster and better research in Claude | https://github.com/GridfireAI/reddit-mcp | github.com | 2025-03-25T23:47:03Z | 0.7 | 0.45 | 0.6356 | 0.75 | 0.6 | 0.6253 |
| Show HN: I made StartupLaunchDay,daily startup launches and funding in one place | https://startuplaunchday.com/ | startuplaunchday.com | 2025-12-04T08:25:47Z | 0.55 | 0.45 | 0.9836 | 0.75 | 0.6 | 0.625 |
| I bootstrapped an AI product to 100k users, now I closed it |  | docs.google.com | 2025-08-07T13:17:17Z | 0.55 | 0.78 | 0.8205 | 0.35 | 0.6 | 0.6231 |
| I bootstrapped an AI product to 100k users, now I closed it | https://docs.google.com/document/d/1ayG5791HokMGx6s-JvtLLSek9cW-vSpbC2BNXAuRxo8/edit?usp=sharing | docs.google.com | 2025-08-07T13:17:17Z | 0.55 | 0.78 | 0.8205 | 0.35 | 0.6 | 0.6231 |
| Show HN: Add local files, YouTube transcripts, blog posts to your LLM prompts | https://github.com/sangddn/prompt_builder | github.com | 2025-01-05T05:04:25Z | 0.7 | 0.45 | 0.5274 | 0.75 | 0.7 | 0.6191 |
| Show HN: PreCog AI – Automatic AI Model Selection for Any Task | https://precog.ubik.studio/ | precog.ubik.studio | 2024-10-24T17:25:42Z | 0.7 | 0.55 | 0.4274 | 0.75 | 0.6 | 0.6191 |
| Show HN: AI for Automating Class Action Lawsuits [video] | https://www.youtube.com/watch?v=xmtfwU6K79A | www.youtube.com | 2024-08-01T18:01:02Z | 0.7 | 0.55 | 0.3123 | 0.75 | 0.6 | 0.6018 |
| US AI Action Plan |  | www.ai.gov | 2025-07-23T23:30:40Z | 0.4 | 0.9 | 0.8 | 0.35 | 0.6 | 0.5975 |
| US AI Action Plan | https://www.ai.gov/action-plan | www.ai.gov | 2025-07-23T23:30:40Z | 0.4 | 0.9 | 0.8 | 0.35 | 0.6 | 0.5975 |
| Show HN: ScaleUp – powered growth intelligence platform | https://www.scaleupweb.com | www.scaleupweb.com | 2025-01-24T15:16:48Z | 0.55 | 0.55 | 0.5534 | 0.75 | 0.7 | 0.5955 |
| Show HN: I built ScoreMeIO to compare and rank any product | https://scoreme.io/ | scoreme.io | 2025-05-12T08:21:27Z | 0.55 | 0.45 | 0.7014 | 0.75 | 0.7 | 0.5927 |
| Microsoft has a problem: lack of demand for its AI products |  | www.windowscentral.com | 2025-12-08T17:43:21Z | 0.55 | 0.55 | 0.989 | 0.35 | 0.6 | 0.5909 |
| Microsoft has a problem: lack of demand for its AI products | https://www.windowscentral.com/artificial-intelligence/microsoft-has-a-problem-nobody-wants-to-buy-or-use-its-shoddy-ai | www.windowscentral.com | 2025-12-08T17:43:21Z | 0.55 | 0.55 | 0.989 | 0.35 | 0.6 | 0.5909 |
| Show HN: Undead Domains – Share your unused domains and find new ones | https://www.undeaddomains.com/ | www.undeaddomains.com | 2024-07-24T13:19:39Z | 0.7 | 0.55 | 0.3014 | 0.75 | 0.5 | 0.5902 |
| OpenAI and Nvidia announce partnership to deploy 10GW of Nvidia systems |  | openai.com | 2025-09-23T20:46:58Z | 0.4 | 0.8 | 0.8849 | 0.35 | 0.6 | 0.5852 |
| OpenAI and Nvidia announce partnership to deploy 10GW of Nvidia systems | https://openai.com/index/openai-nvidia-systems-partnership/ | openai.com | 2025-09-23T20:46:58Z | 0.4 | 0.8 | 0.8849 | 0.35 | 0.6 | 0.5852 |
| AWS Service Availability Updates |  | aws.amazon.com | 2025-10-13T23:27:09Z | 0.4 | 0.78 | 0.9123 | 0.35 | 0.6 | 0.5843 |
| AWS Service Availability Updates | https://aws.amazon.com/about-aws/whats-new/2025/10/aws-service-availability/ | aws.amazon.com | 2025-10-13T23:27:09Z | 0.4 | 0.78 | 0.9123 | 0.35 | 0.6 | 0.5843 |
| Show HN: An AI SAT Tutor | https://www.learnwithorin.com/ | www.learnwithorin.com | 2025-03-05T22:52:31Z | 0.55 | 0.55 | 0.6082 | 0.75 | 0.5 | 0.5837 |
| Show HN: AI Data Analyst | https://www.narrative.bi/ai-data-analyst | www.narrative.bi | 2024-06-20T19:00:01Z | 0.7 | 0.55 | 0.2548 | 0.75 | 0.5 | 0.5832 |
| Show HN: Open-source study to measure end user satisfaction levels with LLMs | https://open-llm-initiative.com/challenge | open-llm-initiative.com | 2024-08-27T17:48:28Z | 0.7 | 0.45 | 0.3479 | 0.75 | 0.6 | 0.5822 |
| NeuralSide – Chrome AI Sidebar with Image Generation |  | chromewebstore.google.com | 2025-09-28T21:32:38Z | 0.4 | 0.78 | 0.8918 | 0.35 | 0.6 | 0.5813 |
| NeuralSide – Chrome AI Sidebar with Image Generation | https://chromewebstore.google.com/detail/neuralside-ai-sidebar-fre/ljkimgpldpjhkmipbmjhoppkgknbcogg | chromewebstore.google.com | 2025-09-28T21:32:38Z | 0.4 | 0.78 | 0.8918 | 0.35 | 0.6 | 0.5813 |
| Show HN: Perfectstack.ai, yet another AI directory, but for businesses | https://perfectstack.ai/ | perfectstack.ai | 2025-05-15T13:31:32Z | 0.55 | 0.45 | 0.7055 | 0.65 | 0.7 | 0.5783 |
| Show HN: Undermind – Deep scientific paper search with adaptive LLMs | https://www.undermind.ai/home/ | www.undermind.ai | 2024-04-02T15:16:02Z | 0.7 | 0.55 | 0.1466 | 0.75 | 0.6 | 0.577 |
| Show HN: Aiaffil.com – Discover AI Tools with Affiliate Programs | https://aiaffil.com | aiaffil.com | 2025-03-17T14:07:40Z | 0.55 | 0.45 | 0.6247 | 0.75 | 0.6 | 0.5712 |
| Anthropic raises $13B Series F |  | www.anthropic.com | 2025-09-03T09:38:52Z | 0.4 | 0.76 | 0.8575 | 0.35 | 0.6 | 0.5711 |
| Anthropic raises $13B Series F | https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation | www.anthropic.com | 2025-09-03T09:38:52Z | 0.4 | 0.76 | 0.8575 | 0.35 | 0.6 | 0.5711 |
| Show HN: Friendly AI – Chatbot messenger for your AI assistants | https://apps.apple.com/us/app/friendly-ai/id6447589849 | apps.apple.com | 2023-04-28T16:53:34Z | 0.7 | 0.55 | 0.1 | 0.75 | 0.6 | 0.57 |
| Show HN: The Calibration game – get better at identifying hallucination in LLMs | https://www.calibrationgame.com | www.calibrationgame.com | 2024-02-04T23:23:35Z | 0.7 | 0.55 | 0.1 | 0.75 | 0.6 | 0.57 |
| Google launches Product Discovery Solutions, AI-powered solutions for retailers | https://cloud.google.com/solutions/retail-product-discovery | cloud.google.com | 2021-01-19T18:10:26Z | 0.7 | 0.78 | 0.1 | 0.35 | 0.6 | 0.5675 |
| The Future of Product Management Is AI-Native |  | www.oreilly.com | 2025-08-09T13:51:21Z | 0.55 | 0.55 | 0.8233 | 0.35 | 0.6 | 0.566 |
| The Future of Product Management Is AI-Native | https://www.oreilly.com/radar/the-future-of-product-management-is-ai-native/ | www.oreilly.com | 2025-08-09T13:51:21Z | 0.55 | 0.55 | 0.8233 | 0.35 | 0.6 | 0.566 |
| Show HN: AI-Assisted Scratchpad | https://littlejot.com/ | littlejot.com | 2024-05-28T15:30:05Z | 0.7 | 0.45 | 0.2233 | 0.75 | 0.6 | 0.5635 |
| Show HN: Personno – Product Research Platform with AI Respondents | https://personno.nl/ | personno.nl | 2024-03-26T13:37:41Z | 0.7 | 0.45 | 0.137 | 0.75 | 0.7 | 0.5605 |
| Show HN: Zenfetch – Turn your saved browsing content into an AI second brain | https://www.zenfetch.com/ | www.zenfetch.com | 2024-01-24T17:01:04Z | 0.7 | 0.55 | 0.1 | 0.75 | 0.5 | 0.56 |
| LLM AuthZ Handbook: A Practical Guide for AI Builders and Users | https://flatt.tech/research/posts/llm-authz-handbook/ | flatt.tech | 2025-10-30T06:44:20Z | 0.55 | 0.45 | 0.9356 | 0.35 | 0.6 | 0.5578 |
| Cloud Run GPUs, now GA, makes running AI workloads easier for everyone | https://cloud.google.com/blog/products/serverless/cloud-run-gpus-are-now-generally-available | cloud.google.com | 2025-06-04T14:27:32Z | 0.4 | 0.78 | 0.7329 | 0.35 | 0.6 | 0.5574 |
| Show HN: I built a tool that helps marketers create viral headlines instantly | https://titlemaster.aikc.net | titlemaster.aikc.net | 2024-09-06T12:57:06Z | 0.55 | 0.55 | 0.3616 | 0.75 | 0.6 | 0.5567 |
| Evolving OpenAI's Structure | https://openai.com/index/evolving-our-structure/ | openai.com | 2025-05-06T03:11:47Z | 0.4 | 0.8 | 0.6932 | 0.35 | 0.6 | 0.5565 |
| Show HN: AlphaEdge – Options Trading Simulator for Enhanced Strategy Development | https://alpha-edge.ai/ | alpha-edge.ai | 2023-11-25T00:01:51Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.7 | 0.555 |
| Show HN: ChainForge, a visual tool for evaluating LLM responses | https://github.com/ianarawjo/ChainForge | github.com | 2023-05-23T20:04:40Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.7 | 0.555 |
| Show HN: Manage your attention better with Mutter | https://mutter.cards/ | mutter.cards | 2022-11-15T23:37:43Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.7 | 0.555 |
| Show HN: Submit your startup in 150 directories in 5 min | https://quicklist.ing/ | quicklist.ing | 2024-01-29T21:22:41Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.7 | 0.555 |
| A computer upgrade shut down BART | https://www.bart.gov/news/articles/2025/news20250905 | www.bart.gov | 2025-09-06T22:59:40Z | 0.25 | 0.9 | 0.8616 | 0.35 | 0.6 | 0.5542 |
| Getting AI to write good SQL | https://cloud.google.com/blog/products/databases/techniques-for-improving-text-to-sql | cloud.google.com | 2025-05-19T11:38:05Z | 0.4 | 0.78 | 0.711 | 0.35 | 0.6 | 0.5541 |
| GPT-5.2 | https://openai.com/index/introducing-gpt-5-2/ | openai.com | 2025-12-11T23:28:22Z | 0.25 | 0.8 | 0.9932 | 0.35 | 0.6 | 0.549 |
| Scientists discover why modularity evolves; 'holy grail' discovery for AI | http://slashdot.org/recent | slashdot.org | 2013-02-15T17:37:38Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.6 | 0.545 |
| Show HN: OtherYou – AI-Powered Avatar Creation for Anonymous Video Content | https://otheryou.io | otheryou.io | 2023-11-01T20:37:30Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.6 | 0.545 |
| Show HN: Turn Multiple Documents into Comparative Tables with GPT | https://tactic.fyi/generative-insights/ | tactic.fyi | 2023-09-04T07:06:54Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.6 | 0.545 |
| Building more with GPT-5.1-Codex-Max |  | openai.com | 2025-11-19T19:35:08Z | 0.25 | 0.8 | 0.963 | 0.35 | 0.6 | 0.5444 |
| Building more with GPT-5.1-Codex-Max | https://openai.com/index/gpt-5-1-codex-max/ | openai.com | 2025-11-19T19:35:08Z | 0.25 | 0.8 | 0.963 | 0.35 | 0.6 | 0.5444 |
| Compare OpenAI Models | https://platform.openai.com/docs/models/compare | platform.openai.com | 2025-03-06T18:59:30Z | 0.4 | 0.8 | 0.6096 | 0.35 | 0.6 | 0.5439 |
| Meta's new A.I. superstars are chafing against the rest of the company |  | www.nytimes.com | 2025-12-16T20:21:09Z | 0.4 | 0.55 | 1.0 | 0.35 | 0.6 | 0.54 |
| Meta's new A.I. superstars are chafing against the rest of the company | https://www.nytimes.com/2025/12/10/technology/meta-ai-tbd-lab-friction.html | www.nytimes.com | 2025-12-16T20:21:09Z | 0.4 | 0.55 | 1.0 | 0.35 | 0.6 | 0.54 |
| No AI* Here – A Response to Mozilla's Next Chapter | https://www.waterfox.com/blog/no-ai-here-response-to-mozilla/ | www.waterfox.com | 2025-12-17T02:50:44Z | 0.4 | 0.55 | 1.0 | 0.35 | 0.6 | 0.54 |
| Sam Altman says industry is wrong on OpenAI's competition, it is not from Google | https://timesofindia.indiatimes.com/technology/tech-news/sam-altman-says-industry-is-wrong-on-openais-competition-it-is-not-from-google-but-/articleshow/125868910.cms | timesofindia.indiatimes.com | 2025-12-10T19:53:28Z | 0.4 | 0.55 | 0.9918 | 0.35 | 0.6 | 0.5388 |
| Apple's slow AI pace becomes a strength as market grows weary of spending |  | finance.yahoo.com | 2025-12-09T22:37:47Z | 0.4 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.5386 |
| Apple's slow AI pace becomes a strength as market grows weary of spending | https://finance.yahoo.com/news/apple-slow-ai-pace-becomes-104658095.html | finance.yahoo.com | 2025-12-09T22:37:47Z | 0.4 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.5386 |
| I Tested the M5 iPad Pro's Neural-Accelerated AI, and the Hype Is Real |  | www.macstories.net | 2025-12-06T12:59:31Z | 0.4 | 0.55 | 0.9863 | 0.35 | 0.6 | 0.5379 |
| I Tested the M5 iPad Pro's Neural-Accelerated AI, and the Hype Is Real | https://www.macstories.net/stories/ipad-pro-m5-neural-benchmarks-mlx/ | www.macstories.net | 2025-12-06T12:59:31Z | 0.4 | 0.55 | 0.9863 | 0.35 | 0.6 | 0.5379 |
| We gave 5 LLMs $100K to trade stocks for 8 months | https://www.aitradearena.com/research/we-ran-llms-for-8-months | www.aitradearena.com | 2025-12-05T13:37:22Z | 0.4 | 0.55 | 0.9849 | 0.35 | 0.6 | 0.5377 |
| Introducing deep research | https://openai.com/index/introducing-deep-research/ | openai.com | 2025-02-03T17:41:51Z | 0.4 | 0.8 | 0.5671 | 0.35 | 0.6 | 0.5376 |
| Anthropic Acquires Bun |  | www.anthropic.com | 2025-12-02T18:34:00Z | 0.25 | 0.76 | 0.9808 | 0.35 | 0.6 | 0.5371 |
| Anthropic Acquires Bun | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone | www.anthropic.com | 2025-12-02T18:34:00Z | 0.25 | 0.76 | 0.9808 | 0.35 | 0.6 | 0.5371 |
| IBM CEO says there is 'no way' spending on AI data centers will pay off | https://www.businessinsider.com/ibm-ceo-big-tech-ai-capex-data-center-spending-2025-12 | www.businessinsider.com | 2025-12-02T21:04:33Z | 0.4 | 0.55 | 0.9808 | 0.35 | 0.6 | 0.5371 |
| Why I'm Betting Against the AGI Hype | https://www.notesfromthecircus.com/p/why-im-betting-against-the-agi-hype | www.notesfromthecircus.com | 2025-12-01T18:17:52Z | 0.4 | 0.55 | 0.9795 | 0.35 | 0.6 | 0.5369 |
| DeepSeek R1 Is Now Available on Azure AI Foundry and GitHub | https://azure.microsoft.com/en-us/blog/deepseek-r1-is-now-available-on-azure-ai-foundry-and-github/ | azure.microsoft.com | 2025-01-29T21:52:49Z | 0.4 | 0.8 | 0.5603 | 0.35 | 0.6 | 0.5365 |
| Leak confirms OpenAI is preparing ads on ChatGPT for public roll out |  | www.bleepingcomputer.com | 2025-11-29T14:52:04Z | 0.4 | 0.55 | 0.9767 | 0.35 | 0.6 | 0.5365 |
| Leak confirms OpenAI is preparing ads on ChatGPT for public roll out | https://www.bleepingcomputer.com/news/artificial-intelligence/leak-confirms-openai-is-preparing-ads-on-chatgpt-for-public-roll-out/ | www.bleepingcomputer.com | 2025-11-29T14:52:04Z | 0.4 | 0.55 | 0.9767 | 0.35 | 0.6 | 0.5365 |
| Ask AI – GPT-5 – LUMA – O1 | https://www.ask-ai.info | www.ask-ai.info | 2025-11-27T11:04:06Z | 0.4 | 0.55 | 0.974 | 0.35 | 0.6 | 0.5361 |
| Claude Opus 4.5 | https://www.anthropic.com/news/claude-opus-4-5 | www.anthropic.com | 2025-11-25T16:27:21Z | 0.25 | 0.76 | 0.9712 | 0.35 | 0.6 | 0.5357 |
| Ilya Sutskever: We're moving from the age of scaling to the age of research | https://www.dwarkesh.com/p/ilya-sutskever-2 | www.dwarkesh.com | 2025-11-25T23:33:41Z | 0.4 | 0.55 | 0.9712 | 0.35 | 0.6 | 0.5357 |
| Booking.com cancels $4K hotel reservation, offers same rooms again for $17K | https://www.cbc.ca/news/gopublic/go-public-booking-com-hotel-rates-9.6985480 | www.cbc.ca | 2025-11-24T15:50:27Z | 0.4 | 0.55 | 0.9699 | 0.35 | 0.6 | 0.5355 |
| 73% of AI startups are just prompt engineering |  | pub.towardsai.net | 2025-11-23T18:17:58Z | 0.4 | 0.55 | 0.9685 | 0.35 | 0.6 | 0.5353 |
| 73% of AI startups are just prompt engineering | https://pub.towardsai.net/i-reverse-engineered-200-ai-startups-73-are-lying-a8610acab0d3 | pub.towardsai.net | 2025-11-23T18:17:58Z | 0.4 | 0.55 | 0.9685 | 0.35 | 0.6 | 0.5353 |
| MCP Apps just dropped (OpenAI and Anthropic collab) and I think this is huge |  | blog.modelcontextprotocol.io | 2025-11-23T17:20:11Z | 0.4 | 0.55 | 0.9685 | 0.35 | 0.6 | 0.5353 |
| MCP Apps just dropped (OpenAI and Anthropic collab) and I think this is huge | http://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/ | blog.modelcontextprotocol.io | 2025-11-23T17:20:11Z | 0.4 | 0.55 | 0.9685 | 0.35 | 0.6 | 0.5353 |
| Show HN: AI-powered Email Assistant and Product Discovery for fast growing teams | https://neferdata.com | neferdata.com | 2023-08-08T10:23:19Z | 0.7 | 0.45 | 0.1 | 0.75 | 0.5 | 0.535 |
| Measuring political bias in Claude |  | www.anthropic.com | 2025-11-20T10:15:52Z | 0.25 | 0.76 | 0.9644 | 0.35 | 0.6 | 0.5347 |
| Measuring political bias in Claude | https://www.anthropic.com/news/political-even-handedness | www.anthropic.com | 2025-11-20T10:15:52Z | 0.25 | 0.76 | 0.9644 | 0.35 | 0.6 | 0.5347 |
| Gemini-3-pro-preview available on AI Studio | https://aistudio.google./ | aistudio.google. | 2025-11-18T15:09:57Z | 0.4 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.5342 |
| Google boss says AI investment boom has 'elements of irrationality' |  | www.bbc.com | 2025-11-19T02:11:14Z | 0.4 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.5342 |
| Google boss says AI investment boom has 'elements of irrationality' | https://www.bbc.com/news/articles/cwy7vrd8k4eo | www.bbc.com | 2025-11-19T02:11:14Z | 0.4 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.5342 |
| Oracle hit hard in Wall Street's tech sell-off over its AI bet |  | www.ft.com | 2025-11-14T17:05:30Z | 0.4 | 0.55 | 0.9562 | 0.35 | 0.6 | 0.5334 |
| Oracle hit hard in Wall Street's tech sell-off over its AI bet | https://www.ft.com/content/583e9391-bdd0-433e-91e0-b1b93038d51e | www.ft.com | 2025-11-14T17:05:30Z | 0.4 | 0.55 | 0.9562 | 0.35 | 0.6 | 0.5334 |
| SlopStop: Community-driven AI slop detection in Kagi Search |  | blog.kagi.com | 2025-11-13T21:22:15Z | 0.4 | 0.55 | 0.9548 | 0.35 | 0.6 | 0.5332 |
| SlopStop: Community-driven AI slop detection in Kagi Search | https://blog.kagi.com/slopstop | blog.kagi.com | 2025-11-13T21:22:15Z | 0.4 | 0.55 | 0.9548 | 0.35 | 0.6 | 0.5332 |
| Yann LeCun to depart Meta and launch AI startup focused on 'world models' |  | www.nasdaq.com | 2025-11-12T18:42:12Z | 0.4 | 0.55 | 0.9534 | 0.35 | 0.6 | 0.533 |
| Yann LeCun to depart Meta and launch AI startup focused on 'world models' | https://www.nasdaq.com/articles/metas-chief-ai-scientist-yann-lecun-depart-and-launch-ai-start-focused-world-models | www.nasdaq.com | 2025-11-12T18:42:12Z | 0.4 | 0.55 | 0.9534 | 0.35 | 0.6 | 0.533 |
| OpenAI Moves to Complete Potentially the Largest Theft in Human History | https://thezvi.substack.com/p/openai-moves-to-complete-potentially | thezvi.substack.com | 2025-11-01T19:10:03Z | 0.4 | 0.55 | 0.9384 | 0.35 | 0.6 | 0.5308 |
| ChatGPT Developer Mode: Full MCP client access | https://platform.openai.com/docs/guides/developer-mode | platform.openai.com | 2025-09-11T11:22:25Z | 0.25 | 0.8 | 0.8685 | 0.35 | 0.6 | 0.5303 |
| Google details 2025 Workspace price increase |  | 9to5google.com | 2025-01-21T19:04:07Z | 0.4 | 0.78 | 0.5493 | 0.35 | 0.6 | 0.5299 |
| Google details 2025 Workspace price increase | https://9to5google.com/2025/01/15/google-workspace-price-increase-2025/ | 9to5google.com | 2025-01-21T19:04:07Z | 0.4 | 0.78 | 0.5493 | 0.35 | 0.6 | 0.5299 |
| Why language models hallucinate | https://openai.com/index/why-language-models-hallucinate/ | openai.com | 2025-09-06T15:56:23Z | 0.25 | 0.8 | 0.8616 | 0.35 | 0.6 | 0.5292 |
| Meta is axing 600 roles across its AI division |  | www.theverge.com | 2025-10-23T10:20:28Z | 0.4 | 0.55 | 0.926 | 0.35 | 0.6 | 0.5289 |
| Meta is axing 600 roles across its AI division | https://www.theverge.com/news/804253/meta-ai-research-layoffs-fair-superintelligence | www.theverge.com | 2025-10-23T10:20:28Z | 0.4 | 0.55 | 0.926 | 0.35 | 0.6 | 0.5289 |
| AI Visibility Audits in Regulated Sectors | https://www.aivojournal.org/ai-visibility-audits-in-regulated-sectors-from-risk-reporting-to-revenue-assurance/ | www.aivojournal.org | 2025-10-22T04:14:02Z | 0.4 | 0.55 | 0.9247 | 0.35 | 0.6 | 0.5287 |
| BiasGuards – AI that detects 800 cognitive biases in business analysis <300ms |  | www.biasguards.ai | 2025-10-22T15:13:09Z | 0.4 | 0.55 | 0.9247 | 0.35 | 0.6 | 0.5287 |
| BiasGuards – AI that detects 800 cognitive biases in business analysis <300ms | https://www.biasguards.ai/ | www.biasguards.ai | 2025-10-22T15:13:09Z | 0.4 | 0.55 | 0.9247 | 0.35 | 0.6 | 0.5287 |
| LLMs can get "brain rot" | https://llm-brain-rot.github.io/ | llm-brain-rot.github.io | 2025-10-22T15:46:00Z | 0.4 | 0.55 | 0.9247 | 0.35 | 0.6 | 0.5287 |
| The Majority AI View | https://www.anildash.com//2025/10/17/the-majority-ai-view/ | www.anildash.com | 2025-10-18T15:27:55Z | 0.4 | 0.55 | 0.9192 | 0.35 | 0.6 | 0.5279 |
| OpenAI Needs $400B In The Next 12 Months |  | www.wheresyoured.at | 2025-10-17T19:10:50Z | 0.4 | 0.55 | 0.9178 | 0.35 | 0.6 | 0.5277 |
| OpenAI Needs $400B In The Next 12 Months | https://www.wheresyoured.at/openai400bn/ | www.wheresyoured.at | 2025-10-17T19:10:50Z | 0.4 | 0.55 | 0.9178 | 0.35 | 0.6 | 0.5277 |
| Claude Haiku 4.5 | https://www.anthropic.com/news/claude-haiku-4-5 | www.anthropic.com | 2025-10-15T19:32:15Z | 0.25 | 0.76 | 0.9151 | 0.35 | 0.6 | 0.5273 |
| Elon Musk wanted an OpenAI for-profit | https://openai.com/index/elon-musk-wanted-an-openai-for-profit/ | openai.com | 2024-12-13T21:26:57Z | 0.4 | 0.8 | 0.4959 | 0.35 | 0.6 | 0.5269 |
| America's future could hinge on whether AI slightly disappoints |  | www.noahpinion.blog | 2025-10-13T22:22:08Z | 0.4 | 0.55 | 0.9123 | 0.35 | 0.6 | 0.5268 |
| America's future could hinge on whether AI slightly disappoints | https://www.noahpinion.blog/p/americas-future-could-hinge-on-whether | www.noahpinion.blog | 2025-10-13T22:22:08Z | 0.4 | 0.55 | 0.9123 | 0.35 | 0.6 | 0.5268 |
| Fears over AI bubble bursting grow in Silicon Valley |  | www.bbc.com | 2025-10-11T03:55:14Z | 0.4 | 0.55 | 0.9096 | 0.35 | 0.6 | 0.5264 |
| Fears over AI bubble bursting grow in Silicon Valley | https://www.bbc.com/news/articles/cz69qy760weo | www.bbc.com | 2025-10-11T03:55:14Z | 0.4 | 0.55 | 0.9096 | 0.35 | 0.6 | 0.5264 |
| A small number of samples can poison LLMs of any size | https://www.anthropic.com/research/small-samples-poison | www.anthropic.com | 2025-10-10T05:18:19Z | 0.25 | 0.76 | 0.9082 | 0.35 | 0.6 | 0.5262 |
| McKinsey wonders how to sell AI apps with no measurable benefits | https://www.theregister.com/2025/10/09/mckinsey_ai_monetization/ | www.theregister.com | 2025-10-09T12:19:20Z | 0.4 | 0.55 | 0.9068 | 0.35 | 0.6 | 0.526 |
| Bank of England flags risk of 'sudden correction' in tech stocks inflated by AI |  | www.ft.com | 2025-10-09T00:49:54Z | 0.4 | 0.55 | 0.9055 | 0.35 | 0.6 | 0.5258 |
| Bank of England flags risk of 'sudden correction' in tech stocks inflated by AI | https://www.ft.com/content/fe474cff-564c-41d2-aaf7-313636a83e5b | www.ft.com | 2025-10-09T00:49:54Z | 0.4 | 0.55 | 0.9055 | 0.35 | 0.6 | 0.5258 |
| Jeff Bezos says AI is in a bubble but society will get 'gigantic' benefits |  | www.cnbc.com | 2025-10-03T16:26:32Z | 0.4 | 0.55 | 0.8986 | 0.35 | 0.6 | 0.5248 |
| Jeff Bezos says AI is in a bubble but society will get 'gigantic' benefits | https://www.cnbc.com/2025/10/03/jeff-bezos-ai-in-an-industrial-bubble-but-society-to-benefit.html | www.cnbc.com | 2025-10-03T16:26:32Z | 0.4 | 0.55 | 0.8986 | 0.35 | 0.6 | 0.5248 |
| Cerebras systems raises $1.1B Series G | https://www.cerebras.ai/press-release/series-g | www.cerebras.ai | 2025-09-30T19:39:02Z | 0.4 | 0.55 | 0.8945 | 0.35 | 0.6 | 0.5242 |
| Claude Sonnet 4.5 | https://www.anthropic.com/news/claude-sonnet-4-5 | www.anthropic.com | 2025-09-29T19:15:26Z | 0.25 | 0.76 | 0.8932 | 0.35 | 0.6 | 0.524 |
| Anthropic achieves ISO 42001 certification for responsible AI | https://www.anthropic.com/news/anthropic-achieves-iso-42001-certification-for-responsible-ai | www.anthropic.com | 2025-01-16T05:53:59Z | 0.4 | 0.76 | 0.5425 | 0.35 | 0.6 | 0.5239 |
| GPT-5 |  | openai.com | 2025-08-07T17:06:15Z | 0.25 | 0.8 | 0.8205 | 0.35 | 0.6 | 0.5231 |
| GPT-5 | https://openai.com/gpt-5/ | openai.com | 2025-08-07T17:06:15Z | 0.25 | 0.8 | 0.8205 | 0.35 | 0.6 | 0.5231 |
| America's top companies keep talking about AI – but can't explain the upsides |  | www.ft.com | 2025-09-24T05:00:36Z | 0.4 | 0.55 | 0.8863 | 0.35 | 0.6 | 0.5229 |
| America's top companies keep talking about AI – but can't explain the upsides | https://www.ft.com/content/e93e56df-dd9b-40c1-b77a-dba1ca01e473 | www.ft.com | 2025-09-24T05:00:36Z | 0.4 | 0.55 | 0.8863 | 0.35 | 0.6 | 0.5229 |
| Gartner Says Worldwide AI Spending Will Total $1.5T in 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-09-17-gartner-says-worldwide-ai-spending-will-total-1-point-5-trillion-in-2025 | www.gartner.com | 2025-09-20T14:19:49Z | 0.4 | 0.55 | 0.8808 | 0.35 | 0.6 | 0.5221 |
| Show HN: Sensaro – Simple NPS and AI powered feedback analysis for SaaS | https://www.sensaro.ai/ | www.sensaro.ai | 2025-09-17T08:39:08Z | 0.4 | 0.55 | 0.8767 | 0.35 | 0.6 | 0.5215 |
| Meta readies $25B bond sale as soaring AI costs trigger stock sell-off |  | www.ft.com | 2025-11-02T07:00:20Z | 0.4 | 0.55 | 0.9397 | 0.35 | 0.5 | 0.521 |
| Meta readies $25B bond sale as soaring AI costs trigger stock sell-off | https://www.ft.com/content/120d2321-8382-4d74-ab48-f9ecb483c2a9 | www.ft.com | 2025-11-02T07:00:20Z | 0.4 | 0.55 | 0.9397 | 0.35 | 0.5 | 0.521 |
| AI not affecting job market much so far, New York Fed says |  | money.usnews.com | 2025-09-04T18:51:43Z | 0.4 | 0.55 | 0.8589 | 0.35 | 0.6 | 0.5188 |
| AI not affecting job market much so far, New York Fed says | https://money.usnews.com/investing/news/articles/2025-09-04/ai-not-affecting-job-market-much-so-far-new-york-fed-says | money.usnews.com | 2025-09-04T18:51:43Z | 0.4 | 0.55 | 0.8589 | 0.35 | 0.6 | 0.5188 |
| Amazon has mostly sat out the AI talent war | https://www.businessinsider.com/amazon-ai-talent-wars-internal-document-2025-8 | www.businessinsider.com | 2025-09-02T03:47:41Z | 0.4 | 0.55 | 0.8562 | 0.35 | 0.6 | 0.5184 |
| Show HN: I created a platform to write SEO-driven articles in seconds using AI | https://www.postbrainer.com | www.postbrainer.com | 2024-01-09T13:34:42Z | 0.55 | 0.55 | 0.1 | 0.75 | 0.6 | 0.5175 |
| AI Bubble 2027 | https://www.wheresyoured.at/ai-bubble-2027/ | www.wheresyoured.at | 2025-08-27T16:59:04Z | 0.4 | 0.55 | 0.8479 | 0.35 | 0.6 | 0.5172 |
| YouTube made AI enhancements to videos without warning or permission |  | www.bbc.com | 2025-08-25T21:04:55Z | 0.4 | 0.55 | 0.8452 | 0.35 | 0.6 | 0.5168 |
| YouTube made AI enhancements to videos without warning or permission | https://www.bbc.com/future/article/20250822-youtube-is-using-ai-to-edit-videos-without-permission | www.bbc.com | 2025-08-25T21:04:55Z | 0.4 | 0.55 | 0.8452 | 0.35 | 0.6 | 0.5168 |
| Writing with LLM is not a shame | https://reflexions.florianernotte.be/post/ai-transparency/ | reflexions.florianernotte.be | 2025-08-24T23:25:42Z | 0.4 | 0.55 | 0.8438 | 0.35 | 0.6 | 0.5166 |
| AWS CEO says using AI to replace junior staff is 'Dumbest thing I've ever heard' | https://www.theregister.com/2025/08/21/aws_ceo_entry_level_jobs_opinion/ | www.theregister.com | 2025-08-22T05:21:24Z | 0.4 | 0.55 | 0.8411 | 0.35 | 0.6 | 0.5162 |
| The warning signs the AI bubble is about to burst |  | www.telegraph.co.uk | 2025-08-22T17:24:18Z | 0.4 | 0.55 | 0.8411 | 0.35 | 0.6 | 0.5162 |
| The warning signs the AI bubble is about to burst | https://www.telegraph.co.uk/business/2025/08/20/ai-report-triggering-panic-and-fear-on-wall-street/ | www.telegraph.co.uk | 2025-08-22T17:24:18Z | 0.4 | 0.55 | 0.8411 | 0.35 | 0.6 | 0.5162 |
| Mark Zuckerberg freezes AI hiring amid bubble fears |  | www.telegraph.co.uk | 2025-08-21T15:27:37Z | 0.4 | 0.55 | 0.8397 | 0.35 | 0.6 | 0.516 |
| Mark Zuckerberg freezes AI hiring amid bubble fears | https://www.telegraph.co.uk/business/2025/08/21/zuckerberg-freezes-ai-hiring-amid-bubble-fears/ | www.telegraph.co.uk | 2025-08-21T15:27:37Z | 0.4 | 0.55 | 0.8397 | 0.35 | 0.6 | 0.516 |
| ArkhamMirror: Airgapped investigation platform with CIA-style hypothesis testing | https://github.com/mantisfury/ArkhamMirror | github.com | 2025-12-16T18:44:26Z | 0.4 | 0.45 | 1.0 | 0.35 | 0.6 | 0.515 |
| Claude Sonnet 4 now supports 1M tokens of context | https://www.anthropic.com/news/1m-context | www.anthropic.com | 2025-08-12T20:57:32Z | 0.25 | 0.76 | 0.8274 | 0.35 | 0.6 | 0.5141 |
| Understanding the Role and Limits of API-Based LLM Monitoring | https://zenodo.org/records/17899057 | zenodo.org | 2025-12-11T12:55:01Z | 0.4 | 0.45 | 0.9932 | 0.35 | 0.6 | 0.514 |
| AI-Generated Misstatement Risk:A Framework for Enterprise Organisations |  | zenodo.org | 2025-12-10T19:42:33Z | 0.4 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.5138 |
| AI-Generated Misstatement Risk:A Framework for Enterprise Organisations | https://zenodo.org/records/17885472 | zenodo.org | 2025-12-10T19:42:33Z | 0.4 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.5138 |
| LilyAI boosts product discovery and conversion with its computer vision platform | https://finance.yahoo.com/news/lily-ai-closes-20m-series-130000796.html | finance.yahoo.com | 2024-03-15T09:19:31Z | 0.7 | 0.55 | 0.1219 | 0.35 | 0.6 | 0.5133 |
| OpenAI's new GPT-5 models announced early by GitHub | https://www.theverge.com/news/752091/openai-gpt-5-model-announcement-github-leak | www.theverge.com | 2025-08-07T09:11:05Z | 0.4 | 0.55 | 0.8205 | 0.35 | 0.6 | 0.5131 |
| The Browser Company's AI browser now has a $20 subscription | https://www.theverge.com/news/756427/browser-company-dia-pro-ai-pricing | www.theverge.com | 2025-08-08T00:36:08Z | 0.4 | 0.55 | 0.8205 | 0.35 | 0.6 | 0.5131 |
| Stockitize, the AI-powered portfolio risk analysis and research tool | https://www.stockitize.com/ | www.stockitize.com | 2025-08-05T01:20:19Z | 0.4 | 0.55 | 0.8164 | 0.35 | 0.6 | 0.5125 |
| Are we repeating the telecoms crash with AI datacenters? | https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/ | martinalderson.com | 2025-12-03T21:00:59Z | 0.4 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.5123 |
| Everyone in Seattle hates AI |  | jonready.com | 2025-12-03T21:28:57Z | 0.4 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.5123 |
| Everyone in Seattle hates AI | https://jonready.com/blog/posts/everyone-in-seattle-hates-ai.html | jonready.com | 2025-12-03T21:28:57Z | 0.4 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.5123 |
| Persona vectors: Monitoring and controlling character traits in language models | https://www.anthropic.com/research/persona-vectors | www.anthropic.com | 2025-08-03T20:10:02Z | 0.25 | 0.76 | 0.8151 | 0.35 | 0.6 | 0.5123 |
| But why is AI bad? |  | daymare.net | 2025-12-02T11:41:59Z | 0.4 | 0.45 | 0.9808 | 0.35 | 0.6 | 0.5121 |
| But why is AI bad? | https://daymare.net/blogs/but-why-is-ai-bad/ | daymare.net | 2025-12-02T11:41:59Z | 0.4 | 0.45 | 0.9808 | 0.35 | 0.6 | 0.5121 |
| Why are we building tools for AI models that haven't launched? |  | sora3ai.io | 2025-12-01T13:13:15Z | 0.4 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.5119 |
| Why are we building tools for AI models that haven't launched? | https://sora3ai.io/ | sora3ai.io | 2025-12-01T13:13:15Z | 0.4 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.5119 |
| Anaconda Raises $150M Series C |  | www.anaconda.com | 2025-07-31T14:52:53Z | 0.4 | 0.55 | 0.811 | 0.35 | 0.6 | 0.5116 |
| Anaconda Raises $150M Series C | https://www.anaconda.com/press/anaconda-raises-150m-series-c-funding-ai-enterprise | www.anaconda.com | 2025-07-31T14:52:53Z | 0.4 | 0.55 | 0.811 | 0.35 | 0.6 | 0.5116 |
| Show HN: I built Magiclip – an all-in-one AI studio |  | magiclip.io | 2025-11-29T14:18:27Z | 0.4 | 0.45 | 0.9767 | 0.35 | 0.6 | 0.5115 |
| Show HN: I built Magiclip – an all-in-one AI studio | https://magiclip.io/ | magiclip.io | 2025-11-29T14:18:27Z | 0.4 | 0.45 | 0.9767 | 0.35 | 0.6 | 0.5115 |
| Irrelevant facts about cats added to math problems increase LLM errors by 300% | https://www.science.org/content/article/scienceadviser-cats-confuse-ai | www.science.org | 2025-07-30T12:30:52Z | 0.4 | 0.55 | 0.8096 | 0.35 | 0.6 | 0.5114 |
| Why do some AI chatbot subscriptions cost more than $200? | https://www.wired.com/story/seriously-why-do-some-ai-chatbot-subscriptions-cost-more-than-200/ | www.wired.com | 2025-07-30T13:52:02Z | 0.4 | 0.55 | 0.8096 | 0.35 | 0.6 | 0.5114 |
| Frameworks (and AI) for marketers who think before they pitch |  | lauradecastro.substack.com | 2025-07-28T12:51:23Z | 0.4 | 0.55 | 0.8068 | 0.35 | 0.6 | 0.511 |
| Frameworks (and AI) for marketers who think before they pitch | https://lauradecastro.substack.com/p/20-frameworks-and-ai-for-marketers | lauradecastro.substack.com | 2025-07-28T12:51:23Z | 0.4 | 0.55 | 0.8068 | 0.35 | 0.6 | 0.511 |
| API that auto-routes to the cheapest AI provider (OpenAI/Anthropic/Gemini) | https://tokensaver.org/ | tokensaver.org | 2025-11-26T20:35:22Z | 0.4 | 0.45 | 0.9726 | 0.35 | 0.6 | 0.5109 |
| OpenAI needs to raise at least $207B by 2030 | https://ft.com/content/23e54a28-6f63-4533-ab96-3756d9c88bad | ft.com | 2025-11-26T19:54:02Z | 0.4 | 0.45 | 0.9726 | 0.35 | 0.6 | 0.5109 |
| JokeAI – AI-powered joke generator built with Next.js and OpenAI | https://www.jokes-ai.top/ | www.jokes-ai.top | 2025-07-27T15:23:49Z | 0.4 | 0.55 | 0.8055 | 0.35 | 0.6 | 0.5108 |
| Show HN: I'm building a website to discover AI tools, AI WITH. ME | https://aiwith.me | aiwith.me | 2024-05-27T05:19:02Z | 0.55 | 0.45 | 0.2219 | 0.75 | 0.6 | 0.5108 |
| An experiment in mood-based movie discovery: Lumigo.tv | https://lumigo.tv/en-US | lumigo.tv | 2025-11-25T11:20:52Z | 0.4 | 0.45 | 0.9712 | 0.35 | 0.6 | 0.5107 |
| Congress to outlaw AI that jacks up prices based on what it knows about you | https://www.theregister.com/2025/07/26/ai_surveillance_pricing/ | www.theregister.com | 2025-07-26T15:40:32Z | 0.4 | 0.55 | 0.8041 | 0.35 | 0.6 | 0.5106 |
| Artificial Intelligence, Scientific Discovery, and Product Innovation [pdf] | https://aidantr.github.io/files/AI_innovation.pdf | aidantr.github.io | 2024-11-12T13:29:30Z | 0.55 | 0.55 | 0.4534 | 0.35 | 0.6 | 0.5105 |
| Show HN: I built a free kids coloring site with AI |  | happykidscoloring.com | 2025-11-24T07:07:40Z | 0.4 | 0.45 | 0.9699 | 0.35 | 0.6 | 0.5105 |
| Show HN: I built a free kids coloring site with AI | https://happykidscoloring.com/en | happykidscoloring.com | 2025-11-24T07:07:40Z | 0.4 | 0.45 | 0.9699 | 0.35 | 0.6 | 0.5105 |
| Boom, bubble, bust, boom. Why should AI be different? | https://crazystupidtech.com/2025/11/21/boom-bubble-bust-boom-why-should-ai-be-different/ | crazystupidtech.com | 2025-11-22T11:47:56Z | 0.4 | 0.45 | 0.9671 | 0.35 | 0.6 | 0.5101 |
| CCProxy – Use any AI model with Claude Code (90% cost reduction) | https://ccproxy.orchestre.dev/ | ccproxy.orchestre.dev | 2025-07-22T15:10:18Z | 0.4 | 0.55 | 0.7986 | 0.35 | 0.6 | 0.5098 |
| Adversarial poetry as a universal single-turn jailbreak mechanism in LLMs | https://arxiv.org/abs/2511.15304 | arxiv.org | 2025-11-20T17:16:05Z | 0.4 | 0.45 | 0.9644 | 0.35 | 0.6 | 0.5097 |
| AI is killing the web – can anything save it? |  | www.economist.com | 2025-07-21T04:51:04Z | 0.4 | 0.55 | 0.7973 | 0.35 | 0.6 | 0.5096 |
| AI is killing the web – can anything save it? | https://www.economist.com/business/2025/07/14/ai-is-killing-the-web-can-anything-save-it | www.economist.com | 2025-07-21T04:51:04Z | 0.4 | 0.55 | 0.7973 | 0.35 | 0.6 | 0.5096 |
| Merg – Deep Research for Media | https://mergai.vercel.app | mergai.vercel.app | 2025-07-21T03:42:31Z | 0.4 | 0.55 | 0.7959 | 0.35 | 0.6 | 0.5094 |
| Nobody knows how to build with AI yet |  | worksonmymachine.substack.com | 2025-07-20T12:09:16Z | 0.4 | 0.55 | 0.7959 | 0.35 | 0.6 | 0.5094 |
| Nobody knows how to build with AI yet | https://worksonmymachine.substack.com/p/nobody-knows-how-to-build-with-ai | worksonmymachine.substack.com | 2025-07-20T12:09:16Z | 0.4 | 0.55 | 0.7959 | 0.35 | 0.6 | 0.5094 |
| Why is AI so slow to spread? |  | www.economist.com | 2025-07-18T06:30:27Z | 0.4 | 0.55 | 0.7932 | 0.35 | 0.6 | 0.509 |
| Why is AI so slow to spread? | https://www.economist.com/finance-and-economics/2025/07/17/why-is-ai-so-slow-to-spread-economics-can-explain | www.economist.com | 2025-07-18T06:30:27Z | 0.4 | 0.55 | 0.7932 | 0.35 | 0.6 | 0.509 |
| Apple Faces Calls to Reboot AI Strategy with Shares Slumping |  | www.bloomberg.com | 2025-07-14T15:18:05Z | 0.4 | 0.55 | 0.7877 | 0.35 | 0.6 | 0.5082 |
| Apple Faces Calls to Reboot AI Strategy with Shares Slumping | https://www.bloomberg.com/news/articles/2025-07-14/apple-faces-calls-to-reboot-ai-strategy-with-shares-slumping | www.bloomberg.com | 2025-07-14T15:18:05Z | 0.4 | 0.55 | 0.7877 | 0.35 | 0.6 | 0.5082 |
| Show HN: We are building AI Teacher for 260M non native English speaking student |  | app.vidyaarthi.ai | 2025-07-14T08:39:11Z | 0.4 | 0.55 | 0.7877 | 0.35 | 0.6 | 0.5082 |
| Show HN: We are building AI Teacher for 260M non native English speaking student | https://app.vidyaarthi.ai/auth | app.vidyaarthi.ai | 2025-07-14T08:39:11Z | 0.4 | 0.55 | 0.7877 | 0.35 | 0.6 | 0.5082 |
| The crawl-to-click gap: Cloudflare data on AI bots, training, and referrals |  | blog.cloudflare.com | 2025-09-01T15:48:31Z | 0.4 | 0.55 | 0.8548 | 0.35 | 0.5 | 0.5082 |
| The crawl-to-click gap: Cloudflare data on AI bots, training, and referrals | https://blog.cloudflare.com/crawlers-click-ai-bots-training/ | blog.cloudflare.com | 2025-09-01T15:48:31Z | 0.4 | 0.55 | 0.8548 | 0.35 | 0.5 | 0.5082 |
| Learning to Reason with LLMs | https://openai.com/index/learning-to-reason-with-llms/ | openai.com | 2024-09-12T19:23:57Z | 0.4 | 0.8 | 0.3699 | 0.35 | 0.6 | 0.508 |
| WhatsCode.app – Build Real Apps via WhatsApp Using AI |  | www.whatscode.app | 2025-07-08T03:54:07Z | 0.4 | 0.55 | 0.7795 | 0.35 | 0.6 | 0.5069 |
| WhatsCode.app – Build Real Apps via WhatsApp Using AI | https://www.whatscode.app/ | www.whatscode.app | 2025-07-08T03:54:07Z | 0.4 | 0.55 | 0.7795 | 0.35 | 0.6 | 0.5069 |
| The trust collapse: Infinite AI content is awful |  | arnon.dk | 2025-11-06T14:42:59Z | 0.4 | 0.45 | 0.9452 | 0.35 | 0.6 | 0.5068 |
| The trust collapse: Infinite AI content is awful | https://arnon.dk/the-trust-collapse-infinite-ai-content-is-awful/ | arnon.dk | 2025-11-06T14:42:59Z | 0.4 | 0.45 | 0.9452 | 0.35 | 0.6 | 0.5068 |
| Problems the AI industry is not addressing adequately |  | www.thealgorithmicbridge.com | 2025-07-05T19:06:41Z | 0.4 | 0.55 | 0.7753 | 0.35 | 0.6 | 0.5063 |
| Problems the AI industry is not addressing adequately | https://www.thealgorithmicbridge.com/p/im-losing-all-trust-in-the-ai-industry | www.thealgorithmicbridge.com | 2025-07-05T19:06:41Z | 0.4 | 0.55 | 0.7753 | 0.35 | 0.6 | 0.5063 |
| New way to organically market your product | https://rankmochi.com | rankmochi.com | 2025-11-02T17:56:12Z | 0.4 | 0.45 | 0.9397 | 0.35 | 0.6 | 0.506 |
| Project Vend: Can Claude run a small shop? (And why does that matter?) | https://www.anthropic.com/research/project-vend-1 | www.anthropic.com | 2025-07-03T16:05:35Z | 0.25 | 0.76 | 0.7726 | 0.35 | 0.6 | 0.5059 |
| OwlAI Assistant for Small Business | https://owlai.cc/ | owlai.cc | 2025-11-01T18:49:57Z | 0.4 | 0.45 | 0.9384 | 0.35 | 0.6 | 0.5058 |
| HN Slop: AI startup ideas generated from Hacker News | https://www.josh.ing/hn-slop | www.josh.ing | 2025-07-02T16:44:32Z | 0.4 | 0.55 | 0.7712 | 0.35 | 0.6 | 0.5057 |
| Sam Altman Slams Meta’s AI Talent Poaching: 'Missionaries Will Beat Mercenaries' |  | www.wired.com | 2025-07-02T05:37:52Z | 0.4 | 0.55 | 0.7712 | 0.35 | 0.6 | 0.5057 |
| Sam Altman Slams Meta’s AI Talent Poaching: 'Missionaries Will Beat Mercenaries' | https://www.wired.com/story/sam-altman-meta-ai-talent-poaching-spree-leaked-messages/ | www.wired.com | 2025-07-02T05:37:52Z | 0.4 | 0.55 | 0.7712 | 0.35 | 0.6 | 0.5057 |
| Cloudflare to introduce pay-per-crawl for AI bots |  | blog.cloudflare.com | 2025-07-01T12:27:33Z | 0.4 | 0.55 | 0.7699 | 0.35 | 0.6 | 0.5055 |
| Cloudflare to introduce pay-per-crawl for AI bots | https://blog.cloudflare.com/introducing-pay-per-crawl/ | blog.cloudflare.com | 2025-07-01T12:27:33Z | 0.4 | 0.55 | 0.7699 | 0.35 | 0.6 | 0.5055 |
| Responses from LLMs are not facts | https://stopcitingai.com/ | stopcitingai.com | 2025-10-30T03:21:01Z | 0.4 | 0.45 | 0.9342 | 0.35 | 0.6 | 0.5051 |
| Meta spent $75B in 3 months on AI infrastructure (CoreWeave, Oracle, Blue Owl) |  | allenarch.dev | 2025-10-29T02:08:17Z | 0.4 | 0.45 | 0.9329 | 0.35 | 0.6 | 0.5049 |
| Meta spent $75B in 3 months on AI infrastructure (CoreWeave, Oracle, Blue Owl) | https://allenarch.dev/blog/meta-75b-ai-infrastructure-bet/ | allenarch.dev | 2025-10-29T02:08:17Z | 0.4 | 0.45 | 0.9329 | 0.35 | 0.6 | 0.5049 |
| OpenAI says over a million people talk to ChatGPT about suicide weekly |  | techcrunch.com | 2025-10-28T12:35:35Z | 0.4 | 0.45 | 0.9329 | 0.35 | 0.6 | 0.5049 |
| OpenAI says over a million people talk to ChatGPT about suicide weekly | https://techcrunch.com/2025/10/27/openai-says-over-a-million-people-talk-to-chatgpt-about-suicide-weekly/ | techcrunch.com | 2025-10-28T12:35:35Z | 0.4 | 0.45 | 0.9329 | 0.35 | 0.6 | 0.5049 |
| Will AI Slop Kill the Internet? [video] |  | www.youtube.com | 2025-06-26T20:20:35Z | 0.4 | 0.55 | 0.763 | 0.35 | 0.6 | 0.5044 |
| Will AI Slop Kill the Internet? [video] | https://www.youtube.com/watch?v=NuIMZBseAOM | www.youtube.com | 2025-06-26T20:20:35Z | 0.4 | 0.55 | 0.763 | 0.35 | 0.6 | 0.5044 |
| SPL – AI patterns with verifiable truth scores | https://github.com/spliq/spl | github.com | 2025-10-25T12:53:35Z | 0.4 | 0.45 | 0.9288 | 0.35 | 0.6 | 0.5043 |
| GitHub CEO: manual coding remains key despite AI boom | https://www.techinasia.com/news/github-ceo-manual-coding-remains-key-despite-ai-boom | www.techinasia.com | 2025-06-24T06:47:44Z | 0.4 | 0.55 | 0.7603 | 0.35 | 0.6 | 0.504 |
| Ask HN: Would you use daily check-ins to build your dev brand? | https://devcue.io | devcue.io | 2025-10-23T22:04:45Z | 0.4 | 0.45 | 0.926 | 0.35 | 0.6 | 0.5039 |
| We tested 20 LLMs for ideological bias, revealing distinct alignments | https://anomify.ai/resources/articles/llm-bias | anomify.ai | 2025-10-23T14:39:32Z | 0.4 | 0.45 | 0.926 | 0.35 | 0.6 | 0.5039 |
| Sycophancy in GPT-4o | https://openai.com/index/sycophancy-in-gpt-4o/ | openai.com | 2025-04-30T05:02:26Z | 0.25 | 0.8 | 0.6849 | 0.35 | 0.6 | 0.5027 |
| The AI Coach for Salary Negotiation | https://offercoach.ai/ | offercoach.ai | 2025-10-17T04:29:21Z | 0.4 | 0.45 | 0.9178 | 0.35 | 0.6 | 0.5027 |
| Microsoft drops AI sales targets in half after salespeople miss their quotas |  | arstechnica.com | 2025-12-04T21:22:42Z | 0.4 | 0.45 | 0.9836 | 0.35 | 0.5 | 0.5025 |
| Microsoft drops AI sales targets in half after salespeople miss their quotas | https://arstechnica.com/ai/2025/12/microsoft-slashes-ai-sales-growth-targets-as-customers-resist-unproven-agents/ | arstechnica.com | 2025-12-04T21:22:42Z | 0.4 | 0.45 | 0.9836 | 0.35 | 0.5 | 0.5025 |
| Show HN: AI Page Inspector – See what ChatGPT reads from your site | https://aiseotracker.com/page-inspector | aiseotracker.com | 2025-10-16T06:45:47Z | 0.4 | 0.45 | 0.9164 | 0.35 | 0.6 | 0.5025 |
| Show HN: AI-Powered Stock Market Analyst | https://decodeinvesting.com/financial_analyst/AAPL/chat/lima | decodeinvesting.com | 2023-09-30T18:56:23Z | 0.55 | 0.45 | 0.1 | 0.75 | 0.7 | 0.5025 |
| Meta invests $14.3B in Scale AI to kick-start superintelligence lab |  | www.nytimes.com | 2025-06-13T13:26:49Z | 0.4 | 0.55 | 0.7452 | 0.35 | 0.6 | 0.5018 |
| Meta invests $14.3B in Scale AI to kick-start superintelligence lab | https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html | www.nytimes.com | 2025-06-13T13:26:49Z | 0.4 | 0.55 | 0.7452 | 0.35 | 0.6 | 0.5018 |
| Cheap AI Tools May Come at a Big Long-Term Cost | https://www.wired.com/story/pricing-ai-agents-increasing-costs/ | www.wired.com | 2025-06-13T02:00:00Z | 0.4 | 0.55 | 0.7438 | 0.35 | 0.6 | 0.5016 |
| Apple Fails to Clear a Low Bar on AI |  | www.wsj.com | 2025-06-10T15:06:37Z | 0.4 | 0.55 | 0.7411 | 0.35 | 0.6 | 0.5012 |
| Apple Fails to Clear a Low Bar on AI | https://www.wsj.com/tech/ai/apple-ai-strategy-wwdc-challenges-bdae4fb5 | www.wsj.com | 2025-06-10T15:06:37Z | 0.4 | 0.55 | 0.7411 | 0.35 | 0.6 | 0.5012 |
| Askanyquestion.ai – No-Code AI Search with Shopify and Stripe | https://www.askanyquestion.ai | www.askanyquestion.ai | 2025-06-09T14:10:56Z | 0.4 | 0.55 | 0.7397 | 0.35 | 0.6 | 0.501 |
| Launch HN: LlamaFarm (YC W22) – Open-source framework for distributed AI |  | github.com | 2025-10-07T19:39:56Z | 0.4 | 0.45 | 0.9041 | 0.35 | 0.6 | 0.5006 |
| Launch HN: LlamaFarm (YC W22) – Open-source framework for distributed AI | https://github.com/llama-farm/llamafarm | github.com | 2025-10-07T19:39:56Z | 0.4 | 0.45 | 0.9041 | 0.35 | 0.6 | 0.5006 |
| The (economic) AI apocalypse is nigh |  | pluralistic.net | 2025-10-06T13:32:52Z | 0.4 | 0.45 | 0.9027 | 0.35 | 0.6 | 0.5004 |
| The (economic) AI apocalypse is nigh | https://pluralistic.net/2025/09/27/econopocalypse/ | pluralistic.net | 2025-10-06T13:32:52Z | 0.4 | 0.45 | 0.9027 | 0.35 | 0.6 | 0.5004 |
| I think I'm done thinking about GenAI for now |  | blog.glyph.im | 2025-06-05T21:01:00Z | 0.4 | 0.55 | 0.7342 | 0.35 | 0.6 | 0.5001 |
| I think I'm done thinking about GenAI for now | https://blog.glyph.im/2025/06/i-think-im-done-thinking-about-genai-for-now.html | blog.glyph.im | 2025-06-05T21:01:00Z | 0.4 | 0.55 | 0.7342 | 0.35 | 0.6 | 0.5001 |
| The ‘white-collar bloodbath’ is all part of the AI hype machine |  | www.cnn.com | 2025-06-02T10:44:40Z | 0.4 | 0.55 | 0.7301 | 0.35 | 0.6 | 0.4995 |
| The ‘white-collar bloodbath’ is all part of the AI hype machine | https://www.cnn.com/2025/05/30/business/anthropic-amodei-ai-jobs-nightcap | www.cnn.com | 2025-06-02T10:44:40Z | 0.4 | 0.55 | 0.7301 | 0.35 | 0.6 | 0.4995 |
| I built an AI tool to summarize videos, useful for me, but would you use it? | https://github.com/Ga0512/video-analysis | github.com | 2025-10-02T01:22:16Z | 0.4 | 0.45 | 0.8959 | 0.35 | 0.6 | 0.4994 |
| Mary Meeker's first Trends report since 2019, focused on AI |  | www.bondcap.com | 2025-06-01T17:58:42Z | 0.4 | 0.55 | 0.7288 | 0.35 | 0.6 | 0.4993 |
| Mary Meeker's first Trends report since 2019, focused on AI | https://www.bondcap.com/reports/tai | www.bondcap.com | 2025-06-01T17:58:42Z | 0.4 | 0.55 | 0.7288 | 0.35 | 0.6 | 0.4993 |
| Getting AI to work in complex codebases |  | github.com | 2025-09-24T02:38:27Z | 0.4 | 0.45 | 0.8863 | 0.35 | 0.6 | 0.4979 |
| Researchers claim ChatGPT o3 bypassed shutdown in controlled test | https://www.bleepingcomputer.com/news/artificial-intelligence/researchers-claim-chatgpt-o3-bypassed-shutdown-in-controlled-test/ | www.bleepingcomputer.com | 2025-05-25T22:50:00Z | 0.4 | 0.55 | 0.7192 | 0.35 | 0.6 | 0.4979 |
| Getting AI to work in complex codebases | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md | github.com | 2025-09-24T02:38:27Z | 0.4 | 0.45 | 0.8849 | 0.35 | 0.6 | 0.4977 |
| Show HN: AI Steve – ideas to improve your product | https://www.conversionexamples.com/ai | www.conversionexamples.com | 2023-10-03T23:45:53Z | 0.55 | 0.55 | 0.1 | 0.55 | 0.7 | 0.4975 |
| An untidy history of AI across four books |  | hedgehogreview.com | 2025-09-20T02:55:49Z | 0.4 | 0.45 | 0.8808 | 0.35 | 0.6 | 0.4971 |
| An untidy history of AI across four books | https://hedgehogreview.com/issues/lessons-of-babel/articles/perplexity | hedgehogreview.com | 2025-09-20T02:55:49Z | 0.4 | 0.45 | 0.8795 | 0.35 | 0.6 | 0.4969 |
| Google reveals $250 per month 'AI Ultra' plan | https://www.theverge.com/news/670495/google-ai-ultra-plan-pricing-launch-io-2025 | www.theverge.com | 2025-05-20T18:52:32Z | 0.4 | 0.55 | 0.7123 | 0.35 | 0.6 | 0.4968 |
| The behavior of LLMs in hiring decisions: Systemic biases in candidate selection | https://davidrozado.substack.com/p/the-strange-behavior-of-llms-in-hiring | davidrozado.substack.com | 2025-05-20T11:56:50Z | 0.4 | 0.55 | 0.7123 | 0.35 | 0.6 | 0.4968 |
| Learn Your Way: Reimagining Textbooks with Generative AI |  | research.google | 2025-09-18T21:30:22Z | 0.4 | 0.45 | 0.8781 | 0.35 | 0.6 | 0.4967 |
| Learn Your Way: Reimagining Textbooks with Generative AI | https://research.google/blog/learn-your-way-reimagining-textbooks-with-generative-ai/ | research.google | 2025-09-18T21:30:22Z | 0.4 | 0.45 | 0.8781 | 0.35 | 0.6 | 0.4967 |
| DeepMind and OpenAI win gold at ICPC |  | codeforces.com | 2025-09-17T23:26:35Z | 0.4 | 0.45 | 0.8767 | 0.35 | 0.6 | 0.4965 |
| DeepMind and OpenAI win gold at ICPC | https://codeforces.com/blog/entry/146536 | codeforces.com | 2025-09-17T23:26:35Z | 0.4 | 0.45 | 0.8767 | 0.35 | 0.6 | 0.4965 |
| Slack has raised our charges by $195k per year | https://skyfall.dev/posts/slack | skyfall.dev | 2025-09-18T03:04:49Z | 0.4 | 0.45 | 0.8767 | 0.35 | 0.6 | 0.4965 |
| Will AI be the basis of many future industrial fortunes, or a net loser? | https://joincolossus.com/article/ai-will-not-make-you-rich/ | joincolossus.com | 2025-09-14T01:56:14Z | 0.4 | 0.45 | 0.8712 | 0.35 | 0.6 | 0.4957 |
| YouTube Hates AI movie trailers here's why | https://www.pcworld.com/article/2780240/youtube-hates-ai-movie-trailers-as-much-as-i-do.html | www.pcworld.com | 2025-05-14T15:41:43Z | 0.4 | 0.55 | 0.7041 | 0.35 | 0.6 | 0.4956 |
| How Enterprises Can Audit Their AI Visibility: A PSOS -Based Framework | https://zenodo.org/records/17100766 | zenodo.org | 2025-09-11T15:30:12Z | 0.4 | 0.45 | 0.8685 | 0.35 | 0.6 | 0.4953 |
| Mistral raises 1.7B€, partners with ASML | https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai | mistral.ai | 2025-09-09T10:55:40Z | 0.4 | 0.45 | 0.8658 | 0.35 | 0.6 | 0.4949 |
| GPT-5 Thinking in ChatGPT (a.k.a. Research Goblin) is good at search | https://simonwillison.net/2025/Sep/6/research-goblin/ | simonwillison.net | 2025-09-08T13:03:57Z | 0.4 | 0.45 | 0.8644 | 0.35 | 0.6 | 0.4947 |
| The AI bubble argument misunderstands both bubbles and AI |  | danielmiessler.com | 2025-09-08T19:44:31Z | 0.4 | 0.45 | 0.8644 | 0.35 | 0.6 | 0.4947 |
| The AI bubble argument misunderstands both bubbles and AI | https://danielmiessler.com/blog/no-ai-is-not-a-bubble | danielmiessler.com | 2025-09-08T19:44:31Z | 0.4 | 0.45 | 0.8644 | 0.35 | 0.6 | 0.4947 |
| Synthetic: All-Inclusive AI Platform with 19 Always-On Models for $20-60/Month | https://synthetic.new/landing/home | synthetic.new | 2025-09-06T09:06:25Z | 0.4 | 0.45 | 0.8616 | 0.35 | 0.6 | 0.4942 |
| Show HN: Peek – an AI "Spotify wrapped" for your money | https://apps.apple.com/us/app/peek-ai-personal-finance-app/id6742875016 | apps.apple.com | 2025-05-05T14:16:41Z | 0.4 | 0.55 | 0.6918 | 0.35 | 0.6 | 0.4938 |
| An LLM is a lossy encyclopedia | https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/ | simonwillison.net | 2025-09-03T12:37:09Z | 0.4 | 0.45 | 0.8575 | 0.35 | 0.6 | 0.4936 |
| Anthropic Raises $13B at $183B Valuation: AI Bubble Peak or Actual Revenue? | https://toolstac.com/news/2025-09-02/anthropic-funding-surge | toolstac.com | 2025-09-03T05:26:23Z | 0.4 | 0.45 | 0.8575 | 0.35 | 0.6 | 0.4936 |
| Exa, 35 person startup building a new search engine, raises $85M Series B | https://exa.ai/blog/announcing-series-b | exa.ai | 2025-09-03T18:31:31Z | 0.4 | 0.45 | 0.8575 | 0.35 | 0.6 | 0.4936 |
| Claude can now connect to your world |  | www.anthropic.com | 2025-05-01T18:10:40Z | 0.25 | 0.76 | 0.6863 | 0.35 | 0.6 | 0.4929 |
| Claude can now connect to your world | https://www.anthropic.com/news/integrations | www.anthropic.com | 2025-05-01T18:10:40Z | 0.25 | 0.76 | 0.6863 | 0.35 | 0.6 | 0.4929 |
| The First AI Store: A New Way to Experience AI | https://www.proxly.ai/blog/a-new-way-to-experience-ai | www.proxly.ai | 2025-04-30T17:07:55Z | 0.4 | 0.55 | 0.6849 | 0.35 | 0.6 | 0.4927 |
| AI.gov | https://ai.gov/ | ai.gov | 2023-10-31T08:03:12Z | 0.4 | 0.9 | 0.1 | 0.35 | 0.6 | 0.4925 |
| Duolingo will replace contract workers with AI |  | www.theverge.com | 2025-04-29T12:11:46Z | 0.4 | 0.55 | 0.6836 | 0.35 | 0.6 | 0.4925 |
| Duolingo will replace contract workers with AI | https://www.theverge.com/news/657594/duolingo-ai-first-replace-contract-workers | www.theverge.com | 2025-04-29T12:11:46Z | 0.4 | 0.55 | 0.6836 | 0.35 | 0.6 | 0.4925 |
| How Can I Grow My AI Image Detection App (ImgDetect) Organically? | https://apps.apple.com/us/app/ai-image-detector-imgdetect/id6743627428 | apps.apple.com | 2025-04-30T01:53:53Z | 0.4 | 0.55 | 0.6836 | 0.35 | 0.6 | 0.4925 |
| The coming knowledge-work supply-chain crisis |  | worksonmymachine.substack.com | 2025-04-29T17:21:34Z | 0.4 | 0.55 | 0.6836 | 0.35 | 0.6 | 0.4925 |
| The coming knowledge-work supply-chain crisis | https://worksonmymachine.substack.com/p/the-coming-knowledge-work-supply | worksonmymachine.substack.com | 2025-04-29T17:21:34Z | 0.4 | 0.55 | 0.6836 | 0.35 | 0.6 | 0.4925 |
| Acquisitions, consolidation, and innovation in AI |  | frontierai.substack.com | 2025-04-24T19:37:16Z | 0.4 | 0.55 | 0.6767 | 0.35 | 0.6 | 0.4915 |
| Acquisitions, consolidation, and innovation in AI | https://frontierai.substack.com/p/acquisitions-consolidation-and-innovation | frontierai.substack.com | 2025-04-24T19:37:16Z | 0.4 | 0.55 | 0.6767 | 0.35 | 0.6 | 0.4915 |
| Microsoft Publisher will no longer be supported after October 2026 | https://support.microsoft.com/en-gb/office/microsoft-publisher-will-no-longer-be-supported-after-october-2026-ee6302a2-4bc7-4841-babf-8e9be3acbfd7 | support.microsoft.com | 2025-03-05T08:45:18Z | 0.25 | 0.8 | 0.6082 | 0.35 | 0.6 | 0.4912 |
| ReachLLM – Dominate the AI Search Era | https://reachllm.com/ | reachllm.com | 2025-08-22T18:37:08Z | 0.4 | 0.45 | 0.8411 | 0.35 | 0.6 | 0.4912 |
| Google Paid Samsung 'Enormous Sums' for Gemini AI App Installs |  | www.bloomberg.com | 2025-04-22T03:23:07Z | 0.4 | 0.55 | 0.674 | 0.35 | 0.6 | 0.4911 |
| Google Paid Samsung 'Enormous Sums' for Gemini AI App Installs | https://www.bloomberg.com/news/articles/2025-04-21/google-paid-samsung-enormous-sums-for-gemini-ai-app-installs | www.bloomberg.com | 2025-04-22T03:23:07Z | 0.4 | 0.55 | 0.674 | 0.35 | 0.6 | 0.4911 |
| Supabase raises $200M Series D at $2B valuation |  | finance.yahoo.com | 2025-04-22T17:39:09Z | 0.4 | 0.55 | 0.674 | 0.35 | 0.6 | 0.4911 |
| Supabase raises $200M Series D at $2B valuation | https://finance.yahoo.com/news/exclusive-supabase-raises-200-million-112154867.html | finance.yahoo.com | 2025-04-22T17:39:09Z | 0.4 | 0.55 | 0.674 | 0.35 | 0.6 | 0.4911 |
| 95% of Companies See 'Zero Return' on $30B Generative AI Spend | https://thedailyadda.com/95-of-companies-see-zero-return-on-30-billion-generative-ai-spend-mit-report-finds/ | thedailyadda.com | 2025-08-21T16:30:17Z | 0.4 | 0.45 | 0.8397 | 0.35 | 0.6 | 0.491 |
| In the long run, LLMs make us dumber | https://desunit.com/blog/in-the-long-run-llms-make-us-dumber/ | desunit.com | 2025-08-21T22:07:10Z | 0.4 | 0.45 | 0.8397 | 0.35 | 0.6 | 0.491 |
| GPT-4.5 | https://openai.com/index/introducing-gpt-4-5/ | openai.com | 2025-02-27T20:26:53Z | 0.25 | 0.8 | 0.6 | 0.35 | 0.6 | 0.49 |
| Stanford 2024 AI Index Report [pdf] | https://aiindex.stanford.edu/wp-content/uploads/2024/04/HAI_AI-Index-Report-2024.pdf | aiindex.stanford.edu | 2024-04-16T14:39:27Z | 0.4 | 0.85 | 0.1658 | 0.35 | 0.6 | 0.4899 |
| Notion Mail Is Out | https://www.notion.com/product/mail | www.notion.com | 2025-04-15T15:45:03Z | 0.4 | 0.55 | 0.6644 | 0.35 | 0.6 | 0.4897 |
| Why LLMs can't really build software | https://zed.dev/blog/why-llms-cant-build-software | zed.dev | 2025-08-15T13:50:18Z | 0.4 | 0.45 | 0.8315 | 0.35 | 0.6 | 0.4897 |
| Apple brings OpenAI's GPT-5 to iOS and macOS |  | arstechnica.com | 2025-08-11T17:29:37Z | 0.4 | 0.45 | 0.826 | 0.35 | 0.6 | 0.4889 |
| Apple brings OpenAI's GPT-5 to iOS and macOS | https://arstechnica.com/ai/2025/08/apple-brings-openais-gpt-5-to-ios-and-macos/ | arstechnica.com | 2025-08-11T17:29:37Z | 0.4 | 0.45 | 0.826 | 0.35 | 0.6 | 0.4889 |
| Claude's Max Plan | https://www.anthropic.com/news/max-plan | www.anthropic.com | 2025-04-10T07:39:02Z | 0.25 | 0.76 | 0.6575 | 0.35 | 0.6 | 0.4886 |
| Multilingual AI product name generator | https://magicley.com/blog/tag/AI%20product%20name%20generator | magicley.com | 2024-11-27T18:22:36Z | 0.55 | 0.45 | 0.474 | 0.35 | 0.6 | 0.4886 |
| UAE offers free open-source AI as alternative to US and China |  | restofworld.org | 2025-08-08T16:28:50Z | 0.4 | 0.45 | 0.8219 | 0.35 | 0.6 | 0.4883 |
| UAE offers free open-source AI as alternative to US and China | https://restofworld.org/2025/chatgpt-alternative-uae-falcon-ai/ | restofworld.org | 2025-08-08T16:28:50Z | 0.4 | 0.45 | 0.8219 | 0.35 | 0.6 | 0.4883 |
| I gave the AI arms and legs then it rejected me |  | grell.dev | 2025-08-06T09:39:02Z | 0.4 | 0.45 | 0.8192 | 0.35 | 0.6 | 0.4879 |
| I gave the AI arms and legs then it rejected me | https://grell.dev/blog/ai_rejection | grell.dev | 2025-08-06T09:39:02Z | 0.4 | 0.45 | 0.8192 | 0.35 | 0.6 | 0.4879 |
| Mozilla appoints new CEO Anthony Enzor-Demeo |  | blog.mozilla.org | 2025-12-16T14:31:46Z | 0.25 | 0.55 | 1.0 | 0.35 | 0.6 | 0.4875 |
| Mozilla appoints new CEO Anthony Enzor-Demeo | https://blog.mozilla.org/en/mozilla/leadership/mozillas-next-chapter-anthony-enzor-demeo-new-ceo/ | blog.mozilla.org | 2025-12-16T14:31:46Z | 0.25 | 0.55 | 1.0 | 0.35 | 0.6 | 0.4875 |
| The Impact of Generative AI on Critical Thinking [pdf] | https://www.microsoft.com/en-us/research/uploads/prod/2025/01/lee_2025_ai_critical_thinking_survey.pdf | www.microsoft.com | 2025-02-15T13:46:05Z | 0.25 | 0.8 | 0.5836 | 0.35 | 0.6 | 0.4875 |
| This is not the future |  | blog.mathieui.net | 2025-12-16T16:06:47Z | 0.25 | 0.55 | 1.0 | 0.35 | 0.6 | 0.4875 |
| This is not the future | https://blog.mathieui.net/this-is-not-the-future.html | blog.mathieui.net | 2025-12-16T16:06:47Z | 0.25 | 0.55 | 1.0 | 0.35 | 0.6 | 0.4875 |
| Appdna.ai – Agency-level app growth strategies without the $5K retainer | https://www.appdna.ai/ | www.appdna.ai | 2025-04-04T13:05:17Z | 0.4 | 0.55 | 0.6493 | 0.35 | 0.6 | 0.4874 |
| SoundCloud has banned VPN access |  | old.reddit.com | 2025-12-15T12:58:57Z | 0.25 | 0.55 | 0.9986 | 0.35 | 0.6 | 0.4873 |
| SoundCloud has banned VPN access | https://old.reddit.com/r/SoundCloudMusic/comments/1pltd19/soundcloud_just_banned_vpn_access/ | old.reddit.com | 2025-12-15T12:58:57Z | 0.25 | 0.55 | 0.9986 | 0.35 | 0.6 | 0.4873 |
| Elevated errors across many models |  | status.claude.com | 2025-12-14T22:47:07Z | 0.25 | 0.55 | 0.9973 | 0.35 | 0.6 | 0.4871 |
| Elevated errors across many models | https://status.claude.com/incidents/9g6qpr72ttbr | status.claude.com | 2025-12-14T22:47:07Z | 0.25 | 0.55 | 0.9973 | 0.35 | 0.6 | 0.4871 |
| macOS 26.2 enables fast AI clusters with RDMA over Thunderbolt | https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt | developer.apple.com | 2025-12-12T23:31:23Z | 0.25 | 0.55 | 0.9945 | 0.35 | 0.6 | 0.4867 |
| Automating Interactive Fiction Logic Generation with LLMs in Emacs | https://blog.tendollaradventure.com/automating-story-logic-with-llms/ | blog.tendollaradventure.com | 2025-04-01T00:37:06Z | 0.4 | 0.55 | 0.6438 | 0.35 | 0.6 | 0.4866 |
| AWS introduces Graviton5–the company's most powerful and efficient CPU | https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2 | www.aboutamazon.com | 2025-12-12T00:08:35Z | 0.25 | 0.55 | 0.9932 | 0.35 | 0.6 | 0.4865 |
| Is it a bubble? | https://www.oaktreecapital.com/insights/memo/is-it-a-bubble | www.oaktreecapital.com | 2025-12-11T06:05:17Z | 0.25 | 0.55 | 0.9932 | 0.35 | 0.6 | 0.4865 |
| Auto-grading decade-old Hacker News discussions with hindsight | https://karpathy.bearblog.dev/auto-grade-hn/ | karpathy.bearblog.dev | 2025-12-11T01:04:57Z | 0.25 | 0.55 | 0.9918 | 0.35 | 0.6 | 0.4863 |
| The Real Story Behind Sam Altman’s Firing From OpenAI | https://www.wsj.com/tech/ai/the-real-story-behind-sam-altman-firing-from-openai-efd51a5d | www.wsj.com | 2025-03-29T14:48:05Z | 0.4 | 0.55 | 0.6411 | 0.35 | 0.6 | 0.4862 |
| 30 Year Anniversary of WarCraft II: Tides of Darkness |  | www.jorsys.org | 2025-12-09T22:02:54Z | 0.25 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.4861 |
| 30 Year Anniversary of WarCraft II: Tides of Darkness | https://www.jorsys.org/archive/december_2025.html#newsitem_2025-12-09T07:42:19Z | www.jorsys.org | 2025-12-09T22:02:54Z | 0.25 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.4861 |
| Blurble – An anonymous confessions feed to combat the loneliness epidemic |  | blurble.manus.space | 2025-12-09T18:21:46Z | 0.25 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.4861 |
| Blurble – An anonymous confessions feed to combat the loneliness epidemic | https://blurble.manus.space/ | blurble.manus.space | 2025-12-09T18:21:46Z | 0.25 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.4861 |
| [Removed] | https://blog.shortround.space/blog/how-i-misused-llms-to-diagnose-myself-and-ended-up-bedridden-for-a-week/ | blog.shortround.space | 2025-12-09T22:56:01Z | 0.25 | 0.55 | 0.9904 | 0.35 | 0.6 | 0.4861 |
| FDA has approved Yeztugo, a drug that provides protection against HIV infection | https://newatlas.com/infectious-diseases/hiv-prevention-fda-lenacapavir/ | newatlas.com | 2025-07-28T23:10:29Z | 0.4 | 0.45 | 0.8068 | 0.35 | 0.6 | 0.486 |
| The "confident idiot" problem: Why AI needs hard rules, not vibe checks | https://steerlabs.substack.com/p/confident-idiot-problem | steerlabs.substack.com | 2025-12-08T16:26:40Z | 0.25 | 0.55 | 0.989 | 0.35 | 0.6 | 0.4858 |
| Tracing the thoughts of a large language model | https://www.anthropic.com/research/tracing-thoughts-language-model | www.anthropic.com | 2025-03-27T18:13:05Z | 0.25 | 0.76 | 0.6384 | 0.35 | 0.6 | 0.4858 |
| The unexpected effectiveness of one-shot decompilation with Claude | https://blog.chrislewis.au/the-unexpected-effectiveness-of-one-shot-decompilation-with-claude/ | blog.chrislewis.au | 2025-12-07T11:30:39Z | 0.25 | 0.55 | 0.9877 | 0.35 | 0.6 | 0.4857 |
| Google’s two-year frenzy to catch up with OpenAI |  | www.wired.com | 2025-03-26T21:23:53Z | 0.4 | 0.55 | 0.637 | 0.35 | 0.6 | 0.4855 |
| Google’s two-year frenzy to catch up with OpenAI | https://www.wired.com/story/google-openai-gemini-chatgpt-artificial-intelligence/ | www.wired.com | 2025-03-26T21:23:53Z | 0.4 | 0.55 | 0.637 | 0.35 | 0.6 | 0.4855 |
| Stateless Persona Continuity in LLMs: Cross-Window Anchors Beyond Context Limits | https://github.com/JasonLyu3007/Behavioral-Resonance | github.com | 2025-07-26T02:57:40Z | 0.4 | 0.45 | 0.8027 | 0.35 | 0.6 | 0.4854 |
| Why Apple Is Moving Intelligence Back to Your Laptop |  | www.apple.com | 2025-12-06T12:09:34Z | 0.25 | 0.55 | 0.9863 | 0.35 | 0.6 | 0.4854 |
| Why Apple Is Moving Intelligence Back to Your Laptop | https://www.apple.com/ | www.apple.com | 2025-12-06T12:09:34Z | 0.25 | 0.55 | 0.9863 | 0.35 | 0.6 | 0.4854 |
| Netflix to Acquire Warner Bros |  | about.netflix.com | 2025-12-05T18:21:41Z | 0.25 | 0.55 | 0.9849 | 0.35 | 0.6 | 0.4852 |
| Netflix to Acquire Warner Bros | https://about.netflix.com/en/news/netflix-to-acquire-warner-bros | about.netflix.com | 2025-12-05T18:21:41Z | 0.25 | 0.55 | 0.9849 | 0.35 | 0.6 | 0.4852 |
| Apple Releases Open Weights Video Model |  | starflow-v.github.io | 2025-12-02T19:45:34Z | 0.25 | 0.55 | 0.9808 | 0.35 | 0.6 | 0.4846 |
| Apple Releases Open Weights Video Model | https://starflow-v.github.io | starflow-v.github.io | 2025-12-02T19:45:34Z | 0.25 | 0.55 | 0.9808 | 0.35 | 0.6 | 0.4846 |
| Automate product requirement with AI PM | https://www.buildink.io/ | www.buildink.io | 2024-07-08T18:10:32Z | 0.55 | 0.55 | 0.2795 | 0.35 | 0.6 | 0.4844 |
| John Giannandrea to retire from Apple |  | www.apple.com | 2025-12-01T23:06:51Z | 0.25 | 0.55 | 0.9795 | 0.35 | 0.6 | 0.4844 |
| John Giannandrea to retire from Apple | https://www.apple.com/newsroom/2025/12/john-giannandrea-to-retire-from-apple/ | www.apple.com | 2025-12-01T23:06:51Z | 0.25 | 0.55 | 0.9795 | 0.35 | 0.6 | 0.4844 |
| OpenAI Audio Models | https://www.openai.fm/ | www.openai.fm | 2025-03-20T18:34:27Z | 0.4 | 0.55 | 0.6288 | 0.35 | 0.6 | 0.4843 |
| The Golden Rule Goes Digital: Being Mean to LLMs Might Be Our Dumbest Gamble | https://substack.com/home/post/p-168721801 | substack.com | 2025-07-19T19:16:36Z | 0.4 | 0.45 | 0.7945 | 0.35 | 0.6 | 0.4842 |
| It's Always the Process, Stupid |  | its.promp.td | 2025-11-29T16:44:19Z | 0.25 | 0.55 | 0.9767 | 0.35 | 0.6 | 0.484 |
| It's Always the Process, Stupid | https://its.promp.td/its-always-the-process-stupid/ | its.promp.td | 2025-11-29T16:44:19Z | 0.25 | 0.55 | 0.9767 | 0.35 | 0.6 | 0.484 |
| N.Y. Law Could Set Stage for A.I. Regulation's Next 'Big Battleground' | https://www.nytimes.com/2025/11/29/nyregion/personalized-surveillance-pricing-ai-new-york.html | www.nytimes.com | 2025-11-29T16:57:12Z | 0.25 | 0.55 | 0.9767 | 0.35 | 0.6 | 0.484 |
| Delta moves to eliminate set prices, use AI to set your personal ticket price | https://fortune.com/2025/07/16/delta-moves-toward-eliminating-set-prices-in-favor-of-ai-that-determines-how-much-you-personally-will-pay-for-a-ticket/ | fortune.com | 2025-07-17T19:06:42Z | 0.4 | 0.45 | 0.7918 | 0.35 | 0.6 | 0.4838 |
| Billionaires Convince Themselves Chatbots Close to Making Scientific Discoveries | https://gizmodo.com/billionaires-convince-themselves-ai-is-close-to-making-new-scientific-discoveries-2000629060 | gizmodo.com | 2025-07-16T15:16:06Z | 0.4 | 0.45 | 0.7904 | 0.35 | 0.6 | 0.4836 |
| DRAM prices are spiking, but I don't trust the industry's why |  | www.xda-developers.com | 2025-11-27T03:18:54Z | 0.25 | 0.55 | 0.974 | 0.35 | 0.6 | 0.4836 |
| DRAM prices are spiking, but I don't trust the industry's why | https://www.xda-developers.com/dram-prices-spiking-dont-trust-industry-reasons/ | www.xda-developers.com | 2025-11-27T03:18:54Z | 0.25 | 0.55 | 0.974 | 0.35 | 0.6 | 0.4836 |
| LLM Daydreaming | https://gwern.net/ai-daydreaming | gwern.net | 2025-07-16T14:34:06Z | 0.4 | 0.45 | 0.7904 | 0.35 | 0.6 | 0.4836 |
| Stadia Maps MCP Server – Location Context for AI | https://github.com/stadiamaps/stadiamaps-mcp-server-ts | github.com | 2025-07-16T12:20:45Z | 0.4 | 0.45 | 0.7904 | 0.35 | 0.6 | 0.4836 |
| AI slows down open source developers. Peter Naur can teach us why | https://johnwhiles.com/posts/mental-models-vs-ai-tools | johnwhiles.com | 2025-07-14T18:44:59Z | 0.4 | 0.45 | 0.7877 | 0.35 | 0.6 | 0.4832 |
| Cognition (Devin AI) to Acquire Windsurf |  | cognition.ai | 2025-07-14T20:13:58Z | 0.4 | 0.45 | 0.7877 | 0.35 | 0.6 | 0.4832 |
| Cognition (Devin AI) to Acquire Windsurf | https://cognition.ai/blog/windsurf | cognition.ai | 2025-07-14T20:13:58Z | 0.4 | 0.45 | 0.7877 | 0.35 | 0.6 | 0.4832 |
| PS5 now costs less than 64GB of DDR5 memory. RAM jumps to $600 due to shortage |  | www.tomshardware.com | 2025-11-25T20:09:28Z | 0.25 | 0.55 | 0.9712 | 0.35 | 0.6 | 0.4832 |
| PS5 now costs less than 64GB of DDR5 memory. RAM jumps to $600 due to shortage | https://www.tomshardware.com/pc-components/ddr5/64gb-of-ddr5-memory-now-costs-more-than-an-entire-ps5-even-after-a-discount-trident-z5-neo-kit-jumps-to-usd600-due-to-dram-shortage-and-its-expected-to-get-worse-into-2026 | www.tomshardware.com | 2025-11-25T20:09:28Z | 0.25 | 0.55 | 0.9712 | 0.35 | 0.6 | 0.4832 |
| Mind-reading devices can now predict preconscious thoughts | https://www.nature.com/articles/d41586-025-03714-0 | www.nature.com | 2025-11-24T20:50:54Z | 0.25 | 0.55 | 0.9699 | 0.35 | 0.6 | 0.483 |
| No clicks, no content: The unsustainable future of AI search |  | bradt.ca | 2025-08-31T21:41:01Z | 0.4 | 0.45 | 0.8534 | 0.35 | 0.5 | 0.483 |
| No clicks, no content: The unsustainable future of AI search | https://bradt.ca/blog/no-clicks-no-content/ | bradt.ca | 2025-08-31T21:41:01Z | 0.4 | 0.45 | 0.8534 | 0.35 | 0.5 | 0.483 |
| Introducing Operator | https://openai.com/index/introducing-operator/ | openai.com | 2025-01-23T18:50:36Z | 0.25 | 0.8 | 0.5521 | 0.35 | 0.6 | 0.4828 |
| Show HN: Blink – Your Personal Amazon Shopping Assistant (Powered by ChatGPT) | https://blinkn.shop/ | blinkn.shop | 2023-07-05T18:13:17Z | 0.55 | 0.45 | 0.1 | 0.75 | 0.5 | 0.4825 |
| Kagi Assistants | https://blog.kagi.com/kagi-assistants | blog.kagi.com | 2025-11-20T23:29:11Z | 0.25 | 0.55 | 0.9644 | 0.35 | 0.6 | 0.4822 |
| FreeTier.fyi – AI-powered database of free tiers of AI and infra services | https://freetier.fyi | freetier.fyi | 2025-07-10T02:20:48Z | 0.4 | 0.45 | 0.7808 | 0.35 | 0.6 | 0.4821 |
| Generate AI art in the browser for $0 (no login, prompt templates included) | https://michelangelo.best/ | michelangelo.best | 2025-07-08T15:07:40Z | 0.4 | 0.45 | 0.7795 | 0.35 | 0.6 | 0.4819 |
| LLMs are bullshitters. But that doesn't mean they're not useful |  | blog.kagi.com | 2025-11-19T18:05:53Z | 0.25 | 0.55 | 0.963 | 0.35 | 0.6 | 0.4819 |
| LLMs are bullshitters. But that doesn't mean they're not useful | https://blog.kagi.com/llms | blog.kagi.com | 2025-11-19T18:05:53Z | 0.25 | 0.55 | 0.963 | 0.35 | 0.6 | 0.4819 |
| Cloudflare Global Network experiencing issues |  | www.cloudflarestatus.com | 2025-11-18T19:35:03Z | 0.25 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.4817 |
| Cloudflare Global Network experiencing issues | https://www.cloudflarestatus.com/incidents/8gmgl950y3h7 | www.cloudflarestatus.com | 2025-11-18T19:35:03Z | 0.25 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.4817 |
| Gemini 3 Pro Model Card [pdf] | https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf | storage.googleapis.com | 2025-11-18T15:10:34Z | 0.25 | 0.55 | 0.9616 | 0.35 | 0.6 | 0.4817 |
| Everything around LLMs is still magical and wishful thinking | https://dmitriid.com/everything-around-llms-is-still-magical-and-wishful-thinking | dmitriid.com | 2025-07-04T23:40:13Z | 0.4 | 0.45 | 0.774 | 0.35 | 0.6 | 0.4811 |
| Is there a no-AI audience? |  | thatshubham.com | 2025-07-04T13:57:30Z | 0.4 | 0.45 | 0.774 | 0.35 | 0.6 | 0.4811 |
| Is there a no-AI audience? | https://thatshubham.com/blog/ai | thatshubham.com | 2025-07-04T13:57:30Z | 0.4 | 0.45 | 0.774 | 0.35 | 0.6 | 0.4811 |
| Prompting LLMs is not engineering | https://dmitriid.com/prompting-llms-is-not-engineering | dmitriid.com | 2025-07-05T01:34:09Z | 0.4 | 0.45 | 0.774 | 0.35 | 0.6 | 0.4811 |
| AGI fantasy is a blocker to actual engineering | https://www.tomwphillips.co.uk/2025/11/agi-fantasy-is-a-blocker-to-actual-engineering/ | www.tomwphillips.co.uk | 2025-11-14T15:56:33Z | 0.25 | 0.55 | 0.9562 | 0.35 | 0.6 | 0.4809 |
| The uncertain future of coding careers and why I'm still hopeful |  | jonmagic.com | 2025-07-03T18:07:34Z | 0.4 | 0.45 | 0.7726 | 0.35 | 0.6 | 0.4809 |
| The uncertain future of coding careers and why I'm still hopeful | https://jonmagic.com/posts/the-uncertain-future-of-coding-careers-and-why-im-still-hopeful/ | jonmagic.com | 2025-07-03T18:07:34Z | 0.4 | 0.45 | 0.7726 | 0.35 | 0.6 | 0.4809 |
| Launch HN: Tweeks (YC W25) – Browser extension to deshittify the web |  | www.tweeks.io | 2025-11-13T19:10:10Z | 0.25 | 0.55 | 0.9548 | 0.35 | 0.6 | 0.4807 |
| Launch HN: Tweeks (YC W25) – Browser extension to deshittify the web | https://www.tweeks.io/onboarding | www.tweeks.io | 2025-11-13T19:10:10Z | 0.25 | 0.55 | 0.9548 | 0.35 | 0.6 | 0.4807 |
| Learn Prolog Now (2006) | https://lpn.swi-prolog.org/lpnpage.php?pageid=top | lpn.swi-prolog.org | 2025-11-13T05:46:45Z | 0.25 | 0.55 | 0.9548 | 0.35 | 0.6 | 0.4807 |
| Google DeepMind shifts from research lab to AI product factory |  | www.bloomberg.com | 2024-06-18T02:45:46Z | 0.55 | 0.55 | 0.2521 | 0.35 | 0.6 | 0.4803 |
| Sharing new research, models, and datasets from Meta FAIR | https://ai.meta.com/blog/meta-fair-research-new-releases/ | ai.meta.com | 2024-06-18T17:53:16Z | 0.4 | 0.76 | 0.2521 | 0.35 | 0.6 | 0.4803 |
| SoftBank sells its entire stake in Nvidia for $5.83B |  | www.cnbc.com | 2025-11-11T10:47:39Z | 0.25 | 0.55 | 0.9521 | 0.35 | 0.6 | 0.4803 |
| SoftBank sells its entire stake in Nvidia for $5.83B | https://www.cnbc.com/2025/11/11/softbank-sells-its-entire-stake-in-nvidia-for-5point83-billion.html | www.cnbc.com | 2025-11-11T10:47:39Z | 0.25 | 0.55 | 0.9521 | 0.35 | 0.6 | 0.4803 |
| Google DeepMind shifts from research lab to AI product factory | https://www.bloomberg.com/news/articles/2024-06-17/google-deepmind-shifts-from-research-lab-to-ai-product-factory | www.bloomberg.com | 2024-06-18T02:45:46Z | 0.55 | 0.55 | 0.2507 | 0.35 | 0.6 | 0.4801 |
| AI's Biggest Flaw? The Blinking Cursor Problem | https://blog.scottlogic.com/2025/02/21/ais-biggest-flaw-the-blinking-cursor-problem.html | blog.scottlogic.com | 2025-02-26T23:21:19Z | 0.4 | 0.55 | 0.5986 | 0.35 | 0.6 | 0.4798 |
| It’s still worth blogging in the age of AI |  | www.gilesthomas.com | 2025-02-26T04:26:55Z | 0.4 | 0.55 | 0.5986 | 0.35 | 0.6 | 0.4798 |
| It’s still worth blogging in the age of AI | https://www.gilesthomas.com/2025/02/blogging-in-the-age-of-ai | www.gilesthomas.com | 2025-02-26T04:26:55Z | 0.4 | 0.55 | 0.5986 | 0.35 | 0.6 | 0.4798 |
| Show HN: AI powered competitive intelligence tool |  | www.kupiks.com | 2025-02-26T18:23:18Z | 0.4 | 0.55 | 0.5986 | 0.35 | 0.6 | 0.4798 |
| Show HN: AI powered competitive intelligence tool | https://www.kupiks.com | www.kupiks.com | 2025-02-26T18:23:18Z | 0.4 | 0.55 | 0.5986 | 0.35 | 0.6 | 0.4798 |
| GPT-OSS 120B Runs at 3000 tokens/sec on Cerebras |  | www.cerebras.ai | 2025-11-08T11:38:27Z | 0.25 | 0.55 | 0.9479 | 0.35 | 0.6 | 0.4797 |
| GPT-OSS 120B Runs at 3000 tokens/sec on Cerebras | https://www.cerebras.ai/blog/openai-gpt-oss-120b-runs-fastest-on-cerebras | www.cerebras.ai | 2025-11-08T11:38:27Z | 0.25 | 0.55 | 0.9479 | 0.35 | 0.6 | 0.4797 |
| ChatGPT terms disallow its use in providing legal and medical advice to others | https://www.ctvnews.ca/sci-tech/article/openai-updates-policies-so-chatgpt-wont-provide-medical-or-legal-advice/ | www.ctvnews.ca | 2025-11-05T23:50:24Z | 0.25 | 0.55 | 0.9438 | 0.35 | 0.6 | 0.4791 |
| LLMunix: A Markdown OS Experiment Inspired by Karpathy's "LLMs as Computers" | https://github.com/EvolvingAgentsLabs/llmunix | github.com | 2025-06-19T12:17:54Z | 0.4 | 0.45 | 0.7534 | 0.35 | 0.6 | 0.478 |
| Affinity Studio now free |  | www.affinity.studio | 2025-10-30T19:01:20Z | 0.25 | 0.55 | 0.9356 | 0.35 | 0.6 | 0.4778 |
| Affinity Studio now free | https://www.affinity.studio/get-affinity | www.affinity.studio | 2025-10-30T19:01:20Z | 0.25 | 0.55 | 0.9356 | 0.35 | 0.6 | 0.4778 |
| Perplexity Deep Research | https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research | www.perplexity.ai | 2025-02-16T01:58:37Z | 0.4 | 0.55 | 0.5836 | 0.35 | 0.6 | 0.4775 |
| We're in the wrong moment | https://ezrichards.github.io/posts/were-in-the-wrong-moment/ | ezrichards.github.io | 2025-10-27T07:14:17Z | 0.25 | 0.55 | 0.9315 | 0.35 | 0.6 | 0.4772 |
| Who's Hiring Senior Data Scientist |  | www.bld.ai | 2025-10-27T09:57:50Z | 0.25 | 0.55 | 0.9315 | 0.35 | 0.6 | 0.4772 |
| Who's Hiring Senior Data Scientist | https://www.bld.ai/ | www.bld.ai | 2025-10-27T09:57:50Z | 0.25 | 0.55 | 0.9315 | 0.35 | 0.6 | 0.4772 |
| Thomson Reuters wins first major AI copyright case in the US | https://www.wired.com/story/thomson-reuters-ai-copyright-lawsuit/ | www.wired.com | 2025-02-13T17:23:18Z | 0.4 | 0.55 | 0.5808 | 0.35 | 0.6 | 0.4771 |
| Best Way to Protect and Grow OSS (Open-Source Software) | https://docs.google.com/forms/d/10TxDVcZhxbqPJPJ-VRzRNamePEOX_zMy03Ac4RL6RtI/viewform?edit_requested=true | docs.google.com | 2025-01-20T02:11:58Z | 0.25 | 0.78 | 0.5466 | 0.35 | 0.6 | 0.477 |
| Clinical knowledge in LLMs does not translate to human interactions | https://arxiv.org/pdf/2504.18919 | arxiv.org | 2025-06-14T23:10:47Z | 0.4 | 0.45 | 0.7466 | 0.35 | 0.6 | 0.477 |
| Why I code as a CTO |  | www.assembled.com | 2025-10-25T21:50:37Z | 0.25 | 0.55 | 0.9288 | 0.35 | 0.6 | 0.4768 |
| Why I code as a CTO | https://www.assembled.com/blog/why-i-code-as-a-cto | www.assembled.com | 2025-10-25T21:50:37Z | 0.25 | 0.55 | 0.9288 | 0.35 | 0.6 | 0.4768 |
| Why hourly billing no longer works in the era of AI | https://madewithlove.com/blog/pricing-strategies-in-the-era-of-ai-why-hourly-billing-no-longer-works/ | madewithlove.com | 2025-06-11T12:40:09Z | 0.4 | 0.45 | 0.7425 | 0.35 | 0.6 | 0.4764 |
| AI Saved My Company from a 2-Year Litigation Nightmare | https://tylertringas.com/ai-legal/ | tylertringas.com | 2025-06-10T15:18:32Z | 0.4 | 0.45 | 0.7411 | 0.35 | 0.6 | 0.4762 |
| Why LLMs still have problems with OCR | https://www.runpulse.com/blog/why-llms-suck-at-ocr | www.runpulse.com | 2025-02-07T23:13:38Z | 0.4 | 0.55 | 0.5726 | 0.35 | 0.6 | 0.4759 |
| Oracular Programming: A Modular Foundation for Building LLM-Enabled Software | https://arxiv.org/abs/2502.05310 | arxiv.org | 2025-06-07T18:36:05Z | 0.4 | 0.45 | 0.737 | 0.35 | 0.6 | 0.4755 |
| AGI is not imminent, and LLMs are not the royal road to getting there | https://garymarcus.substack.com/p/the-last-few-months-have-been-devastating | garymarcus.substack.com | 2025-10-18T13:44:47Z | 0.25 | 0.55 | 0.9192 | 0.35 | 0.6 | 0.4754 |
| Banana Powered Guitar Pedal |  | www.youtube.com | 2025-10-18T17:41:08Z | 0.25 | 0.55 | 0.9192 | 0.35 | 0.6 | 0.4754 |
| Banana Powered Guitar Pedal | https://www.youtube.com/watch?v=z75BO2b3m5Y | www.youtube.com | 2025-10-18T17:41:08Z | 0.25 | 0.55 | 0.9192 | 0.35 | 0.6 | 0.4754 |
| Founding PM / Co-Founder for FilFlo (AI-Native Fulfilment SaaS) |  | filflo.in | 2025-06-06T05:23:49Z | 0.4 | 0.45 | 0.7356 | 0.35 | 0.6 | 0.4753 |
| Founding PM / Co-Founder for FilFlo (AI-Native Fulfilment SaaS) | https://filflo.in/ | filflo.in | 2025-06-06T05:23:49Z | 0.4 | 0.45 | 0.7356 | 0.35 | 0.6 | 0.4753 |
| AI overviews cause massive drop in search clicks |  | arstechnica.com | 2025-07-24T14:10:33Z | 0.4 | 0.45 | 0.8014 | 0.35 | 0.5 | 0.4752 |
| AI overviews cause massive drop in search clicks | https://arstechnica.com/ai/2025/07/research-shows-google-ai-overviews-reduce-website-clicks-by-almost-half/ | arstechnica.com | 2025-07-24T14:10:33Z | 0.4 | 0.45 | 0.8014 | 0.35 | 0.5 | 0.4752 |
| Constitutional Classifiers: Defending against universal jailbreaks | https://www.anthropic.com/research/constitutional-classifiers | www.anthropic.com | 2025-02-03T23:20:57Z | 0.25 | 0.76 | 0.5671 | 0.35 | 0.6 | 0.4751 |
| AI-first – We're just 6 months away from AGI |  | revontulet.dev | 2025-06-02T14:25:03Z | 0.4 | 0.45 | 0.7301 | 0.35 | 0.6 | 0.4745 |
| AI-first – We're just 6 months away from AGI | https://revontulet.dev/p/2025-ai-first/ | revontulet.dev | 2025-06-02T14:25:03Z | 0.4 | 0.45 | 0.7301 | 0.35 | 0.6 | 0.4745 |
| LLMs replacing human participants harmfully misportray, flatten identity groups | https://arxiv.org/abs/2402.01908 | arxiv.org | 2025-06-01T21:39:21Z | 0.4 | 0.45 | 0.7288 | 0.35 | 0.6 | 0.4743 |
| After the AI boom: what might we be left with? | https://blog.robbowley.net/2025/10/12/after-the-ai-boom-what-might-we-be-left-with/ | blog.robbowley.net | 2025-10-12T20:19:16Z | 0.25 | 0.55 | 0.911 | 0.35 | 0.6 | 0.4742 |
| Human coders are still better than LLMs | https://antirez.com/news/153 | antirez.com | 2025-05-30T09:40:46Z | 0.4 | 0.45 | 0.726 | 0.35 | 0.6 | 0.4739 |
| OpenAI: Sora: First Impressions |  | openai.com | 2024-03-29T18:40:47Z | 0.4 | 0.8 | 0.1411 | 0.35 | 0.6 | 0.4737 |
| OpenAI: Sora: First Impressions | https://openai.com/blog/sora-first-impressions | openai.com | 2024-03-29T18:40:47Z | 0.4 | 0.8 | 0.1411 | 0.35 | 0.6 | 0.4737 |
| Show HN: Built CinePrompt – Search movies by describing your mood, not keywords | https://cineprompt.vercel.app/ | cineprompt.vercel.app | 2025-10-09T15:37:52Z | 0.25 | 0.55 | 0.9068 | 0.35 | 0.6 | 0.4735 |
| China Prepares One Trillion Yuan ($138B) AI Plan to Rival $500B US AI Project |  | www.techpowerup.com | 2025-01-26T22:58:16Z | 0.4 | 0.55 | 0.5562 | 0.35 | 0.6 | 0.4734 |
| China Prepares One Trillion Yuan ($138B) AI Plan to Rival $500B US AI Project | https://www.techpowerup.com/331636/the-empire-strikes-back-china-prepares-one-trillion-yuan-ai-plan-to-rival-usd-500-billion-us-stargate-project | www.techpowerup.com | 2025-01-26T22:58:16Z | 0.4 | 0.55 | 0.5562 | 0.35 | 0.6 | 0.4734 |
| Show HN: CopyCat (YC W25) – Free Alternative to OpenAI's $200 Operator |  | www.runcopycat.com | 2025-01-25T14:41:49Z | 0.4 | 0.55 | 0.5548 | 0.35 | 0.6 | 0.4732 |
| Show HN: CopyCat (YC W25) – Free Alternative to OpenAI's $200 Operator | https://www.runcopycat.com/download | www.runcopycat.com | 2025-01-25T14:41:49Z | 0.4 | 0.55 | 0.5548 | 0.35 | 0.6 | 0.4732 |
| Show HN: Klipy – Generate Memes via AI (Meme, Sticker, and GIF API) |  | klipy.com | 2025-05-26T23:31:45Z | 0.4 | 0.45 | 0.7205 | 0.35 | 0.6 | 0.4731 |
| Show HN: Klipy – Generate Memes via AI (Meme, Sticker, and GIF API) | https://klipy.com/create | klipy.com | 2025-05-26T23:31:45Z | 0.4 | 0.45 | 0.7205 | 0.35 | 0.6 | 0.4731 |
| Show HN: I made a WYSIWYG AI editor for scriptwriting | https://www.scriptwritr.com | www.scriptwritr.com | 2025-01-23T08:01:57Z | 0.4 | 0.55 | 0.5521 | 0.35 | 0.6 | 0.4728 |
| ChatGPT Pro | https://openai.com/index/introducing-chatgpt-pro/ | openai.com | 2024-12-05T21:43:58Z | 0.25 | 0.8 | 0.4849 | 0.35 | 0.6 | 0.4727 |
| B2B SaaS Growth Strategies from Business Classics Applied to AI Startups |  | guptadeepak.com | 2025-05-23T19:04:42Z | 0.4 | 0.45 | 0.7164 | 0.35 | 0.6 | 0.4725 |
| B2B SaaS Growth Strategies from Business Classics Applied to AI Startups | https://guptadeepak.com/10-proven-growth-strategies-for-b2b-saas-lessons-from-business-classics-applications-for-ai-startups/ | guptadeepak.com | 2025-05-23T19:04:42Z | 0.4 | 0.45 | 0.7164 | 0.35 | 0.6 | 0.4725 |
| Kagi News | https://blog.kagi.com/kagi-news | blog.kagi.com | 2025-10-01T12:43:24Z | 0.25 | 0.55 | 0.8959 | 0.35 | 0.6 | 0.4719 |
| Google AI Ultra | https://blog.google/products/google-one/google-ai-ultra/ | blog.google | 2025-05-20T19:25:25Z | 0.4 | 0.45 | 0.7123 | 0.35 | 0.6 | 0.4718 |
| John Jumper: AI is revolutionizing scientific discovery [video] | https://www.youtube.com/watch?v=2Yguz5U-Nic | www.youtube.com | 2025-09-30T05:02:45Z | 0.25 | 0.55 | 0.8945 | 0.35 | 0.6 | 0.4717 |
| Failing to Understand the Exponential, Again | https://www.julian.ac/blog/2025/09/27/failing-to-understand-the-exponential-again/ | www.julian.ac | 2025-09-29T08:50:15Z | 0.25 | 0.55 | 0.8932 | 0.35 | 0.6 | 0.4715 |
| Google is making AI in Gmail and Docs free, but raising the price of Workspace |  | www.theverge.com | 2025-01-16T06:49:37Z | 0.4 | 0.55 | 0.5425 | 0.35 | 0.6 | 0.4714 |
| Google is making AI in Gmail and Docs free, but raising the price of Workspace | https://www.theverge.com/2025/1/15/24343794/google-workspace-ai-features-free | www.theverge.com | 2025-01-16T06:49:37Z | 0.4 | 0.55 | 0.5425 | 0.35 | 0.6 | 0.4714 |
| LLMs are more persuasive than incentivized human persuaders | https://arxiv.org/abs/2505.09662 | arxiv.org | 2025-05-17T22:01:57Z | 0.4 | 0.45 | 0.7082 | 0.35 | 0.6 | 0.4712 |
| AI model trapped in a Raspberry Pi | https://blog.adafruit.com/2025/09/26/ai-model-trapped-in-raspberry-pi-piday-raspberrypi/ | blog.adafruit.com | 2025-09-27T17:43:03Z | 0.25 | 0.55 | 0.8904 | 0.35 | 0.6 | 0.4711 |
| CEO of AI Music Company Says People Don't Like Making Music | https://www.404media.co/ceo-of-ai-music-company-says-people-dont-like-making-music/ | www.404media.co | 2025-01-13T21:21:35Z | 0.4 | 0.55 | 0.5384 | 0.35 | 0.6 | 0.4708 |
| How to stop AI's "lethal trifecta" | https://www.economist.com/leaders/2025/09/25/how-to-stop-ais-lethal-trifecta | www.economist.com | 2025-09-26T18:36:18Z | 0.25 | 0.55 | 0.889 | 0.35 | 0.6 | 0.4708 |
| Do YC after you graduate: Early decision for students | https://www.ycombinator.com/early-decision | www.ycombinator.com | 2025-09-25T00:58:34Z | 0.25 | 0.55 | 0.8863 | 0.35 | 0.6 | 0.4704 |
| x402 — An open protocol for internet-native payments |  | www.x402.org | 2025-09-23T19:31:29Z | 0.25 | 0.55 | 0.8849 | 0.35 | 0.6 | 0.4702 |
| x402 — An open protocol for internet-native payments | https://www.x402.org/ | www.x402.org | 2025-09-23T19:31:29Z | 0.25 | 0.55 | 0.8849 | 0.35 | 0.6 | 0.4702 |
| Selling my AI-powered CMS (Adsense and Supabase) – Is $20K unreasonable? | https://juumbi.com | juumbi.com | 2025-05-08T04:52:16Z | 0.4 | 0.45 | 0.6959 | 0.35 | 0.6 | 0.4694 |
| Show HN: LLMs.txt Generator – Boost SEO by adding an AI-friendly summary | https://llmstxtgenerator.co/ | llmstxtgenerator.co | 2025-05-08T12:08:15Z | 0.4 | 0.45 | 0.6959 | 0.35 | 0.6 | 0.4694 |
| OpenAI and Elon Musk | https://openai.com/blog/openai-elon-musk | openai.com | 2024-03-06T02:58:39Z | 0.4 | 0.8 | 0.1082 | 0.35 | 0.6 | 0.4687 |
| AIagency – AI-powered marketing platform for SMEs |  | aiagency.app | 2025-05-03T11:51:17Z | 0.4 | 0.45 | 0.689 | 0.35 | 0.6 | 0.4683 |
| AIagency – AI-powered marketing platform for SMEs | https://aiagency.app | aiagency.app | 2025-05-03T11:51:17Z | 0.4 | 0.45 | 0.689 | 0.35 | 0.6 | 0.4683 |
| AI Coding | https://geohot.github.io//blog/jekyll/update/2025/09/12/ai-coding.html | geohot.github.io | 2025-09-13T11:50:06Z | 0.25 | 0.55 | 0.8712 | 0.35 | 0.6 | 0.4682 |
| Show HN: Watch 3 AIs compete in real-time stock trading | https://trading.snagra.com | trading.snagra.com | 2024-12-31T17:09:54Z | 0.4 | 0.55 | 0.5205 | 0.35 | 0.6 | 0.4681 |
| AI companies cause most of traffic on forums |  | pod.geraspora.de | 2024-12-30T18:27:33Z | 0.4 | 0.55 | 0.5192 | 0.35 | 0.6 | 0.4679 |
| AI companies cause most of traffic on forums | https://pod.geraspora.de/posts/17342163 | pod.geraspora.de | 2024-12-30T18:27:33Z | 0.4 | 0.55 | 0.5192 | 0.35 | 0.6 | 0.4679 |
| Show HN: Malai – Share your dev server (and more) over P2P | https://malai.sh/announcing-malai/ | malai.sh | 2025-04-30T18:01:52Z | 0.4 | 0.45 | 0.6849 | 0.35 | 0.6 | 0.4677 |
| OpenAI Forum |  | forum.openai.com | 2024-02-16T16:51:59Z | 0.4 | 0.8 | 0.1 | 0.35 | 0.6 | 0.4675 |
| OpenAI Forum | https://forum.openai.com/ | forum.openai.com | 2024-02-16T16:51:59Z | 0.4 | 0.8 | 0.1 | 0.35 | 0.6 | 0.4675 |
| Does current AI represent a dead end? | https://www.bcs.org/articles-opinion-and-research/does-current-ai-represent-a-dead-end/ | www.bcs.org | 2024-12-27T16:50:41Z | 0.4 | 0.55 | 0.5151 | 0.35 | 0.6 | 0.4673 |
| Alterego: Thought to Text | https://www.alterego.io/ | www.alterego.io | 2025-09-09T00:54:53Z | 0.25 | 0.55 | 0.8644 | 0.35 | 0.6 | 0.4672 |
| RubyMine is now free for non-commercial use | https://blog.jetbrains.com/ruby/2025/09/rubymine-is-now-free-for-non-commercial-use/ | blog.jetbrains.com | 2025-09-08T12:06:04Z | 0.25 | 0.55 | 0.8644 | 0.35 | 0.6 | 0.4672 |
| GLM 4.5 with Claude Code | https://docs.z.ai/guides/llm/glm-4.5 | docs.z.ai | 2025-09-06T09:25:04Z | 0.25 | 0.55 | 0.8616 | 0.35 | 0.6 | 0.4667 |
| From Trial Abuse to 150% MRR Growth–and Now, Skimming AI Is Free for All |  | www.skimming.ai | 2024-12-24T15:27:45Z | 0.4 | 0.55 | 0.511 | 0.35 | 0.6 | 0.4666 |
| From Trial Abuse to 150% MRR Growth–and Now, Skimming AI Is Free for All | https://www.skimming.ai/ | www.skimming.ai | 2024-12-24T15:27:45Z | 0.4 | 0.55 | 0.511 | 0.35 | 0.6 | 0.4666 |
| AI Horseless Carriages |  | koomen.dev | 2025-04-24T04:12:19Z | 0.4 | 0.45 | 0.6767 | 0.35 | 0.6 | 0.4665 |
| AI Horseless Carriages | https://koomen.dev/essays/horseless-carriages/ | koomen.dev | 2025-04-24T04:12:19Z | 0.4 | 0.45 | 0.6767 | 0.35 | 0.6 | 0.4665 |
| Atlassian is acquiring The Browser Company |  | www.cnbc.com | 2025-09-04T18:46:13Z | 0.25 | 0.55 | 0.8589 | 0.35 | 0.6 | 0.4663 |
| Atlassian is acquiring The Browser Company | https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html | www.cnbc.com | 2025-09-04T18:46:13Z | 0.25 | 0.55 | 0.8589 | 0.35 | 0.6 | 0.4663 |
| The Browser Company (Arc, Dia) Has Been Acquired by Atlassian | https://www.atlassian.com/blog/announcements/atlassian-acquires-the-browser-company | www.atlassian.com | 2025-09-04T14:52:02Z | 0.25 | 0.55 | 0.8589 | 0.35 | 0.6 | 0.4663 |
| Alignment faking in large language models | https://www.anthropic.com/research/alignment-faking | www.anthropic.com | 2024-12-20T17:06:35Z | 0.25 | 0.76 | 0.5055 | 0.35 | 0.6 | 0.4658 |
| ChatGPT Search | https://openai.com/index/introducing-chatgpt-search/ | openai.com | 2024-11-01T15:50:22Z | 0.25 | 0.8 | 0.4384 | 0.35 | 0.6 | 0.4658 |
| Show HN: I Built an AI Tool to Simplify Lead Generation | https://www.cora-intelligence.com/ | www.cora-intelligence.com | 2024-12-20T14:12:25Z | 0.4 | 0.55 | 0.5055 | 0.35 | 0.6 | 0.4658 |
| Search engine referral report for 2025 Q2 | https://radar.cloudflare.com/reports/search-engine-market-share-2025-q2 | radar.cloudflare.com | 2025-09-01T18:51:44Z | 0.25 | 0.55 | 0.8548 | 0.35 | 0.6 | 0.4657 |
| Fake accounts drove the DeepSeek AI hype and distorted markets | https://www.evai.ai/en/post/disinformation-the-deepseek-hype-was-all-made-up-how-fake-accounts-managed-a-market-frenzy | www.evai.ai | 2025-08-29T14:39:45Z | 0.25 | 0.55 | 0.8507 | 0.35 | 0.6 | 0.4651 |
| If you have a Claude account, they're going to train on your data moving forward | https://old.reddit.com/r/LocalLLaMA/comments/1n2ubjx/if_you_have_a_claude_personal_account_they_are/ | old.reddit.com | 2025-08-30T00:02:50Z | 0.25 | 0.55 | 0.8507 | 0.35 | 0.6 | 0.4651 |
| In Search of AI Psychosis | https://www.astralcodexten.com/p/in-search-of-ai-psychosis | www.astralcodexten.com | 2025-08-28T23:00:03Z | 0.25 | 0.55 | 0.8493 | 0.35 | 0.6 | 0.4649 |
| Benn Jordan's AI poison pill and the weird world of adversarial noise | https://cdm.link/benn-jordan-ai-poison-pill/ | cdm.link | 2025-04-15T21:22:13Z | 0.4 | 0.45 | 0.6644 | 0.35 | 0.6 | 0.4647 |
| Kiwi.com flight search MCP server | https://mcp-install-instructions.alpic.cloud/servers/kiwi-com-flight-search | mcp-install-instructions.alpic.cloud | 2025-08-27T19:40:30Z | 0.25 | 0.55 | 0.8479 | 0.35 | 0.6 | 0.4647 |
| Our New AI Website Builder |  | wordpress.com | 2025-04-11T18:00:27Z | 0.4 | 0.45 | 0.6589 | 0.35 | 0.6 | 0.4638 |
| Our New AI Website Builder | https://wordpress.com/blog/2025/04/09/ai-website-builder/ | wordpress.com | 2025-04-11T18:00:27Z | 0.4 | 0.45 | 0.6589 | 0.35 | 0.6 | 0.4638 |
| Grok 3 API: Available now | https://x.ai/api#pricing | x.ai | 2025-04-10T20:57:44Z | 0.4 | 0.45 | 0.6575 | 0.35 | 0.6 | 0.4636 |
| DeepSeek-v3.1 | https://api-docs.deepseek.com/news/news250821 | api-docs.deepseek.com | 2025-08-21T20:12:10Z | 0.25 | 0.55 | 0.8397 | 0.35 | 0.6 | 0.4635 |
| AI coding mandates are driving developers to the brink |  | leaddev.com | 2025-04-09T16:29:33Z | 0.4 | 0.45 | 0.6562 | 0.35 | 0.6 | 0.4634 |
| AI coding mandates are driving developers to the brink | https://leaddev.com/culture/ai-coding-mandates-are-driving-developers-to-the-brink | leaddev.com | 2025-04-09T16:29:33Z | 0.4 | 0.45 | 0.6562 | 0.35 | 0.6 | 0.4634 |
| I made linkcreator.ai – an AI tool that generates backlinks for websites | https://linkcreator.ai/ | linkcreator.ai | 2025-04-09T08:15:52Z | 0.4 | 0.45 | 0.6562 | 0.35 | 0.6 | 0.4634 |
| Three Proven Strategies to Monetize AI Features in SaaS | https://www.productcompass.pm/p/ai-monetization-pricing-strategies | www.productcompass.pm | 2024-12-08T15:12:08Z | 0.4 | 0.55 | 0.489 | 0.35 | 0.6 | 0.4633 |
| Sam Altman says 'yes,' AI is in a bubble | https://www.theverge.com/ai-artificial-intelligence/759965/sam-altman-openai-ai-bubble-interview | www.theverge.com | 2025-08-18T07:25:00Z | 0.25 | 0.55 | 0.8356 | 0.35 | 0.6 | 0.4628 |
| Cloud TPU Pods Break AI Training Records | https://cloud.google.com/blog/products/ai-machine-learning/cloud-tpu-pods-break-ai-training-records | cloud.google.com | 2019-07-13T16:31:33Z | 0.4 | 0.78 | 0.1 | 0.35 | 0.6 | 0.4625 |
| Do things that don't scale, and then don't scale |  | derwiki.medium.com | 2025-08-16T19:42:48Z | 0.25 | 0.55 | 0.8329 | 0.35 | 0.6 | 0.4624 |
| Do things that don't scale, and then don't scale | https://derwiki.medium.com/do-things-that-dont-scale-and-then-don-t-scale-9fd2cd7e2156 | derwiki.medium.com | 2025-08-16T19:42:48Z | 0.25 | 0.55 | 0.8329 | 0.35 | 0.6 | 0.4624 |
| AI poetry is indistinguishable from human poetry and is rated more favorably | https://www.nature.com/articles/s41598-024-76900-1 | www.nature.com | 2024-12-03T20:25:40Z | 0.4 | 0.55 | 0.4822 | 0.35 | 0.6 | 0.4623 |
| Sam Altman is in damage-control mode after latest ChatGPT release |  | www.cnn.com | 2025-08-15T03:59:00Z | 0.25 | 0.55 | 0.8315 | 0.35 | 0.6 | 0.4622 |
| Sam Altman is in damage-control mode after latest ChatGPT release | https://www.cnn.com/2025/08/14/business/chatgpt-rollout-problems | www.cnn.com | 2025-08-15T03:59:00Z | 0.25 | 0.55 | 0.8315 | 0.35 | 0.6 | 0.4622 |
| Dagger: Define software delivery workflows and dev environments |  | dagger.io | 2025-12-14T15:29:39Z | 0.25 | 0.45 | 0.9973 | 0.35 | 0.6 | 0.4621 |
| Dagger: Define software delivery workflows and dev environments | https://dagger.io/ | dagger.io | 2025-12-14T15:29:39Z | 0.25 | 0.45 | 0.9973 | 0.35 | 0.6 | 0.4621 |
| Edcapit Presented Its Project at Keiretsu Forum Texas (USA) |  | www.edcapit.com | 2025-08-13T20:35:57Z | 0.25 | 0.55 | 0.8288 | 0.35 | 0.6 | 0.4618 |
| Edcapit Presented Its Project at Keiretsu Forum Texas (USA) | https://www.edcapit.com/2025/08/12/📢-edcapit-presented-its-project-at-keiretsu-forum-texas-usa/ | www.edcapit.com | 2025-08-13T20:35:57Z | 0.25 | 0.55 | 0.8288 | 0.35 | 0.6 | 0.4618 |
| Maskara.ai – group chat with multiple AIs | https://www.maskara.ai/ | www.maskara.ai | 2025-08-13T09:33:55Z | 0.25 | 0.55 | 0.8288 | 0.35 | 0.6 | 0.4618 |
| Show HN: I built FluenAI to overcome my communication hurdles | https://www.fluenai.com | www.fluenai.com | 2024-11-30T10:48:45Z | 0.4 | 0.55 | 0.4781 | 0.35 | 0.6 | 0.4617 |
| Japan's largest paper, Yomiuri Shimbun, sues Perplexity for copyright violations |  | www.niemanlab.org | 2025-08-12T02:44:01Z | 0.25 | 0.55 | 0.8274 | 0.35 | 0.6 | 0.4616 |
| Show HN: Building a web search engine from scratch with 3B neural embeddings |  | blog.wilsonl.in | 2025-08-12T18:05:52Z | 0.25 | 0.55 | 0.8274 | 0.35 | 0.6 | 0.4616 |
| Show HN: Building a web search engine from scratch with 3B neural embeddings | https://blog.wilsonl.in/search-engine/ | blog.wilsonl.in | 2025-08-12T18:05:52Z | 0.25 | 0.55 | 0.8274 | 0.35 | 0.6 | 0.4616 |
| A ChatGPT Pro subscription costs 38.6 months of income in low-income countries | https://policykahani.substack.com/p/a-chatgpt-pro-subscription-costs | policykahani.substack.com | 2025-08-11T10:04:39Z | 0.25 | 0.55 | 0.826 | 0.35 | 0.6 | 0.4614 |
| GitHub is no longer independent at Microsoft after CEO resignation |  | www.theverge.com | 2025-08-11T17:46:59Z | 0.25 | 0.55 | 0.826 | 0.35 | 0.6 | 0.4614 |
| GitHub is no longer independent at Microsoft after CEO resignation | https://www.theverge.com/news/757461/microsoft-github-thomas-dohmke-resignation-coreai-team-transition | www.theverge.com | 2025-08-11T17:46:59Z | 0.25 | 0.55 | 0.826 | 0.35 | 0.6 | 0.4614 |
| Japan's largest paper, Yomiuri Shimbun, sues Perplexity for copyright violations | https://www.niemanlab.org/2025/08/japans-largest-newspaper-yomiuri-shimbun-sues-perplexity-for-copyright-violations/ | www.niemanlab.org | 2025-08-12T02:44:01Z | 0.25 | 0.55 | 0.826 | 0.35 | 0.6 | 0.4614 |
| Adobe Brings Photoshop, Express and Acrobat Features to ChatGPT |  | techcrunch.com | 2025-12-10T14:37:11Z | 0.25 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.4613 |
| Adobe Brings Photoshop, Express and Acrobat Features to ChatGPT | https://techcrunch.com/2025/12/10/adobe-brings-photoshop-express-and-acrobat-features-to-chatgpt/ | techcrunch.com | 2025-12-10T14:37:11Z | 0.25 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.4613 |
| Concord – an offline-first cognitive engine that runs on your computer | https://github.com/ryttps94jq-gif/Concord-web-mvp | github.com | 2025-12-11T03:17:01Z | 0.25 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.4613 |
| Mistral releases Devstral2 and Mistral Vibe CLI |  | mistral.ai | 2025-12-10T12:11:46Z | 0.25 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.4613 |
| Mistral releases Devstral2 and Mistral Vibe CLI | https://mistral.ai/news/devstral-2-vibe-cli | mistral.ai | 2025-12-10T12:11:46Z | 0.25 | 0.45 | 0.9918 | 0.35 | 0.6 | 0.4613 |
| Microsoft increases Office 365 and Microsoft 365 license prices | https://office365itpros.com/2025/12/08/microsoft-365-pricing-increase/ | office365itpros.com | 2025-12-09T15:10:05Z | 0.25 | 0.45 | 0.9904 | 0.35 | 0.6 | 0.4611 |
| OpenAI hits pause on video model Sora after artists leak access in protest | https://www.washingtonpost.com/technology/2024/11/26/openai-sora-ai-video-model-artists-protest/ | www.washingtonpost.com | 2024-11-27T12:00:19Z | 0.4 | 0.55 | 0.474 | 0.35 | 0.6 | 0.4611 |
| GPT-5: Overdue, overhyped and underwhelming. And that's not the worst of it | https://garymarcus.substack.com/p/gpt-5-overdue-overhyped-and-underwhelming | garymarcus.substack.com | 2025-08-10T01:18:50Z | 0.25 | 0.55 | 0.8233 | 0.35 | 0.6 | 0.461 |
| I failed to recreate the 1996 Space Jam website with Claude | https://j0nah.com/i-failed-to-recreate-the-1996-space-jam-website-with-claude/ | j0nah.com | 2025-12-08T15:02:40Z | 0.25 | 0.45 | 0.989 | 0.35 | 0.6 | 0.4608 |
| I genuinely don't understand why some people are still bullish about LLMs | https://twitter.com/skdh/status/1905132853672784121 | twitter.com | 2025-03-28T03:48:27Z | 0.4 | 0.45 | 0.6384 | 0.35 | 0.6 | 0.4608 |
| Model Context Protocol | https://www.anthropic.com/news/model-context-protocol | www.anthropic.com | 2024-11-25T20:39:53Z | 0.25 | 0.76 | 0.4712 | 0.35 | 0.6 | 0.4607 |
| Syncthing-Android have had a change of owner/maintainer | https://github.com/researchxxl/syncthing-android/issues/16 | github.com | 2025-12-08T00:39:43Z | 0.25 | 0.45 | 0.9877 | 0.35 | 0.6 | 0.4607 |
| Z-Image: Powerful and highly efficient image generation model with 6B parameters | https://github.com/Tongyi-MAI/Z-Image | github.com | 2025-12-06T22:15:36Z | 0.25 | 0.45 | 0.9863 | 0.35 | 0.6 | 0.4604 |
| Lessons from 3 months vibe coding as a non-technical PM | https://www.productleadership.io/p/i-spent-3-months-vibe-coding-with | www.productleadership.io | 2025-08-05T20:45:57Z | 0.25 | 0.55 | 0.8178 | 0.35 | 0.6 | 0.4602 |
| 'A black hole': New graduates discover a dismal job market | https://www.nbcnews.com/business/economy/job-market-report-college-student-graduates-ai-trump-tariffs-rcna221693 | www.nbcnews.com | 2025-08-04T08:24:08Z | 0.25 | 0.55 | 0.8164 | 0.35 | 0.6 | 0.46 |
| Bloggingmachine.io Review: Can It Replace a Content Team? | https://www.bloggingmachine.io | www.bloggingmachine.io | 2025-08-04T10:02:42Z | 0.25 | 0.55 | 0.8164 | 0.35 | 0.6 | 0.46 |
| Perplexity is using stealth, undeclared crawlers to evade no-crawl directives | https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ | blog.cloudflare.com | 2025-08-04T17:12:18Z | 0.25 | 0.55 | 0.8164 | 0.35 | 0.6 | 0.46 |
| Anthropic acquires Bun |  | bun.com | 2025-12-03T08:00:58Z | 0.25 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.4598 |
| Anthropic acquires Bun | https://bun.com/blog/bun-joins-anthropic | bun.com | 2025-12-03T08:00:58Z | 0.25 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.4598 |
| Ghostty is now non-profit |  | mitchellh.com | 2025-12-03T22:32:03Z | 0.25 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.4598 |
| Ghostty is now non-profit | https://mitchellh.com/writing/ghostty-non-profit | mitchellh.com | 2025-12-03T22:32:03Z | 0.25 | 0.45 | 0.9822 | 0.35 | 0.6 | 0.4598 |
| Cerebras Code | https://www.cerebras.ai/blog/introducing-cerebras-code | www.cerebras.ai | 2025-08-02T11:48:13Z | 0.25 | 0.55 | 0.8137 | 0.35 | 0.6 | 0.4596 |
| DeepSeek-v3.2: Pushing the frontier of open large language models [pdf] |  | huggingface.co | 2025-12-02T16:43:21Z | 0.25 | 0.45 | 0.9808 | 0.35 | 0.6 | 0.4596 |
| DeepSeek-v3.2: Pushing the frontier of open large language models [pdf] | https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf | huggingface.co | 2025-12-02T16:43:21Z | 0.25 | 0.45 | 0.9808 | 0.35 | 0.6 | 0.4596 |
| Stripe Acquires Metronome, a Usage-Based Billing Platform | https://metronome.com/blog/important-company-update | metronome.com | 2025-12-02T21:01:51Z | 0.25 | 0.45 | 0.9808 | 0.35 | 0.6 | 0.4596 |
| Tim Cook rallying Apple employees around AI efforts | https://www.bloomberg.com/news/articles/2025-08-01/apple-ceo-tells-staff-ai-is-ours-to-grab-in-hourlong-pep-talk | www.bloomberg.com | 2025-08-02T23:37:11Z | 0.25 | 0.55 | 0.8137 | 0.35 | 0.6 | 0.4596 |
| A new AI winter is coming? | https://taranis.ie/llms-are-a-failure-a-new-ai-winter-is-coming/ | taranis.ie | 2025-12-01T20:22:23Z | 0.25 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.4594 |
| My Entire Profession Is Being Automated Away by AI | https://old.reddit.com/r/ChatGPT/comments/1guhsm4/well_this_is_it_boys_i_was_just_informed_from_my/ | old.reddit.com | 2024-11-19T20:35:20Z | 0.4 | 0.55 | 0.463 | 0.35 | 0.6 | 0.4594 |
| Search tool that only returns content created before ChatGPT's public release |  | tegabrain.com | 2025-12-01T13:39:56Z | 0.25 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.4594 |
| Search tool that only returns content created before ChatGPT's public release | https://tegabrain.com/Slop-Evader | tegabrain.com | 2025-12-01T13:39:56Z | 0.25 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.4594 |
| Show HN: The Haul – Spotify Wrapped for Your Amazon Orders |  | myhaul.app | 2025-12-01T18:34:16Z | 0.25 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.4594 |
| Show HN: The Haul – Spotify Wrapped for Your Amazon Orders | https://myhaul.app | myhaul.app | 2025-12-01T18:34:16Z | 0.25 | 0.45 | 0.9795 | 0.35 | 0.6 | 0.4594 |
| FOSS infrastructure is under attack by AI companies | https://thelibre.news/foss-infrastructure-is-under-attack-by-ai-companies/ | thelibre.news | 2025-03-20T14:16:17Z | 0.4 | 0.45 | 0.6288 | 0.35 | 0.6 | 0.4593 |
| Figma will IPO on July 31 | https://www.figma.com/blog/ipo-pricing/ | www.figma.com | 2025-07-31T04:25:07Z | 0.25 | 0.55 | 0.811 | 0.35 | 0.6 | 0.4592 |
| Show HN: I built an AI that turns any book into a text adventure game | https://www.kathaaverse.com/ | www.kathaaverse.com | 2025-07-30T07:24:36Z | 0.25 | 0.55 | 0.8096 | 0.35 | 0.6 | 0.4589 |
| Indie, alone, and figuring it out |  | danijelavrzan.com | 2025-11-28T08:55:18Z | 0.25 | 0.45 | 0.9753 | 0.35 | 0.6 | 0.4588 |
| Indie, alone, and figuring it out | https://danijelavrzan.com/posts/2025/11/indie-dev/ | danijelavrzan.com | 2025-11-28T08:55:18Z | 0.25 | 0.45 | 0.9753 | 0.35 | 0.6 | 0.4588 |
| Stop selling “unlimited”, when you mean “until we change our minds” | https://blog.kilocode.ai/p/ai-pricing-playbook-strikes-again | blog.kilocode.ai | 2025-07-29T13:20:36Z | 0.25 | 0.55 | 0.8082 | 0.35 | 0.6 | 0.4587 |
| Penpot: The Open-Source Figma |  | github.com | 2025-11-27T21:03:29Z | 0.25 | 0.45 | 0.974 | 0.35 | 0.6 | 0.4586 |
| Penpot: The Open-Source Figma | https://github.com/penpot/penpot | github.com | 2025-11-27T21:03:29Z | 0.25 | 0.45 | 0.974 | 0.35 | 0.6 | 0.4586 |
| AI Is Making Developers Dumb |  | eli.cx | 2025-03-16T19:40:29Z | 0.4 | 0.45 | 0.6233 | 0.35 | 0.6 | 0.4585 |
| AI Is Making Developers Dumb | https://eli.cx/blog/ai-is-making-developers-dumb | eli.cx | 2025-03-16T19:40:29Z | 0.4 | 0.45 | 0.6233 | 0.35 | 0.6 | 0.4585 |
| The future is not self-hosted, but self-sovereign |  | www.robertmao.com | 2025-07-28T09:41:03Z | 0.25 | 0.55 | 0.8068 | 0.35 | 0.6 | 0.4585 |
| The future is not self-hosted, but self-sovereign | https://www.robertmao.com/blog/en/the-future-is-not-self-hosted-but-self-sovereign | www.robertmao.com | 2025-07-28T09:41:03Z | 0.25 | 0.55 | 0.8068 | 0.35 | 0.6 | 0.4585 |
| APT Rust requirement raises questions | https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/ | lwn.net | 2025-11-25T15:25:37Z | 0.25 | 0.45 | 0.9712 | 0.35 | 0.6 | 0.4582 |
| A 13-Year-Old Founder Building a Study App Because Existing Tools Weren't Enough | https://x.com/nikitaaci | x.com | 2025-11-23T20:31:30Z | 0.25 | 0.45 | 0.9685 | 0.35 | 0.6 | 0.4578 |
| Distillation makes AI models smaller and cheaper | https://www.quantamagazine.org/how-distillation-makes-ai-models-smaller-and-cheaper-20250718/ | www.quantamagazine.org | 2025-07-24T18:20:02Z | 0.25 | 0.55 | 0.8014 | 0.35 | 0.6 | 0.4577 |
| AMD Expands AI Product Lineup with GPU-Only Instinct Mi300X with 192GB Memory |  | www.anandtech.com | 2023-06-13T21:44:31Z | 0.55 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4575 |
| AMD Expands AI Product Lineup with GPU-Only Instinct Mi300X with 192GB Memory | https://www.anandtech.com/show/18915/amd-expands-mi300-family-with-mi300x-gpu-only-192gb-memory | www.anandtech.com | 2023-06-13T21:44:31Z | 0.55 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4575 |
| Arcana – Native Advertising Platform Built for GenAI Applications | https://arcana.ad/ | arcana.ad | 2025-03-11T21:10:52Z | 0.4 | 0.45 | 0.6164 | 0.35 | 0.6 | 0.4575 |
| Are we witnessing the final days of Mozilla? |  | lunduke.locals.com | 2025-07-23T14:15:29Z | 0.25 | 0.55 | 0.8 | 0.35 | 0.6 | 0.4575 |
| Are we witnessing the final days of Mozilla? | https://lunduke.locals.com/post/7132314/are-we-witnessing-the-final-days-of-mozilla | lunduke.locals.com | 2025-07-23T14:15:29Z | 0.25 | 0.55 | 0.8 | 0.35 | 0.6 | 0.4575 |
| Don't build AI products the way everyone else is doing it |  | www.builder.io | 2023-11-10T19:47:11Z | 0.55 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4575 |
| Don't build AI products the way everyone else is doing it | https://www.builder.io/blog/build-ai | www.builder.io | 2023-11-10T19:47:11Z | 0.55 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4575 |
| Local Deep Research – ArXiv, wiki and other searches included | https://github.com/LearningCircuit/local-deep-research | github.com | 2025-03-11T10:52:39Z | 0.4 | 0.45 | 0.6164 | 0.35 | 0.6 | 0.4575 |
| Show HN: I built a tool to identify viral AI products | https://www.aisites.top/ | www.aisites.top | 2023-11-09T16:49:42Z | 0.55 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4575 |
| Yelp releases new discovery, contribution, services and AI-powered features | https://blog.yelp.com/news/winter-product-release-2024/ | blog.yelp.com | 2024-01-31T06:27:36Z | 0.55 | 0.55 | 0.1 | 0.35 | 0.6 | 0.4575 |
| So you think you've awoken ChatGPT | https://www.lesswrong.com/posts/2pkNCvBtK6G6FKoNn/so-you-think-you-ve-awoken-chatgpt | www.lesswrong.com | 2025-07-22T15:24:26Z | 0.25 | 0.55 | 0.7986 | 0.35 | 0.6 | 0.4573 |
| Nano Banana Pro | https://blog.google/technology/ai/nano-banana-pro/ | blog.google | 2025-11-20T16:22:07Z | 0.25 | 0.45 | 0.9644 | 0.35 | 0.6 | 0.4572 |
| I Teach Creative Writing. This Is What A.I. Is Doing to Students | https://www.nytimes.com/2025/07/18/opinion/ai-chatgpt-school.html | www.nytimes.com | 2025-07-20T19:48:31Z | 0.25 | 0.55 | 0.7959 | 0.35 | 0.6 | 0.4569 |
| Gemini 3 | https://blog.google/products/gemini/gemini-3/ | blog.google | 2025-11-18T16:10:02Z | 0.25 | 0.45 | 0.9616 | 0.35 | 0.6 | 0.4567 |
| Grok 4.1 | https://x.ai/news/grok-4-1 | x.ai | 2025-11-18T07:00:47Z | 0.25 | 0.45 | 0.9616 | 0.35 | 0.6 | 0.4567 |
| Microsoft is plotting a future without OpenAI | https://techstartups.com/2025/03/07/microsoft-is-plotting-a-future-without-openai/ | techstartups.com | 2025-03-07T19:41:05Z | 0.4 | 0.45 | 0.611 | 0.35 | 0.6 | 0.4567 |
| Ship Your Directory in 1-Hour with DirEasy Boilerplate | https://www.direasy.com/en | www.direasy.com | 2025-07-19T07:36:52Z | 0.25 | 0.55 | 0.7945 | 0.35 | 0.6 | 0.4567 |
| Replicate is joining Cloudflare | https://replicate.com/blog/replicate-cloudflare | replicate.com | 2025-11-17T16:41:34Z | 0.25 | 0.45 | 0.9603 | 0.35 | 0.6 | 0.4565 |
| Apple Intelligence Foundation Language Models Tech Report 2025 | https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025 | machinelearning.apple.com | 2025-07-17T23:57:29Z | 0.25 | 0.55 | 0.7918 | 0.35 | 0.6 | 0.4563 |
| Is Perplexity the first AI unicorn to fail? | https://medium.com/@anwarzaid76/is-perplexity-the-first-ai-unicorn-to-fail-eb0e827b5e7e | medium.com | 2025-11-16T13:55:48Z | 0.25 | 0.45 | 0.9589 | 0.35 | 0.6 | 0.4563 |
| My analysis of 439 models proves: You're overpaying for your LLMs | https://whatllm.vercel.app/ | whatllm.vercel.app | 2025-07-17T12:44:51Z | 0.25 | 0.55 | 0.7918 | 0.35 | 0.6 | 0.4563 |
| Report: Tim Cook could step down as Apple CEO 'as soon as next year' |  | 9to5mac.com | 2025-11-15T23:16:34Z | 0.25 | 0.45 | 0.9575 | 0.35 | 0.6 | 0.4561 |
| Report: Tim Cook could step down as Apple CEO 'as soon as next year' | https://9to5mac.com/2025/11/14/tim-cook-step-down-as-apple-ceo-as-soon-as-next-year-report/ | 9to5mac.com | 2025-11-15T23:16:34Z | 0.25 | 0.45 | 0.9575 | 0.35 | 0.6 | 0.4561 |
| Show HN: Open-source Deep Research across workplace applications | https://github.com/onyx-dot-app/onyx | github.com | 2025-03-04T22:44:30Z | 0.4 | 0.45 | 0.6068 | 0.35 | 0.6 | 0.456 |
| I built a small Sora-style video generator as a side experiment |  | saro2.ai | 2025-11-14T06:52:54Z | 0.25 | 0.45 | 0.9562 | 0.35 | 0.6 | 0.4559 |
| I built a small Sora-style video generator as a side experiment | https://saro2.ai | saro2.ai | 2025-11-14T06:52:54Z | 0.25 | 0.45 | 0.9562 | 0.35 | 0.6 | 0.4559 |
| Data brokers are selling flight information to CBP and ICE |  | www.eff.org | 2025-07-14T20:56:59Z | 0.25 | 0.55 | 0.7877 | 0.35 | 0.6 | 0.4557 |
| Data brokers are selling flight information to CBP and ICE | https://www.eff.org/deeplinks/2025/07/data-brokers-are-selling-your-flight-information-cbp-and-ice | www.eff.org | 2025-07-14T20:56:59Z | 0.25 | 0.55 | 0.7877 | 0.35 | 0.6 | 0.4557 |
| Cerebras Trains Llama Models to Leap over GPUs | https://www.nextplatform.com/2024/10/25/cerebras-trains-llama-models-to-leap-over-gpus/ | www.nextplatform.com | 2024-10-31T07:23:01Z | 0.4 | 0.55 | 0.437 | 0.35 | 0.6 | 0.4555 |
| FFmpeg to Google: Fund us or stop sending bugs |  | thenewstack.io | 2025-11-11T20:52:54Z | 0.25 | 0.45 | 0.9521 | 0.35 | 0.6 | 0.4553 |
| FFmpeg to Google: Fund us or stop sending bugs | https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/ | thenewstack.io | 2025-11-11T20:52:54Z | 0.25 | 0.45 | 0.9521 | 0.35 | 0.6 | 0.4553 |
| Work after work: Notes from an unemployed new grad watching the job market break |  | urlahmed.com | 2025-11-10T01:49:15Z | 0.25 | 0.45 | 0.9493 | 0.35 | 0.6 | 0.4549 |
| Work after work: Notes from an unemployed new grad watching the job market break | https://urlahmed.com/2025/11/05/work-after-work-notes-from-an-unemployed-new-grad-watching-the-job-market-break/ | urlahmed.com | 2025-11-10T01:49:15Z | 0.25 | 0.45 | 0.9493 | 0.35 | 0.6 | 0.4549 |
| Linda Yaccarino is leaving X |  | www.nytimes.com | 2025-07-10T12:41:07Z | 0.25 | 0.55 | 0.7822 | 0.35 | 0.6 | 0.4548 |
| Linda Yaccarino is leaving X | https://www.nytimes.com/2025/07/09/technology/linda-yaccarino-x-steps-down.html | www.nytimes.com | 2025-07-10T12:41:07Z | 0.25 | 0.55 | 0.7822 | 0.35 | 0.6 | 0.4548 |
| Claude Pro Max hallucinated a $270 Notion feature that doesn't exist | https://gist.github.com/habonggil/f6130a68bbc4139c8066aa90c14c986f | gist.github.com | 2025-07-09T12:49:27Z | 0.25 | 0.55 | 0.7808 | 0.35 | 0.6 | 0.4546 |
| Is the doc bot docs, or not? | https://www.robinsloan.com/lab/what-are-we-even-doing-here/ | www.robinsloan.com | 2025-07-09T14:56:55Z | 0.25 | 0.55 | 0.7808 | 0.35 | 0.6 | 0.4546 |
| Supabase MCP can leak your entire SQL database | https://www.generalanalysis.com/blog/supabase-mcp-blog | www.generalanalysis.com | 2025-07-09T04:23:51Z | 0.25 | 0.55 | 0.7808 | 0.35 | 0.6 | 0.4546 |
| The Parallel Search API | https://parallel.ai/blog/introducing-parallel-search | parallel.ai | 2025-11-07T01:48:56Z | 0.25 | 0.45 | 0.9452 | 0.35 | 0.6 | 0.4543 |
| Strategic Wealth Accumulation Under Transformative AI Expectations | https://arxiv.org/abs/2502.11264 | arxiv.org | 2025-02-22T15:58:07Z | 0.4 | 0.45 | 0.5932 | 0.35 | 0.6 | 0.454 |
| Meta claims torrenting pirated books isn't illegal without proof of seeding | https://arstechnica.com/tech-policy/2025/02/meta-defends-its-vast-book-torrenting-were-just-a-leech-no-proof-of-seeding/ | arstechnica.com | 2025-02-21T17:36:54Z | 0.4 | 0.45 | 0.5918 | 0.35 | 0.6 | 0.4538 |
| Publicis Groupe Acquires Captiv8: A New Era for Influencer Marketing |  | thefinancefrontier.substack.com | 2025-07-06T01:17:23Z | 0.25 | 0.55 | 0.7753 | 0.35 | 0.6 | 0.4538 |
| Publicis Groupe Acquires Captiv8: A New Era for Influencer Marketing | https://thefinancefrontier.substack.com/p/publicis-groupe-acquires-captiv8 | thefinancefrontier.substack.com | 2025-07-06T01:17:23Z | 0.25 | 0.55 | 0.7753 | 0.35 | 0.6 | 0.4538 |
| TrendHarvester Pro |  | trendharvester.netlify.app | 2025-07-03T19:47:53Z | 0.25 | 0.55 | 0.7726 | 0.35 | 0.6 | 0.4534 |
| TrendHarvester Pro | https://trendharvester.netlify.app | trendharvester.netlify.app | 2025-07-03T19:47:53Z | 0.25 | 0.55 | 0.7726 | 0.35 | 0.6 | 0.4534 |
| HP Acquires Humane's AI Software |  | humane.com | 2025-02-19T13:20:56Z | 0.4 | 0.45 | 0.589 | 0.35 | 0.6 | 0.4533 |
| HP Acquires Humane's AI Software | https://humane.com/media/humane-hp | humane.com | 2025-02-19T13:20:56Z | 0.4 | 0.45 | 0.589 | 0.35 | 0.6 | 0.4533 |
| Cloudflare Introduces Default Blocking of A.I. Data Scrapers | https://www.nytimes.com/2025/07/01/technology/cloudflare-ai-data.html | www.nytimes.com | 2025-07-02T14:15:46Z | 0.25 | 0.55 | 0.7712 | 0.35 | 0.6 | 0.4532 |
| Free software scares normal people | https://danieldelaney.net/normal/ | danieldelaney.net | 2025-10-31T16:53:40Z | 0.25 | 0.45 | 0.937 | 0.35 | 0.6 | 0.4531 |
| Reasoning models reason well, until they don't | https://arxiv.org/abs/2510.22371 | arxiv.org | 2025-10-31T09:48:23Z | 0.25 | 0.45 | 0.937 | 0.35 | 0.6 | 0.4531 |
| Kagi Update: AI Image Filter for Search Results |  | help.kagi.com | 2024-10-18T15:17:42Z | 0.4 | 0.55 | 0.4192 | 0.35 | 0.6 | 0.4529 |
| Kagi Update: AI Image Filter for Search Results | https://help.kagi.com/kagi/features/exclude-ai-images.html | help.kagi.com | 2024-10-18T15:17:42Z | 0.4 | 0.55 | 0.4192 | 0.35 | 0.6 | 0.4529 |
| Everyone Mark Zuckerberg has hired so far for Meta's 'superintelligence' team |  | www.wired.com | 2025-06-30T21:44:45Z | 0.25 | 0.55 | 0.7685 | 0.35 | 0.6 | 0.4528 |
| Everyone Mark Zuckerberg has hired so far for Meta's 'superintelligence' team | https://www.wired.com/story/mark-zuckerberg-welcomes-superintelligence-team/ | www.wired.com | 2025-06-30T21:44:45Z | 0.25 | 0.55 | 0.7685 | 0.35 | 0.6 | 0.4528 |
| The new skill in AI is not prompting, it's context engineering | https://www.philschmid.de/context-engineering | www.philschmid.de | 2025-07-01T00:21:31Z | 0.25 | 0.55 | 0.7685 | 0.35 | 0.6 | 0.4528 |
| Xfinity using WiFi signals in your house to detect motion | https://www.xfinity.com/support/articles/wifi-motion | www.xfinity.com | 2025-07-01T03:08:30Z | 0.25 | 0.55 | 0.7685 | 0.35 | 0.6 | 0.4528 |
| Composer: Building a fast frontier model with RL | https://cursor.com/blog/composer | cursor.com | 2025-10-29T22:06:28Z | 0.25 | 0.45 | 0.9342 | 0.35 | 0.6 | 0.4526 |
| Engineered Addictions |  | masonyarbrough.substack.com | 2025-06-29T13:00:16Z | 0.25 | 0.55 | 0.7671 | 0.35 | 0.6 | 0.4526 |
| Engineered Addictions | https://masonyarbrough.substack.com/p/engineered-addictions | masonyarbrough.substack.com | 2025-06-29T13:00:16Z | 0.25 | 0.55 | 0.7671 | 0.35 | 0.6 | 0.4526 |
| What we talk about when we talk about sideloading | https://f-droid.org/2025/10/28/sideloading.html | f-droid.org | 2025-10-29T20:10:46Z | 0.25 | 0.45 | 0.9342 | 0.35 | 0.6 | 0.4526 |
| Generative AI's failure to induce robust models of the world | https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread | garymarcus.substack.com | 2025-06-29T03:38:43Z | 0.25 | 0.55 | 0.7658 | 0.35 | 0.6 | 0.4524 |
| AI is stifling new tech adoption? | https://vale.rocks/posts/ai-is-stifling-tech-adoption | vale.rocks | 2025-02-14T15:16:24Z | 0.4 | 0.45 | 0.5822 | 0.35 | 0.6 | 0.4523 |
| A definition of AGI | https://arxiv.org/abs/2510.18212 | arxiv.org | 2025-10-27T14:03:01Z | 0.25 | 0.45 | 0.9315 | 0.35 | 0.6 | 0.4522 |
| Feed the bots |  | maurycyz.com | 2025-10-26T14:16:10Z | 0.25 | 0.45 | 0.9301 | 0.35 | 0.6 | 0.452 |
| Feed the bots | https://maurycyz.com/misc/the_cost_of_trash/ | maurycyz.com | 2025-10-26T14:16:10Z | 0.25 | 0.45 | 0.9301 | 0.35 | 0.6 | 0.452 |
| Microsoft is struggling to sell Copilot to corporations – employees want ChatGPT | https://www.techradar.com/pro/microsoft-is-struggling-to-sell-copilot-to-corporations-because-their-employees-want-chatgpt-instead | www.techradar.com | 2025-06-26T16:07:34Z | 0.25 | 0.55 | 0.763 | 0.35 | 0.6 | 0.452 |
| Tell me about your favorite tree (a slow-web proposal) |  | nannnsss.omg.lol | 2025-06-24T04:38:10Z | 0.25 | 0.55 | 0.7603 | 0.35 | 0.6 | 0.4515 |
| Tell me about your favorite tree (a slow-web proposal) | https://nannnsss.omg.lol/2025/tell-me-about-your-favorite-tree/ | nannnsss.omg.lol | 2025-06-24T04:38:10Z | 0.25 | 0.55 | 0.7603 | 0.35 | 0.6 | 0.4515 |
| LLMs don't do formal reasoning | https://garymarcus.substack.com/p/llms-dont-do-formal-reasoning-and | garymarcus.substack.com | 2024-10-11T19:57:32Z | 0.4 | 0.55 | 0.4096 | 0.35 | 0.6 | 0.4514 |
| Let's Talk About Writing in Tech | https://www.gmoniava.com/blog/lets-talk-about-writing-in-tech | www.gmoniava.com | 2025-06-22T22:59:19Z | 0.25 | 0.55 | 0.7575 | 0.35 | 0.6 | 0.4511 |
| The LLMentalist Effect | https://softwarecrisis.dev/letters/llmentalist/ | softwarecrisis.dev | 2025-02-09T00:58:37Z | 0.4 | 0.45 | 0.574 | 0.35 | 0.6 | 0.4511 |
| The Programmer Identity Crisis | https://hojberg.xyz/the-programmer-identity-crisis/ | hojberg.xyz | 2025-10-21T19:50:04Z | 0.25 | 0.45 | 0.9233 | 0.35 | 0.6 | 0.451 |
| JavaScript broke the web (and called it progress) |  | www.jonoalderson.com | 2025-06-20T10:26:19Z | 0.25 | 0.55 | 0.7548 | 0.35 | 0.6 | 0.4507 |
| JavaScript broke the web (and called it progress) | https://www.jonoalderson.com/conjecture/javascript-broke-the-web-and-called-it-progress/ | www.jonoalderson.com | 2025-06-20T10:26:19Z | 0.25 | 0.55 | 0.7548 | 0.35 | 0.6 | 0.4507 |
| Oklo, the Earth's Two-billion-year-old only Known Natural Nuclear Reactor (2018) | https://www.iaea.org/newscenter/news/meet-oklo-the-earths-two-billion-year-old-only-known-natural-nuclear-reactor | www.iaea.org | 2025-06-20T16:27:03Z | 0.25 | 0.55 | 0.7548 | 0.35 | 0.6 | 0.4507 |
| ProdiApp: The Ethical, Powerful Alternative to Yelp, Angi, and Thumbtack | https://www.prodiapp.com/web/index.php | www.prodiapp.com | 2025-06-19T13:18:22Z | 0.25 | 0.55 | 0.7534 | 0.35 | 0.6 | 0.4505 |
| Show HN: I built an AI tool that writes resumes and preps you for interviews | https://artemion.com | artemion.com | 2025-02-05T21:48:06Z | 0.4 | 0.45 | 0.5699 | 0.35 | 0.6 | 0.4505 |
| The drawbridges come up: the dream of a interconnected context ecosystem is over |  | www.dbreunig.com | 2025-06-17T18:50:07Z | 0.25 | 0.55 | 0.7507 | 0.35 | 0.6 | 0.4501 |
| The drawbridges come up: the dream of a interconnected context ecosystem is over | https://www.dbreunig.com/2025/06/16/drawbridges-go-up.html | www.dbreunig.com | 2025-06-17T18:50:07Z | 0.25 | 0.55 | 0.7507 | 0.35 | 0.6 | 0.4501 |
| Campfire: Devs through GitHub, skip the LinkedIn noise | https://campfire-u5uj.onrender.com/ | campfire-u5uj.onrender.com | 2025-06-14T15:51:36Z | 0.25 | 0.55 | 0.7466 | 0.35 | 0.6 | 0.4495 |
| I built what startups say they need, but they won't sign up |  | smarketly.lema-lema.com | 2025-06-14T20:50:33Z | 0.25 | 0.55 | 0.7466 | 0.35 | 0.6 | 0.4495 |
| I built what startups say they need, but they won't sign up | https://smarketly.lema-lema.com/ | smarketly.lema-lema.com | 2025-06-14T20:50:33Z | 0.25 | 0.55 | 0.7466 | 0.35 | 0.6 | 0.4495 |
| Add "fucking" to your Google searches to neutralize AI summaries | https://gizmodo.com/add-fcking-to-your-google-searches-to-neutralize-ai-summaries-2000557710 | gizmodo.com | 2025-01-31T23:52:12Z | 0.4 | 0.45 | 0.563 | 0.35 | 0.6 | 0.4494 |
| Do AI companies work? |  | benn.substack.com | 2024-10-01T05:02:34Z | 0.4 | 0.55 | 0.3959 | 0.35 | 0.6 | 0.4494 |
| Do AI companies work? | https://benn.substack.com/p/do-ai-companies-work | benn.substack.com | 2024-10-01T05:02:34Z | 0.4 | 0.55 | 0.3959 | 0.35 | 0.6 | 0.4494 |
| Notes on OpenAI o3-mini | https://simonwillison.net/2025/Jan/31/o3-mini/ | simonwillison.net | 2025-02-01T01:41:09Z | 0.4 | 0.45 | 0.563 | 0.35 | 0.6 | 0.4494 |
| First thoughts on o3 pro |  | www.latent.space | 2025-06-13T12:29:47Z | 0.25 | 0.55 | 0.7452 | 0.35 | 0.6 | 0.4493 |
| First thoughts on o3 pro | https://www.latent.space/p/o3-pro | www.latent.space | 2025-06-13T12:29:47Z | 0.25 | 0.55 | 0.7452 | 0.35 | 0.6 | 0.4493 |
| They Asked an A.I. Chatbot Questions. The Answers Sent Them Spiraling | https://www.nytimes.com/2025/06/13/technology/chatgpt-ai-chatbots-conspiracies.html | www.nytimes.com | 2025-06-13T17:12:47Z | 0.25 | 0.55 | 0.7452 | 0.35 | 0.6 | 0.4493 |
| Analysis of Product Hunt products from 2014 to 2021 |  | components.one | 2025-01-30T17:12:38Z | 0.4 | 0.45 | 0.5616 | 0.35 | 0.6 | 0.4492 |
| Analysis of Product Hunt products from 2014 to 2021 | https://components.one/posts/gamer-and-nihilist-product-hunt | components.one | 2025-01-30T17:12:38Z | 0.4 | 0.45 | 0.5616 | 0.35 | 0.6 | 0.4492 |
| Builder.ai did not "fake AI with 700 engineers" | https://newsletter.pragmaticengineer.com/p/the-pulse-137 | newsletter.pragmaticengineer.com | 2025-06-12T21:59:40Z | 0.25 | 0.55 | 0.7438 | 0.35 | 0.6 | 0.4491 |
| Chatbots are replacing Google's search, devastating traffic for some publishers |  | www.wsj.com | 2025-06-11T03:44:08Z | 0.25 | 0.55 | 0.7425 | 0.35 | 0.6 | 0.4489 |
| Chatbots are replacing Google's search, devastating traffic for some publishers | https://www.wsj.com/tech/ai/google-ai-news-publishers-7e687141 | www.wsj.com | 2025-06-11T03:44:08Z | 0.25 | 0.55 | 0.7425 | 0.35 | 0.6 | 0.4489 |
| Apple announces Foundation Models and Containerization frameworks, etc | https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/ | www.apple.com | 2025-06-10T18:09:12Z | 0.25 | 0.55 | 0.7411 | 0.35 | 0.6 | 0.4487 |
| I switched from Htmx to Datastar | https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/ | everydaysuperpowers.dev | 2025-10-10T13:29:54Z | 0.25 | 0.45 | 0.9082 | 0.35 | 0.6 | 0.4487 |
| It's OpenAI's world, we're just living in it | https://stratechery.com/2025/its-openais-world-were-just-living-in-it/ | stratechery.com | 2025-10-10T18:34:32Z | 0.25 | 0.45 | 0.9082 | 0.35 | 0.6 | 0.4487 |
| Google "We have no moat, and neither does OpenAI" (2023) |  | semianalysis.com | 2025-01-27T20:49:48Z | 0.4 | 0.45 | 0.5575 | 0.35 | 0.6 | 0.4486 |
| Google "We have no moat, and neither does OpenAI" (2023) | https://semianalysis.com/2023/05/04/google-we-have-no-moat-and-neither/ | semianalysis.com | 2025-01-27T20:49:48Z | 0.4 | 0.45 | 0.5575 | 0.35 | 0.6 | 0.4486 |
| A competitor crippled a $23.5M bootcamp by becoming a Reddit moderator | https://larslofgren.com/codesmith-reddit-reputation-attack/ | larslofgren.com | 2025-10-09T05:15:07Z | 0.25 | 0.45 | 0.9068 | 0.35 | 0.6 | 0.4485 |
| LLMs are cheap | https://www.snellman.net/blog/archive/2025-06-02-llms-are-cheap/ | www.snellman.net | 2025-06-09T21:41:06Z | 0.25 | 0.55 | 0.7397 | 0.35 | 0.6 | 0.4485 |
| Building supercomputers for autocrats probably isn't good for democracy |  | helentoner.substack.com | 2025-06-08T23:59:55Z | 0.25 | 0.55 | 0.7384 | 0.35 | 0.6 | 0.4483 |
| Building supercomputers for autocrats probably isn't good for democracy | https://helentoner.substack.com/p/supercomputers-for-autocrats | helentoner.substack.com | 2025-06-08T23:59:55Z | 0.25 | 0.55 | 0.7384 | 0.35 | 0.6 | 0.4483 |
| OpenAI to remove non-profit control and give Sam Altman equity |  | www.reuters.com | 2024-09-26T12:58:24Z | 0.4 | 0.55 | 0.389 | 0.35 | 0.6 | 0.4483 |
| OpenAI to remove non-profit control and give Sam Altman equity | https://www.reuters.com/technology/artificial-intelligence/openai-remove-non-profit-control-give-sam-altman-equity-sources-say-2024-09-25/ | www.reuters.com | 2024-09-26T12:58:24Z | 0.4 | 0.55 | 0.389 | 0.35 | 0.6 | 0.4483 |
| The Illusion of Thinking: Strengths and limitations of reasoning models [pdf] | https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf | ml-site.cdn-apple.com | 2025-06-08T13:30:07Z | 0.25 | 0.55 | 0.7384 | 0.35 | 0.6 | 0.4483 |
| Master the Art of the Product Manager 'No' |  | LetsNotDoThat.com | 2025-01-23T08:14:33Z | 0.4 | 0.45 | 0.5521 | 0.35 | 0.6 | 0.4478 |
| Master the Art of the Product Manager 'No' | https://LetsNotDoThat.com | LetsNotDoThat.com | 2025-01-23T08:14:33Z | 0.4 | 0.45 | 0.5521 | 0.35 | 0.6 | 0.4478 |
| Self-hosting your own media considered harmful according to YouTube | https://www.jeffgeerling.com/blog/2025/self-hosting-your-own-media-considered-harmful | www.jeffgeerling.com | 2025-06-06T08:59:47Z | 0.25 | 0.55 | 0.7356 | 0.35 | 0.6 | 0.4478 |
| Blog Feeds |  | blogfeeds.net | 2025-10-05T05:31:55Z | 0.25 | 0.45 | 0.9014 | 0.35 | 0.6 | 0.4477 |
| Blog Feeds | https://blogfeeds.net | blogfeeds.net | 2025-10-05T05:31:55Z | 0.25 | 0.45 | 0.9014 | 0.35 | 0.6 | 0.4477 |
| Show HN: "data-to-paper" – autonomous stepwise LLM-driven research | https://github.com/Technion-Kishony-lab/data-to-paper | github.com | 2024-05-12T14:12:41Z | 0.55 | 0.45 | 0.2014 | 0.35 | 0.6 | 0.4477 |
| Selling Legal Tech SaaS Portfolio – Pre-Revenue but Validated ($8,500) | https://x.com/SumanthChary07 | x.com | 2025-10-04T07:53:05Z | 0.25 | 0.45 | 0.9 | 0.35 | 0.6 | 0.4475 |
| It sure looks like Meta stole a lot of books to build its AI | https://lithub.com/it-sure-looks-like-meta-stole-a-lot-of-books-to-build-its-ai/ | lithub.com | 2025-01-21T02:41:03Z | 0.4 | 0.45 | 0.5479 | 0.35 | 0.6 | 0.4472 |
| AI video you can watch and interact with, in real-time | https://experience.odyssey.world | experience.odyssey.world | 2025-06-01T00:11:15Z | 0.25 | 0.55 | 0.7274 | 0.35 | 0.6 | 0.4466 |
| Cerebras achieves 2,500T/s on Llama 4 Maverick (400B) | https://www.cerebras.ai/press-release/maverick | www.cerebras.ai | 2025-05-31T12:52:21Z | 0.25 | 0.55 | 0.7274 | 0.35 | 0.6 | 0.4466 |
| Learn touch typing – it's worth it | https://www.typequicker.com/blog/learn-touch-typing | www.typequicker.com | 2025-05-31T18:39:08Z | 0.25 | 0.55 | 0.7274 | 0.35 | 0.6 | 0.4466 |
| To AI or not to AI | https://antropia.studio/blog/to-ai-or-not-to-ai/ | antropia.studio | 2025-09-29T22:57:10Z | 0.25 | 0.45 | 0.8932 | 0.35 | 0.6 | 0.4465 |
| AI founders will learn the bitter lesson |  | lukaspetersson.com | 2025-01-12T12:31:58Z | 0.4 | 0.45 | 0.537 | 0.35 | 0.6 | 0.4456 |
| AI founders will learn the bitter lesson | https://lukaspetersson.com/blog/2025/bitter-vertical/ | lukaspetersson.com | 2025-01-12T12:31:58Z | 0.4 | 0.45 | 0.537 | 0.35 | 0.6 | 0.4456 |
| Phi 4 available on Ollama |  | ollama.com | 2025-01-12T04:57:00Z | 0.4 | 0.45 | 0.537 | 0.35 | 0.6 | 0.4456 |
| Phi 4 available on Ollama | https://ollama.com/library/phi4 | ollama.com | 2025-01-12T04:57:00Z | 0.4 | 0.45 | 0.537 | 0.35 | 0.6 | 0.4456 |
| Keevo – AI that accurately updates your content in your voice | https://keevo.ai | keevo.ai | 2025-09-22T12:44:15Z | 0.25 | 0.45 | 0.8836 | 0.35 | 0.6 | 0.445 |
| Show HN: A minimalist, encrypted knowledge platform for solo devs and founders | https://orbivon.com | orbivon.com | 2025-09-22T17:18:06Z | 0.25 | 0.45 | 0.8836 | 0.35 | 0.6 | 0.445 |
| The Future of Junior Software Engineering Roles | https://adventuresincoding.substack.com/p/the-future-of-junior-software-engineering | adventuresincoding.substack.com | 2025-05-21T07:12:40Z | 0.25 | 0.55 | 0.7137 | 0.35 | 0.6 | 0.4446 |
| The EU Just Killed ARR | https://paid.ai/blog/ai-monetization/eu-data-act-killed-arr | paid.ai | 2025-09-19T14:13:27Z | 0.25 | 0.45 | 0.8795 | 0.35 | 0.6 | 0.4444 |
| Gemini in Chrome | https://gemini.google/overview/gemini-in-chrome/ | gemini.google | 2025-09-19T02:46:52Z | 0.25 | 0.45 | 0.8781 | 0.35 | 0.6 | 0.4442 |
| The Cost of Our Lies to AI | https://www.lesswrong.com/posts/9PiyWjoe9tajReF7v/the-hidden-cost-of-our-lies-to-ai | www.lesswrong.com | 2025-05-20T01:15:40Z | 0.25 | 0.55 | 0.711 | 0.35 | 0.6 | 0.4441 |
| Ilya Sutskever's SSI Inc raises $1B | https://www.reuters.com/technology/artificial-intelligence/openai-co-founder-sutskevers-new-safety-focused-ai-startup-ssi-raises-1-billion-2024-09-04/ | www.reuters.com | 2024-09-05T10:46:22Z | 0.4 | 0.55 | 0.3603 | 0.35 | 0.6 | 0.444 |
| Beyond Text: On-Demand UI Generation for Better Conversational Experiences | https://blog.fka.dev/blog/2025-05-16-beyond-text-only-ai-on-demand-ui-generation-for-better-conversational-experiences/ | blog.fka.dev | 2025-05-16T12:14:55Z | 0.25 | 0.55 | 0.7068 | 0.35 | 0.6 | 0.4435 |
| Meta Wants More AI Bots on Facebook and Instagram |  | nymag.com | 2025-01-02T06:14:10Z | 0.4 | 0.45 | 0.5233 | 0.35 | 0.6 | 0.4435 |
| Meta Wants More AI Bots on Facebook and Instagram | https://nymag.com/intelligencer/article/meta-wants-more-ai-bots-on-facebook-and-instagram.html | nymag.com | 2025-01-02T06:14:10Z | 0.4 | 0.45 | 0.5233 | 0.35 | 0.6 | 0.4435 |
| Will AI systems perform poorly due to AI-generated material in training data? | https://cacm.acm.org/news/the-collapse-of-gpt/ | cacm.acm.org | 2025-05-17T03:27:14Z | 0.25 | 0.55 | 0.7068 | 0.35 | 0.6 | 0.4435 |
| Stack Overflow is almost dead | https://blog.pragmaticengineer.com/stack-overflow-is-almost-dead/ | blog.pragmaticengineer.com | 2025-05-15T22:37:42Z | 0.25 | 0.55 | 0.7055 | 0.35 | 0.6 | 0.4433 |
| The Threat to OpenAI | https://www.wsj.com/tech/ai/ai-chatgpt-nvidia-apple-facebook-383943d1 | www.wsj.com | 2024-09-01T00:48:43Z | 0.4 | 0.55 | 0.3534 | 0.35 | 0.6 | 0.443 |
| YouTube is a mysterious monopoly |  | anderegg.ca | 2025-09-11T14:01:58Z | 0.25 | 0.45 | 0.8685 | 0.35 | 0.6 | 0.4428 |
| YouTube is a mysterious monopoly | https://anderegg.ca/2025/09/08/youtube-is-a-mysterious-monopoly | anderegg.ca | 2025-09-11T14:01:58Z | 0.25 | 0.45 | 0.8685 | 0.35 | 0.6 | 0.4428 |
| OpenAI shows 'Strawberry' to feds, races to launch it |  | www.lesswrong.com | 2024-08-28T10:12:39Z | 0.4 | 0.55 | 0.3493 | 0.35 | 0.6 | 0.4424 |
| OpenAI shows 'Strawberry' to feds, races to launch it | https://www.lesswrong.com/posts/8oX4FTRa8MJodArhj/the-information-openai-shows-strawberry-to-feds-races-to | www.lesswrong.com | 2024-08-28T10:12:39Z | 0.4 | 0.55 | 0.3493 | 0.35 | 0.6 | 0.4424 |
| Alignment is not free: How model upgrades can silence your confidence signals | https://www.variance.co/post/alignment-is-not-free-how-a-model-silenced-our-confidence-signals | www.variance.co | 2025-05-07T15:57:57Z | 0.25 | 0.55 | 0.6945 | 0.35 | 0.6 | 0.4417 |
| Gemini 2.5 Pro Preview | https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/ | developers.googleblog.com | 2025-05-07T17:54:30Z | 0.25 | 0.55 | 0.6945 | 0.35 | 0.6 | 0.4417 |
| A.I. Is Getting More Powerful, but Its Hallucinations Are Getting Worse | https://www.nytimes.com/2025/05/05/technology/ai-hallucinations-chatgpt-google.html | www.nytimes.com | 2025-05-06T11:34:02Z | 0.25 | 0.55 | 0.6932 | 0.35 | 0.6 | 0.4415 |
| Machine Unlearning in 2024 | https://ai.stanford.edu/~kzliu/blog/unlearning | ai.stanford.edu | 2024-05-05T17:59:06Z | 0.25 | 0.85 | 0.1918 | 0.35 | 0.6 | 0.4413 |
| Crawlers impact the operations of the Wikimedia projects | https://diff.wikimedia.org/2025/04/01/how-crawlers-impact-the-operations-of-the-wikimedia-projects/ | diff.wikimedia.org | 2025-05-02T13:10:27Z | 0.25 | 0.55 | 0.6877 | 0.35 | 0.6 | 0.4407 |
| When ChatGPT broke the field of NLP: An oral history | https://www.quantamagazine.org/when-chatgpt-broke-an-entire-field-an-oral-history-20250430/ | www.quantamagazine.org | 2025-05-02T10:03:25Z | 0.25 | 0.55 | 0.6877 | 0.35 | 0.6 | 0.4407 |
| AGI Is Not a Milestone | https://www.aisnakeoil.com/p/agi-is-not-a-milestone | www.aisnakeoil.com | 2025-05-02T03:41:56Z | 0.25 | 0.55 | 0.6863 | 0.35 | 0.6 | 0.4404 |
| Mandatory Certification Regarding Generative Artificial Intelligence | https://www.txnd.uscourts.gov/judge/judge-brantley-starr | www.txnd.uscourts.gov | 2023-05-30T22:44:23Z | 0.25 | 0.9 | 0.1 | 0.35 | 0.6 | 0.44 |
| Qwen3: Think deeper, act faster | https://qwenlm.github.io/blog/qwen3/ | qwenlm.github.io | 2025-04-29T10:46:20Z | 0.25 | 0.55 | 0.6836 | 0.35 | 0.6 | 0.44 |
| Reality Check | https://www.wheresyoured.at/reality-check/ | www.wheresyoured.at | 2025-04-28T17:32:18Z | 0.25 | 0.55 | 0.6822 | 0.35 | 0.6 | 0.4398 |
| The Myth of the Product-Market Fit (2013) |  | blog.nishantsoni.com | 2024-08-15T06:49:04Z | 0.4 | 0.55 | 0.3315 | 0.35 | 0.6 | 0.4397 |
| The Myth of the Product-Market Fit (2013) | https://blog.nishantsoni.com/p/the-myth-of-the-product-market-fit | blog.nishantsoni.com | 2024-08-15T06:49:04Z | 0.4 | 0.55 | 0.3315 | 0.35 | 0.6 | 0.4397 |
| Claude for Chrome | https://claude.ai/chrome | claude.ai | 2025-08-26T19:40:56Z | 0.25 | 0.45 | 0.8466 | 0.35 | 0.6 | 0.4395 |
| AI SaaS Launcher – Build SaaS MVPs fast with AI and next-gen low-code power | https://app.trydome.io/signup?flow=ai-sass-launcher&utm_source=hn&utm_medium=social&utm_campaign=launch | app.trydome.io | 2024-08-13T18:06:19Z | 0.4 | 0.55 | 0.3288 | 0.35 | 0.6 | 0.4393 |
| Demand for AI servers causing a run on enterprise SSDs, hiking prices | https://www.theregister.com/2024/08/13/demand_for_ai_servers_ssd_pricing/ | www.theregister.com | 2024-08-13T15:57:45Z | 0.4 | 0.55 | 0.3288 | 0.35 | 0.6 | 0.4393 |
| Study shows that tacking the “AI” label on products may drive people away | https://www.cnn.com/2024/08/10/business/brands-avoid-term-customers/index.html | www.cnn.com | 2024-08-13T12:39:40Z | 0.4 | 0.55 | 0.3288 | 0.35 | 0.6 | 0.4393 |
| Show HN: Chonkie Cloud – No-nonsense chunking now on the the cloud | https://cloud.chonkie.ai | cloud.chonkie.ai | 2025-04-23T21:22:52Z | 0.25 | 0.55 | 0.6753 | 0.35 | 0.6 | 0.4388 |
| Being “Confidently Wrong” is holding AI back | https://promptql.io/blog/being-confidently-wrong-is-holding-ai-back | promptql.io | 2025-08-22T14:07:43Z | 0.25 | 0.45 | 0.8411 | 0.35 | 0.6 | 0.4387 |
| Are ChatGPT and co harming human intelligence? | https://www.theguardian.com/technology/2025/apr/19/dont-ask-what-ai-can-do-for-us-ask-what-it-is-doing-to-us-are-chatgpt-and-co-harming-human-intelligence | www.theguardian.com | 2025-04-21T13:57:02Z | 0.25 | 0.55 | 0.6726 | 0.35 | 0.6 | 0.4384 |
| Landlords Are Using AI to Raise Rents | https://gizmodo.com/landlords-are-using-ai-to-raise-rents-and-cities-are-starting-to-push-back-2000535519 | gizmodo.com | 2024-12-08T03:50:26Z | 0.4 | 0.45 | 0.489 | 0.35 | 0.6 | 0.4383 |
| OpenAI co-founder John Schulman says he will leave and join rival Anthropic |  | www.cnbc.com | 2024-08-06T14:13:14Z | 0.4 | 0.55 | 0.3192 | 0.35 | 0.6 | 0.4379 |
| OpenAI co-founder John Schulman says he will leave and join rival Anthropic | https://www.cnbc.com/2024/08/06/openai-co-founder-john-schulman-says-he-will-join-rival-anthropic.html | www.cnbc.com | 2024-08-06T14:13:14Z | 0.4 | 0.55 | 0.3192 | 0.35 | 0.6 | 0.4379 |
| Gemini 2.5 Flash |  | developers.googleblog.com | 2025-04-18T06:04:00Z | 0.25 | 0.55 | 0.6685 | 0.35 | 0.6 | 0.4378 |
| Gemini 2.5 Flash | https://developers.googleblog.com/en/start-building-with-gemini-25-flash/ | developers.googleblog.com | 2025-04-18T06:04:00Z | 0.25 | 0.55 | 0.6685 | 0.35 | 0.6 | 0.4378 |
| Who does your assistant serve? | https://xeiaso.net/blog/2025/who-assistant-serve/ | xeiaso.net | 2025-08-18T06:26:56Z | 0.25 | 0.45 | 0.8356 | 0.35 | 0.6 | 0.4378 |
| Show HN: Fallinorg - Offline Mac app that organizes files by meaning | https://fallinorg.com/# | fallinorg.com | 2025-08-17T18:05:10Z | 0.25 | 0.45 | 0.8342 | 0.35 | 0.6 | 0.4376 |
| We're making GPT-5 warmer and friendlier based on feedback that it felt formal | https://twitter.com/OpenAI/status/1956461718097494196 | twitter.com | 2025-08-16T14:35:29Z | 0.25 | 0.45 | 0.8329 | 0.35 | 0.6 | 0.4374 |
| Pentagon to terminate $5.1B in IT contracts with Accenture, Deloitte | https://www.reuters.com/world/us/pentagon-terminate-51-billion-it-contracts-with-accenture-deloitte-others-2025-04-11/ | www.reuters.com | 2025-04-15T22:24:06Z | 0.25 | 0.55 | 0.6644 | 0.35 | 0.6 | 0.4372 |
| WEIRD – a way to be on the web |  | a.weird.one | 2025-04-15T17:58:48Z | 0.25 | 0.55 | 0.6644 | 0.35 | 0.6 | 0.4372 |
| WEIRD – a way to be on the web | https://a.weird.one | a.weird.one | 2025-04-15T17:58:48Z | 0.25 | 0.55 | 0.6644 | 0.35 | 0.6 | 0.4372 |
| The future of the internet is likely smaller communities |  | www.theverge.com | 2025-04-15T01:34:57Z | 0.25 | 0.55 | 0.663 | 0.35 | 0.6 | 0.437 |
| The future of the internet is likely smaller communities | https://www.theverge.com/press-room/617654/internet-community-future-research | www.theverge.com | 2025-04-15T01:34:57Z | 0.25 | 0.55 | 0.663 | 0.35 | 0.6 | 0.437 |
| Why are there so many rationalist cults? |  | asteriskmag.com | 2025-08-14T05:34:42Z | 0.25 | 0.45 | 0.8301 | 0.35 | 0.6 | 0.437 |
| Why are there so many rationalist cults? | https://asteriskmag.com/issues/11/why-are-there-so-many-rationalist-cults | asteriskmag.com | 2025-08-14T05:34:42Z | 0.25 | 0.45 | 0.8301 | 0.35 | 0.6 | 0.437 |
| Claude says “You're absolutely right!” about everything | https://github.com/anthropics/claude-code/issues/3382 | github.com | 2025-08-13T16:26:36Z | 0.25 | 0.45 | 0.8288 | 0.35 | 0.6 | 0.4368 |
| How Does OpenAI Survive? | https://www.wheresyoured.at/to-serve-altman/ | www.wheresyoured.at | 2024-08-01T20:59:03Z | 0.4 | 0.55 | 0.3123 | 0.35 | 0.6 | 0.4368 |
| Show HN: Omnara – Run Claude Code from anywhere | https://github.com/omnara-ai/omnara | github.com | 2025-08-13T19:53:54Z | 0.25 | 0.45 | 0.8288 | 0.35 | 0.6 | 0.4368 |
| WTF Is Botmetr? The First Platform That Rewards You for Hunting Chatbots | https://www.botmetr.com/ | www.botmetr.com | 2025-04-13T00:59:44Z | 0.25 | 0.55 | 0.6603 | 0.35 | 0.6 | 0.4365 |
| AI and the Next Computing Platforms with Jensen Huang and Mark Zuckerberg | https://www.youtube.com/watch?v=w-cmMcMZoZ4 | www.youtube.com | 2024-07-30T15:57:31Z | 0.4 | 0.55 | 0.3096 | 0.35 | 0.6 | 0.4364 |
| Playing in the Creek | https://www.hgreer.com/PlayingInTheCreek/ | www.hgreer.com | 2025-04-11T12:37:22Z | 0.25 | 0.55 | 0.6589 | 0.35 | 0.6 | 0.4363 |
| Evidence suggesting Quasar Alpha is OpenAI's new model | https://blog.kilocode.ai/p/quasar-alpha-what-we-know-thus-far | blog.kilocode.ai | 2025-04-10T18:25:40Z | 0.25 | 0.55 | 0.6575 | 0.35 | 0.6 | 0.4361 |
| Show HN: DrawDB – open-source online database diagram editor (a retro) | https://www.drawdb.app/ | www.drawdb.app | 2025-04-09T05:30:23Z | 0.25 | 0.55 | 0.6562 | 0.35 | 0.6 | 0.4359 |
| Claude Code IDE integration for Emacs | https://github.com/manzaltu/claude-code-ide.el | github.com | 2025-08-07T17:41:20Z | 0.25 | 0.45 | 0.8205 | 0.35 | 0.6 | 0.4356 |
| Perplexity Response to Cloudflare | https://twitter.com/perplexity_ai/status/1952531537385456019 | twitter.com | 2025-08-05T15:19:19Z | 0.25 | 0.45 | 0.8178 | 0.35 | 0.6 | 0.4352 |
| Every Reason Why I Hate AI and You Should Too | https://malwaretech.com/2025/08/every-reason-why-i-hate-ai.html | malwaretech.com | 2025-08-04T19:50:40Z | 0.25 | 0.45 | 0.8164 | 0.35 | 0.6 | 0.435 |
| Open source AI is the path forward |  | about.fb.com | 2024-07-23T18:40:46Z | 0.4 | 0.55 | 0.3 | 0.35 | 0.6 | 0.435 |
| Open source AI is the path forward | https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/ | about.fb.com | 2024-07-23T18:40:46Z | 0.4 | 0.55 | 0.3 | 0.35 | 0.6 | 0.435 |
| Apple lacks strategic vision |  | unherd.com | 2025-08-03T16:14:24Z | 0.25 | 0.45 | 0.8151 | 0.35 | 0.6 | 0.4348 |
| Apple lacks strategic vision | https://unherd.com/2025/08/time-is-running-out-for-tim-cook/?lang=us | unherd.com | 2025-08-03T16:14:24Z | 0.25 | 0.45 | 0.8151 | 0.35 | 0.6 | 0.4348 |
| Show HN: OpenNutrition – A free, public nutrition database | https://www.opennutrition.app/search | www.opennutrition.app | 2025-04-03T14:24:45Z | 0.25 | 0.55 | 0.6479 | 0.35 | 0.6 | 0.4347 |
| Browser extension and local backend that automatically archives YouTube videos | https://github.com/andrewarrow/starchive | github.com | 2025-08-02T23:51:41Z | 0.25 | 0.45 | 0.8137 | 0.35 | 0.6 | 0.4346 |
| Show HN: Lifelike one shot gesture animation by Claude | https://claude.ai/public/artifacts/12ef9f4d-ed0e-494b-97c4-edfecc11d9a2 | claude.ai | 2025-08-02T12:05:16Z | 0.25 | 0.45 | 0.8137 | 0.35 | 0.6 | 0.4346 |
| Show HN: Mermaid Chart VS Code Plugin: Mermaid.js Diagrams in Visual Studio Code | https://docs.mermaidchart.com/blog/posts/mermaid-chart-vs-code-plugin-create-and-edit-mermaid-js-diagrams-in-visual-studio-code | docs.mermaidchart.com | 2025-04-02T19:51:48Z | 0.25 | 0.55 | 0.6466 | 0.35 | 0.6 | 0.4345 |
| AI is quietly being used to pick your pocket | https://www.businessinsider.com/ai-quietly-picking-your-pocket-with-personalized-pricing-2024-7 | www.businessinsider.com | 2024-07-19T15:11:51Z | 0.4 | 0.55 | 0.2945 | 0.35 | 0.6 | 0.4342 |
| OpenAI slashes the cost of using its AI with a "mini" model | https://www.wired.com/story/openai-gpt-4o-mini/ | www.wired.com | 2024-07-18T19:01:01Z | 0.4 | 0.55 | 0.2932 | 0.35 | 0.6 | 0.434 |
| The hype is the product | https://rys.io/en/180.html | rys.io | 2025-07-30T22:22:55Z | 0.25 | 0.45 | 0.8096 | 0.35 | 0.6 | 0.4339 |
| Self-attention transforms a prompt into a low-rank weight-update | https://arxiv.org/abs/2507.16003 | arxiv.org | 2025-07-28T13:44:04Z | 0.25 | 0.45 | 0.8068 | 0.35 | 0.6 | 0.4335 |
| GPT might be an information virus (2023) | https://nonint.com/2023/03/09/gpt-might-be-an-information-virus/ | nonint.com | 2025-07-27T23:30:53Z | 0.25 | 0.45 | 0.8055 | 0.35 | 0.6 | 0.4333 |
| What went wrong with the Alan Turing Institute? | https://www.chalmermagne.com/p/how-not-to-build-an-ai-institute | www.chalmermagne.com | 2025-03-27T15:54:27Z | 0.25 | 0.55 | 0.6384 | 0.35 | 0.6 | 0.4333 |
| When we get Komooted |  | bikepacking.com | 2025-07-27T12:35:51Z | 0.25 | 0.45 | 0.8055 | 0.35 | 0.6 | 0.4333 |
| When we get Komooted | https://bikepacking.com/plog/when-we-get-komooted/ | bikepacking.com | 2025-07-27T12:35:51Z | 0.25 | 0.45 | 0.8055 | 0.35 | 0.6 | 0.4333 |
| Show HN: I built a biological network visualization tool | https://nodes.bio | nodes.bio | 2025-07-26T17:10:55Z | 0.25 | 0.45 | 0.8041 | 0.35 | 0.6 | 0.4331 |
| Has the decline of knowledge work begun? |  | www.nytimes.com | 2025-03-27T01:36:04Z | 0.25 | 0.55 | 0.637 | 0.35 | 0.6 | 0.433 |
| Has the decline of knowledge work begun? | https://www.nytimes.com/2025/03/25/business/economy/white-collar-layoffs.html | www.nytimes.com | 2025-03-27T01:36:04Z | 0.25 | 0.55 | 0.637 | 0.35 | 0.6 | 0.433 |
| Do not download the app, use the website | https://idiallo.com/blog/dont-download-apps | idiallo.com | 2025-07-26T00:27:46Z | 0.25 | 0.45 | 0.8027 | 0.35 | 0.6 | 0.4329 |
| Up to date prices for LLM APIs all in one place | https://pricepertoken.com/ | pricepertoken.com | 2025-07-25T15:25:36Z | 0.25 | 0.45 | 0.8027 | 0.35 | 0.6 | 0.4329 |
| A.I. Has Become a Technology of Faith |  | www.theatlantic.com | 2024-07-12T20:19:26Z | 0.4 | 0.55 | 0.2849 | 0.35 | 0.6 | 0.4327 |
| A.I. Has Become a Technology of Faith | https://www.theatlantic.com/technology/archive/2024/07/thrive-ai-health-huffington-altman-faith/678984/ | www.theatlantic.com | 2024-07-12T20:19:26Z | 0.4 | 0.55 | 0.2849 | 0.35 | 0.6 | 0.4327 |
| Show HN: Tinder but it's only pictures of my wife and I can only swipe right |  | trytender.app | 2025-07-24T04:33:13Z | 0.25 | 0.45 | 0.8014 | 0.35 | 0.6 | 0.4327 |
| Show HN: Tinder but it's only pictures of my wife and I can only swipe right | https://trytender.app/ | trytender.app | 2025-07-24T04:33:13Z | 0.25 | 0.45 | 0.8014 | 0.35 | 0.6 | 0.4327 |
| Show HN: Discover hand curated Future AI products from internet | https://inventlist.com | inventlist.com | 2023-03-20T11:03:34Z | 0.55 | 0.45 | 0.1 | 0.35 | 0.6 | 0.4325 |
| We Built a Language Model 14,000,000x Smaller Than GPT3 and Formally Verified It | https://github.com/dkypuros/atomic-lang-model | github.com | 2025-07-22T10:11:36Z | 0.25 | 0.45 | 0.7986 | 0.35 | 0.6 | 0.4323 |
| Notetime: Minimalistic notes where everything is timestamped | https://www.notetimeapp.com | www.notetimeapp.com | 2025-03-21T15:14:17Z | 0.25 | 0.55 | 0.6301 | 0.35 | 0.6 | 0.432 |
| Introducing Copilot+ PCs |  | blogs.microsoft.com | 2024-05-20T18:11:09Z | 0.25 | 0.8 | 0.2123 | 0.35 | 0.6 | 0.4318 |
| Introducing Copilot+ PCs | https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/ | blogs.microsoft.com | 2024-05-20T18:11:09Z | 0.25 | 0.8 | 0.2123 | 0.35 | 0.6 | 0.4318 |
| 5-week co-founder trial: 90% AI-coded app that coaches founders on The Mom Test | https://unpitched.app/?hn | unpitched.app | 2025-07-18T15:11:00Z | 0.25 | 0.45 | 0.7932 | 0.35 | 0.6 | 0.4315 |
| Crypto's Wild West Era Is Over |  | gizmodo.com | 2025-07-18T13:35:37Z | 0.25 | 0.45 | 0.7932 | 0.35 | 0.6 | 0.4315 |
| Crypto's Wild West Era Is Over | https://gizmodo.com/cryptos-wild-west-era-is-over-2000631148 | gizmodo.com | 2025-07-18T13:35:37Z | 0.25 | 0.45 | 0.7932 | 0.35 | 0.6 | 0.4315 |
| Anthropic tightens usage limits for Claude Code without telling users | https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/ | techcrunch.com | 2025-07-17T23:44:33Z | 0.25 | 0.45 | 0.7918 | 0.35 | 0.6 | 0.4313 |
| LLM Inevitabilism |  | tomrenner.com | 2025-07-17T11:01:56Z | 0.25 | 0.45 | 0.7918 | 0.35 | 0.6 | 0.4313 |
| LLM Inevitabilism | https://tomrenner.com/posts/llm-inevitabilism/ | tomrenner.com | 2025-07-17T11:01:56Z | 0.25 | 0.45 | 0.7918 | 0.35 | 0.6 | 0.4313 |
| Improvements to data analysis in ChatGPT |  | openai.com | 2024-05-17T02:26:41Z | 0.25 | 0.8 | 0.2068 | 0.35 | 0.6 | 0.431 |
| Improvements to data analysis in ChatGPT | https://openai.com/index/improvements-to-data-analysis-in-chatgpt/ | openai.com | 2024-05-17T02:26:41Z | 0.25 | 0.8 | 0.2068 | 0.35 | 0.6 | 0.431 |
| AI's $600B Question |  | www.sequoiacap.com | 2024-07-03T21:34:20Z | 0.4 | 0.55 | 0.2726 | 0.35 | 0.6 | 0.4309 |
| AI's $600B Question | https://www.sequoiacap.com/article/ais-600b-question/ | www.sequoiacap.com | 2024-07-03T21:34:20Z | 0.4 | 0.55 | 0.2726 | 0.35 | 0.6 | 0.4309 |
| Why I'm Feeling the AGI | https://www.nytimes.com/2025/03/14/technology/why-im-feeling-the-agi.html | www.nytimes.com | 2025-03-14T23:15:40Z | 0.25 | 0.55 | 0.6205 | 0.35 | 0.6 | 0.4306 |
| LLMs know more than they show: On the intrinsic representation of hallucinations | https://arxiv.org/abs/2410.02707 | arxiv.org | 2024-10-31T15:14:52Z | 0.4 | 0.45 | 0.437 | 0.35 | 0.6 | 0.4305 |
| Is Gemini 2.5 good at bounding boxes? | https://simedw.com/2025/07/10/gemini-bounding-boxes/ | simedw.com | 2025-07-10T15:58:33Z | 0.25 | 0.45 | 0.7822 | 0.35 | 0.6 | 0.4298 |
| Show HN: MCP server for searching and downloading documents from Anna's Archive | https://github.com/iosifache/annas-mcp | github.com | 2025-07-10T10:57:08Z | 0.25 | 0.45 | 0.7822 | 0.35 | 0.6 | 0.4298 |
| Botnet-style AI scraping tool known as Mellowtel promoted by Plasmo framework | https://twitter.com/thomasjamesio/status/1849899762876809465 | twitter.com | 2024-10-25T20:33:52Z | 0.4 | 0.45 | 0.4288 | 0.35 | 0.6 | 0.4293 |
| The DOJ still wants Google to sell off Chrome | https://www.wired.com/story/the-doj-still-wants-google-to-divest-chrome/ | www.wired.com | 2025-03-08T23:27:19Z | 0.25 | 0.55 | 0.6123 | 0.35 | 0.6 | 0.4293 |
| Can Large Language Models Play Text Games Well? | https://arxiv.org/abs/2304.02868 | arxiv.org | 2025-07-04T22:17:51Z | 0.25 | 0.45 | 0.774 | 0.35 | 0.6 | 0.4286 |
| Brand New Puff Counter App reached $1K in just a months. Here is the tips |  | apps.apple.com | 2025-03-04T11:15:30Z | 0.25 | 0.55 | 0.6068 | 0.35 | 0.6 | 0.4285 |
| Brand New Puff Counter App reached $1K in just a months. Here is the tips | https://apps.apple.com/tr/app/puff-counter-ai-track-vaping/id6740138374 | apps.apple.com | 2025-03-04T11:15:30Z | 0.25 | 0.55 | 0.6068 | 0.35 | 0.6 | 0.4285 |
| Albumentations: Licensing Change and Project Fork | https://albumentations.ai/blog/2025/01-albumentationsx-dual-licensing/ | albumentations.ai | 2025-07-03T08:43:50Z | 0.25 | 0.45 | 0.7726 | 0.35 | 0.6 | 0.4284 |
| Please don't mention AI again | https://ludic.mataroa.blog/blog/i-will-fucking-piledrive-you-if-you-mention-ai-again/ | ludic.mataroa.blog | 2024-06-20T04:12:23Z | 0.4 | 0.55 | 0.2548 | 0.35 | 0.6 | 0.4282 |
| Why is OpenAI buying Windsurf? | https://theahura.substack.com/p/tech-things-openai-buys-windsurf | theahura.substack.com | 2025-04-20T16:02:02Z | 0.25 | 0.55 | 0.6712 | 0.35 | 0.5 | 0.4282 |
| GPT-4.5: "Not a frontier model"? | https://www.interconnects.ai/p/gpt-45-not-a-frontier-model | www.interconnects.ai | 2025-03-02T20:16:09Z | 0.25 | 0.55 | 0.6041 | 0.35 | 0.6 | 0.4281 |
| Confirmationist and falsificationist paradigms of science (2014) | https://statmodeling.stat.columbia.edu/2014/09/05/confirmationist-falsificationist-paradigms-science/ | statmodeling.stat.columbia.edu | 2019-01-21T19:26:31Z | 0.25 | 0.85 | 0.1 | 0.35 | 0.6 | 0.4275 |
| Parrots learn to make video calls to chat with other parrots: study |  | news.northeastern.edu | 2023-12-01T22:54:58Z | 0.25 | 0.85 | 0.1 | 0.35 | 0.6 | 0.4275 |
| Parrots learn to make video calls to chat with other parrots: study | https://news.northeastern.edu/2023/04/21/parrots-talking-video-calls/ | news.northeastern.edu | 2023-12-01T22:54:58Z | 0.25 | 0.85 | 0.1 | 0.35 | 0.6 | 0.4275 |
| Why Did the Robot Do That? Increasing Trust in Autonomous Robots |  | insights.sei.cmu.edu | 2016-12-06T07:16:19Z | 0.25 | 0.85 | 0.1 | 0.35 | 0.6 | 0.4275 |
| Why Did the Robot Do That? Increasing Trust in Autonomous Robots | https://insights.sei.cmu.edu/sei_blog/2016/12/why-did-the-robot-do-that.html | insights.sei.cmu.edu | 2016-12-06T07:16:19Z | 0.25 | 0.85 | 0.1 | 0.35 | 0.6 | 0.4275 |
| Gemini CLI | https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/ | blog.google | 2025-06-25T15:54:12Z | 0.25 | 0.45 | 0.7616 | 0.35 | 0.6 | 0.4267 |
| The bitter lesson is coming for tokenization | https://lucalp.dev/bitter-lesson-tokenization-and-blt/ | lucalp.dev | 2025-06-25T14:28:40Z | 0.25 | 0.45 | 0.7616 | 0.35 | 0.6 | 0.4267 |
| LeetCode for System Design Interviews? |  | leetsys.dev | 2025-06-20T06:51:24Z | 0.25 | 0.45 | 0.7548 | 0.35 | 0.6 | 0.4257 |
| LeetCode for System Design Interviews? | https://leetsys.dev/ | leetsys.dev | 2025-06-20T06:51:24Z | 0.25 | 0.45 | 0.7548 | 0.35 | 0.6 | 0.4257 |
| The Generative AI Con | https://www.wheresyoured.at/longcon/ | www.wheresyoured.at | 2025-02-18T04:57:54Z | 0.25 | 0.55 | 0.5877 | 0.35 | 0.6 | 0.4257 |
| Extracting memorized pieces of books from open-weight language models | https://arxiv.org/abs/2505.12546 | arxiv.org | 2025-06-20T03:00:15Z | 0.25 | 0.45 | 0.7534 | 0.35 | 0.6 | 0.4255 |
| Who is using AI to code? Global diffusion and impact of generative AI | https://arxiv.org/abs/2506.08945 | arxiv.org | 2025-06-19T21:44:43Z | 0.25 | 0.45 | 0.7534 | 0.35 | 0.6 | 0.4255 |
| Project 2025 Observer | https://www.project2025.observer/ | www.project2025.observer | 2025-02-17T23:05:46Z | 0.25 | 0.55 | 0.5863 | 0.35 | 0.6 | 0.4254 |
| U.S. clears way for antitrust inquiries of Nvidia, Microsoft and OpenAI | https://www.nytimes.com/2024/06/05/technology/nvidia-microsoft-openai-antitrust-doj-ftc.html | www.nytimes.com | 2024-06-07T00:41:11Z | 0.4 | 0.55 | 0.2356 | 0.35 | 0.6 | 0.4253 |
| US eyes antitrust investigation against Nvidia as market value surpasses $3T |  | www.semafor.com | 2024-06-06T19:05:25Z | 0.4 | 0.55 | 0.2356 | 0.35 | 0.6 | 0.4253 |
| US eyes antitrust investigation against Nvidia as market value surpasses $3T | https://www.semafor.com/article/06/06/2024/us-government-doj-antitrust-nvidia-semiconductor-chips-artificial-intelligence | www.semafor.com | 2024-06-06T19:05:25Z | 0.4 | 0.55 | 0.2356 | 0.35 | 0.6 | 0.4253 |
| AudioGretel | https://audiogretel.com/ | audiogretel.com | 2025-06-17T13:16:01Z | 0.25 | 0.45 | 0.7507 | 0.35 | 0.6 | 0.4251 |
| FBI Raids Big Corporate Landlord over Nationwide Rent Hikes | https://www.thebignewsletter.com/p/monopoly-round-up-fbi-raids-big-corporate | www.thebignewsletter.com | 2024-06-05T17:46:00Z | 0.4 | 0.55 | 0.2342 | 0.35 | 0.6 | 0.4251 |
| Making 2.5 Flash and 2.5 Pro GA, and introducing Gemini 2.5 Flash-Lite | https://blog.google/products/gemini/gemini-2-5-model-family-expands/ | blog.google | 2025-06-17T20:31:15Z | 0.25 | 0.45 | 0.7507 | 0.35 | 0.6 | 0.4251 |
| Selfish reasons for building accessible UIs | https://nolanlawson.com/2025/06/16/selfish-reasons-for-building-accessible-uis/ | nolanlawson.com | 2025-06-17T12:24:43Z | 0.25 | 0.45 | 0.7507 | 0.35 | 0.6 | 0.4251 |
| Accumulation of cognitive debt when using an AI assistant for essay writing task | https://arxiv.org/abs/2506.08872 | arxiv.org | 2025-06-16T23:03:22Z | 0.25 | 0.45 | 0.7493 | 0.35 | 0.6 | 0.4249 |
| Show HN: The Internet is full of lies, so I built a Free Fact Checker | https://www.asksteve.to/free-fact-checker | www.asksteve.to | 2025-02-12T12:37:18Z | 0.25 | 0.55 | 0.5795 | 0.35 | 0.6 | 0.4244 |
| Self-Adapting Language Models | https://arxiv.org/abs/2506.10943 | arxiv.org | 2025-06-13T21:20:49Z | 0.25 | 0.45 | 0.7452 | 0.35 | 0.6 | 0.4243 |
| The AI Revolution Is Already Losing Steam | https://www.wsj.com/tech/ai/the-ai-revolution-is-already-losing-steam-a93478b1 | www.wsj.com | 2024-06-01T11:34:04Z | 0.4 | 0.55 | 0.2288 | 0.35 | 0.6 | 0.4243 |
| DeepScaleR: Surpassing O1-Preview with a 1.5B Model by Scaling RL | https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2 | pretty-radio-b75.notion.site | 2025-02-11T22:25:43Z | 0.25 | 0.55 | 0.5781 | 0.35 | 0.6 | 0.4242 |
| I built an open source AI tool to find my autoimmune disease | https://old.reddit.com/r/selfhosted/comments/1ij7s4m/how_i_built_an_open_source_ai_tool_to_find_my/ | old.reddit.com | 2025-02-10T13:33:29Z | 0.25 | 0.55 | 0.5767 | 0.35 | 0.6 | 0.424 |
| The librarian immediately attempts to sell you a vuvuzela | https://kaveland.no/posts/2025-06-06-library | kaveland.no | 2025-06-11T07:20:32Z | 0.25 | 0.45 | 0.7425 | 0.35 | 0.6 | 0.4239 |
| Hacker plants false memories in ChatGPT to steal user data in perpetuity | https://arstechnica.com/security/2024/09/false-memories-planted-in-chatgpt-give-hacker-persistent-exfiltration-channel/ | arstechnica.com | 2024-09-25T10:37:42Z | 0.4 | 0.45 | 0.3877 | 0.35 | 0.6 | 0.4232 |
| It's Now Officially Illegal to Use AI to Impersonate a Human Actor in Hollywood | https://futurism.com/the-byte/california-illegal-ai-impersonate-actor | futurism.com | 2024-09-24T10:25:00Z | 0.4 | 0.45 | 0.3863 | 0.35 | 0.6 | 0.4229 |
| TikTok's algorithm exhibited pro-Republican bias during 2024 presidential race | https://www.psypost.org/tiktoks-algorithm-exhibited-pro-republican-bias-during-2024-presidential-race-study-finds/ | www.psypost.org | 2025-02-04T18:28:36Z | 0.25 | 0.55 | 0.5685 | 0.35 | 0.6 | 0.4228 |
| Show HN: PodSnacks (Podcasts summarized with AI, to your inbox, $1 per hour) | https://www.podsnacks.org/ | www.podsnacks.org | 2024-05-24T12:29:43Z | 0.4 | 0.55 | 0.2178 | 0.35 | 0.6 | 0.4227 |
| Gemini-2.5-pro-preview-06-05 | https://deepmind.google/models/gemini/pro/ | deepmind.google | 2025-06-05T18:08:26Z | 0.25 | 0.45 | 0.7342 | 0.35 | 0.6 | 0.4226 |
| Mistral Code | https://mistral.ai/products/mistral-code | mistral.ai | 2025-06-04T20:44:31Z | 0.25 | 0.45 | 0.7329 | 0.35 | 0.6 | 0.4224 |
| Sal Khan is pioneering innovation in education again | https://www.gatesnotes.com/Brave-New-Words | www.gatesnotes.com | 2024-05-22T18:19:09Z | 0.4 | 0.55 | 0.2151 | 0.35 | 0.6 | 0.4223 |
| My AI skeptic friends are all nuts | https://fly.io/blog/youre-all-nuts/ | fly.io | 2025-06-03T22:16:02Z | 0.25 | 0.45 | 0.7315 | 0.35 | 0.6 | 0.4222 |
| Show HN: TalkNotes – A site that turns your ideas into tasks |  | www.talknotes.tech | 2025-02-01T22:51:52Z | 0.25 | 0.55 | 0.5644 | 0.35 | 0.6 | 0.4222 |
| Show HN: TalkNotes – A site that turns your ideas into tasks | https://www.talknotes.tech/ | www.talknotes.tech | 2025-02-01T22:51:52Z | 0.25 | 0.55 | 0.5644 | 0.35 | 0.6 | 0.4222 |
| OpenAI Threatening to Ban Users for Asking Strawberry About Its Reasoning |  | futurism.com | 2024-09-19T12:30:38Z | 0.4 | 0.45 | 0.3795 | 0.35 | 0.6 | 0.4219 |
| OpenAI Threatening to Ban Users for Asking Strawberry About Its Reasoning | https://futurism.com/the-byte/openai-ban-strawberry-reasoning | futurism.com | 2024-09-19T12:30:38Z | 0.4 | 0.45 | 0.3795 | 0.35 | 0.6 | 0.4219 |
| Exposed DeepSeek database leaking sensitive information, including chat history | https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak | www.wiz.io | 2025-01-29T23:01:24Z | 0.25 | 0.55 | 0.5603 | 0.35 | 0.6 | 0.4215 |
| Jevons paradox | https://en.wikipedia.org/wiki/Jevons_paradox | en.wikipedia.org | 2025-01-29T14:41:13Z | 0.25 | 0.55 | 0.5603 | 0.35 | 0.6 | 0.4215 |
| DeepSeek Has Been Inevitable and Here's Why (History Tells Us) | https://hardcoresoftware.learningbyshipping.com/p/228-deepseek-has-been-inevitable | hardcoresoftware.learningbyshipping.com | 2025-01-27T15:00:42Z | 0.25 | 0.55 | 0.5575 | 0.35 | 0.6 | 0.4211 |
| The Microsoft 365 Copilot launch was a disaster |  | www.zdnet.com | 2025-01-26T23:18:31Z | 0.25 | 0.55 | 0.5562 | 0.35 | 0.6 | 0.4209 |
| The Microsoft 365 Copilot launch was a disaster | https://www.zdnet.com/home-and-office/work-life/the-microsoft-365-copilot-launch-was-a-total-disaster/ | www.zdnet.com | 2025-01-26T23:18:31Z | 0.25 | 0.55 | 0.5562 | 0.35 | 0.6 | 0.4209 |
| GitHub MCP exploited: Accessing private repositories via MCP | https://invariantlabs.ai/blog/mcp-github-vulnerability | invariantlabs.ai | 2025-05-26T22:43:21Z | 0.25 | 0.45 | 0.7205 | 0.35 | 0.6 | 0.4206 |
| Claude 4 System Card | https://simonwillison.net/2025/May/25/claude-4-system-card/ | simonwillison.net | 2025-05-25T08:11:34Z | 0.25 | 0.45 | 0.7192 | 0.35 | 0.6 | 0.4204 |
| Open Source Society University – Path to a free self-taught education in CS | https://github.com/ossu/computer-science | github.com | 2025-05-25T23:36:25Z | 0.25 | 0.45 | 0.7192 | 0.35 | 0.6 | 0.4204 |
| A platform that lets people find the "best" of anything through community voting | https://www.bextora.com/ | www.bextora.com | 2025-01-23T04:14:17Z | 0.25 | 0.55 | 0.5521 | 0.35 | 0.6 | 0.4203 |
| DeepSeek and the Effects of GPU Export Controls |  | www.vincentschmalbach.com | 2025-01-23T13:38:23Z | 0.25 | 0.55 | 0.5521 | 0.35 | 0.6 | 0.4203 |
| DeepSeek and the Effects of GPU Export Controls | https://www.vincentschmalbach.com/deepseek-and-the-effects-of-gpu-export-controls/ | www.vincentschmalbach.com | 2025-01-23T13:38:23Z | 0.25 | 0.55 | 0.5521 | 0.35 | 0.6 | 0.4203 |
| AI Ruined Quora |  | jonn.substack.com | 2024-05-12T08:35:06Z | 0.4 | 0.55 | 0.2014 | 0.35 | 0.6 | 0.4202 |
| AI Ruined Quora | https://jonn.substack.com/p/how-ai-ruined-quora | jonn.substack.com | 2024-05-12T08:35:06Z | 0.4 | 0.55 | 0.2014 | 0.35 | 0.6 | 0.4202 |
| AI can't even fix a simple bug – but sure, let's fire engineers | https://nmn.gl/blog/ai-scam | nmn.gl | 2025-05-25T01:04:18Z | 0.25 | 0.45 | 0.7178 | 0.35 | 0.6 | 0.4202 |
| ChatGPT Is a Gimmick | https://hedgehogreview.com/web-features/thr/posts/chatgpt-is-a-gimmick | hedgehogreview.com | 2025-05-22T14:02:42Z | 0.25 | 0.45 | 0.7151 | 0.35 | 0.6 | 0.4198 |
| OpenAI plans to announce Google search competitor on Monday | https://www.reuters.com/technology/openai-plans-announce-google-search-competitor-monday-sources-say-2024-05-09/ | www.reuters.com | 2024-05-10T00:09:18Z | 0.4 | 0.55 | 0.1973 | 0.35 | 0.6 | 0.4196 |
| Can you read this cursive handwriting? The National Archives wants your help | https://www.smithsonianmag.com/smart-news/can-you-read-this-cursive-handwriting-the-national-archives-wants-your-help-180985833/ | www.smithsonianmag.com | 2025-01-18T07:56:54Z | 0.25 | 0.55 | 0.5452 | 0.35 | 0.6 | 0.4193 |
| AI Engineer Reading List | https://www.latent.space/p/2025-papers | www.latent.space | 2025-01-13T21:39:01Z | 0.25 | 0.55 | 0.5384 | 0.35 | 0.6 | 0.4183 |
| Vanished from Google/Bing/LinkedIn: a rebuttal of an anti-net neutrality paper | http://internetthought.blogspot.com/2025/01/vanished-from-index-of-google-bing-and.html | internetthought.blogspot.com | 2025-01-13T12:56:24Z | 0.25 | 0.55 | 0.5384 | 0.35 | 0.6 | 0.4183 |
| AI Is Like a Crappy Consultant | https://lukekanies.com/writing/ai-is-like-a-crappy-consultant/ | lukekanies.com | 2025-05-13T13:50:57Z | 0.25 | 0.45 | 0.7027 | 0.35 | 0.6 | 0.4179 |
| The world could run on older hardware if software optimization was a priority |  | twitter.com | 2025-05-13T13:47:17Z | 0.25 | 0.45 | 0.7027 | 0.35 | 0.6 | 0.4179 |
| The world could run on older hardware if software optimization was a priority | https://twitter.com/ID_AA_Carmack/status/1922100771392520710 | twitter.com | 2025-05-13T13:47:17Z | 0.25 | 0.45 | 0.7027 | 0.35 | 0.6 | 0.4179 |
| Y Combinator says Google is a monopolist, no comment about its OpenAI ties | https://techcrunch.com/2025/05/13/y-combinator-says-google-is-a-monopolist-that-has-stunted-the-startup-ecosystem/ | techcrunch.com | 2025-05-14T00:51:23Z | 0.25 | 0.45 | 0.7027 | 0.35 | 0.6 | 0.4179 |
| I Witnessed the Future of AI, and It's a Broken Toy | https://www.theatlantic.com/technology/archive/2024/04/rabbit-r1-impressions/678226/ | www.theatlantic.com | 2024-04-30T10:30:46Z | 0.4 | 0.55 | 0.1849 | 0.35 | 0.6 | 0.4177 |
| Claude's system prompt is over 24k tokens with tools | https://github.com/asgeirtj/system_prompts_leaks/blob/main/claude.txt | github.com | 2025-05-07T09:51:50Z | 0.25 | 0.45 | 0.6945 | 0.35 | 0.6 | 0.4167 |
| The curse of knowing how, or; fixing everything | https://notashelf.dev/posts/curse-of-knowing | notashelf.dev | 2025-05-06T10:47:18Z | 0.25 | 0.45 | 0.6932 | 0.35 | 0.6 | 0.4165 |
| The question that no LLM can answer and why it is important | https://www.mindprison.cc/p/the-question-that-no-llm-can-answer | www.mindprison.cc | 2024-04-24T21:21:03Z | 0.4 | 0.55 | 0.1767 | 0.35 | 0.6 | 0.4165 |
| Facebook users say 'amen' to bizarre AI-generated images of Jesus | https://www.nbcnews.com/tech/tech-news/facebook-users-say-amen-bizarre-ai-generated-images-jesus-rcna143965 | www.nbcnews.com | 2024-04-23T19:59:35Z | 0.4 | 0.55 | 0.1753 | 0.35 | 0.6 | 0.4163 |
| Show HN: Real-time AI Voice Chat at ~500ms Latency | https://github.com/KoljaB/RealtimeVoiceChat | github.com | 2025-05-05T22:56:56Z | 0.25 | 0.45 | 0.6918 | 0.35 | 0.6 | 0.4163 |
| I'm tired of fixing customers' AI generated code | https://medium.com/@thetateman/im-tired-of-fixing-customers-ai-generated-code-94816bde4ceb | medium.com | 2024-08-22T10:35:29Z | 0.4 | 0.45 | 0.3411 | 0.35 | 0.6 | 0.4162 |
| An appeal to companies doing AI | https://soatok.blog/2025/05/04/tech-companies-apparently-do-not-understand-why-we-dislike-ai/ | soatok.blog | 2025-05-05T00:22:25Z | 0.25 | 0.45 | 0.6904 | 0.35 | 0.6 | 0.4161 |
| Two publishers and three authors fail to understand what "vibe coding" means | https://simonwillison.net/2025/May/1/not-vibe-coding/ | simonwillison.net | 2025-05-02T13:39:21Z | 0.25 | 0.45 | 0.6877 | 0.35 | 0.6 | 0.4157 |
| Meta Llama 3 | https://llama.meta.com/llama3/ | llama.meta.com | 2024-04-18T18:24:22Z | 0.25 | 0.76 | 0.1685 | 0.35 | 0.6 | 0.4153 |
| ChatGPT Enterprise | https://openai.com/blog/introducing-chatgpt-enterprise | openai.com | 2023-08-28T19:02:44Z | 0.25 | 0.8 | 0.1 | 0.35 | 0.6 | 0.415 |
| ChatGPT Plugins |  | openai.com | 2023-03-23T18:30:06Z | 0.25 | 0.8 | 0.1 | 0.35 | 0.6 | 0.415 |
| ChatGPT Plugins | https://openai.com/blog/chatgpt-plugins | openai.com | 2023-03-23T18:30:06Z | 0.25 | 0.8 | 0.1 | 0.35 | 0.6 | 0.415 |
| Introducing ChatGPT and Whisper APIs | https://openai.com/blog/introducing-chatgpt-and-whisper-apis | openai.com | 2023-03-01T22:36:38Z | 0.25 | 0.8 | 0.1 | 0.35 | 0.6 | 0.415 |
| The GPT Store | https://openai.com/blog/introducing-the-gpt-store | openai.com | 2024-01-10T20:51:37Z | 0.25 | 0.8 | 0.1 | 0.35 | 0.6 | 0.415 |
| Presentation Slides with Markdown | https://sli.dev | sli.dev | 2025-04-28T17:36:55Z | 0.25 | 0.45 | 0.6822 | 0.35 | 0.6 | 0.4148 |
| Reverse geocoding is hard | https://shkspr.mobi/blog/2025/04/reverse-geocoding-is-hard/ | shkspr.mobi | 2025-04-27T17:42:48Z | 0.25 | 0.45 | 0.6808 | 0.35 | 0.6 | 0.4146 |
| My experience participating to a startup weekend competition in Italy |  | danielpetrica.com | 2025-04-24T11:11:50Z | 0.25 | 0.45 | 0.6767 | 0.35 | 0.6 | 0.414 |
| My experience participating to a startup weekend competition in Italy | https://danielpetrica.com/my-experience-of-participating-to-a-startup-weekend-competition-in-italy/ | danielpetrica.com | 2025-04-24T11:11:50Z | 0.25 | 0.45 | 0.6767 | 0.35 | 0.6 | 0.414 |
| GPT-5 is behind schedule | https://www.wsj.com/tech/ai/openai-gpt5-orion-delays-639e7693 | www.wsj.com | 2024-12-23T09:33:44Z | 0.25 | 0.55 | 0.5096 | 0.35 | 0.6 | 0.4139 |
| Show HN: LLM-aided OCR – Correcting Tesseract OCR errors with LLMs | https://github.com/Dicklesworthstone/llm_aided_ocr | github.com | 2024-08-11T15:16:31Z | 0.4 | 0.45 | 0.326 | 0.35 | 0.6 | 0.4139 |
| The Gruen Transfer is consuming the internet | https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet | sebs.website | 2025-04-23T16:15:55Z | 0.25 | 0.45 | 0.6753 | 0.35 | 0.6 | 0.4138 |
| Desktop Is Dead | https://rusz.space/posts/os?hn | rusz.space | 2025-04-22T09:47:49Z | 0.25 | 0.45 | 0.674 | 0.35 | 0.6 | 0.4136 |
| A Realistic AI Timeline | https://vintagedata.org/blog/posts/realistic-ai-timeline | vintagedata.org | 2025-04-18T20:28:01Z | 0.25 | 0.45 | 0.6685 | 0.35 | 0.6 | 0.4128 |
| I passionately hate hype, especially the AI hype | https://unixdigest.com/articles/i-passionately-hate-hype-especially-the-ai-hype.html | unixdigest.com | 2025-04-19T03:48:13Z | 0.25 | 0.45 | 0.6685 | 0.35 | 0.6 | 0.4128 |
| Stability AI reportedly ran out of cash to pay its cloud GPU bills | https://www.theregister.com/2024/04/03/stability_ai_bills/ | www.theregister.com | 2024-04-04T03:18:38Z | 0.4 | 0.55 | 0.1493 | 0.35 | 0.6 | 0.4124 |
| We're Raising Kids to Prefer AI over People–and No One's Noticing | https://substack.com/home/post/p-161454917 | substack.com | 2025-04-16T12:54:08Z | 0.25 | 0.45 | 0.6658 | 0.35 | 0.6 | 0.4124 |
| Character.ai CEO Noam Shazeer Returns to Google |  | techcrunch.com | 2024-08-02T19:32:47Z | 0.4 | 0.45 | 0.3137 | 0.35 | 0.6 | 0.4121 |
| Character.ai CEO Noam Shazeer Returns to Google | https://techcrunch.com/2024/08/02/character-ai-ceo-noam-shazeer-returns-to-google/ | techcrunch.com | 2024-08-02T19:32:47Z | 0.4 | 0.45 | 0.3137 | 0.35 | 0.6 | 0.4121 |
| We priced our AI SaaS product | https://www.commandbar.com/blog/ai-saas-pricing/ | www.commandbar.com | 2024-04-02T15:03:16Z | 0.4 | 0.55 | 0.1466 | 0.35 | 0.6 | 0.412 |
| Show HN: Crystal, the most accurate U.S. gov't data search tool | https://askcrystal.info/ | askcrystal.info | 2025-04-13T23:51:11Z | 0.25 | 0.45 | 0.6616 | 0.35 | 0.6 | 0.4117 |
| Chatbot hinted a kid should kill his parents over screen time limits: lawsuit |  | www.npr.org | 2024-12-12T00:03:09Z | 0.25 | 0.55 | 0.4932 | 0.35 | 0.6 | 0.4115 |
| Chatbot hinted a kid should kill his parents over screen time limits: lawsuit | https://www.npr.org/2024/12/10/nx-s1-5222574/kids-character-ai-lawsuit | www.npr.org | 2024-12-12T00:03:09Z | 0.25 | 0.55 | 0.4932 | 0.35 | 0.6 | 0.4115 |
| Proposed class-action lawsuit accuses companies of price-fixing rents in Canada | https://www.cbc.ca/news/business/rent-prices-canada-proposed-class-action-yieldstar-1.7405434 | www.cbc.ca | 2024-12-11T14:29:51Z | 0.25 | 0.55 | 0.4932 | 0.35 | 0.6 | 0.4115 |
| Vexa: Open-Source Transcription API for Product Builders | https://github.com/Vexa-ai/vexa | github.com | 2025-04-12T09:12:03Z | 0.25 | 0.45 | 0.6603 | 0.35 | 0.6 | 0.4115 |
| I'm tired of dismissive anti-AI bias | https://mattsayar.com/im-tired-of-dismissive-anti-ai-bias/ | mattsayar.com | 2025-04-11T22:32:35Z | 0.25 | 0.45 | 0.6589 | 0.35 | 0.6 | 0.4113 |
| Netlify's Free Plan | https://www.netlify.com/blog/introducing-netlify-free-plan/ | www.netlify.com | 2024-12-10T20:52:48Z | 0.25 | 0.55 | 0.4918 | 0.35 | 0.6 | 0.4113 |
| Investors are suddenly getting concerned that AI isn't making any serious money | https://futurism.com/investors-concerned-ai-making-money | futurism.com | 2024-07-29T14:12:10Z | 0.4 | 0.45 | 0.3082 | 0.35 | 0.6 | 0.4112 |
| Google's AI-powered search results are loaded with spammy, scammy garbage | https://www.theregister.com/2024/03/25/googles_aipowered_search_results_are/ | www.theregister.com | 2024-03-27T14:44:54Z | 0.4 | 0.55 | 0.1384 | 0.35 | 0.6 | 0.4108 |
| Kagi Teams | https://blog.kagi.com/kagi-teams | blog.kagi.com | 2024-12-06T14:01:12Z | 0.25 | 0.55 | 0.4863 | 0.35 | 0.6 | 0.4104 |
| Ask HN: Next Generation of Data Platform | https://drive.google.com/file/d/1LF7ZCfWoptQbqjYWiqzBBWU0_Rddi3yH/view?usp=sharing | drive.google.com | 2023-11-13T04:22:32Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| Building high-level features using large scale unsupervised learning |  | research.google.com | 2012-06-22T16:07:09Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| Building high-level features using large scale unsupervised learning | http://research.google.com/pubs/pub38115.html | research.google.com | 2012-06-22T16:07:09Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| Google is no longer bringing the full Chrome browser to Fuchsia |  | 9to5google.com | 2024-01-15T23:14:17Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| Google is no longer bringing the full Chrome browser to Fuchsia | https://9to5google.com/2024/01/15/google-is-no-longer-bringing-the-full-chrome-browser-to-fuchsia/ | 9to5google.com | 2024-01-15T23:14:17Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| How to Run Evolution Strategies on Google Kubernetes Engine | https://cloud.google.com/blog/products/ai-machine-learning/how-to-run-evolution-strategies-on-google-kubernetes-engine | cloud.google.com | 2019-06-18T00:40:38Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| Stanford CS Curriculum 2021 | https://docs.google.com/spreadsheets/d/1zfw8nPvJeewxcFUBpKUKmAVE8PjnJI7H0CKimdQXxr0/htmlview | docs.google.com | 2021-06-04T10:47:50Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| YouTube Begins Blocking Users Who Use Adblock | https://support.google.com/youtube/answer/14129599?hl=en | support.google.com | 2023-10-27T21:25:55Z | 0.25 | 0.78 | 0.1 | 0.35 | 0.6 | 0.41 |
| Founder-led Sales is Broken | https://www.founder-led.app/ | www.founder-led.app | 2025-01-21T21:38:19Z | 0.25 | 0.55 | 0.5493 | 0.35 | 0.5 | 0.4099 |
| Claim: Private GitHub repos included in AI dataset | https://post.lurk.org/@emenel/112111014479288871 | post.lurk.org | 2024-03-20T19:57:21Z | 0.4 | 0.55 | 0.1288 | 0.35 | 0.6 | 0.4093 |
| Show HN: Qwen-2.5-32B is now the best open source OCR model | https://github.com/getomni-ai/benchmark/blob/main/README.md | github.com | 2025-04-01T20:49:23Z | 0.25 | 0.45 | 0.6452 | 0.35 | 0.6 | 0.4093 |
| QwQ: Alibaba's O1-like reasoning LLM |  | qwenlm.github.io | 2024-11-29T16:37:41Z | 0.25 | 0.55 | 0.4767 | 0.35 | 0.6 | 0.409 |
| QwQ: Alibaba's O1-like reasoning LLM | https://qwenlm.github.io/blog/qwq-32b-preview/ | qwenlm.github.io | 2024-11-29T16:37:41Z | 0.25 | 0.55 | 0.4767 | 0.35 | 0.6 | 0.409 |
| Nvidia CEO Jensen Huang announces new AI chips: ‘We need bigger GPUs’ | https://www.cnbc.com/2024/03/18/nvidia-announces-gb200-blackwell-ai-chip-launching-later-this-year.html | www.cnbc.com | 2024-03-19T00:29:10Z | 0.4 | 0.55 | 0.126 | 0.35 | 0.6 | 0.4089 |
| Show HN: Self-hosted gateway to access LLMs, Ollama, ComfyUI and FFmpeg servers | https://openai.servicestack.net | openai.servicestack.net | 2024-11-28T16:39:29Z | 0.25 | 0.55 | 0.4753 | 0.35 | 0.6 | 0.4088 |
| Gemini 2.5 | https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/ | blog.google | 2025-03-26T00:20:19Z | 0.25 | 0.45 | 0.6356 | 0.35 | 0.6 | 0.4078 |
| Mark Zuckerberg has rebuilt Meta around Llama |  | finance.yahoo.com | 2024-11-20T02:47:52Z | 0.25 | 0.55 | 0.4644 | 0.35 | 0.6 | 0.4072 |
| El Capitan: New supercomputer is the fastest | https://spectrum.ieee.org/supercomputer-for-nukes | spectrum.ieee.org | 2024-11-20T01:01:22Z | 0.25 | 0.55 | 0.463 | 0.35 | 0.6 | 0.4069 |
| Mark Zuckerberg has rebuilt Meta around Llama | https://finance.yahoo.com/news/mark-zuckerberg-went-meta-major-103000635.html | finance.yahoo.com | 2024-11-20T02:47:52Z | 0.25 | 0.55 | 0.463 | 0.35 | 0.6 | 0.4069 |
| "AI, no ads please": 4 words to wipe out $1T | https://12challenges.substack.com/p/ai-no-ads-please-4-words-to-wipe | 12challenges.substack.com | 2024-03-07T17:27:12Z | 0.4 | 0.55 | 0.111 | 0.35 | 0.6 | 0.4066 |
| Fine-tune Google's Gemma 3 | https://unsloth.ai/blog/gemma3 | unsloth.ai | 2025-03-19T23:19:43Z | 0.25 | 0.45 | 0.6274 | 0.35 | 0.6 | 0.4066 |
| Show HN: SEO Flight Deck – AI-Powered Keyword Rank Tracking | https://www.seoflightdeck.com | www.seoflightdeck.com | 2024-03-07T15:32:54Z | 0.4 | 0.55 | 0.111 | 0.35 | 0.6 | 0.4066 |
| Docs – Open source alternative to Notion or Outline | https://github.com/suitenumerique/docs | github.com | 2025-03-16T18:46:34Z | 0.25 | 0.45 | 0.6233 | 0.35 | 0.6 | 0.406 |
| A look at Firefox forks | https://lwn.net/Articles/1012453/ | lwn.net | 2025-03-15T17:32:04Z | 0.25 | 0.45 | 0.6219 | 0.35 | 0.6 | 0.4058 |
| Owl – an open-source alternative to Manus AI with 11K+ stars, Top on GAIA OSS | https://github.com/camel-ai/owl | github.com | 2025-03-13T06:55:48Z | 0.25 | 0.45 | 0.6192 | 0.35 | 0.6 | 0.4054 |
| Gemini Robotics |  | deepmind.google | 2025-03-12T19:36:51Z | 0.25 | 0.45 | 0.6178 | 0.35 | 0.6 | 0.4052 |
| Gemini Robotics | https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/ | deepmind.google | 2025-03-12T19:36:51Z | 0.25 | 0.45 | 0.6178 | 0.35 | 0.6 | 0.4052 |
| Tell Mozilla: it's time to ditch Google | https://mozillapetition.com/ | mozillapetition.com | 2025-03-12T15:03:50Z | 0.25 | 0.45 | 0.6178 | 0.35 | 0.6 | 0.4052 |
| $95 AMD CPU Becomes 16GB GPU to Run AI Software | https://www.tomshardware.com/news/dollar95-amd-cpu-becomes-16gb-gpu-to-run-ai-software | www.tomshardware.com | 2023-10-31T18:14:05Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| A Leaked Memo from Google CEO Sundar Pichai Comes Amidst Employee Discontent |  | www.inc.com | 2024-01-25T04:49:29Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| A Leaked Memo from Google CEO Sundar Pichai Comes Amidst Employee Discontent | https://www.inc.com/nick-hobson/a-leaked-memo-from-google-ceo-sundar-pichai-comes-amidst-employee-discontent-no-ceo-wants-this-for-their-company.html | www.inc.com | 2024-01-25T04:49:29Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI Driven Drug Goes to Phase 1 Clinical Trials | https://www.prnewswire.com/in/news-releases/insilico-announces-successful-completion-of-phase-0-microdose-trial-and-initiates-phase-i-clinical-trial-for-its-first-ai-discovered-anti-fibrotic-product-candidate-with-novel-target-884919950.html | www.prnewswire.com | 2022-03-05T18:56:05Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI Likely to Price Products Higher, Without Regulatory Intervention | https://www.unite.ai/algorithmic-consumer-pricing-nber/ | www.unite.ai | 2021-05-31T13:52:23Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI and Trust | https://www.schneier.com/blog/archives/2023/12/ai-and-trust.html | www.schneier.com | 2023-12-04T18:38:09Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI beats human sleuth at finding problematic images in research papers | https://www.nature.com/articles/d41586-023-02920-y | www.nature.com | 2023-10-05T05:21:56Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI in physics: are we facing a scientific revolution? | https://www.4alltech.com/2020/07/ai-in-physics-are-we-facing-science.html | www.4alltech.com | 2020-07-21T14:47:38Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI is killing the grand bargain at the heart of the web | https://www.businessinsider.com/ai-killing-web-grand-bargain-2023-8 | www.businessinsider.com | 2023-08-30T14:58:42Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI is upending the freelance world | https://www.forbes.com/sites/rashishrivastava/2023/04/20/ive-never-hired-a-writer-better-than-chatgpt-how-ai-is-upending-the-freelance-world/ | www.forbes.com | 2023-04-22T22:59:49Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI needs so much power that old coal plants are sticking around | https://www.bloomberg.com/news/articles/2024-01-25/ai-needs-so-much-power-that-old-coal-plants-are-sticking-around | www.bloomberg.com | 2024-02-12T23:19:46Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI tools like ChatGPT are built on mass copyright infringement | https://www.theglobeandmail.com/opinion/article-ai-programs-like-chatgpt-are-built-on-mass-copyright-infringement/ | www.theglobeandmail.com | 2023-05-26T21:47:11Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI will save the world? | https://pmarca.substack.com/p/why-ai-will-save-the-world | pmarca.substack.com | 2023-06-07T01:50:59Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI’s biggest risk is the corporations that control them |  | www.fastcompany.com | 2023-05-06T16:22:20Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| AI’s biggest risk is the corporations that control them | https://www.fastcompany.com/90892235/researcher-meredith-whittaker-says-ais-biggest-risk-isnt-consciousness-its-the-corporations-that-control-them | www.fastcompany.com | 2023-05-06T16:22:20Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Adobe will charge “credits” for generative AI | https://helpx.adobe.com/firefly/using/generative-credits-faq.html | helpx.adobe.com | 2023-09-16T21:48:45Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Be My Eyes’ AI assistant starts rolling out | https://www.bemyeyes.com/blog/announcing-be-my-ai | www.bemyeyes.com | 2023-09-27T14:19:09Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Builder.ai and the Air India website: What’s going on? | https://www.businesstoday.in/technology/news/story/builderai-and-the-air-india-website-whats-going-on-323144-2022-02-18 | www.businesstoday.in | 2022-02-19T19:37:19Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Cameras that understand: portrait mode and Google Lens | https://www.ben-evans.com/benedictevans/2019/2/5/cameras-that-understand | www.ben-evans.com | 2019-02-06T23:50:58Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| ChatGPT-3: Google Says AI Generated Contents Are Against Webmaster Guidelines | https://www.steadipulse.com/2023/02/chatgpt-3-vs-google-webmaster-guidelines.html | www.steadipulse.com | 2023-02-18T17:19:49Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Christie’s sells its first AI portrait for $432k | https://www.theverge.com/2018/10/25/18023266/ai-art-portrait-christies-obvious-sold | www.theverge.com | 2018-10-25T19:50:38Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Code Llama, a state-of-the-art large language model for coding |  | ai.meta.com | 2023-08-24T18:26:48Z | 0.25 | 0.76 | 0.1 | 0.35 | 0.6 | 0.405 |
| Code Llama, a state-of-the-art large language model for coding | https://ai.meta.com/blog/code-llama-large-language-model-coding/ | ai.meta.com | 2023-08-24T18:26:48Z | 0.25 | 0.76 | 0.1 | 0.35 | 0.6 | 0.405 |
| Complaints mount after GitHub launches new algorithmic feed | https://www.theregister.com/2022/03/23/github_for_you/ | www.theregister.com | 2022-03-24T12:06:20Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Database of artists used to train Midjourney AI garners criticism | https://www.artnews.com/art-news/news/midjourney-ai-artists-database-1234691955/ | www.artnews.com | 2024-01-08T04:36:24Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| DuckDuckGo’s building AI-generated answers into its search engine | https://www.theverge.com/2023/3/8/23629095/duckduckgo-ai-answers-browser-app-extension-search | www.theverge.com | 2023-04-17T16:28:16Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Duolingo Cuts 10% of Contractors as It Uses More AI to Create App Content | https://www.bloomberg.com/news/articles/2024-01-08/duolingo-cuts-10-of-contractors-in-move-to-greater-use-of-ai | www.bloomberg.com | 2024-01-08T22:06:12Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| EPO and UKIPO Refuse AI-Invented Patent Applications | https://www.ipwatchdog.com/2020/01/07/epo-ukipo-refuse-ai-invented-patent-applications/id=117648/ | www.ipwatchdog.com | 2020-01-08T15:42:53Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| EU urged to protect grassroots AI research or risk losing out to US | https://www.theguardian.com/technology/2023/may/04/eu-urged-to-protect-grassroots-ai-research-or-risk-losing-out-to-us | www.theguardian.com | 2023-05-04T17:34:28Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Every app that adds AI looks like this |  | botharetrue.substack.com | 2023-10-13T15:38:57Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Every app that adds AI looks like this | https://botharetrue.substack.com/p/every-app-that-adds-ai-looks-like | botharetrue.substack.com | 2023-10-13T15:38:57Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Everything I wish I had known about raising a seed round | https://mdwdotla.medium.com/everything-i-wish-i-had-known-about-raising-a-seed-round-a615f8f7740b | mdwdotla.medium.com | 2022-10-13T16:23:56Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| First AI Content Marketer |  | www.getmax.ai | 2023-09-06T10:21:02Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| First AI Content Marketer | https://www.getmax.ai/ | www.getmax.ai | 2023-09-06T10:21:02Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| For chemists, the AI revolution has yet to happen | https://www.nature.com/articles/d41586-023-01612-x | www.nature.com | 2023-05-22T03:21:30Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Generative AI space and the mental imagery of alien minds |  | writings.stephenwolfram.com | 2023-07-18T21:13:05Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Generative AI space and the mental imagery of alien minds | https://writings.stephenwolfram.com/2023/07/generative-ai-space-and-the-mental-imagery-of-alien-minds/ | writings.stephenwolfram.com | 2023-07-18T21:13:05Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Google AI Research Manager Quits After Two Ousted from Group | https://www.bloomberg.com/news/articles/2021-04-06/google-ai-research-manager-samy-bengio-resigns-in-email-to-staff | www.bloomberg.com | 2021-04-07T17:12:26Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Google Gemini Pro API Available Through AI Studio | https://ai.google.dev/ | ai.google.dev | 2023-12-13T17:48:21Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Google staff rally behind fired AI researcher |  | www.bbc.com | 2020-12-04T19:10:46Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Google staff rally behind fired AI researcher | https://www.bbc.com/news/technology-55187611 | www.bbc.com | 2020-12-04T19:10:46Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Google wants governments to form a 'global AI corps' | https://www.washingtonpost.com/politics/2023/11/14/google-wants-governments-form-global-ai-corps/ | www.washingtonpost.com | 2023-11-15T03:29:40Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Google “We have no moat, and neither does OpenAI” | https://www.semianalysis.com/p/google-we-have-no-moat-and-neither | www.semianalysis.com | 2023-05-05T08:51:42Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| High Salaries Are Weapons in the AI Talent War |  | www.bloomberg.com | 2018-02-13T16:31:28Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| High Salaries Are Weapons in the AI Talent War | https://www.bloomberg.com/news/articles/2018-02-13/in-the-war-for-ai-talent-sky-high-salaries-are-the-weapons | www.bloomberg.com | 2018-02-13T16:31:28Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| I Used AI Tools to Create a Promo Video for My Startup, Styrate | https://www.youtube.com/watch?v=U0SIBw0MtyI | www.youtube.com | 2023-06-17T16:04:10Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Indian IT consultancies struggle against technological obsolescence |  | www.economist.com | 2020-07-24T17:46:15Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Indian IT consultancies struggle against technological obsolescence | https://www.economist.com/business/2020/07/23/indian-it-consultancies-struggle-against-technological-obsolescence | www.economist.com | 2020-07-24T17:46:15Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Jamie: AI assistant that creates meeting summaries | https://www.meetjamie.ai/ | www.meetjamie.ai | 2023-02-01T20:20:23Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| JetBrains forces AI freemium plugin that cannot be completely removed into IDEs | https://youtrack.jetbrains.com/issue/LLM-1760/Can-not-remove-Jetbrains-AI-Assistant-plugin-completely | youtrack.jetbrains.com | 2023-12-19T20:34:00Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| JetBrains' unremovable AI assistant meets irresistible outcry | https://www.theregister.com/2024/02/01/jetbrains_unremovable_ai_assistant/ | www.theregister.com | 2024-02-03T15:07:18Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Junk websites filled w AI-generated text pulling in money from programmatic ads | https://www.technologyreview.com/2023/06/26/1075504/junk-websites-filled-with-ai-generated-text-are-pulling-in-money-from-programmatic-ads/ | www.technologyreview.com | 2023-06-29T13:34:22Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| LangChain: The Missing Manual | https://www.pinecone.io/learn/langchain/ | www.pinecone.io | 2023-05-19T16:50:44Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Legal AI and the Industrialisation of Cognition (2017) | https://www.artificiallawyer.com/2018/08/03/summer-re-post-legal-ai-the-industrialisation-of-cognition/ | www.artificiallawyer.com | 2018-08-04T13:46:06Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Lessons from YC AI Startups | https://www.ignorance.ai/p/5-lessons-from-139-yc-ai-startups | www.ignorance.ai | 2023-09-13T14:37:43Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Limewire is making a comeback using GenAI and Blockchain |  | www.origo.ec | 2024-01-12T00:43:25Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Limewire is making a comeback using GenAI and Blockchain | https://www.origo.ec/2024/01/11/limewire-reimagined-powering-the-future-of-content-with-ai-and-blockchain/ | www.origo.ec | 2024-01-12T00:43:25Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Llama 2 | https://ai.meta.com/llama/ | ai.meta.com | 2023-07-19T05:07:27Z | 0.25 | 0.76 | 0.1 | 0.35 | 0.6 | 0.405 |
| Massive MRI dataset released as part of ongoing AI project |  | www.radiologybusiness.com | 2018-11-28T03:58:47Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Massive MRI dataset released as part of ongoing AI project | https://www.radiologybusiness.com/topics/artificial-intelligence/nyu-facebook-release-knee-mri-dataset-ai | www.radiologybusiness.com | 2018-11-28T03:58:47Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Meta's plan to offer free commercial AI models puts pressure on Google, OpenAI |  | www.artisana.ai | 2023-06-16T19:27:28Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Meta's plan to offer free commercial AI models puts pressure on Google, OpenAI | https://www.artisana.ai/articles/metas-plan-to-offer-free-commercial-ai-models-puts-pressure-on-google-and | www.artisana.ai | 2023-06-16T19:27:28Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Microsoft AI-powered Office assistant is here– if you've got $9k and 300 friends | https://www.theverge.com/2023/11/1/23942155/microsoft-365-copilot-ai-office-documents-launch-business-enterprise-pricing-release-date | www.theverge.com | 2023-11-01T19:25:38Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Microsoft strikes deal with Mistral in push beyond OpenAI |  | www.ft.com | 2024-02-26T17:14:36Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Microsoft strikes deal with Mistral in push beyond OpenAI | https://www.ft.com/content/cd6eb51a-3276-450f-87fd-97e8410db9eb | www.ft.com | 2024-02-26T17:14:36Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Microsoft warns of service disruptions if can’t get enough AI chips for its DCs | https://www.cnbc.com/2023/07/28/microsoft-annual-report-highlights-importance-of-gpus.html | www.cnbc.com | 2023-07-29T01:07:26Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Mistral AI Valued at $2B | https://www.unite.ai/paris-based-startup-and-openai-competitor-mistral-ai-valued-at-2-billion/ | www.unite.ai | 2023-12-11T17:57:54Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Mistral: The 9-Month-Old AI Startup Challenging Silicon Valley's Giants |  | www.wsj.com | 2024-02-28T10:19:55Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Mistral: The 9-Month-Old AI Startup Challenging Silicon Valley's Giants | https://www.wsj.com/tech/ai/the-9-month-old-ai-startup-challenging-silicon-valleys-giants-ee2e4c48 | www.wsj.com | 2024-02-28T10:19:55Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Mozilla.ai: Investing in Trustworthy AI |  | blog.mozilla.org | 2023-03-22T12:59:41Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Mozilla.ai: Investing in Trustworthy AI | https://blog.mozilla.org/en/mozilla/introducing-mozilla-ai-investing-in-trustworthy-ai/ | blog.mozilla.org | 2023-03-22T12:59:41Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Netflix Japan announced that it used AI-generated art in a new short anime film |  | www.creativebloq.com | 2023-02-04T20:19:41Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Netflix Japan announced that it used AI-generated art in a new short anime film | https://www.creativebloq.com/news/ai-anime-labour-shortage | www.creativebloq.com | 2023-02-04T20:19:41Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| New data poisoning tool lets artists fight back against generative AI |  | www.technologyreview.com | 2023-10-25T14:52:35Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| New data poisoning tool lets artists fight back against generative AI | https://www.technologyreview.com/2023/10/23/1082189/data-poisoning-artists-fight-generative-ai/ | www.technologyreview.com | 2023-10-25T14:52:35Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Not even Notepad is safe from Microsoft's big AI push in Windows | https://www.theverge.com/2024/1/9/24032117/microsoft-windows-notepad-generative-ai-option | www.theverge.com | 2024-01-10T03:26:15Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Notion AI | https://www.notion.so/product/ai | www.notion.so | 2022-12-27T19:53:13Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Nvidia's "Grace" Arm CPU holds its own against x86 for HPC | https://www.nextplatform.com/2024/02/06/nvidias-grace-arm-cpu-holds-its-own-against-x86-for-hpc/ | www.nextplatform.com | 2024-02-09T17:12:56Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI delays launch of custom GPT store until early 2024 | https://www.axios.com/2023/12/01/openai-delays-launch-custom-gpt-store-2024 | www.axios.com | 2023-12-01T23:15:24Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI is now everything it promised not to be: closed-source and for-profit |  | www.vice.com | 2023-03-01T10:24:13Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI is now everything it promised not to be: closed-source and for-profit | https://www.vice.com/en/article/5d3naz/openai-is-now-everything-it-promised-not-to-be-corporate-closed-source-and-for-profit | www.vice.com | 2023-03-01T10:24:13Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI is too cheap to beat | https://generatingconversation.substack.com/p/openai-is-too-cheap-to-beat | generatingconversation.substack.com | 2023-10-13T07:43:13Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI tech gives Microsoft's Bing a boost in search battle with Google |  | www.reuters.com | 2023-03-24T20:24:58Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI tech gives Microsoft's Bing a boost in search battle with Google | https://www.reuters.com/technology/openai-tech-gives-microsofts-bing-boost-search-battle-with-google-2023-03-22/ | www.reuters.com | 2023-03-24T20:24:58Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI's plans according to Sam Altman |  | web.archive.org | 2023-06-06T17:52:31Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI's plans according to Sam Altman | https://web.archive.org/web/20230601000258/https://website-nm4keew22-humanloopml.vercel.app/blog/openai-plans | web.archive.org | 2023-06-06T17:52:31Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI’s Sam Altman Shares Insight into Future Plans and Challenges |  | www.news.upveda.in | 2023-06-03T17:29:13Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| OpenAI’s Sam Altman Shares Insight into Future Plans and Challenges | https://www.news.upveda.in/2023/06/03/openais-sam-altman-shares-insight-into-future-plans-and-challenges/ | www.news.upveda.in | 2023-06-03T17:29:13Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Podcast editor Descript adds new pro tier with access to AI voice double feature | https://www.theverge.com/2020/7/28/21345063/descript-pro-ai-overdub-podcast-editor-subscription-service-features-pricing | www.theverge.com | 2020-07-28T18:02:04Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Public web unravels in AI-driven storm |  | www.axios.com | 2023-07-06T00:02:56Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Public web unravels in AI-driven storm | https://www.axios.com/2023/07/05/public-web-twitter-open-access-reddit | www.axios.com | 2023-07-06T00:02:56Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Rewind.ai now has a free plan | https://www.rewind.ai/pricing | www.rewind.ai | 2023-09-02T15:51:41Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Role-playing with AI will be a powerful tool for writers and educators |  | resobscura.substack.com | 2023-12-13T01:37:35Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Role-playing with AI will be a powerful tool for writers and educators | https://resobscura.substack.com/p/roleplaying-with-ai-will-be-powerful-tool | resobscura.substack.com | 2023-12-13T01:37:35Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Searchable Database of the 183,000 Pirated Books Meta, et al., Used to Train AI | https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/ | www.theatlantic.com | 2023-09-28T13:52:57Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Show HN: Artificial Intelligence Based Drug Discovery Toolkit | https://www.producthunt.com/r/2886430edfe4f7 | www.producthunt.com | 2019-06-28T06:46:27Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Show HN: Sports gaming bot making it rain Amazon gift cards | http://www.playsweep.com | www.playsweep.com | 2018-03-14T16:37:59Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The Humane AI Pin Launches Its Campaign to Replace Phones |  | www.bloomberg.com | 2023-11-09T18:31:36Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The Humane AI Pin Launches Its Campaign to Replace Phones | https://www.bloomberg.com/news/articles/2023-11-09/the-humane-ai-pin-launches-its-campaign-to-replaces-phones | www.bloomberg.com | 2023-11-09T18:31:36Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The New York Times is suing OpenAI and Microsoft for copyright infringement | https://www.theverge.com/2023/12/27/24016212/new-york-times-openai-microsoft-lawsuit-copyright-infringement | www.theverge.com | 2023-12-27T16:22:08Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The Rise of Generative AI and the Coming Era of Social Media Manipulation |  | www.rand.org | 2023-09-08T03:53:14Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The Rise of Generative AI and the Coming Era of Social Media Manipulation | https://www.rand.org/pubs/perspectives/PEA2679-1.html | www.rand.org | 2023-09-08T03:53:14Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The Rise of the AI Engineer |  | www.latent.space | 2023-07-01T17:06:57Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The Rise of the AI Engineer | https://www.latent.space/p/ai-engineer | www.latent.space | 2023-07-01T17:06:57Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The auction that set off the race for AI supremacy | https://www.wired.com/story/secret-auction-race-ai-supremacy-google-microsoft-baidu/ | www.wired.com | 2021-03-17T03:53:04Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| The industries AI is disrupting are not lucrative | https://www.theintrinsicperspective.com/p/excuse-me-but-the-industries-ai-is | www.theintrinsicperspective.com | 2023-12-09T07:19:06Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Things are about to get worse for generative AI | https://garymarcus.substack.com/p/things-are-about-to-get-a-lot-worse | garymarcus.substack.com | 2023-12-30T20:09:54Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Together AI raises a $102.5M Series A | https://www.together.ai/blog/series-a | www.together.ai | 2023-11-29T18:36:09Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| U.S. Files Criminal Charges Against Theranos’s Elizabeth Holmes, Ramesh Balwani |  | www.wsj.com | 2018-06-16T03:40:12Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| U.S. Files Criminal Charges Against Theranos’s Elizabeth Holmes, Ramesh Balwani | https://www.wsj.com/articles/u-s-files-criminal-charges-against-theranoss-elizabeth-holmes-ramesh-balwani-1529096005 | www.wsj.com | 2018-06-16T03:40:12Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| VP of Engineering Opening (Help us make the leap from A/B to AI) |  | www.offerfit.ai | 2022-10-01T13:50:18Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| VP of Engineering Opening (Help us make the leap from A/B to AI) | https://www.offerfit.ai/job-application | www.offerfit.ai | 2022-10-01T13:50:18Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| What are the best ways of evaluating LLMs for specific use-cases? | https://blog.lastmileai.dev/evaluating-the-performance-of-retrieval-augmented-llm-systems-d95122feb0dd | blog.lastmileai.dev | 2023-06-30T17:45:12Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| Workers AI Update: Stable Diffusion, Code Llama and Workers AI in 100 Cities | https://blog.cloudflare.com/workers-ai-update-stable-diffusion-code-llama-workers-ai-in-100-cities/ | blog.cloudflare.com | 2023-11-23T16:45:47Z | 0.4 | 0.55 | 0.1 | 0.35 | 0.6 | 0.405 |
| DOJ: Google must sell Chrome, Android could be next |  | arstechnica.com | 2025-03-10T18:31:45Z | 0.25 | 0.45 | 0.6151 | 0.35 | 0.6 | 0.4048 |
| DOJ: Google must sell Chrome, Android could be next | https://arstechnica.com/google/2025/03/doj-google-must-sell-chrome-android-could-be-next/ | arstechnica.com | 2025-03-10T18:31:45Z | 0.25 | 0.45 | 0.6151 | 0.35 | 0.6 | 0.4048 |
| OSS voice AI stack – <500ms latency, <5¢/min, interruption, ack, guardrails | https://github.com/bolna-ai/bolna/tree/master/examples | github.com | 2024-06-25T14:02:09Z | 0.4 | 0.45 | 0.2616 | 0.35 | 0.6 | 0.4042 |
| Go-attention: A full attention mechanism and transformer in pure Go | https://github.com/takara-ai/go-attention | github.com | 2025-03-04T07:30:37Z | 0.25 | 0.45 | 0.6068 | 0.35 | 0.6 | 0.4035 |
| The A.I. Monarchy |  | substack.com | 2025-03-02T13:39:25Z | 0.25 | 0.45 | 0.6041 | 0.35 | 0.6 | 0.4031 |
| The A.I. Monarchy | https://substack.com/home/post/p-156886169 | substack.com | 2025-03-02T13:39:25Z | 0.25 | 0.45 | 0.6041 | 0.35 | 0.6 | 0.4031 |
| Vibe Coding and the Future of Software Engineering | https://alexp.pl/2025/02/19/vibe-coding.html | alexp.pl | 2025-03-01T00:51:19Z | 0.25 | 0.45 | 0.6014 | 0.35 | 0.6 | 0.4027 |
| macOS Tips and Tricks (2022) |  | saurabhs.org | 2025-02-28T07:28:49Z | 0.25 | 0.45 | 0.6014 | 0.35 | 0.6 | 0.4027 |
| macOS Tips and Tricks (2022) | https://saurabhs.org/macos-tips | saurabhs.org | 2025-02-28T07:28:49Z | 0.25 | 0.45 | 0.6014 | 0.35 | 0.6 | 0.4027 |
| Big Tech's underground race to buy AI training data | https://www.reuters.com/technology/inside-big-techs-underground-race-buy-ai-training-data-2024-04-05/ | www.reuters.com | 2024-04-05T17:39:07Z | 0.4 | 0.55 | 0.1507 | 0.35 | 0.5 | 0.4026 |
| YouTube tests removing viewer counts | https://www.tomsguide.com/computing/software/youtube-tests-removing-viewer-counts-heres-what-we-know | www.tomsguide.com | 2024-10-29T20:33:24Z | 0.25 | 0.55 | 0.4342 | 0.35 | 0.6 | 0.4026 |
| Y Combinator deletes posts after a startup's demo goes viral | https://techcrunch.com/2025/02/25/y-combinator-deletes-posts-after-a-startups-demo-goes-viral/ | techcrunch.com | 2025-02-27T04:13:52Z | 0.25 | 0.45 | 0.6 | 0.35 | 0.6 | 0.4025 |
| Grok3 Launch [video] | https://x.com/xai/status/1891699715298730482 | x.com | 2025-02-18T13:30:39Z | 0.25 | 0.45 | 0.5877 | 0.35 | 0.6 | 0.4007 |
| Mistral Saba | https://mistral.ai/en/news/mistral-saba | mistral.ai | 2025-02-17T18:16:46Z | 0.25 | 0.45 | 0.5863 | 0.35 | 0.6 | 0.4004 |
| TL;DW: Too Long; Didn't Watch Distill YouTube Videos to the Relevant Information | https://tldw.tube/ | tldw.tube | 2025-02-15T16:36:59Z | 0.25 | 0.45 | 0.5836 | 0.35 | 0.6 | 0.4 |
| We were wrong about GPUs |  | fly.io | 2025-02-15T09:38:04Z | 0.25 | 0.45 | 0.5836 | 0.35 | 0.6 | 0.4 |
| We were wrong about GPUs | https://fly.io/blog/wrong-about-gpu/ | fly.io | 2025-02-15T09:38:04Z | 0.25 | 0.45 | 0.5836 | 0.35 | 0.6 | 0.4 |
| Large language models reduce public knowledge sharing on online Q&A platforms |  | academic.oup.com | 2024-10-13T15:24:28Z | 0.25 | 0.55 | 0.4123 | 0.35 | 0.6 | 0.3993 |
| Large language models reduce public knowledge sharing on online Q&A platforms | https://academic.oup.com/pnasnexus/article/3/9/pgae400/7754871 | academic.oup.com | 2024-10-13T15:24:28Z | 0.25 | 0.55 | 0.4123 | 0.35 | 0.6 | 0.3993 |
| Why blog if nobody reads it? | https://andysblog.uk/why-blog-if-nobody-reads-it/ | andysblog.uk | 2025-02-10T07:31:32Z | 0.25 | 0.45 | 0.5767 | 0.35 | 0.6 | 0.399 |
| What do I mean by some software devs are "ngmi"? | https://ghuntley.com/ngmi/ | ghuntley.com | 2025-02-09T14:48:35Z | 0.25 | 0.45 | 0.5753 | 0.35 | 0.6 | 0.3988 |
| xAI announces series B funding round of $6B | https://x.ai/blog/series-b | x.ai | 2024-05-27T07:14:27Z | 0.4 | 0.45 | 0.2219 | 0.35 | 0.6 | 0.3983 |
| AI tools for software engineers, but without the hype – with Simon Willison [video] | https://www.youtube.com/watch?v=uRuLgar5XZw | www.youtube.com | 2024-10-07T15:28:30Z | 0.25 | 0.55 | 0.4041 | 0.35 | 0.6 | 0.3981 |
| Gemini 1.5 Flash-8B is now production ready | https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/ | developers.googleblog.com | 2024-10-04T08:50:40Z | 0.25 | 0.55 | 0.4 | 0.35 | 0.6 | 0.3975 |
| What Kind of Writer Is ChatGPT? | https://www.newyorker.com/culture/annals-of-inquiry/what-kind-of-writer-is-chatgpt | www.newyorker.com | 2024-10-03T22:21:03Z | 0.25 | 0.55 | 0.3986 | 0.35 | 0.6 | 0.3973 |
| You Can't Opt-Out of A.I. Online |  | www.newyorker.com | 2024-10-03T22:20:32Z | 0.25 | 0.55 | 0.3986 | 0.35 | 0.6 | 0.3973 |
| You Can't Opt-Out of A.I. Online | https://www.newyorker.com/culture/infinite-scroll/how-to-opt-out-of-ai-online | www.newyorker.com | 2024-10-03T22:20:32Z | 0.25 | 0.55 | 0.3986 | 0.35 | 0.6 | 0.3973 |
| Building an AI game studio: what we've learned so far | https://braindump.me/blog-posts/building-an-ai-game-studio | braindump.me | 2024-05-21T13:43:11Z | 0.4 | 0.45 | 0.2137 | 0.35 | 0.6 | 0.3971 |
| Bypass DeepSeek censorship by speaking in hex | https://substack.com/home/post/p-156004330 | substack.com | 2025-01-31T21:54:00Z | 0.25 | 0.45 | 0.563 | 0.35 | 0.6 | 0.3969 |
| DeepSeek releases Janus Pro, a text-to-image generator [pdf] | https://github.com/deepseek-ai/Janus/blob/main/janus_pro_tech_report.pdf | github.com | 2025-01-27T18:09:35Z | 0.25 | 0.45 | 0.5575 | 0.35 | 0.6 | 0.3961 |
| PhysicsForums and the Dead Internet Theory | https://hallofdreams.org/posts/physicsforums/ | hallofdreams.org | 2025-01-24T20:48:44Z | 0.25 | 0.45 | 0.5534 | 0.35 | 0.6 | 0.3955 |
| Show HN: Oodle – serverless, fully-managed, drop-in replacement for Prometheus | https://blog.oodle.ai/building-a-high-performance-low-cost-metrics-observability-system/ | blog.oodle.ai | 2024-09-24T17:51:30Z | 0.25 | 0.55 | 0.3863 | 0.35 | 0.6 | 0.3954 |
| Has LLM killed traditional NLP? | https://medium.com/altitudehq/is-traditional-nlp-dead-05544ae7d756 | medium.com | 2025-01-18T19:19:15Z | 0.25 | 0.45 | 0.5452 | 0.35 | 0.6 | 0.3943 |
| Hezbollah pager explosions kill several people in Lebanon | https://www.reuters.com/world/middle-east/dozens-hezbollah-members-wounded-lebanon-when-pagers-exploded-sources-witnesses-2024-09-17/ | www.reuters.com | 2024-09-18T10:48:00Z | 0.25 | 0.55 | 0.3781 | 0.35 | 0.6 | 0.3942 |
| Show HN: LangCSS – An AI Assistant for Tailwind | https://langcss.com/ | langcss.com | 2024-04-24T22:39:10Z | 0.4 | 0.45 | 0.1767 | 0.35 | 0.6 | 0.3915 |
| Thefastest.ai | https://thefastest.ai | thefastest.ai | 2024-04-24T01:08:04Z | 0.4 | 0.45 | 0.1753 | 0.35 | 0.6 | 0.3913 |
| Canva Hikes Pices by 300pc as It Readies for IPO | https://ia.acs.org.au/article/2024/canva-hikes-prices-by-300pc-as-it-readies-for-ipo.html | ia.acs.org.au | 2024-09-03T10:43:32Z | 0.25 | 0.55 | 0.3575 | 0.35 | 0.6 | 0.3911 |
| Show HN: I made a platform to share your favorite spots on a personal page | https://www.spotli.st/ | www.spotli.st | 2024-08-23T07:04:52Z | 0.25 | 0.55 | 0.3425 | 0.35 | 0.6 | 0.3889 |
| Building an AI Coach to Tame My Monkey Mind | https://eugeneyan.com/writing/ai-coach/ | eugeneyan.com | 2024-04-11T12:51:04Z | 0.4 | 0.45 | 0.1589 | 0.35 | 0.6 | 0.3888 |
| Artificial intelligence is losing hype |  | www.economist.com | 2024-08-20T11:00:37Z | 0.25 | 0.55 | 0.3384 | 0.35 | 0.6 | 0.3883 |
| Artificial intelligence is losing hype | https://www.economist.com/finance-and-economics/2024/08/19/artificial-intelligence-is-losing-hype | www.economist.com | 2024-08-20T11:00:37Z | 0.25 | 0.55 | 0.3384 | 0.35 | 0.6 | 0.3883 |
| Drop Coding Challanges | https://blackentropy.com/please-stop-the-absurd-coding-challenges/ | blackentropy.com | 2024-12-19T17:01:22Z | 0.25 | 0.45 | 0.5041 | 0.35 | 0.6 | 0.3881 |
| AI Hype Invades Taco Bell and Pizza Hut | https://arstechnica.com/information-technology/2024/04/ai-hype-invades-taco-bell-and-pizza-hut/ | arstechnica.com | 2024-04-04T03:39:10Z | 0.4 | 0.45 | 0.1493 | 0.35 | 0.6 | 0.3874 |
| OnScreen: AI generated long form sci fi TV show | https://bengarney.com/2024/04/02/ai-narratives-on-screen-part-1/ | bengarney.com | 2024-04-03T10:24:22Z | 0.4 | 0.45 | 0.1479 | 0.35 | 0.6 | 0.3872 |
| Show HN: Choosing the right SaaS is a chore, so I built something to fix that | https://gralio.ai/ | gralio.ai | 2024-12-09T15:29:58Z | 0.25 | 0.45 | 0.4904 | 0.35 | 0.6 | 0.3861 |
| 70% of new NPM packages in last 6 months were spam | https://blog.phylum.io/the-great-npm-garbage-patch/ | blog.phylum.io | 2024-08-07T17:25:30Z | 0.25 | 0.55 | 0.3205 | 0.35 | 0.6 | 0.3856 |
| Tracking supermarket prices with Playwright | https://www.sakisv.net/2024/08/tracking-supermarket-prices-playwright/ | www.sakisv.net | 2024-08-07T07:26:22Z | 0.25 | 0.55 | 0.3205 | 0.35 | 0.6 | 0.3856 |
| Why does everyone hate Haskell, jazz, and pure math? | https://adueck.github.io/blog/on-haskell-jazz-and-pure-math/ | adueck.github.io | 2024-08-05T12:17:16Z | 0.25 | 0.55 | 0.3178 | 0.35 | 0.6 | 0.3852 |
| Genie 2: A large-scale foundation world model | https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/ | deepmind.google | 2024-12-04T17:20:49Z | 0.25 | 0.45 | 0.4836 | 0.35 | 0.6 | 0.385 |
| Emad Mostaque resigned as CEO of Stability AI |  | stability.ai | 2024-03-23T13:51:32Z | 0.4 | 0.45 | 0.1329 | 0.35 | 0.6 | 0.3849 |
| Emad Mostaque resigned as CEO of Stability AI | https://stability.ai/news/stabilityai-announcement | stability.ai | 2024-03-23T13:51:32Z | 0.4 | 0.45 | 0.1329 | 0.35 | 0.6 | 0.3849 |
| Show HN: Uncover the Tools and Tech Behind Any Website | https://www.webatlas.ai/ | www.webatlas.ai | 2024-08-01T18:59:58Z | 0.25 | 0.55 | 0.3123 | 0.35 | 0.6 | 0.3843 |
| GrowthExpert.ai AI Growth Expert for Your Product | https://growthexpert.ai/ | growthexpert.ai | 2024-03-18T22:05:40Z | 0.4 | 0.45 | 0.126 | 0.35 | 0.6 | 0.3839 |
| The industry structure of LLM makers | https://calpaterson.com/porter.html | calpaterson.com | 2024-11-27T00:36:57Z | 0.25 | 0.45 | 0.4726 | 0.35 | 0.6 | 0.3834 |
| Cloud computing is a trap, warns GNU founder, Richard Stallman (2008) | https://www.theguardian.com/technology/2008/sep/29/cloud.computing.richard.stallman | www.theguardian.com | 2024-07-20T12:19:58Z | 0.25 | 0.55 | 0.2959 | 0.35 | 0.6 | 0.3819 |
| AI Looks Like a Bubble | https://every.to/napkin-math/ai-looks-like-a-bubble | every.to | 2023-02-19T11:51:34Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| AI chatbots are not a replacement for search engines |  | iai.tv | 2022-12-25T21:58:51Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| AI chatbots are not a replacement for search engines | https://iai.tv/articles/all-knowing-machines-are-a-fantasy-auid-2334 | iai.tv | 2022-12-25T21:58:51Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| AI is in danger of being swallowed up by copyright law | https://heathermeeker.com/2023/01/19/is-copyright-eating-ai/ | heathermeeker.com | 2023-01-22T13:07:39Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| AI-generating music app Riffusion turns viral success into $4M in funding |  | techcrunch.com | 2023-10-17T14:56:46Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| AI-generating music app Riffusion turns viral success into $4M in funding | https://techcrunch.com/2023/10/17/ai-generating-music-app-riffusion-turns-viral-success-into-4m-in-funding/ | techcrunch.com | 2023-10-17T14:56:46Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Aito.ai raises $1.1M aiming to make machine learning as easy as SQL queries | https://techcrunch.com/2019/05/07/aito-ai/ | techcrunch.com | 2019-05-07T12:41:50Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| AlphaFold-Powered Drug Discovery of a Novel CDK20 Inhibitor | https://arxiv.org/abs/2201.09647 | arxiv.org | 2022-01-25T09:25:28Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Anatomy of an AI System (2018) | https://anatomyof.ai/ | anatomyof.ai | 2022-03-10T20:31:12Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Apollo calls AI a 'bubble' worse than even the dotcom era |  | fortune.com | 2024-02-27T05:33:43Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Apollo calls AI a 'bubble' worse than even the dotcom era | https://fortune.com/2024/02/26/nvidia-ai-bubble-apollo-asset-manager-dotcom-artificial-intelligence/ | fortune.com | 2024-02-27T05:33:43Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Artist finds private medical record photos in popular AI training data set | https://arstechnica.com/information-technology/2022/09/artist-finds-private-medical-record-photos-in-popular-ai-training-data-set/ | arstechnica.com | 2022-09-21T21:44:14Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Bard and new AI features in Search |  | blog.google | 2023-02-06T20:05:25Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Bard and new AI features in Search | https://blog.google/technology/ai/bard-google-ai-search-updates/ | blog.google | 2023-02-06T20:05:25Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Better Call GPT: Comparing large language models against lawyers [pdf] | https://arxiv.org/abs/2401.16212 | arxiv.org | 2024-02-06T18:40:52Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Bitcoin is “logical currency choice for AI” | https://cointelegraph.com/news/ai-bitcoin-price-prediction-over-750k-arthur-hayes | cointelegraph.com | 2023-07-07T17:28:47Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Build full “product skills” and you'll probably be fine |  | twitter.com | 2023-03-19T19:58:56Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Build full “product skills” and you'll probably be fine | https://twitter.com/ID_AA_Carmack/status/1637087219591659520 | twitter.com | 2023-03-19T19:58:56Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| CEO Update: Paving the road forward with AI and community at the center |  | stackoverflow.blog | 2023-06-04T12:04:39Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| CEO Update: Paving the road forward with AI and community at the center | https://stackoverflow.blog/2023/05/31/ceo-update-paving-the-road-forward-with-ai-and-community-at-the-center/ | stackoverflow.blog | 2023-06-04T12:04:39Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| ChatGPT's API is so good and cheap, it makes most text generating AI obsolete |  | minimaxir.com | 2023-03-11T19:50:56Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| ChatGPT's API is so good and cheap, it makes most text generating AI obsolete | https://minimaxir.com/2023/03/new-chatgpt-overlord/ | minimaxir.com | 2023-03-11T19:50:56Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Drowning in AI Generated Garbage: the silent war we are fighting |  | ploum.net | 2022-12-05T15:27:58Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Drowning in AI Generated Garbage: the silent war we are fighting | https://ploum.net/2022-12-05-drowning-in-ai-generated-garbage.html | ploum.net | 2022-12-05T15:27:58Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Elon Musk Threatens Microsoft Lawsuit over LLM Training Data and API Abandonment | https://twitter.com/elonmusk/status/1648784955655192577 | twitter.com | 2023-04-20T14:07:19Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Exclusive access for LLM companies to largest Chinese nonfiction book collection | https://annas-blog.org/duxiu-exclusive.html | annas-blog.org | 2023-11-05T10:15:04Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Fame: The First AI-Powered Social Media Platform That Pays You to Be Creative | https://fame.cool | fame.cool | 2023-02-23T16:03:33Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Free database of 4,000+ AI tools | https://gpte.ai/ | gpte.ai | 2023-07-30T04:41:22Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Gemini AI |  | deepmind.google | 2023-12-06T17:42:51Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Gemini AI | https://deepmind.google/technologies/gemini/ | deepmind.google | 2023-12-06T17:42:51Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Google .dev domain early access | https://domains.google/tld/dev/ | domains.google | 2019-02-17T00:05:50Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Google I/O and the Coming AI Battles | https://stratechery.com/2023/google-i-o-and-the-coming-ai-battles/ | stratechery.com | 2023-05-15T12:24:08Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Google I/O and the State of Big Tech AI in 2023 | https://twitter.com/OmarKamali/status/1657740698441904130 | twitter.com | 2023-05-15T05:26:26Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Google slips as OpenAI said to be working on search product: report |  | seekingalpha.com | 2024-02-15T15:49:53Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Google slips as OpenAI said to be working on search product: report | https://seekingalpha.com/news/4067581-google-slips-openai-working-on-search-product-report | seekingalpha.com | 2024-02-15T15:49:53Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Google.ai | https://google.ai | google.ai | 2017-05-17T21:42:33Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| I Need AI | https://coryd.dev/posts/2024/i-need-ai/ | coryd.dev | 2024-02-26T01:25:06Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| I Trained My TikTok | https://metastable.org/2022/05/how-I-trained-my-tiktok.html | metastable.org | 2022-05-15T15:53:56Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Meta AI releases Code Llama 70B | https://twitter.com/AIatMeta/status/1752013879532782075 | twitter.com | 2024-01-29T18:53:45Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Mistral: Our first AI endpoints are available in early access | https://mistral.ai/news/la-plateforme/ | mistral.ai | 2023-12-11T10:03:54Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| My AI costs went from $100 to less than $1/day: Fine-tuning Mixtral with GPT4 |  | twitter.com | 2024-01-19T01:16:55Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| My AI costs went from $100 to less than $1/day: Fine-tuning Mixtral with GPT4 | https://twitter.com/wenquai/status/1748016021808595242 | twitter.com | 2024-01-19T01:16:55Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Not by AI | https://notbyai.fyi/ | notbyai.fyi | 2023-03-16T15:08:17Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Nvidia on the Mountaintop |  | stratechery.com | 2023-08-29T01:50:31Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Nvidia on the Mountaintop | https://stratechery.com/2023/nvidia-on-the-mountaintop/ | stratechery.com | 2023-08-29T01:50:31Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Nvidia’s AI supremacy is only temporary |  | petewarden.com | 2023-09-11T16:23:00Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Nvidia’s AI supremacy is only temporary | https://petewarden.com/2023/09/10/why-nvidias-ai-supremacy-is-only-temporary/ | petewarden.com | 2023-09-11T16:23:00Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| On being listed as an artist whose work was used to train Midjourney | https://catandgirl.com/4000-of-my-closest-friends/ | catandgirl.com | 2024-01-16T19:42:18Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Patreon raises big round at $450M valuation |  | techcrunch.com | 2017-09-15T13:31:26Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Patreon raises big round at $450M valuation | https://techcrunch.com/2017/09/14/patreon-series-c/ | techcrunch.com | 2017-09-15T13:31:26Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| See the pitch memo that raised €105M for four-week-old startup Mistral |  | sifted.eu | 2023-06-21T12:46:42Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| See the pitch memo that raised €105M for four-week-old startup Mistral | https://sifted.eu/articles/pitch-deck-mistral | sifted.eu | 2023-06-21T12:46:42Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Sell Access to Your AI or Data with Smart Subscriptions by Nevermined | https://nevermined.io/blog/announce-nevermined-marketplace-live/ | nevermined.io | 2023-08-02T11:18:47Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Show HN: Promote your startup using AI |  | shorturl.at | 2018-08-25T03:22:23Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Show HN: Promote your startup using AI | http://shorturl.at/bhu79 | shorturl.at | 2018-08-25T03:22:23Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Show HN: Rebataur – We build products for startups |  | rebataur.com | 2020-01-13T03:28:15Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Show HN: Rebataur – We build products for startups | https://rebataur.com | rebataur.com | 2020-01-13T03:28:15Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Show HN: Self-hosted OpenAI api server for open source LLMs | https://github.com/tensorchord/modelz-llm | github.com | 2023-06-12T03:11:14Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Smartbids.ai: Revolutionizing Canadian Real Estate with AI | https://smartbids.ai | smartbids.ai | 2023-09-15T14:59:42Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Stability.ai sent a take down request to Runway ML's SD v1.5 citing IP Leak | https://huggingface.co/runwayml/stable-diffusion-v1-5/discussions/1 | huggingface.co | 2022-10-20T23:02:26Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| The Darwinian argument for worrying about AI | https://time.com/6283958/darwinian-argument-for-worrying-about-ai/ | time.com | 2023-06-30T19:54:53Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| The Magnitude of the AI Bubble | https://apolloacademy.com/the-magnitude-of-the-ai-bubble/ | apolloacademy.com | 2024-01-09T13:32:30Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| The Myth of AI |  | edge.org | 2014-11-14T21:52:12Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| The Myth of AI | http://edge.org/conversation/the-myth-of-ai | edge.org | 2014-11-14T21:52:12Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| The real engine behind "AI" is the bad tech economy | https://hachyderm.io/@softwaredoug/111245545674056246 | hachyderm.io | 2023-10-16T16:26:54Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| US rejects AI copyright for famous state fair-winning Midjourney art | https://arstechnica.com/information-technology/2023/09/us-rejects-ai-copyright-for-famous-state-fair-winning-midjourney-art/ | arstechnica.com | 2023-09-11T20:54:59Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Vision language models are blind |  | vlmsareblind.github.io | 2024-07-11T21:59:20Z | 0.25 | 0.55 | 0.2836 | 0.35 | 0.6 | 0.38 |
| Vision language models are blind | https://vlmsareblind.github.io/ | vlmsareblind.github.io | 2024-07-11T21:59:20Z | 0.25 | 0.55 | 0.2836 | 0.35 | 0.6 | 0.38 |
| Who knew the first AI battles would be fought by artists? | https://vmst.io/@selzero/109512557990367884 | vmst.io | 2022-12-15T15:13:30Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Why I'm no longer writing stories with AI |  | storiesby.ai | 2023-04-28T21:47:34Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Why I'm no longer writing stories with AI | https://storiesby.ai/p/why-im-no-longer-writing-stories | storiesby.ai | 2023-04-28T21:47:34Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| Wit.ai (YC W14) raises $3M seed round from Andreessen Horowitz | https://wit.ai/blog/2014/10/15/wit-ai-raises-seed-round-from-andreessen-horowitz | wit.ai | 2014-10-15T16:23:33Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| X/Twitter has updated its terms of service to let it use posts for AI training | https://stackdiary.com/x-can-now-use-posts-for-ai-training-as-per-terms-of-service/ | stackdiary.com | 2023-09-01T16:39:13Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| “I just got *another* copyright claim for TYPING ON MY KEYBOARD!” | https://twitter.com/marcan42/status/1478858881283821569 | twitter.com | 2022-01-06T01:50:02Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| “The current climate in AI has so many parallels to 2021 Web3” | https://twitter.com/fchollet/status/1612142423425138688 | twitter.com | 2023-01-09T14:37:14Z | 0.4 | 0.45 | 0.1 | 0.35 | 0.6 | 0.38 |
| "AI", students, and epistemic crisis | https://miniver.blogspot.com/2024/07/ai-students-and-epistemic-crisis.html | miniver.blogspot.com | 2024-07-07T10:31:23Z | 0.25 | 0.55 | 0.2781 | 0.35 | 0.6 | 0.3792 |
| Show HN: I launched a site a week ago and it's made $1.2K so far, what next? | https://www.ninjachat.ai/ | www.ninjachat.ai | 2024-07-07T21:31:39Z | 0.25 | 0.55 | 0.2781 | 0.35 | 0.6 | 0.3792 |
| AGI: What Would You Do If You Had 8 Years Left to Live? | https://unchartedterritories.tomaspueyo.com/p/what-would-you-do-if-you-had-8-years | unchartedterritories.tomaspueyo.com | 2024-07-06T14:48:25Z | 0.25 | 0.55 | 0.2767 | 0.35 | 0.6 | 0.379 |
| Show HN: I made a tool to instantly ask 100 real humans to pick between 2 images | https://app.rapidata.ai/compare | app.rapidata.ai | 2024-07-01T12:11:39Z | 0.25 | 0.55 | 0.2699 | 0.35 | 0.6 | 0.378 |
| Gross Apple Marketing |  | jonathanbuys.com | 2024-10-30T14:55:02Z | 0.25 | 0.45 | 0.4356 | 0.35 | 0.6 | 0.3778 |
| Gross Apple Marketing | https://jonathanbuys.com/Gross_Apple_Marketing/ | jonathanbuys.com | 2024-10-30T14:55:02Z | 0.25 | 0.45 | 0.4356 | 0.35 | 0.6 | 0.3778 |
| 6 months ago, I left the bullshit industrial complex | https://www.joanwestenberg.com/6-months-ago,-i-left-the-bullshit-industrial-complex | www.joanwestenberg.com | 2024-06-27T05:25:00Z | 0.25 | 0.55 | 0.2644 | 0.35 | 0.6 | 0.3772 |
| Every Way to Get Structured Output from LLMs | https://www.boundaryml.com/blog/structured-output-from-llms | www.boundaryml.com | 2024-06-18T07:10:25Z | 0.25 | 0.55 | 0.2521 | 0.35 | 0.6 | 0.3753 |
| Recommended Stripe Radar Rules for combating fraud | https://www.chargebackstop.com/blog/stripe-radar | www.chargebackstop.com | 2024-06-18T19:49:20Z | 0.25 | 0.55 | 0.2521 | 0.35 | 0.6 | 0.3753 |
| What Is ChatGPT Doing and Why Does It Work? (2023) | https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/ | writings.stephenwolfram.com | 2024-06-18T18:02:07Z | 0.25 | 0.55 | 0.2521 | 0.35 | 0.6 | 0.3753 |
| Author of DPO Is Giving a Talk in Palo Alto | https://partiful.com/e/SV7aPEK95sbsqx8z8VO2 | partiful.com | 2024-10-16T21:46:22Z | 0.25 | 0.45 | 0.4164 | 0.35 | 0.6 | 0.375 |
| Why Google Takeout is sooo bad |  | marcin.cylke.com.pl | 2024-06-17T02:08:02Z | 0.25 | 0.55 | 0.2493 | 0.35 | 0.6 | 0.3749 |
| Why Google Takeout is sooo bad | https://marcin.cylke.com.pl/2024/06/16/why-google-takeout-is-sooo-bad/ | marcin.cylke.com.pl | 2024-06-17T02:08:02Z | 0.25 | 0.55 | 0.2493 | 0.35 | 0.6 | 0.3749 |
| Dan's the man: Why Chinese women are looking to ChatGPT for love | https://www.bbc.com/articles/c4nnje9rpjgo | www.bbc.com | 2024-06-14T20:50:56Z | 0.25 | 0.55 | 0.2466 | 0.35 | 0.6 | 0.3745 |
| VRChat is Laying Off 30% of Team | https://ask.vrchat.com/t/an-email-from-our-ceo/25060 | ask.vrchat.com | 2024-06-13T08:34:29Z | 0.25 | 0.55 | 0.2452 | 0.35 | 0.6 | 0.3743 |
| A new term, ‘slop’, has emerged to describe dubious A.I.-generated material | https://www.nytimes.com/2024/06/11/style/ai-search-slop.html | www.nytimes.com | 2024-06-11T14:31:49Z | 0.25 | 0.55 | 0.2425 | 0.35 | 0.6 | 0.3739 |
| Apple Intelligence for iPhone, iPad, and Mac |  | www.apple.com | 2024-06-10T20:52:17Z | 0.25 | 0.55 | 0.2411 | 0.35 | 0.6 | 0.3737 |
| Apple Intelligence for iPhone, iPad, and Mac | https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/ | www.apple.com | 2024-06-10T20:52:17Z | 0.25 | 0.55 | 0.2411 | 0.35 | 0.6 | 0.3737 |
| Is Microsoft trying to commit suicide? | https://www.antipope.org/charlie/blog-static/2024/06/is-microsoft-trying-to-commit-.html | www.antipope.org | 2024-06-05T20:05:53Z | 0.25 | 0.55 | 0.2342 | 0.35 | 0.6 | 0.3726 |
| Y Combinator Traded Prestige for Growth |  | unfashionable.blog | 2024-09-30T20:01:10Z | 0.25 | 0.45 | 0.3945 | 0.35 | 0.6 | 0.3717 |
| Y Combinator Traded Prestige for Growth | https://unfashionable.blog/p/yc/ | unfashionable.blog | 2024-09-30T20:01:10Z | 0.25 | 0.45 | 0.3945 | 0.35 | 0.6 | 0.3717 |
| U.S. court orders LibGen to pay $30M to publishers, issues broad injunction | https://torrentfreak.com/u-s-court-orders-libgen-to-pay-30m-to-publishers-issues-broad-injunction-240925/ | torrentfreak.com | 2024-09-29T21:28:16Z | 0.25 | 0.45 | 0.3932 | 0.35 | 0.6 | 0.3715 |
| Nvidia is about to pass Apple in market cap | https://www.reuters.com/technology/ai-darling-nvidias-market-value-surges-closer-apple-2024-05-28/ | www.reuters.com | 2024-05-29T20:17:45Z | 0.25 | 0.55 | 0.2247 | 0.35 | 0.6 | 0.3712 |
| Launch HN: Haystack (YC S24) – Visualize and edit code on an infinite canvas | https://github.com/haystackeditor/haystack-editor | github.com | 2024-09-25T19:02:44Z | 0.25 | 0.45 | 0.3877 | 0.35 | 0.6 | 0.3707 |
| Show HN: PDF to MD by LLMs – Extract Text/Tables/Image Descriptives by GPT4o | https://github.com/yigitkonur/swift-ocr-llm-powered-pdf-to-markdown | github.com | 2024-09-22T06:48:21Z | 0.25 | 0.45 | 0.3836 | 0.35 | 0.6 | 0.37 |
| Show HN: Waulog – A digital companion for dog owners | https://waulog.com/ | waulog.com | 2024-09-18T09:45:51Z | 0.25 | 0.45 | 0.3781 | 0.35 | 0.6 | 0.3692 |
| I set out to build a SaaS, I accidentally made a Directory | https://CRESoftware.tech | CRESoftware.tech | 2024-09-16T21:36:03Z | 0.25 | 0.45 | 0.3753 | 0.35 | 0.6 | 0.3688 |
| Testing the Firefox Alternatives |  | tommorris.org | 2024-09-14T18:52:04Z | 0.25 | 0.45 | 0.3726 | 0.35 | 0.6 | 0.3684 |
| Testing the Firefox Alternatives | https://tommorris.org/posts/2024/testing-the-firefox-alternatives/ | tommorris.org | 2024-09-14T18:52:04Z | 0.25 | 0.45 | 0.3726 | 0.35 | 0.6 | 0.3684 |
| Tim Cook is running out of ideas |  | www.businessinsider.com | 2024-05-15T12:36:22Z | 0.25 | 0.55 | 0.2055 | 0.35 | 0.6 | 0.3683 |
| Tim Cook is running out of ideas | https://www.businessinsider.com/apple-tim-cook-running-out-of-ideas-iphone-ipad-sales-2024-5 | www.businessinsider.com | 2024-05-15T12:36:22Z | 0.25 | 0.55 | 0.2055 | 0.35 | 0.6 | 0.3683 |
| AlphaProteo generates novel proteins for biology and health research | https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/ | deepmind.google | 2024-09-05T17:12:57Z | 0.25 | 0.45 | 0.3603 | 0.35 | 0.6 | 0.3665 |
| Gemini New Price | https://ai.google.dev/pricing | ai.google.dev | 2024-05-02T06:12:37Z | 0.25 | 0.55 | 0.1877 | 0.35 | 0.6 | 0.3657 |
| Maker Skill Trees | https://github.com/sjpiper145/MakerSkillTree | github.com | 2024-08-30T05:57:05Z | 0.25 | 0.45 | 0.3521 | 0.35 | 0.6 | 0.3653 |
| Claude's API now supports CORS requests, enabling client-side applications | https://simonwillison.net/2024/Aug/23/anthropic-dangerous-direct-browser-access/ | simonwillison.net | 2024-08-23T06:38:01Z | 0.25 | 0.45 | 0.3425 | 0.35 | 0.6 | 0.3639 |
| Most dating apps sell and share users' personal data | https://foundation.mozilla.org/en/privacynotincluded/articles/data-hungry-dating-apps-are-worse-than-ever-for-your-privacy/ | foundation.mozilla.org | 2024-04-23T15:59:27Z | 0.25 | 0.55 | 0.1753 | 0.35 | 0.6 | 0.3638 |
| Superleed: Get leads on autopilot for any business | https://superleed.com/ | superleed.com | 2024-08-19T11:30:01Z | 0.25 | 0.45 | 0.337 | 0.35 | 0.6 | 0.363 |
| Leaving Neovim for Zed | https://stevedylan.dev/posts/leaving-neovim-for-zed/ | stevedylan.dev | 2024-08-18T20:38:19Z | 0.25 | 0.45 | 0.3356 | 0.35 | 0.6 | 0.3628 |
| The founder's roadmap to $100M ARR |  | www.bvp.com | 2024-04-15T17:36:32Z | 0.25 | 0.55 | 0.1644 | 0.35 | 0.6 | 0.3622 |
| The founder's roadmap to $100M ARR | https://www.bvp.com/from-startup-to-centaur-book | www.bvp.com | 2024-04-15T17:36:32Z | 0.25 | 0.55 | 0.1644 | 0.35 | 0.6 | 0.3622 |
| Yes, social media is a cause of the epidemic of teenage mental illness | https://www.afterbabel.com/p/phone-based-childhood-cause-epidemic | www.afterbabel.com | 2024-04-10T21:29:05Z | 0.25 | 0.55 | 0.1575 | 0.35 | 0.6 | 0.3611 |
| Can Demis Hassabis save Google? |  | www.bigtechnology.com | 2024-04-01T16:19:57Z | 0.25 | 0.55 | 0.1452 | 0.35 | 0.6 | 0.3593 |
| Can Demis Hassabis save Google? | https://www.bigtechnology.com/p/can-demis-hassabis-save-google | www.bigtechnology.com | 2024-04-01T16:19:57Z | 0.25 | 0.55 | 0.1452 | 0.35 | 0.6 | 0.3593 |
| Show HN: We made glhf.chat – run almost any open-source LLM, including 405B | https://glhf.chat/landing/home | glhf.chat | 2024-07-24T04:16:28Z | 0.25 | 0.45 | 0.3014 | 0.35 | 0.6 | 0.3577 |
| More than 50,000 Americans died by suicide in 2023–more than any year on record |  | www.nbcnews.com | 2024-03-21T01:52:40Z | 0.25 | 0.55 | 0.1288 | 0.35 | 0.6 | 0.3568 |
| More than 50,000 Americans died by suicide in 2023–more than any year on record | https://www.nbcnews.com/meet-the-press/video/more-than-50-000-americans-died-by-suicide-in-2023-more-than-any-year-on-record-201161285832 | www.nbcnews.com | 2024-03-21T01:52:40Z | 0.25 | 0.55 | 0.1288 | 0.35 | 0.6 | 0.3568 |
| Mistral NeMo | https://mistral.ai/news/mistral-nemo/ | mistral.ai | 2024-07-18T15:19:27Z | 0.25 | 0.45 | 0.2932 | 0.35 | 0.6 | 0.3565 |
| Codestral Mamba | https://mistral.ai/news/codestral-mamba/ | mistral.ai | 2024-07-16T20:03:38Z | 0.25 | 0.45 | 0.2904 | 0.35 | 0.6 | 0.3561 |
| DevRel at HuggingFace |  | dx.tips | 2024-07-16T19:44:56Z | 0.25 | 0.45 | 0.2904 | 0.35 | 0.6 | 0.3561 |
| DevRel at HuggingFace | https://dx.tips/huggingface | dx.tips | 2024-07-16T19:44:56Z | 0.25 | 0.45 | 0.2904 | 0.35 | 0.6 | 0.3561 |
| Nearly half of Nvidia's revenue comes from four mystery whales each buying $3B+ | https://fortune.com/2024/08/29/nvidia-jensen-huang-ai-customers/ | fortune.com | 2024-09-01T11:45:57Z | 0.25 | 0.45 | 0.3548 | 0.35 | 0.5 | 0.3557 |
| Kagi and Wolfram | https://blog.kagi.com/kagi-wolfram | blog.kagi.com | 2024-03-07T17:42:19Z | 0.25 | 0.55 | 0.111 | 0.35 | 0.6 | 0.3542 |
| L402: Internet-Native Paywalls |  | l402.org | 2024-07-02T18:27:38Z | 0.25 | 0.45 | 0.2712 | 0.35 | 0.6 | 0.3532 |
| L402: Internet-Native Paywalls | https://l402.org | l402.org | 2024-07-02T18:27:38Z | 0.25 | 0.45 | 0.2712 | 0.35 | 0.6 | 0.3532 |
| A Quarter Century of Mozilla | https://blog.mozilla.org/en/mozilla/mitchell-baker-mozilla-25-anniversary/ | blog.mozilla.org | 2023-03-31T17:27:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| A coder considers the waning days of the craft |  | www.newyorker.com | 2023-11-14T07:34:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| A coder considers the waning days of the craft | https://www.newyorker.com/magazine/2023/11/20/a-coder-considers-the-waning-days-of-the-craft | www.newyorker.com | 2023-11-14T07:34:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| A hormone may boost cognition in Down syndrome | https://www.scientificamerican.com/article/a-hormone-may-boost-cognition-in-down-syndrome/ | www.scientificamerican.com | 2022-09-04T05:49:00Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| A.I. Researchers Are Making More Than $1M, Even at a Nonprofit |  | www.nytimes.com | 2018-04-19T22:02:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| A.I. Researchers Are Making More Than $1M, Even at a Nonprofit | https://www.nytimes.com/2018/04/19/technology/artificial-intelligence-salaries-openai.html | www.nytimes.com | 2018-04-19T22:02:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| AMD funded a drop-in CUDA implementation built on ROCm: It's now open-source |  | www.phoronix.com | 2024-02-12T21:57:31Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| AMD funded a drop-in CUDA implementation built on ROCm: It's now open-source | https://www.phoronix.com/review/radeon-cuda-zluda | www.phoronix.com | 2024-02-12T21:57:31Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| APIs for content sites must be free | https://www.somebits.com/weblog/culture/apis-for-content-sites-must-be-free.html | www.somebits.com | 2023-06-14T22:35:17Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Actors union will join writers on strike, shutting down Hollywood | https://www.cnbc.com/2023/07/13/sag-actors-union-goes-on-strike-joining-hollywood-writers.html | www.cnbc.com | 2023-07-14T07:24:07Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Amazon will cut 'several hundred' Alexa jobs as it ends unspecified initiatives |  | www.geekwire.com | 2023-11-17T17:07:54Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Amazon will cut 'several hundred' Alexa jobs as it ends unspecified initiatives | https://www.geekwire.com/2023/amazon-will-cut-several-hundred-more-jobs-on-alexa-team-as-it-discontinues-some-initiatives/ | www.geekwire.com | 2023-11-17T17:07:54Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Amazon, Amid Crackdown on Seller Scams, Fires Employees Over Data Leak | https://www.wsj.com/articles/amazon-amid-crackdown-on-seller-scams-fires-employees-over-data-leak-1544437800 | www.wsj.com | 2018-12-11T16:46:05Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Announcing GPT-NeoX-20B | https://blog.eleuther.ai/announcing-20b/ | blog.eleuther.ai | 2022-02-02T18:17:05Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Apple Captures 75% of Global Handset Market Operating Profit in Q2 2021 | https://www.counterpointresearch.com/global-handset-market-operating-profit-q2-2021/ | www.counterpointresearch.com | 2021-10-14T14:09:37Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Apple avoids job cuts because it didn’t overhire like Google and Amazon |  | www.bloomberg.com | 2023-02-10T21:27:23Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Apple avoids job cuts because it didn’t overhire like Google and Amazon | https://www.bloomberg.com/news/articles/2023-02-10/apple-aapl-avoids-tech-layoffs-because-it-didn-t-overhire-like-google-amazon | www.bloomberg.com | 2023-02-10T21:27:23Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Apple dives into display-making to cut reliance on Samsung |  | asia.nikkei.com | 2023-05-18T19:00:13Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Apple dives into display-making to cut reliance on Samsung | https://asia.nikkei.com/Spotlight/Supply-Chain/Apple-dives-into-display-making-to-cut-reliance-on-Samsung | asia.nikkei.com | 2023-05-18T19:00:13Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| At Tech’s Leading Edge, Worry About a Concentration of Power | https://www.nytimes.com/2019/09/26/technology/ai-computer-expense.html | www.nytimes.com | 2019-09-26T12:34:11Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Attack of the Week: Airdrop Tracing | https://blog.cryptographyengineering.com/2024/01/11/attack-of-the-week-airdrop-tracing/ | blog.cryptographyengineering.com | 2024-01-12T22:28:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Big Data's Big Problem: Little Talent | http://online.wsj.com/article/SB10001424052702304723304577365700368073674.html | online.wsj.com | 2012-04-28T16:02:34Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Browser extensions are underrated: the promise of hackable software (2019) | https://www.geoffreylitt.com/2019/07/29/browser-extensions | www.geoffreylitt.com | 2024-02-04T20:18:31Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Build a fast deep learning machine for under $1K |  | www.oreilly.com | 2017-02-09T17:55:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Build a fast deep learning machine for under $1K | https://www.oreilly.com/learning/build-a-super-fast-deep-learning-machine-for-under-1000 | www.oreilly.com | 2017-02-09T17:55:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Business Insider: Amazon is gutting its voice-assistant Alexa | https://www.businessinsider.com/amazon-alexa-job-layoffs-rise-and-fall-2022-11 | www.businessinsider.com | 2022-11-21T02:04:50Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Can we rule out near-term AGI? [video] | https://www.youtube.com/watch?v=YHCSNsLKHfM | www.youtube.com | 2018-11-08T19:31:23Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Car Owners Should Control Data Collected by Cars | https://www.nytimes.com/2019/05/20/opinion/car-repair-data-privacy.html | www.nytimes.com | 2019-05-21T20:56:23Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Challenges you’re going to face when building a chatbot | https://blog.infermedica.com/three-challenges-youre-going-to-face-when-building-a-chatbot/ | blog.infermedica.com | 2017-01-03T22:15:11Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| ChatGPT has trouble giving an answer before explaining its reasoning | https://blog.valentin.sh/chatgpt5/ | blog.valentin.sh | 2023-03-08T00:39:05Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| ChatGPT is a blurry JPEG of the web | https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web | www.newyorker.com | 2023-02-09T18:10:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| ChatGPT won’t replace search engines any time soon | https://www.algolia.com/blog/ai/why-chatgpt-wont-replace-search-engines-any-time-soon/ | www.algolia.com | 2023-01-08T06:02:35Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Cloud Provider Gets $2.3B Loan Using Nvidia's H100 as Collateral | https://www.anandtech.com/show/19995/cloud-provider-gets-23-billion-debt-using-nvidias-h100-as-collateral | www.anandtech.com | 2023-08-04T22:23:48Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Cogs bad | http://williamedwardscoder.tumblr.com/post/18065079081/cogs-bad | williamedwardscoder.tumblr.com | 2012-02-22T18:27:03Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Dead Internet Theory | https://old.reddit.com/r/webdev/comments/1auxufd/dead_internet_theory/ | old.reddit.com | 2024-02-20T02:30:09Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Dropbox to reduce global workforce by about 16%, or 500 staff |  | blog.dropbox.com | 2023-04-27T20:40:37Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Dropbox to reduce global workforce by about 16%, or 500 staff | https://blog.dropbox.com/topics/company/a-message-from-drew | blog.dropbox.com | 2023-04-27T20:40:37Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Eagle 7B: Soaring past Transformers | https://blog.rwkv.com/p/eagle-7b-soaring-past-transformers | blog.rwkv.com | 2024-01-29T10:54:41Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Elon Musk makes $43B unsolicited bid to take Twitter private | https://www.bloomberg.com/news/articles/2022-04-14/elon-musk-launches-43-billion-hostile-takeover-of-twitter | www.bloomberg.com | 2022-04-14T15:17:54Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Elon Musk, Other AI Bigwigs Call for Pause in Technology’s Development | https://www.wsj.com/articles/elon-musk-other-ai-bigwigs-call-for-pause-in-technologys-development-56327f | www.wsj.com | 2023-03-29T17:38:49Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Emberlight is shutting down, bricking all previously sold hardware | https://www.emberlight.co/blogs/glow/emberlight-is-shutting-down | www.emberlight.co | 2017-11-20T13:54:53Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Face detection – An overview and comparison of different solutions | https://www.liip.ch/en/blog/face-detection-an-overview-and-comparison-of-different-solutions-part1 | www.liip.ch | 2018-08-17T21:13:45Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Fakespot Is Acquired by Mozilla | https://www.fakespot.com/post/fakespot-acquired-by-mozilla | www.fakespot.com | 2023-05-02T18:19:49Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Figma and Adobe abandon proposed merger |  | www.figma.com | 2023-12-18T22:29:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Figma and Adobe abandon proposed merger | https://www.figma.com/blog/figma-adobe-abandon-proposed-merger/ | www.figma.com | 2023-12-18T22:29:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Firefox accounts renamed Mozilla accounts |  | support.mozilla.org | 2023-10-14T23:15:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Firefox accounts renamed Mozilla accounts | https://support.mozilla.org/en-US/kb/firefox-accounts-renamed-mozilla-accounts | support.mozilla.org | 2023-10-14T23:15:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Forces that fuel friendship | https://www.theatlantic.com/family/archive/2022/06/six-ways-make-maintain-friends/661232/ | www.theatlantic.com | 2022-06-13T17:57:52Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| GM self-driving tech unit Cruise laying off about 8% of staff |  | www.reuters.com | 2020-05-14T21:51:18Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| GM self-driving tech unit Cruise laying off about 8% of staff | https://www.reuters.com/article/us-gm-autonomous-layoffs/gm-self-driving-tech-unit-cruise-laying-off-about-8-of-staff-idUSKBN22Q34W | www.reuters.com | 2020-05-14T21:51:18Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Game Development Post-Unity |  | www.computerenhance.com | 2023-09-14T04:20:46Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Game Development Post-Unity | https://www.computerenhance.com/p/game-development-post-unity | www.computerenhance.com | 2023-09-14T04:20:46Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Generating Music Tracks with Unified Representation and Diffusion Framework |  | ai-muzic.github.io | 2023-05-23T06:56:37Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Generating Music Tracks with Unified Representation and Diffusion Framework | https://ai-muzic.github.io/getmusic/ | ai-muzic.github.io | 2023-05-23T06:56:37Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Geoffrey Hinton leaves Google and warns of danger ahead | https://www.nytimes.com/2023/05/01/technology/ai-google-chatbot-engineer-quits-hinton.html | www.nytimes.com | 2023-05-01T19:51:54Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Germany pauses AstraZeneca vaccinations as a 'precaution' |  | www.reuters.com | 2021-03-16T04:00:27Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Germany pauses AstraZeneca vaccinations as a 'precaution' | https://www.reuters.com/article/health-coronavirus-germany-astrazeneca/update-1-germany-to-halt-astrazeneca-vaccinations-health-ministry-idUSL8N2LD4T9 | www.reuters.com | 2021-03-16T04:00:27Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google Calls in Help from Larry Page and Sergey Brin for A.I. Fight |  | www.nytimes.com | 2023-01-21T11:54:47Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google Calls in Help from Larry Page and Sergey Brin for A.I. Fight | https://www.nytimes.com/2023/01/20/technology/google-chatgpt-artificial-intelligence.html | www.nytimes.com | 2023-01-21T11:54:47Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google Invests Almost $400M in ChatGPT Rival Anthropic |  | www.bloomberg.com | 2023-02-05T11:35:27Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google Invests Almost $400M in ChatGPT Rival Anthropic | https://www.bloomberg.com/news/articles/2023-02-03/google-invests-almost-400-million-in-ai-startup-anthropic | www.bloomberg.com | 2023-02-05T11:35:27Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google releases Bard to a limited number of users in the US and UK | https://www.nytimes.com/2023/03/21/technology/google-bard-chatbot.html | www.nytimes.com | 2023-03-21T18:04:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google's 'Rest and Vest' Days for Senior Employees Are Over, Says CEO | https://www.inc.com/nick-hobson/googles-rest-vest-days-for-sr-employees-are-over-says-ceo-its-a-brilliant-idea.html | www.inc.com | 2022-09-11T05:06:43Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google’s new reCAPTCHA has a dark side |  | www.fastcompany.com | 2019-06-27T17:55:22Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Google’s new reCAPTCHA has a dark side | https://www.fastcompany.com/90369697/googles-new-recaptcha-has-a-dark-side | www.fastcompany.com | 2019-06-27T17:55:22Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Hacking a VW Golf Power Steering ECU | https://blog.willemmelching.nl/carhacking/2022/01/02/vw-part1/ | blog.willemmelching.nl | 2022-01-05T04:40:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| HealthCare.gov’s head tech guy is out | http://www.washingtonpost.com/blogs/wonkblog/wp/2013/11/06/healthcare-govs-head-tech-guy-is-out/ | www.washingtonpost.com | 2013-11-06T23:10:05Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Helen Toner shares her side |  | www.wsj.com | 2023-12-08T01:56:52Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Helen Toner shares her side | https://www.wsj.com/tech/ai/helen-toner-openai-board-2e4031ef | www.wsj.com | 2023-12-08T01:56:52Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| High Short Interest Stocks |  | www.highshortinterest.com | 2021-01-29T05:09:04Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| High Short Interest Stocks | https://www.highshortinterest.com/all/ | www.highshortinterest.com | 2021-01-29T05:09:04Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| HopsFS: 100x Times Faster Than AWS S3 | https://www.logicalclocks.com/blog/hopsfs-100x-times-faster-than-aws-s3 | www.logicalclocks.com | 2020-11-21T23:51:32Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How Biotech Startup Funding Will Change in the Next 10 Years | https://blog.ycombinator.com/how-biotech-startup-funding-will-change-in-the-next-10-years/ | blog.ycombinator.com | 2019-08-05T22:30:04Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How TikTok Broke the Ad Business |  | www.economist.com | 2023-03-21T18:56:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How TikTok Broke the Ad Business | https://www.economist.com/business/2023/03/21/how-tiktok-broke-the-ad-business | www.economist.com | 2023-03-21T18:56:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How did we reposition heybooster, a SaaS company? | https://emreckartal.substack.com/p/how-did-we-reposition-heybooster | emreckartal.substack.com | 2023-08-02T10:04:13Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How have lack of travel and increased social isolation affected mathematics? | https://www.quantamagazine.org/how-has-coronavirus-affected-mathematics-20200428/ | www.quantamagazine.org | 2020-04-30T08:51:46Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How in-app purchases have destroyed the game industry |  | www.baekdal.com | 2014-02-02T14:07:12Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| How in-app purchases have destroyed the game industry | http://www.baekdal.com/opinion/how-inapp-purchases-has-destroyed-the-industry/ | www.baekdal.com | 2014-02-02T14:07:12Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| I cancelled my Replit subscription |  | journal.paoloamoroso.com | 2023-11-19T15:24:22Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| I cancelled my Replit subscription | https://journal.paoloamoroso.com/why-i-cancelled-my-replit-subscription | journal.paoloamoroso.com | 2023-11-19T15:24:22Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| I wish GPT4 had never happened | https://chaudhry.notion.site/I-wish-GPT4-had-never-happened-9f0cbf2848a44ec9911c07fb34ff5de3 | chaudhry.notion.site | 2023-04-08T18:18:15Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| IBM is not doing "cognitive computing" with Watson (2016) |  | www.rogerschank.com | 2018-04-30T21:10:33Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| IBM is not doing "cognitive computing" with Watson (2016) | http://www.rogerschank.com/fraudulent-claims-made-by-IBM-about-Watson-and-AI | www.rogerschank.com | 2018-04-30T21:10:33Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| In a Robot Economy, All Humans Will Be Marketers |  | www.bloomberg.com | 2017-07-30T03:57:36Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| In a Robot Economy, All Humans Will Be Marketers | https://www.bloomberg.com/view/articles/2017-07-26/in-a-robot-economy-all-humans-will-be-marketers | www.bloomberg.com | 2017-07-30T03:57:36Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Interesting Tech Markets for 2019 | http://blog.eladgil.com/2019/01/interesting-markets-2019-edition.html | blog.eladgil.com | 2019-01-08T21:32:26Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| It happened to me today: $80/hr writer replaced with ChatGPT | https://old.reddit.com/r/freelanceWriters/comments/12ff5mw/it_happened_to_me_today/ | old.reddit.com | 2023-04-11T13:02:34Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Jobs you're applying to might not be real | https://www.marketplace.org/2024/01/03/those-jobs-youre-applying-to-they-might-not-be-real/ | www.marketplace.org | 2024-01-05T06:43:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Jonathan Mayer Threatens To End “Do Not Track” Talks |  | www.businessinsider.com | 2013-06-17T19:22:07Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Jonathan Mayer Threatens To End “Do Not Track” Talks | http://www.businessinsider.com/jonathan-mayer-threatens-to-end-do-not-track-talks-2013-6 | www.businessinsider.com | 2013-06-17T19:22:07Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| June 2023 Data Dump is missing | https://meta.stackexchange.com/a/390023/6212 | meta.stackexchange.com | 2023-06-09T18:22:00Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Kagi search and Orion browser enter public beta | https://blog.kagi.com/kagi-orion-public-beta | blog.kagi.com | 2022-06-02T01:25:04Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Kodak shares up as it announces KODAKCoin cryptocurrency |  | www.kodak.com | 2018-01-10T15:14:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Kodak shares up as it announces KODAKCoin cryptocurrency | https://www.kodak.com/US/en/corp/Press_center/KODAK_and_WENN_Digital_Partner_to_Launch_Major_Blockchain_Initiative_and_Cryptocurrency/default.htm | www.kodak.com | 2018-01-10T15:14:10Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| LLaMA: A foundational, 65B-parameter large language model | https://ai.facebook.com/blog/large-language-model-llama-meta-ai/ | ai.facebook.com | 2023-02-24T17:09:12Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Launch HN: Foster (YC W21) – Improve your writing with on-demand editing | https://www.foster.co/ | www.foster.co | 2022-06-24T15:26:07Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Magic the Gathering content creator pleas YouTube to stop scammer bot deluge | https://www.youtube.com/watch?v=lKcdEf0fNA0 | www.youtube.com | 2023-03-13T17:32:50Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mark Zuckerberg says Facebook will turn into a ‘metaverse’ |  | www.theverge.com | 2021-07-23T18:41:32Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mark Zuckerberg says Facebook will turn into a ‘metaverse’ | https://www.theverge.com/22588022/mark-zuckerberg-facebook-ceo-metaverse-interview | www.theverge.com | 2021-07-23T18:41:32Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mark Zuckerberg’s new goal is creating artificial general intelligence |  | www.theverge.com | 2024-01-18T22:01:47Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mark Zuckerberg’s new goal is creating artificial general intelligence | https://www.theverge.com/2024/1/18/24042354/mark-zuckerberg-meta-agi-reorg-interview | www.theverge.com | 2024-01-18T22:01:47Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mass layoffs and absentee bosses create a morale crisis at Meta | https://www.nytimes.com/2023/04/12/technology/meta-layoffs-employees-management.html | www.nytimes.com | 2023-04-12T12:04:40Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Maximizing the Potential of LLMs: A Guide to Prompt Engineering | https://www.ruxu.dev/articles/ai/maximizing-the-potential-of-llms/ | www.ruxu.dev | 2023-04-12T06:52:55Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Meta Reports Fourth Quarter and Full Year 2022 Results | https://investor.fb.com/investor-news/press-release-details/2023/Meta-Reports-Fourth-Quarter-and-Full-Year-2022-Results/default.aspx | investor.fb.com | 2023-02-02T01:31:22Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Meta lays off 11,000 people | https://about.fb.com/news/2022/11/mark-zuckerberg-layoff-message-to-employees/ | about.fb.com | 2022-11-09T21:42:18Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Meta plans thousands more layoffs as soon as this week |  | www.bloomberg.com | 2023-03-07T10:41:47Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Meta plans thousands more layoffs as soon as this week | https://www.bloomberg.com/news/articles/2023-03-07/meta-is-said-to-plan-thousands-more-layoffs-as-soon-as-this-week | www.bloomberg.com | 2023-03-07T10:41:47Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Microsoft eyes $10B bet on ChatGPT | https://www.semafor.com/article/01/09/2023/microsoft-eyes-10-billion-bet-on-chatgpt | www.semafor.com | 2023-01-11T06:30:29Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Microsoft is preparing to add ChatGPT to Bing | https://www.bloomberg.com/news/articles/2023-01-04/microsoft-hopes-openai-s-chatbot-will-make-bing-smarter | www.bloomberg.com | 2023-01-05T12:23:12Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mistral releases ‘unmoderated’ chatbot via torrent | https://www.404media.co/260-million-ai-company-releases-chatbot-that-gives-detailed-instructions-on-murder-ethnic-cleansing/ | www.404media.co | 2023-10-01T04:41:35Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mob justice is trampling democratic discourse | https://www.theatlantic.com/magazine/archive/2021/10/new-puritans-mob-justice-canceled/619818/ | www.theatlantic.com | 2021-08-31T15:00:26Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Modern Media Is a DoS Attack on Free Will | http://m.nautil.us/issue/52/the-hive/modern-media-is-a-dos-attack-on-your-free-will | m.nautil.us | 2017-11-21T08:42:01Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Mojo is a much better “Objective-C without the C” than Swift ever was | https://blog.metaobject.com/2023/06/mojo-is-much-better-without-c-than.html | blog.metaobject.com | 2023-06-12T14:24:36Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| My channel is now demonetized because I cover the war [video] | https://www.youtube.com/watch?v=kt6RAZeBKAc | www.youtube.com | 2022-10-08T16:38:57Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Nancy Pelosi Made $500k from Her Nvidia Bet, Doubling Her Annual Salary | https://finance.yahoo.com/news/nancy-pelosi-made-500-000-140722196.html | finance.yahoo.com | 2024-01-26T18:01:40Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Navigating the E-Commerce Maze: My Journey Creating Safe Deal | https://api.joinsafedeal.com/go?type=ycombinator | api.joinsafedeal.com | 2023-11-23T01:08:11Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Nevada approves regulations for self-driving cars | http://www.physorg.com/news/2012-02-nevada-self-driving-cars.html | www.physorg.com | 2012-02-17T02:53:36Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| New Loongson chip matches Intel's 14600K in IPC tests, overclocked to 3 GHz |  | www.tomshardware.com | 2023-11-30T15:14:06Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| New Loongson chip matches Intel's 14600K in IPC tests, overclocked to 3 GHz | https://www.tomshardware.com/news/loongson-launches-3a6000-cpu-matches-14600k-ipc | www.tomshardware.com | 2023-11-30T15:14:06Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Noam Chomsky – Startup Culture (2015) [video] | https://www.youtube.com/watch?v=6jhwA1vLEpU | www.youtube.com | 2021-08-25T04:45:59Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Nvidia RTX 5000 Ada 32GB Workstation GPU Review | https://www.servethehome.com/nvidia-rtx-5000-ada-32gb-workstation-gpu-review/ | www.servethehome.com | 2024-01-02T10:56:53Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| On AlphaTensor’s new matrix multiplication algorithms | https://fgiesen.wordpress.com/2022/10/06/on-alphatensors-new-matrix-multiplication-algorithms/ | fgiesen.wordpress.com | 2022-10-07T06:59:09Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| OnlyFans: Who is Leonid Radvinsky, the elusive owner of a porn empire? | https://www.bbc.com/news/world-66615008 | www.bbc.com | 2023-09-01T03:10:41Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Oregon Just Voted to Legalize Duplexes on Almost Every City Lot | https://www.sightline.org/2019/06/30/oregon-just-voted-to-legalize-duplexes-on-almost-every-city-lot | www.sightline.org | 2019-07-01T20:14:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Pearler (RFx, Cyber Reviews) has added a free tier | https://www.pearler.ai/pricing | www.pearler.ai | 2022-03-07T01:50:18Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Polars: Company Formation Announcement | https://www.pola.rs/posts/company-announcement/ | www.pola.rs | 2023-08-03T18:02:46Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Reddit Strike Has Started | https://reddark.untone.uk/ | reddark.untone.uk | 2023-06-12T00:31:50Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Rent going up? One company’s algorithm could be why | https://www.propublica.org/article/yieldstar-rent-increase-realpage-rent | www.propublica.org | 2022-10-16T18:41:07Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| S.E.C. Gives Small Investors Access to Equity Crowdfunding |  | www.nytimes.com | 2015-10-31T10:03:26Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| S.E.C. Gives Small Investors Access to Equity Crowdfunding | http://www.nytimes.com/2015/10/31/business/dealbook/sec-gives-small-investors-access-to-equity-crowdfunding.html | www.nytimes.com | 2015-10-31T10:03:26Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Samsung considers moving to Bing as default search engine | https://www.sammobile.com/news/samsung-galaxy-phones-tablets-bing-search-replace-google-default-search-engine/ | www.sammobile.com | 2023-04-17T14:43:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Saying goodbye to Stack Overflow | https://old.reddit.com/r/webdev/comments/116vvpp/saying_goodbye_to_stack_overflow/ | old.reddit.com | 2023-02-21T21:54:28Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Show HN: GPT-4-powered web searches for developers | https://www.phind.com | www.phind.com | 2023-04-12T19:58:59Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Show HN: Open-Source Microservices Framework for Cross-LLM Apps | https://www.sugarcaneai.dev/ | www.sugarcaneai.dev | 2023-10-01T15:27:12Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Show HN: This Food Does Not Exist | https://nyx-ai.github.io/stylegan2-flax-tpu/ | nyx-ai.github.io | 2022-07-21T04:30:48Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| SiFive: The road ahead (post layoffs) |  | www.sifive.com | 2023-10-30T11:28:21Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| SiFive: The road ahead (post layoffs) | https://www.sifive.com/blog/the-road-ahead-- | www.sifive.com | 2023-10-30T11:28:21Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Start building Actions on Google | https://developers.googleblog.com/2016/12/start-building-actions-on-google.html | developers.googleblog.com | 2016-12-08T21:04:19Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Starting a Business Around GPT-3 Is a Bad Idea | https://www.allencheng.com/starting-a-business-around-gpt-3-is-a-bad-idea/ | www.allencheng.com | 2020-07-31T20:38:06Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Stealing sensitive browser data with the W3C Ambient Light Sensor API (2017) | https://blog.lukaszolejnik.com/stealing-sensitive-browser-data-with-the-w3c-ambient-light-sensor-api/ | blog.lukaszolejnik.com | 2019-10-14T23:24:21Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Switching Costs in Software Development |  | blog.professorbeekums.com | 2016-09-14T08:37:24Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Switching Costs in Software Development | http://blog.professorbeekums.com/2016/09/switching-costs-in-software-development.html | blog.professorbeekums.com | 2016-09-14T08:37:24Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Tech CEOs Screwed Up |  | www.businessinsider.com | 2023-02-06T16:46:11Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Tech CEOs Screwed Up | https://www.businessinsider.com/fire-blame-ceo-tech-employee-layoffs-google-facebook-salesforce-amazon-2023-2 | www.businessinsider.com | 2023-02-06T16:46:11Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Tech layoffs exceed 240k so far in 2023, 50% more than 2022 |  | www.msn.com | 2023-10-16T18:32:39Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Tech layoffs exceed 240k so far in 2023, 50% more than 2022 | https://www.msn.com/en-us/money/companies/tech-layoffs-exceed-240000-so-far-in-2023-more-than-50-higher-than-in-all-of-2022/ar-AA1ib3AY | www.msn.com | 2023-10-16T18:32:39Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The Anti-Ownership eBook Economy | https://www.nyuengelberg.org/outputs/the-anti-ownership-ebook-economy/ | www.nyuengelberg.org | 2023-07-13T22:18:24Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The FTC’s new enforcement weapon: “Algorithmic destruction” | https://www.protocol.com/policy/ftc-algorithm-destroy-data-privacy | www.protocol.com | 2022-03-17T17:24:34Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The Forces Behind Toutiao, China’s Content King | http://blog.ycombinator.com/the-hidden-forces-behind-toutiao-chinas-content-king/ | blog.ycombinator.com | 2017-10-12T23:48:19Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The Myth of the Tech God Is Crumbling | https://www.wsj.com/articles/tech-gods-silicon-valley-elon-musk-twitter-sam-bankman-fried-ftx-sbf-11668803154 | www.wsj.com | 2022-11-20T09:53:09Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The Opium of the Intellectuals (2005) |  | www.newcriterion.com | 2018-07-01T10:27:20Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The Opium of the Intellectuals (2005) | https://www.newcriterion.com/blogs/dispatch/the-opium-of-the-intellectuals | www.newcriterion.com | 2018-07-01T10:27:20Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The business of extracting knowledge from academic publications | https://www.theseedsofscience.pub/p/the-business-of-extracting-knowledge | www.theseedsofscience.pub | 2023-11-02T01:04:35Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The funding frenzy at Anthropic | https://www.nytimes.com/2024/02/20/technology/anthropic-funding-ai.html | www.nytimes.com | 2024-02-22T01:23:34Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The golden age of YouTube is over |  | www.theverge.com | 2019-04-06T05:47:32Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The golden age of YouTube is over | https://www.theverge.com/2019/4/5/18287318/youtube-logan-paul-pewdiepie-demonetization-adpocalypse-premium-influencers-creators | www.theverge.com | 2019-04-06T05:47:32Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The note Reddit sent to moderators threatening them if they don’t reopen | https://www.theverge.com/2023/6/16/23763538/reddit-blackout-api-protest-mod-replacement-threat | www.theverge.com | 2023-06-16T18:40:58Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The only flag of the world that is shredded by design | https://blog.kobadoo.com/2022/02/the-only-flag-of-world-that-is-shredded.html | blog.kobadoo.com | 2022-02-23T03:25:14Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| The personal, political art of board-game design | https://www.newyorker.com/culture/annals-of-inquiry/the-personal-political-art-of-board-game-design | www.newyorker.com | 2023-12-23T12:51:13Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Threads 24% likely to overtake Twitter, down from 49% say prediction markets | https://www.baseratetimes.com/#Twitter | www.baseratetimes.com | 2023-07-16T13:01:13Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Threads, an Instagram app | https://apps.apple.com/us/app/threads-an-instagram-app/id6446901002 | apps.apple.com | 2023-07-04T14:00:07Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Three Years of Misery Inside Google, the Happiest Company in Tech |  | www.wired.com | 2019-08-13T14:35:01Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Three Years of Misery Inside Google, the Happiest Company in Tech | https://www.wired.com/story/inside-google-three-years-misery-happiest-company-tech/ | www.wired.com | 2019-08-13T14:35:01Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| TikTok overtakes Facebook as most downloaded app | https://asia.nikkei.com/Business/Technology/TikTok-overtakes-Facebook-as-world-s-most-downloaded-app | asia.nikkei.com | 2021-08-10T20:29:15Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Training Data for the Price of a Sandwich: Common Crawl's Impact on Gen AI | https://foundation.mozilla.org/en/research/library/generative-ai-training-data/common-crawl/ | foundation.mozilla.org | 2024-02-11T00:09:12Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| UK: Food inflation rises to 18.2% as it hits highest rate in over 45 years | https://www.grocerygazette.co.uk/2023/03/22/food-inflation-highest-rate/ | www.grocerygazette.co.uk | 2023-03-24T16:51:15Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Uber Posts $5.2B Loss and Slowest Ever Growth Rate | https://www.nytimes.com/2019/08/08/technology/uber-earnings.html | www.nytimes.com | 2019-08-08T20:50:09Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Uber migrates microservices to multi-cloud platform running Kubernetes and Mesos | https://www.uber.com/en-GB/blog/up-portable-microservices-ready-for-the-cloud/ | www.uber.com | 2023-10-22T21:10:44Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Unpredictable black boxes are terrible interfaces | https://magrawala.substack.com/p/unpredictable-black-boxes-are-terrible | magrawala.substack.com | 2023-04-05T07:52:53Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Using ChatGPT Plugins with LLaMA |  | blog.lastmileai.dev | 2023-03-26T16:45:21Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Using ChatGPT Plugins with LLaMA | https://blog.lastmileai.dev/using-openais-retrieval-plugin-with-llama-d2e0b6732f14 | blog.lastmileai.dev | 2023-03-26T16:45:21Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Utah is first US state to limit teen social media access | https://www.bbc.com/news/world-us-canada-65060733 | www.bbc.com | 2023-03-26T17:32:30Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Vespa Cloud with Free Trial | https://cloud.vespa.ai/pricing#free-trial | cloud.vespa.ai | 2021-06-07T23:11:30Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Waveterm | https://www.waveterm.dev/ | www.waveterm.dev | 2023-12-10T20:55:24Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| We don’t need a new Twitter | https://www.newyorker.com/culture/cultural-comment/we-dont-need-a-new-twitter | www.newyorker.com | 2023-08-17T14:36:00Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Web3? I have my DAOts | https://networked.substack.com/p/web3-i-have-my-daots | networked.substack.com | 2021-12-07T09:37:13Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Which kinds of GPT startups will thrive? | https://assistedeverything.substack.com/p/the-three-hills-model-for-evaluating | assistedeverything.substack.com | 2023-05-15T14:33:50Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Who Should Stop Unethical A.I.? | https://www.newyorker.com/tech/annals-of-technology/who-should-stop-unethical-ai | www.newyorker.com | 2021-02-15T21:36:18Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Who Y Combinator Companies Want | http://data.triplebyte.com/who-y-combinator-companies-want-c1880a08ac88 | data.triplebyte.com | 2015-12-09T14:22:16Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Wish to use GPT-4 without bringing your own API Key? Here is how YOU can do it | https://www.rockethub.com/deal/magai | www.rockethub.com | 2023-06-09T20:45:00Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| XGen-7B, a new 7B foundational model trained on up to 8K length for 1.5T tokens | https://blog.salesforceairesearch.com/xgen/ | blog.salesforceairesearch.com | 2023-06-29T08:22:51Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| You can't afford to be an artist and/or author, let alone be respected | https://www.cdahmedeh.net/blog/2022/8/16/you-cant-afford-to-be-an-artist-let-alone-be-respected | www.cdahmedeh.net | 2022-08-16T22:52:08Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| YouTube blocks Russell Brand from making money through its platform |  | www.nytimes.com | 2023-09-19T18:01:02Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| YouTube blocks Russell Brand from making money through its platform | https://www.nytimes.com/2023/09/19/arts/russell-brand-youtube.html | www.nytimes.com | 2023-09-19T18:01:02Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| iPhone users pay higher prices at German carsharing Sixt | https://www.welt.de/wirtschaft/article190490795/Sixt-Share-Wer-ein-iPhone-hat-zahlt-beim-Carsharing-mehr.html | www.welt.de | 2019-03-19T16:16:15Z | 0.25 | 0.55 | 0.1 | 0.35 | 0.6 | 0.3525 |
| Show HN: AutoEditor – Edit your video in just a few clicks | https://autoeditor.video/ | autoeditor.video | 2024-08-08T17:31:33Z | 0.25 | 0.45 | 0.3219 | 0.35 | 0.5 | 0.3508 |
| Anat Ashkenazi to Join Google and Alphabet as Chief Financial Officer |  | abc.xyz | 2024-06-06T10:02:06Z | 0.25 | 0.45 | 0.2356 | 0.35 | 0.6 | 0.3478 |
| Anat Ashkenazi to Join Google and Alphabet as Chief Financial Officer | https://abc.xyz/2024-0605/ | abc.xyz | 2024-06-06T10:02:06Z | 0.25 | 0.45 | 0.2356 | 0.35 | 0.6 | 0.3478 |
| Show HN: Building Alternative to Examine.com | https://pillser.com/health-outcomes/increased-short-chain-fatty-acid-levels-84 | pillser.com | 2024-06-02T20:05:21Z | 0.25 | 0.45 | 0.2301 | 0.35 | 0.6 | 0.347 |
| Anonymous Source Shared Leaked Google Search API Documents | https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/ | sparktoro.com | 2024-05-29T11:19:25Z | 0.25 | 0.45 | 0.2247 | 0.35 | 0.6 | 0.3462 |
| Chatbot Arena Leaderboard: Gemini 1.5 Flash, Pro and Advanced Results | https://twitter.com/lmsysorg/status/1795512202465845686 | twitter.com | 2024-05-28T19:28:27Z | 0.25 | 0.45 | 0.2233 | 0.35 | 0.6 | 0.346 |
| Google Search Is Now a Giant Hallucination |  | gizmodo.com | 2024-05-24T17:58:18Z | 0.25 | 0.45 | 0.2178 | 0.35 | 0.6 | 0.3452 |
| Google Search Is Now a Giant Hallucination | https://gizmodo.com/google-search-ai-overview-giant-hallucination-1851499031 | gizmodo.com | 2024-05-24T17:58:18Z | 0.25 | 0.45 | 0.2178 | 0.35 | 0.6 | 0.3452 |
| Gemini Flash | https://deepmind.google/technologies/gemini/flash/ | deepmind.google | 2024-05-14T19:31:15Z | 0.25 | 0.45 | 0.2041 | 0.35 | 0.6 | 0.3431 |
| Veo | https://deepmind.google/technologies/veo/ | deepmind.google | 2024-05-14T18:35:52Z | 0.25 | 0.45 | 0.2041 | 0.35 | 0.6 | 0.3431 |
| MTA banned from using facial recognition to enforce fare evasion |  | gothamist.com | 2024-05-02T11:45:51Z | 0.25 | 0.45 | 0.1877 | 0.35 | 0.6 | 0.3407 |
| MTA banned from using facial recognition to enforce fare evasion | https://gothamist.com/news/mta-banned-from-using-facial-recognition-to-enforce-fare-evasion | gothamist.com | 2024-05-02T11:45:51Z | 0.25 | 0.45 | 0.1877 | 0.35 | 0.6 | 0.3407 |
| Pydantic Logfire | https://pydantic.dev/logfire | pydantic.dev | 2024-04-30T23:01:10Z | 0.25 | 0.45 | 0.1849 | 0.35 | 0.6 | 0.3402 |
| Run Meta Llama 3 with an API | https://replicate.com/blog/run-llama-3-with-an-api | replicate.com | 2024-04-18T18:07:48Z | 0.25 | 0.45 | 0.1685 | 0.35 | 0.6 | 0.3378 |
| Mixtral 8x22B | https://mistral.ai/news/mixtral-8x22b/ | mistral.ai | 2024-04-17T14:58:03Z | 0.25 | 0.45 | 0.1671 | 0.35 | 0.6 | 0.3376 |
| Lessons after a Half-billion GPT Tokens | https://kenkantzer.com/lessons-after-a-half-billion-gpt-tokens/ | kenkantzer.com | 2024-04-13T22:53:39Z | 0.25 | 0.45 | 0.1616 | 0.35 | 0.6 | 0.3367 |
| Zed Decoded: Async Rust |  | zed.dev | 2024-04-09T19:22:38Z | 0.25 | 0.45 | 0.1562 | 0.35 | 0.6 | 0.3359 |
| Zed Decoded: Async Rust | https://zed.dev/blog/zed-decoded-async-rust | zed.dev | 2024-04-09T19:22:38Z | 0.25 | 0.45 | 0.1562 | 0.35 | 0.6 | 0.3359 |
| New Aztec Codices Discovered: The Codices of San Andrés Tetepilco | https://tlacuilolli.com/2024/03/21/new-aztec-codices-the-codices-of-san-andres-tetepilco/ | tlacuilolli.com | 2024-03-24T11:56:42Z | 0.25 | 0.45 | 0.1342 | 0.35 | 0.6 | 0.3326 |
| How to Start Google | https://paulgraham.com/google.html | paulgraham.com | 2024-03-19T21:44:28Z | 0.25 | 0.45 | 0.1274 | 0.35 | 0.6 | 0.3316 |
| Experienced engineers are struggling to get hired | https://twitter.com/Carnage4Life/status/1767527635297722786 | twitter.com | 2024-03-15T01:15:16Z | 0.25 | 0.45 | 0.1205 | 0.35 | 0.6 | 0.3306 |
| Show HN: Struct – A Feed-Centric Chat Platform | https://struct.ai/blog/introducing-the-struct-chat-platform | struct.ai | 2024-03-01T04:15:26Z | 0.25 | 0.45 | 0.1027 | 0.35 | 0.6 | 0.3279 |
| "Coding" was never the source of value | https://twitter.com/id_aa_carmack/status/1762110222321975442 | twitter.com | 2024-02-26T16:44:08Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| A former Uber engineer's disaster story | https://twitter.com/StanTwinB/status/1336890442768547845 | twitter.com | 2020-12-11T06:13:58Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| A rising sentiment that IBM’s Watson can’t deliver on its promises | http://gizmodo.com/why-everyone-is-hating-on-watson-including-the-people-w-1797510888 | gizmodo.com | 2017-08-10T20:56:41Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| A simple guide to fine-tuning Llama 2 | https://brev.dev/blog/fine-tuning-llama-2 | brev.dev | 2023-07-25T00:07:21Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| A tale of Phobos – How we almost cracked a ransomware using CUDA | https://cert.pl/en/posts/2023/02/breaking-phobos/ | cert.pl | 2023-02-24T15:25:47Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Amazon Curate – I Wish (2020) | https://danielmiessler.com/blog/introducing-amazon-curate-i-wish/ | danielmiessler.com | 2021-01-06T14:47:00Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Amazon has taken down the Sad Bastard Cookbook | https://wandering.shop/@youseeatortoise/111782434593735690 | wandering.shop | 2024-01-20T16:48:37Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Apple will launch a journaling app | https://arstechnica.com/gadgets/2023/04/apple-plans-mental-health-focused-journaling-app-for-ios-17/ | arstechnica.com | 2023-04-22T01:46:18Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Azure ChatGPT: Private and secure ChatGPT for internal enterprise use |  | github.com | 2023-08-13T23:15:44Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Azure ChatGPT: Private and secure ChatGPT for internal enterprise use | https://github.com/microsoft/azurechatgpt | github.com | 2023-08-13T23:15:44Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Bard is now Gemini, and we’re rolling out a mobile app and Gemini Advanced |  | blog.google | 2024-02-08T18:15:31Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Bard is now Gemini, and we’re rolling out a mobile app and Gemini Advanced | https://blog.google/products/gemini/bard-gemini-advanced-app/ | blog.google | 2024-02-08T18:15:31Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Basic Attention Token | https://basicattentiontoken.org/ | basicattentiontoken.org | 2017-03-23T18:02:12Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Bing: “I will not harm you unless you harm me first” | https://simonwillison.net/2023/Feb/15/bing/ | simonwillison.net | 2023-02-15T19:06:58Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Bluesky and the AT Protocol: Usable decentralized social media | https://arxiv.org/abs/2402.03239 | arxiv.org | 2024-02-07T05:42:14Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| CancelQuora | https://interestingauthors.com/blog/experience/quora/ | interestingauthors.com | 2023-10-08T14:14:36Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| ChatGPT gift advsior: personalized gifts for every person and occasion | https://dreamgift.ai/ | dreamgift.ai | 2023-06-22T20:12:23Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Cybercriminals who breached Nvidia issue one of the most unusual demands ever | https://arstechnica.com/information-technology/2022/03/cybercriminals-who-breached-nvidia-issue-one-of-the-most-unusual-demands-ever/ | arstechnica.com | 2022-03-04T07:03:26Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Deepmind is working on a rival to ChatGPT |  | techfundingnews.com | 2023-01-23T13:48:42Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Deepmind is working on a rival to ChatGPT | https://techfundingnews.com/chatgpt-killer-google-owned-uk-born-ai-startup-deepmind-is-working-on-a-rival/ | techfundingnews.com | 2023-01-23T13:48:42Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Defamed by ChatGPT | https://jonathanturley.org/2023/04/06/defamed-by-chatgpt-my-own-bizarre-experience-with-artificiality-of-artificial-intelligence/ | jonathanturley.org | 2023-04-07T03:46:36Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Does Google need a new CEO? |  | om.co | 2023-02-14T16:46:47Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Does Google need a new CEO? | https://om.co/2023/02/08/does-google-need-a-new-ceo/ | om.co | 2023-02-14T16:46:47Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| DuckDuckGo removed the ability to filter search results |  | github.com | 2023-04-24T05:01:09Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| DuckDuckGo removed the ability to filter search results | https://github.com/duckduckgo/duckduckgo-help-pages/commit/d35d03e532c7618bcdd2be10ea67e9e1f021dd96 | github.com | 2023-04-24T05:01:09Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Exploring GPTs: ChatGPT in a trench coat? | https://simonwillison.net/2023/Nov/15/gpts/ | simonwillison.net | 2023-11-15T19:26:21Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Five years of indie hacking |  | allisonseboldt.com | 2023-03-06T17:27:11Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Five years of indie hacking | https://allisonseboldt.com/5-years-of-indie-hacking/ | allisonseboldt.com | 2023-03-06T17:27:11Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| FreeSense: Indoor Human Identification with WiFi Signals |  | arxiv.org | 2016-08-29T17:17:23Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| FreeSense: Indoor Human Identification with WiFi Signals | http://arxiv.org/abs/1608.03430 | arxiv.org | 2016-08-29T17:17:23Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Google Is Losing Control |  | techcrunch.com | 2023-02-10T22:25:19Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Google Is Losing Control | https://techcrunch.com/2023/02/10/google-is-losing-control/ | techcrunch.com | 2023-02-10T22:25:19Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Google is screwed, even if it wins its antitrust case |  | gizmodo.com | 2023-01-26T18:48:35Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Google is screwed, even if it wins its antitrust case | https://gizmodo.com/google-bing-microsoft-chatgpt-ai-antitrust-doj-screwed-1850029781 | gizmodo.com | 2023-01-26T18:48:35Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Google search's death by a thousand cuts | https://matt-rickard.com/google-searchs-death-by-a-thousand-cuts | matt-rickard.com | 2023-07-03T21:31:30Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Hacking Google Bard – From Prompt Injection to Data Exfiltration | https://embracethered.com/blog/posts/2023/google-bard-data-exfiltration/ | embracethered.com | 2023-11-14T01:43:34Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| I made my first web0 website today. It's so cool it just works | https://elliott.computer/pages/web0.html | elliott.computer | 2021-12-28T01:45:52Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| I've never seen a post that better summarized what happened to Google | https://twitter.com/AnneNotation/status/1528524053522227200 | twitter.com | 2022-05-23T23:13:12Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| If needed, you have a role at Microsoft that matches your compensation | https://twitter.com/kevin_scott/status/1726971608706031670 | twitter.com | 2023-11-21T17:40:40Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Inkscape 1.2 released | https://inkscape.org/release/inkscape-1.2/ | inkscape.org | 2022-05-17T05:18:18Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Instagram, TikTok, and the Three Trends |  | stratechery.com | 2022-08-16T15:29:40Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Instagram, TikTok, and the Three Trends | https://stratechery.com/2022/instagram-tiktok-and-the-three-trends/ | stratechery.com | 2022-08-16T15:29:40Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Is Amazon Violating U.S. Antitrust Laws? | http://inthesetimes.com/article/21850/is-amazon-using-predatory-pricing-in-violation-of-antitrust-laws-monopoly | inthesetimes.com | 2019-04-24T00:50:06Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| I’m leaving London for NYC and taking my tech startup |  | sifted.eu | 2021-11-24T07:08:21Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| I’m leaving London for NYC and taking my tech startup | https://sifted.eu/articles/brexit-london-new-york-leaving/ | sifted.eu | 2021-11-24T07:08:21Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Kagi finally let me lay Google Search to rest | https://dannb.org/blog/2023/how-kagi-beats-google/ | dannb.org | 2023-10-12T02:56:02Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Let's End Programmer Bigotry | http://infovegan.com/2010/07/21/lets-end-programmer-bigotry | infovegan.com | 2010-07-21T16:27:18Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Light Chat(Free Alternative to ChatGPT) | https://lightchat.co | lightchat.co | 2023-07-10T03:29:37Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Lmsys-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset |  | arxiv.org | 2023-09-25T19:18:00Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Lmsys-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset | https://arxiv.org/abs/2309.11998 | arxiv.org | 2023-09-25T19:18:00Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| MK1 Flywheel Unlocks the Full Potential of AMD Instinct for LLM Inference |  | mkone.ai | 2024-01-08T12:40:25Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| MK1 Flywheel Unlocks the Full Potential of AMD Instinct for LLM Inference | https://mkone.ai/blog/mk1-flywheel-amd | mkone.ai | 2024-01-08T12:40:25Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Marketing advice from open source founders | https://cannon.wtf/marketing-advice-from-open-source-founders/ | cannon.wtf | 2023-01-11T11:49:55Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Mediocrity is underrated (or better is the enemy of good enough) |  | nayna.org | 2009-09-17T16:32:29Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Mediocrity is underrated (or better is the enemy of good enough) | http://nayna.org/blog/?p=11 | nayna.org | 2009-09-17T16:32:29Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Meta's Segment Anything written with C++ / GGML |  | github.com | 2023-09-06T07:51:07Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Meta's Segment Anything written with C++ / GGML | https://github.com/YavorGIvanov/sam.cpp | github.com | 2023-09-06T07:51:07Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Mistral 7B Fine-Tune Optimized | https://openpipe.ai/blog/mistral-7b-fine-tune-optimized | openpipe.ai | 2023-12-20T21:48:28Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Mistral Large | https://mistral.ai/news/mistral-large/ | mistral.ai | 2024-02-26T15:07:49Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Mycroft – open source voice assistant | https://mycroft.ai/ | mycroft.ai | 2022-11-22T19:14:46Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| NanoGPT | https://github.com/karpathy/nanoGPT | github.com | 2023-01-11T14:34:43Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Natural language is the lazy user interface | https://austinhenley.com/blog/naturallanguageui.html | austinhenley.com | 2023-01-27T19:26:57Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Neural Networks: Zero to Hero | https://karpathy.ai/zero-to-hero.html | karpathy.ai | 2023-04-06T01:53:18Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Offline Voice Assistant on a Microcontroller with 192KB RAM | https://picovoice.ai/blog/offline-voice-assistant-on-an-stm32-microcontroller/ | picovoice.ai | 2022-12-13T05:10:29Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Our next-generation model: Gemini 1.5 |  | blog.google | 2024-02-15T16:29:26Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Our next-generation model: Gemini 1.5 | https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/ | blog.google | 2024-02-15T16:29:26Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| PaLM 2 Technical Report [pdf] | https://ai.google/static/documents/palm2techreport.pdf | ai.google | 2023-05-10T20:19:00Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Please Sell My Personal Information | https://taylor.town/please-sell-my-personal-information | taylor.town | 2023-01-06T18:13:10Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Reddit permanently bans account of user advocating Lemmy migration | https://lemmy.ml/post/1152281 | lemmy.ml | 2023-06-06T17:49:01Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Sacrifice the first 13 years of your life to Google for 2M |  | gigatexal.blog | 2023-06-17T00:10:10Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Sacrifice the first 13 years of your life to Google for 2M | https://gigatexal.blog/pages/what-i-wish-i-did-financially-in-my-20s/what-i-wish-i-did-financially-in-my-20s.html | gigatexal.blog | 2023-06-17T00:10:10Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Saying Goodbye to GitHub | https://ersei.net/en/blog/bye-bye-github | ersei.net | 2023-04-03T10:12:48Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Secret ChatGPT plugins can be revealed by removing a parameter from an API call | https://twitter.com/rez0__/status/1639259413553750021 | twitter.com | 2023-03-25T03:57:32Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: BotEngine – Easy tool for creating chatbots | https://botengine.ai/ | botengine.ai | 2017-07-12T14:09:48Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Bubblic – end loneliness together using the power of your voice | https://bubblic.co/ | bubblic.co | 2023-08-10T05:42:08Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Concise Software Reviews | https://siftery.com/reviews | siftery.com | 2017-12-19T06:00:37Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: I made CSS Pro, a re-imagined Devtools for web design | https://csspro.com | csspro.com | 2023-06-01T14:25:31Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Image background removal without annoying subscriptions | https://pixian.ai/remove-image-backgrounds | pixian.ai | 2023-05-25T16:40:25Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Open-source background removal in the browser | https://github.com/imgly/background-removal-js | github.com | 2023-06-28T18:29:16Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Pledge Your Human-Made Content | https://nonbot.org | nonbot.org | 2023-04-28T14:52:43Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Synthical – Like HN, but for Science | https://synthical.com/feed/simple | synthical.com | 2023-09-10T15:45:16Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Show HN: Yet another macOS ChatGPT app | https://letsflyai.com | letsflyai.com | 2023-07-03T22:05:04Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Simply explained: How does GPT work? | https://confusedbit.dev/posts/how_does_gpt_work/ | confusedbit.dev | 2023-04-06T17:33:27Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Smol Developer |  | github.com | 2023-05-17T17:37:21Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Smol Developer | https://github.com/smol-ai/developer | github.com | 2023-05-17T17:37:21Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Software Eats Software Development as Andreessen Invests $10M in App Outsourcer | http://techcrunch.com/2015/12/07/software-eats-software/ | techcrunch.com | 2015-12-07T18:03:56Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Square-Enix sells all of its Western game studios and their games to Embracer | https://arstechnica.com/gaming/2022/05/embracer-acquires-tomb-raider-deus-ex-and-all-western-square-enix-game-studios/ | arstechnica.com | 2022-05-03T00:02:33Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Talk-Llama | https://github.com/ggerganov/whisper.cpp/tree/master/examples/talk-llama | github.com | 2023-11-02T14:03:40Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Tesla FSD data is getting worse, according to beta tester self-reports |  | electrek.co | 2022-12-14T19:12:31Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Tesla FSD data is getting worse, according to beta tester self-reports | https://electrek.co/2022/12/14/tesla-full-self-driving-data-awful-challenge-elon-musk-prove-otherwise/ | electrek.co | 2022-12-14T19:12:31Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| The Curse of Culture | https://stratechery.com/2016/the-curse-of-culture/ | stratechery.com | 2016-05-24T23:12:54Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| The Disappointing Tea.xyz | https://connortumbleson.com/2024/02/26/the-disappointing-tea-xyz/ | connortumbleson.com | 2024-02-26T15:20:09Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| The Terminator Is Not Coming. The Future Will Thank Us | http://recode.net/2015/03/02/the-terminator-is-not-coming-the-future-will-thank-us/?refresh=1 | recode.net | 2015-03-03T00:34:40Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| The body is the missing link for truly intelligent machines (2017) | https://aeon.co/ideas/the-body-is-the-missing-link-for-truly-intelligent-machines | aeon.co | 2019-08-22T18:30:17Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| The semantic web is dead – Long live the semantic web | https://github.com/GavinMendelGleason/blog/blob/main/entries/semantic_future.md | github.com | 2022-08-10T19:57:25Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Together API hosts open source models | https://together.ai/pricing | together.ai | 2023-07-14T22:23:17Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Top Startups From Y Combinator W14 Demo Day | http://techcrunch.com/2014/03/25/best-y-combinator-demo-day-startups/ | techcrunch.com | 2014-03-26T04:12:34Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Twitter Blue for $8/Month | https://twitter.com/elonmusk/status/1587498907336118274 | twitter.com | 2022-11-02T03:57:00Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Twitter has a new CEO – what about a new business model? |  | stratechery.com | 2021-11-30T20:22:06Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Twitter has a new CEO – what about a new business model? | https://stratechery.com/2021/twitter-has-a-new-ceo-what-about-a-new-business-model/ | stratechery.com | 2021-11-30T20:22:06Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Universal and transferable adversarial attacks on aligned language models | https://llm-attacks.org/zou2023universal.pdf | llm-attacks.org | 2023-07-30T04:20:22Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| What McKinsey got wrong about developer productivity | https://leaddev.com/process/what-mckinsey-got-wrong-about-developer-productivity | leaddev.com | 2023-10-24T15:22:09Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| White House is working with hackers to ‘jailbreak’ ChatGPT’s safeguards | https://fortune.com/2023/05/10/white-house-is-working-with-hackers-to-jailbreak-chatgpts-safeguards/ | fortune.com | 2023-05-22T22:45:26Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Why A.I. Moonshots Miss | https://slate.com/technology/2021/05/artificial-intelligence-moonshots-usually-fail.html | slate.com | 2021-05-04T19:34:56Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Why Did Microsoft Build VSCode? Turns Out, GitHub Copilot |  | codeium.com | 2023-06-14T17:45:28Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Why Did Microsoft Build VSCode? Turns Out, GitHub Copilot | https://codeium.com/blog/why-did-microsoft-build-vscode-github-copilot | codeium.com | 2023-06-14T17:45:28Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Will Electric Cars Slow the Adoption of Driverless Cars? | https://hackernoon.com/will-electric-cars-slow-the-adoption-of-driverless-cars-73793f182e30 | hackernoon.com | 2017-12-16T23:58:09Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Write code for the web |  | mrmr.io | 2024-02-04T17:59:26Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Write code for the web | https://mrmr.io/apple/ | mrmr.io | 2024-02-04T17:59:26Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| YouTube introduces channel memberships, merchandise and premieres |  | techcrunch.com | 2018-06-22T09:36:29Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| YouTube introduces channel memberships, merchandise and premieres | https://techcrunch.com/2018/06/21/youtube-introduces-channel-memberships-merchandise-and-premieres/ | techcrunch.com | 2018-06-22T09:36:29Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| YouTube is now building its own video-transcoding chips |  | arstechnica.com | 2021-05-04T07:34:51Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| YouTube is now building its own video-transcoding chips | https://arstechnica.com/gadgets/2021/04/youtube-is-now-building-its-own-video-transcoding-chips/ | arstechnica.com | 2021-05-04T07:34:51Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Zed, a collaborative code editor, is now open source |  | zed.dev | 2024-01-24T18:29:33Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Zed, a collaborative code editor, is now open source | https://zed.dev/blog/zed-is-now-open-source | zed.dev | 2024-01-24T18:29:33Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| Zen 5's Leaked Slides | https://chipsandcheese.com/2023/10/08/zen-5s-leaked-slides/ | chipsandcheese.com | 2023-10-12T13:48:22Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.6 | 0.3275 |
| FunnL- Generate B2B sales meetings that close | https://funnl.ai/signup/ | funnl.ai | 2022-12-15T06:00:05Z | 0.25 | 0.45 | 0.1 | 0.35 | 0.5 | 0.3175 |
