# New-axis proposal — hf-caveman-so/trim-1

**Model:** caveman-so/trim-1 (HF) — vault note [[hf-caveman-so_trim-1]], screened 2026-11-01, score 8/10.

## What the model shows
1.2 MB LightGBM context compressor (712 gradient-boosted trees, 67 line-level features: BM25 vs. query, line-kind, position, neighbours), apache-2.0. It keeps only the lines of a context the query needs, verbatim and order-preserved, in milliseconds on one CPU core, and fails closed (returns the context unchanged on edge cases). Quote (model card): "It saves the most on long-document retrieval, where it removes most of the input and keeps the evidence."

## Why not expressible in RAG-NIMBF today
Context compression / selection under a token budget is explicitly listed as not expressible. RAG-NIMBF's pipeline goes retrieval → (optional reranker) → prompt with `generation_context_k` controlling only the *count* of documents; there is no stage that scores and drops individual lines/chunks of the retrieved context before prompt assembly. `reranker_models` is the wrong slot: trim-1 selects within documents rather than re-ordering documents.

## What RAG-NIMBF would need
- New pipeline stage between reranking and prompting: config key `context_compressor: <none | model id>` (+ `context_compressor_operating_point: <conservative | balanced | aggressive>` and optionally a `context_token_budget`).
- New component: `benchmark/context_compression.py` implementing a `Compressor` protocol (`compress(query, documents) -> documents`); trim-1 plugs in via its published Python package (CPU, tiny, deterministic — no GPU cost, no answer-quality risk from generation).
- Evaluation note: token count before/after compression should be logged next to existing metrics so quality-vs-budget is visible.

## Estimated effort
Small (~2–3 days): one protocol + one adapter class + config wiring + tests; the compressor is CPU-only and fail-closed, so integration risk is low.
