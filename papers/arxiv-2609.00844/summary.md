# Staged Linguistic Seeding: Grounded Query Expansion for Verified-Unit QA in AI Contact Centers

**arXiv:** https://arxiv.org/abs/2609.00844 · **Score:** 8/10 (A2 B2 C1 D2 E1) · **Axis:** Query-Transformation · **Screened:** 2026-10-26

## Core idea
Offline staged query-expansion seeding of the index (human slot recipe + LLM variants + human gate) lifts hybrid R@1 by +0.27/+0.34 with no query-time generation.

## Key results (verbatim quotes)
- "SLS lifts hybrid R@1 to 0.881/0.930 (+0.27/+0.34), with gains across all five retrievers tested." (Abstract)
- "Verified-unit answering also removes free-form generation's unsupported-content surface (7-13% versus approximately 0%)." (Abstract)

## Rubric justification
- A=2: grounded staged seeding is a new variant of the Query-Transformation axis (offline instead of query-time)
- B=2: held-out variants from two industrial domains, gains across five retrievers, doc2query baseline
- C=1: no public code mentioned
- D=2: single retrieval pass, no query-time generation
- E=1: RAG-NIMBF has no index-enrichment key

## RAG-NIMBF fit
Not expressible today (index-side enrichment). Candidate for a new axis `index_expansion` (weekly fit check).
