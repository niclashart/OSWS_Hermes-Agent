# New-axis proposal — arXiv:2611.10238

**Paper:** "CoRA-Bench: Evaluating Evidence Preservation by Context Selectors Under Token Budgets" (arXiv:2611.10238) — vault note [[arxiv-2611.10238]], screened 2026-11-11, score 8/10.

## What the paper shows
Benchmark comparing context-selection methods (truncation, BM25, dense, dense+rerank, LLMLingua-2, Provence) under *shared token budgets*, scoring evidence preservation and downstream accuracy. Quote (Abstract): "BM25 achieves 0.921 supporting-fact recall on BABILong at 128K … and method rankings vary across evidence types and between evidence recall and downstream accuracy."

## Why not expressible in RAG-NIMBF today
RAG-NIMBF has no context-compression/selection stage and no token-budget constraint: there is no config knob that caps the prompt context at N tokens with a selectable selection method, and no evidence-preservation metrics (supporting-fact/needle/answer-bearing-turn recall against a budget). `generation_context_k` only truncates the ranked list; it does not budget tokens or swap selection strategies.

## What RAG-NIMBF would need
- Config key `context_selection: none | truncation | bm25 | dense | dense-rerank | llmlingua2 | provence` plus `context_token_budget`.
- New post-retrieval component between reranker and prompt builder; dataset adapters exposing per-question evidence annotations for the preservation metrics; evidence-recall metrics in `custom_metrics.py`.

## Estimated effort
Large (~2 weeks): the selection component is straightforward, but the evidence-annotation dataset adapters and new metric family are the real work. Datasets themselves are pluggable today via `hf-generic`.
