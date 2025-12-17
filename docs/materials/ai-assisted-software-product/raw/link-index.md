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
|  |  |  |  |  |  |  |  |  |  |

### Prototyping & UX
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Engineering & Tooling
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Data, RAG, and Agents
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Deployment, MLOps, and Evaluation
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Governance & Ethics
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Templates, SOPs, and Checklists
| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### General References
Use this section for links that do not fit the above buckets but still support the book.

| Title | URL | Source/Domain | Pub Date | Relevance | Authority | Recency | Completeness | Readability | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
