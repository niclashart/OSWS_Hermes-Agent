# New-axis proposal — arXiv:2611.02550

**Paper:** "Re$^3$Rank: Listwise Reranking with Reasoning-Conditioned Retrieval Heads" (arXiv:2611.02550) — vault note [[arxiv-2611.02550]], screened 2026-11-04, score 9/10.

## What the paper shows
Generator LLM writes a reasoning trace conditioned on the query and candidate list; a small scorer reads relevance off the trace's retrieval-head activations to produce a listwise ranking. Quote (Abstract): "our 4B variant exceeds the strongest baseline by 3.11 NDCG@10 points on average, and even our 0.6B variant surpasses rerankers with up to 32B parameters."

## Why not expressible in RAG-NIMBF today
`reranker_models` accepts only sentence-transformers `CrossEncoder` models (reference/nimbf-capabilities.md: "Only cross-encoders; late interaction (ColBERT) / LLM rerankers = new provider"). A listwise reranker that needs (a) a generator call producing a reasoning trace and (b) a scorer over the trace cannot be expressed as a cross-encoder slot value.

## What RAG-NIMBF would need
- New reranker provider kind `llm-listwise` beside the `CrossEncoder` path in `benchmark/reranker.py`: config values like `llm-listwise:<generator-model>+<scorer-model>`.
- Component interface `rerank(query, documents) -> documents` implemented as two-stage pipeline (generate trace → score traces → order documents); reuses existing `llm_models` provider plumbing.
- Cost note: per-query LLM calls should be logged into the existing efficiency/token-cost tracking.

## Estimated effort
Medium (~1 week): provider class + registry wiring + tests; generation and scoring reuse existing provider code. The 0.6B scorer variant is consumer-GPU/Ollama-feasible.
