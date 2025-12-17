#!/usr/bin/env python3
"""
Bulk-harvest external links for the AI-Assisted Software Product book.

Features
- Pulls search results from Bing Web Search (or API-compatible endpoint).
- Iterates through themed keyword bundles to reach 3,000+ unique URLs.
- Applies light heuristics to categorize and score each result with traceable reasons.
- Writes a CSV that matches the Markdown index schema.

Usage
  python tools/link_harvester.py --api-key "$BING_SEARCH_KEY" --out docs/materials/ai-assisted-software-product/raw/link-index.csv
"""
from __future__ import annotations

import argparse
import csv
import dataclasses
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Optional

import requests

try:
    from duckduckgo_search import DDGS
except ImportError:  # pragma: no cover - optional dependency
    DDGS = None

CATEGORY_KEYWORDS: Dict[str, List[str]] = {
    "Discovery & Product Strategy": [
        "product strategy",
        "market research",
        "monetization",
        "pricing",
        "user research",
        "positioning",
        "problem discovery",
    ],
    "Prototyping & UX": [
        "prototype",
        "wireframe",
        "design system",
        "ux",
        "prompt ux",
        "ai-first ux",
        "usability testing",
    ],
    "Engineering & Tooling": [
        "platform engineering",
        "ci/cd",
        "sdk",
        "security",
        "performance",
        "architecture",
    ],
    "Data, RAG, and Agents": [
        "rag",
        "vector database",
        "retrieval",
        "agent",
        "tool use",
        "data pipeline",
        "feature store",
    ],
    "Deployment, MLOps, and Evaluation": [
        "llmops",
        "mlops",
        "deployment",
        "observability",
        "evaluation",
        "canary",
        "rollback",
    ],
    "Governance & Ethics": [
        "governance",
        "privacy",
        "safety",
        "fairness",
        "compliance",
        "risk management",
        "policy",
    ],
    "Templates, SOPs, and Checklists": [
        "playbook",
        "sop",
        "runbook",
        "checklist",
        "how-to",
    ],
}

DEFAULT_QUERIES: List[str] = [
    "AI product strategy", "AI monetization", "AI pricing", "LLM user research", "AI product discovery",
    "AI wireframes", "AI design system", "prompt UX", "AI-first UX patterns", "LLM usability testing",
    "AI engineering platform", "AI SDLC", "LLM SDK", "LLM security", "AI performance tuning",
    "RAG architecture", "vector database benchmark", "LLM agent framework", "tool use orchestrator",
    "LLM deployment", "LLM observability", "LLM evaluation", "AI canary rollout", "LLM rollback playbook",
    "AI governance", "LLM privacy", "AI fairness", "AI safety policy", "LLM compliance",
    "AI product checklist", "LLM runbook", "AI SOP", "prompt engineering checklist",
]

AUTHORITY_PRIORS = {
    ".gov": 0.9,
    ".edu": 0.85,
    "microsoft.com": 0.8,
    "openai.com": 0.8,
    "aws.amazon.com": 0.78,
    "google.com": 0.78,
    "meta.com": 0.76,
    "anthropic.com": 0.76,
}

BLACKLISTED_DOMAINS = {"pinterest.com", "reddit.com", "quora.com"}


@dataclasses.dataclass
class LinkRecord:
    title: str
    url: str
    source_domain: str
    pub_date: Optional[str]
    category: str
    score_relevance: float
    score_authority: float
    score_recency: float
    score_completeness: float
    score_readability: float
    score_reason: str

    @property
    def score_total(self) -> float:
        return round(
            0.35 * self.score_relevance
            + 0.25 * self.score_authority
            + 0.15 * self.score_recency
            + 0.15 * self.score_completeness
            + 0.10 * self.score_readability,
            4,
        )


class LinkHarvester:
    def __init__(
        self,
        api_key: str,
        endpoint: str,
        pages_per_query: int,
        page_size: int = 50,
        provider: str = "bing",
        target_count: int = 3200,
        seed_urls: Optional[Iterable[str]] = None,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.pages_per_query = pages_per_query
        self.page_size = page_size
        self.provider = provider.lower()
        self.target_count = target_count
        self.seed_urls = set(seed_urls or [])

    def harvest(self, queries: Iterable[str]) -> List[LinkRecord]:
        seen: set[str] = set(self.seed_urls)
        results: List[LinkRecord] = []
        counts = defaultdict(int)

        for query in queries:
            if self.provider == "duckduckgo":
                for item in self._duckduckgo_search(query):
                    if self._handle_item(item, query, seen, results, counts):
                        break
            elif self.provider == "hn":
                for page in range(self.pages_per_query):
                    for item in self._hn_search(query, page):
                        if self._handle_item(item, query, seen, results, counts):
                            break
                    if len(results) >= self.target_count:
                        break
            else:
                for page in range(self.pages_per_query):
                    offset = page * self.page_size
                    for item in self._bing_search(query, offset):
                        if self._handle_item(item, query, seen, results, counts):
                            break
                    if len(results) >= self.target_count:
                        break
            if len(results) >= self.target_count:
                break
        return results

    def _handle_item(
        self,
        item: dict,
        query: str,
        seen: set[str],
        results: List[LinkRecord],
        counts: Dict[str, int],
    ) -> bool:
        url = (
            item.get("url")
            or item.get("link")
            or item.get("href")
            or item.get("story_url")
        )
        if not url or url in seen:
            return False
        domain = self._extract_domain(url)
        if domain in BLACKLISTED_DOMAINS:
            return False
        seen.add(url)
        record = self._build_record(query, item, domain, url)
        counts[record.category] += 1
        results.append(record)
        return len(results) >= self.target_count

    def _bing_search(self, query: str, offset: int) -> List[dict]:
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": query, "count": self.page_size, "offset": offset, "mkt": "en-US"}
        resp = requests.get(self.endpoint, headers=headers, params=params, timeout=20)
        resp.raise_for_status()
        payload = resp.json()
        return payload.get("webPages", {}).get("value", [])

    def _duckduckgo_search(self, query: str) -> List[dict]:
        if DDGS is None:
            raise RuntimeError(
                "duckduckgo_search is not installed. Install it or use provider=bing."
            )
        max_results = self.page_size * self.pages_per_query
        with DDGS() as ddgs:
            return list(
                ddgs.text(
                    query,
                    region="us-en",
                    safesearch="moderate",
                    max_results=max_results,
                )
            )

    def _hn_search(self, query: str, page: int) -> List[dict]:
        params = {"query": query, "page": page, "hitsPerPage": self.page_size}
        resp = requests.get(
            "https://hn.algolia.com/api/v1/search", params=params, timeout=20
        )
        resp.raise_for_status()
        payload = resp.json()
        return payload.get("hits", [])

    def _build_record(self, query: str, item: dict, domain: str, url: str) -> LinkRecord:
        title = item.get("name") or item.get("title") or item.get("story_title") or ""
        snippet = (
            item.get("snippet")
            or item.get("description")
            or item.get("body")
            or item.get("story_text")
            or ""
        )
        date_published = item.get("datePublished") or item.get("date") or item.get("created_at")

        category = classify(title, snippet)
        relevance = score_relevance(query, title, snippet, category)
        authority = score_authority(domain)
        recency = score_recency(date_published)
        completeness = score_completeness(snippet, category)
        readability = score_readability(title, snippet)

        score_reason = build_score_reason(
            query=query,
            title=title,
            snippet=snippet,
            category=category,
            domain=domain,
            relevance=relevance,
            authority=authority,
            recency=recency,
            completeness=completeness,
            readability=readability,
            pub_date=date_published,
        )

        return LinkRecord(
            title=title.strip(),
            url=url,
            source_domain=domain,
            pub_date=date_published,
            category=category,
            score_relevance=relevance,
            score_authority=authority,
            score_recency=recency,
            score_completeness=completeness,
            score_readability=readability,
            score_reason=score_reason,
        )

    @staticmethod
    def _extract_domain(url: str) -> str:
        match = re.search(r"https?://([^/]+)/?", url)
        return match.group(1) if match else url


def classify(title: str, snippet: str) -> str:
    text = f"{title} {snippet}".lower()
    best_category = "General References"
    best_hits = 0
    for category, keywords in CATEGORY_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in text)
        if hits > best_hits:
            best_category, best_hits = category, hits
    return best_category


def score_relevance(query: str, title: str, snippet: str, category: str) -> float:
    text = f"{title} {snippet}".lower()
    q_terms = query.lower().split()
    matches = sum(1 for term in q_terms if term in text)
    cat_hits = sum(1 for kw in CATEGORY_KEYWORDS.get(category, []) if kw in text)
    score = min(1.0, 0.15 * matches + 0.1 * cat_hits + 0.25)
    return round(score, 4)


def score_authority(domain: str) -> float:
    domain = domain.lower()
    if domain in BLACKLISTED_DOMAINS:
        return 0.05
    for suffix, prior in AUTHORITY_PRIORS.items():
        if domain.endswith(suffix):
            return prior
    if domain.count(".") >= 2:
        return 0.55
    return 0.45


def score_recency(date_str: Optional[str]) -> float:
    if not date_str:
        return 0.55
    try:
        published = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        delta_days = (datetime.now(timezone.utc) - published).days
        if delta_days < 0:
            return 0.7
        return round(max(0.1, min(1.0, 1.0 - delta_days / 730)), 4)
    except Exception:
        return 0.55


def score_completeness(snippet: str, category: str) -> float:
    length = len(snippet.split())
    if length >= 60:
        base = 0.75
    elif length >= 30:
        base = 0.65
    elif length >= 10:
        base = 0.55
    else:
        base = 0.35
    keyword_bonus = min(0.15, 0.05 * sum(1 for kw in CATEGORY_KEYWORDS.get(category, []) if kw in snippet.lower()))
    return round(min(1.0, base + keyword_bonus), 4)


def score_readability(title: str, snippet: str) -> float:
    text = f"{title} {snippet}".lower()
    penalties = 0
    for spam in ["!!!", "???", "click", "buy", "sale", "% off"]:
        if spam in text:
            penalties += 0.1
    length = len(snippet.split())
    if length < 5 or length > 120:
        penalties += 0.1
    return round(max(0.2, 0.7 - penalties), 4)


def load_queries(extra_query_file: Optional[str]) -> List[str]:
    queries = list(dict.fromkeys(DEFAULT_QUERIES))  # dedupe, preserve order
    if extra_query_file:
        with open(extra_query_file, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    queries.append(line)
    return queries


def load_seed_urls(seed_file: str) -> set[str]:
    urls: set[str] = set()
    with open(seed_file, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            url = (row.get("URL") or row.get("Url") or row.get("url") or "").strip()
            if url:
                urls.add(url)
    return urls


def build_score_reason(
    *,
    query: str,
    title: str,
    snippet: str,
    category: str,
    domain: str,
    relevance: float,
    authority: float,
    recency: float,
    completeness: float,
    readability: float,
    pub_date: Optional[str] = None,
) -> str:
    text = f"{title} {snippet}".lower()
    q_terms = [term for term in query.lower().split() if term]
    matched_terms = [term for term in q_terms if term in text]
    matched_cats = [kw for kw in CATEGORY_KEYWORDS.get(category, []) if kw in text]
    snippet_words = len(snippet.split())

    suffix_reason = None
    for suffix in AUTHORITY_PRIORS:
        if domain.endswith(suffix):
            suffix_reason = suffix
            break
    authority_reason = (
        f"Authority {authority:.2f}: domain {domain} carries prior for {suffix_reason}"
        if suffix_reason
        else f"Authority {authority:.2f}: neutral domain {domain}"
    )

    recency_reason: str
    if pub_date:
        try:
            published = datetime.fromisoformat(pub_date.replace("Z", "+00:00"))
            days_old = (datetime.now(timezone.utc) - published).days
            recency_reason = f"Recency {recency:.2f}: published {days_old} days ago"
        except Exception:
            recency_reason = f"Recency {recency:.2f}: used neutral fallback (unparsable date)"
    else:
        recency_reason = "Recency {:.2f}: missing date, neutral score".format(recency)

    completeness_reason = (
        f"Completeness {completeness:.2f}: {snippet_words} words in snippet with {len(matched_cats)} category keyword hits"
    )

    spam_tokens = [tok for tok in ["!!!", "???", "click", "buy", "sale", "% off"] if tok in text]
    readability_reason = (
        f"Readability {readability:.2f}: penalized for {', '.join(spam_tokens)}"
        if spam_tokens
        else f"Readability {readability:.2f}: snippet length {snippet_words} words"
    )

    relevance_reason = (
        f"Relevance {relevance:.2f}: matched query terms {matched_terms} and {len(matched_cats)} category keywords for {category}"
    )

    return " | ".join(
        [
            relevance_reason,
            authority_reason,
            recency_reason,
            completeness_reason,
            readability_reason,
        ]
    )


def write_csv(records: List[LinkRecord], out_path: str) -> None:
    fieldnames = [
        "Title",
        "URL",
        "Source/Domain",
        "Pub Date",
        "Category",
        "Relevance",
        "Authority",
        "Recency",
        "Completeness",
        "Readability",
        "Total",
        "Score Reason",
    ]
    with open(out_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "Title": record.title,
                    "URL": record.url,
                    "Source/Domain": record.source_domain,
                    "Pub Date": record.pub_date or "",
                    "Category": record.category,
                    "Relevance": record.score_relevance,
                    "Authority": record.score_authority,
                    "Recency": record.score_recency,
                    "Completeness": record.score_completeness,
                    "Readability": record.score_readability,
                    "Total": record.score_total,
                    "Score Reason": record.score_reason,
                }
            )


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Harvest AI-assisted software product links.")
    parser.add_argument(
        "--api-key",
        default=os.getenv("BING_SEARCH_KEY"),
        help="API key for Bing Web Search or compatible endpoint (ignored for duckduckgo).",
    )
    parser.add_argument(
        "--endpoint",
        default="https://api.bing.microsoft.com/v7.0/search",
        help="Search endpoint URL (bing only).",
    )
    parser.add_argument(
        "--pages-per-query",
        type=int,
        default=10,
        help="Number of pages per query (count x pages).",
    )
    parser.add_argument(
        "--page-size", type=int, default=50, help="Results per page (API max is often 50)."
    )
    parser.add_argument(
        "--provider",
        choices=["bing", "duckduckgo", "hn"],
        default="bing",
        help="Search provider to use.",
    )
    parser.add_argument(
        "--target-count", type=int, default=3200, help="Stop once this many unique links are collected."
    )
    parser.add_argument("--extra-query-file", help="Optional path to a file with extra queries (one per line).")
    parser.add_argument("--seed-file", help="Optional CSV to pre-load URLs and avoid duplicates.")
    parser.add_argument("--out", required=True, help="Output CSV path.")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    if args.provider == "bing" and not args.api_key:
        sys.stderr.write("Error: provide --api-key or set BING_SEARCH_KEY.\n")
        return 1

    queries = load_queries(args.extra_query_file)
    seed_urls = load_seed_urls(args.seed_file) if args.seed_file else None
    harvester = LinkHarvester(
        api_key=args.api_key,
        endpoint=args.endpoint,
        pages_per_query=args.pages_per_query,
        page_size=args.page_size,
        provider=args.provider,
        target_count=args.target_count,
        seed_urls=seed_urls,
    )
    records = harvester.harvest(queries)
    write_csv(records, args.out)
    print(f"Wrote {len(records)} records to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
