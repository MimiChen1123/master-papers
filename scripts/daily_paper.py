#!/usr/bin/env python3
"""Generate one daily recommender-systems paper note."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from xml.etree import ElementTree


REPO_ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = REPO_ROOT / "papers"
TODAY = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date()

TOP_VENUES = [
    ("NeurIPS", 100),
    ("ICML", 95),
    ("ICLR", 90),
    ("SIGIR", 82),
    ("RecSys", 78),
]

SEARCH_QUERIES = [
    "recommender systems recommendation",
    "recommendation system collaborative filtering",
    "sequential recommendation recommender systems",
    "retrieval ranking recommender systems",
]


def request_json(url: str, headers: dict[str, str] | None = None) -> dict:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def normalize(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def venue_name(paper: dict) -> str:
    venue = normalize(paper.get("venue"))
    publication_venue = paper.get("publicationVenue") or {}
    pub_venue_name = normalize(publication_venue.get("name"))
    return pub_venue_name or venue


def paper_url(paper: dict) -> str:
    if paper.get("url"):
        return paper["url"]
    external_ids = paper.get("externalIds") or {}
    if external_ids.get("ArXiv"):
        return f"https://arxiv.org/abs/{external_ids['ArXiv']}"
    if external_ids.get("DOI"):
        return f"https://doi.org/{external_ids['DOI']}"
    return ""


def existing_notes_text() -> str:
    if not PAPERS_DIR.exists():
        return ""
    return "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in PAPERS_DIR.rglob("*.md"))


def existing_note_count() -> int:
    if not PAPERS_DIR.exists():
        return 0
    return len(list(PAPERS_DIR.rglob("*.md")))


def score_paper(paper: dict, seen_text: str) -> float:
    title = normalize(paper.get("title"))
    abstract = normalize(paper.get("abstract"))
    venue = venue_name(paper)
    combined = f"{title} {abstract}".lower()
    if not title or not abstract:
        return -1
    if title.lower() in seen_text.lower() or paper_url(paper) in seen_text:
        return -1
    if not any(term in combined for term in ["recommend", "recommender", "collaborative filtering", "ranking"]):
        return -1

    score = 0.0
    venue_lower = venue.lower()
    for name, weight in TOP_VENUES:
        if name.lower() in venue_lower:
            score += weight
            break

    year = paper.get("year") or 0
    if isinstance(year, int):
        score += max(0, min(30, year - 2018))

    score += min(20, (paper.get("citationCount") or 0) ** 0.5)

    if paper_url(paper):
        score += 5
    return score


def search_semantic_scholar(seen_text: str) -> list[dict]:
    fields = ",".join(
        [
            "title",
            "url",
            "abstract",
            "venue",
            "year",
            "citationCount",
            "externalIds",
            "publicationVenue",
            "openAccessPdf",
        ]
    )
    headers = {}
    if os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = os.environ["S2_API_KEY"]

    papers: list[dict] = []
    for query in SEARCH_QUERIES:
        encoded = urllib.parse.urlencode({"query": query, "limit": "100", "fields": fields})
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?{encoded}"
        try:
            data = request_json(url, headers=headers)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"Semantic Scholar search failed for {query!r}: {exc}", file=sys.stderr)
            continue
        papers.extend(data.get("data") or [])
        time.sleep(1)

    unique: dict[str, dict] = {}
    for paper in papers:
        key = paper.get("paperId") or paper_url(paper) or normalize(paper.get("title")).lower()
        unique[key] = paper

    return sorted(unique.values(), key=lambda paper: score_paper(paper, seen_text), reverse=True)


def search_arxiv_fallback(seen_text: str) -> list[dict]:
    query = urllib.parse.quote('all:"recommender systems" OR all:"recommendation system"')
    url = f"https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            root = ElementTree.fromstring(response.read())
    except (urllib.error.URLError, TimeoutError, ElementTree.ParseError) as exc:
        print(f"arXiv fallback failed: {exc}", file=sys.stderr)
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    papers = []
    for entry in root.findall("atom:entry", ns):
        title = normalize(entry.findtext("atom:title", default="", namespaces=ns))
        abstract = normalize(entry.findtext("atom:summary", default="", namespaces=ns))
        url_text = normalize(entry.findtext("atom:id", default="", namespaces=ns))
        if title.lower() in seen_text.lower() or url_text in seen_text:
            continue
        papers.append(
            {
                "title": title,
                "abstract": abstract,
                "venue": "arXiv",
                "year": TODAY.year,
                "citationCount": 0,
                "url": url_text,
            }
        )
    return papers


def fallback_summaries(abstract: str) -> dict[str, str]:
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    english = " ".join(sentences[:3]).strip() or abstract[:800]
    zh_tw = (
        "未設定 OPENAI_API_KEY，因此此處先保留可讀的摘要重點："
        + english
    )
    return {"english_summary": english, "zh_tw_summary": zh_tw}


def openai_summaries(title: str, abstract: str) -> dict[str, str]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return fallback_summaries(abstract)

    model = os.environ.get("OPENAI_MODEL") or "gpt-5-mini"
    prompt = textwrap.dedent(
        f"""
        Summarize this recommender-systems paper for a graduate student.
        Return strict JSON with keys english_summary and zh_tw_summary.

        Requirements:
        - english_summary: 2 concise paragraphs in English.
        - zh_tw_summary: 2 concise paragraphs in Traditional Chinese.
        - Mention the core problem, method, and why it matters.

        Title: {title}
        Abstract: {abstract}
        """
    ).strip()

    payload = {
        "model": model,
        "input": prompt,
        "text": {"format": {"type": "json_object"}},
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"OpenAI summary failed: {exc}", file=sys.stderr)
        return fallback_summaries(abstract)

    output_text = data.get("output_text")
    if not output_text:
        parts = []
        for item in data.get("output", []):
            for content in item.get("content", []):
                if content.get("type") in {"output_text", "text"}:
                    parts.append(content.get("text", ""))
        output_text = "\n".join(parts)

    try:
        parsed = json.loads(output_text)
    except (TypeError, json.JSONDecodeError):
        return fallback_summaries(abstract)

    return {
        "english_summary": normalize(parsed.get("english_summary")) or fallback_summaries(abstract)["english_summary"],
        "zh_tw_summary": normalize(parsed.get("zh_tw_summary")) or fallback_summaries(abstract)["zh_tw_summary"],
    }


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug[:80] or "paper"


def markdown_for(paper: dict) -> str:
    title = normalize(paper.get("title"))
    abstract = normalize(paper.get("abstract"))
    venue = venue_name(paper) or "Unknown"
    year = paper.get("year") or "Unknown"
    url = paper_url(paper) or "Unknown"
    summaries = openai_summaries(title, abstract)

    return textwrap.dedent(
        f"""\
        ---
        date: {TODAY.isoformat()}
        title: "{title.replace('"', '\\"')}"
        venue: "{venue.replace('"', '\\"')}"
        year: {year}
        ---

        # {title}

        - Paper link: {url}
        - Venue: {venue}
        - Year: {year}

        ## English Summary

        {summaries["english_summary"]}

        ## 繁中摘要

        {summaries["zh_tw_summary"]}

        ## Abstract

        {abstract}
        """
    )


def main() -> int:
    seen_text = existing_notes_text()
    candidates = search_semantic_scholar(seen_text)
    candidates = [paper for paper in candidates if score_paper(paper, seen_text) >= 0]
    if not candidates:
        candidates = search_arxiv_fallback(seen_text)

    if not candidates:
        print("No candidate paper found.", file=sys.stderr)
        return 1

    paper = candidates[existing_note_count() % len(candidates)]
    month_dir = PAPERS_DIR / TODAY.strftime("%Y-%m")
    month_dir.mkdir(parents=True, exist_ok=True)
    path = month_dir / f"{TODAY.isoformat()}-{slugify(normalize(paper.get('title')))}.md"

    if path.exists():
        print(f"Today's note already exists: {path}")
        return 0

    path.write_text(markdown_for(paper), encoding="utf-8")
    print(f"Generated {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

