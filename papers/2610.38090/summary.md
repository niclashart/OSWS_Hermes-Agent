# 2610.38090 — Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a Distilled 4B Student on Ten Engines under Controlled Retrieval

**Score:** 8/10 · **Axis:** Reranking · [arXiv](https://arxiv.org/abs/2610.38090) · [HTML](https://arxiv.org/html/2610.38090)

## Core idea
Benchmarks 36 scorer configurations for predicting which sources generative answer engines will cite (citation share), on GEO-Bench queries answered by ten engines under controlled retrieval. Distils teacher labels into Qwen3-Reranker students (0.6B/4B/8B); releases GEO Citation Ranker 4B.

## Key results (verbatim quotes)
> "A Qwen3-Reranker-4B fine-tuned with low-rank adapters on teacher labels for other GEO-Bench queries, released as GEO Citation Ranker 4B, reaches 0.542 to 0.549 across three seeds" (Abstract)

## Rubric score with justification
A 2 (new pluggable reranker value + new evaluation target: citation share) · B 2 (229 queries x 10 engines, 1220 groups, clustered intervals) · C 2 (model, benchmark, predictions, code released) · D 2 (4B student) · E 1 (reranker drops into matrix.reranker_models; citation-share metric needs a custom metric)

## Affected axis
Reranking: Expressible in part: GEO Citation Ranker 4B is a sentence-transformers-compatible reranker value; citation-share Spearman could be a custom_metrics entry. Strong weekly-fit candidate.
