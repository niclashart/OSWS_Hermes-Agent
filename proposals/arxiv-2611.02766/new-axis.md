# New-axis proposal — arXiv:2611.02766

**Paper:** "EffComp: Efficient Prompt Compression via Hybrid Reinforcement & Supervised Learning" (arXiv:2611.02766) — vault note [[arxiv-2611.02766]], screened 2026-11-04, score 8/10.

## What the paper shows
A learned prompt compressor trained with hybrid RL + supervised objectives, optimizing the compression-ratio/accuracy trade-off at minimal latency. Quote (Abstract): "EffComp outperforms state-of-the-art prompt compression methods achieving the best trade-off between compression ratio and accuracy with minimal latency."

## Why not expressible in RAG-NIMBF today
Context compression / selection under a token budget is explicitly listed as not expressible. The pipeline goes retrieval → (optional reranker) → prompt; `generation_context_k` controls only the document count. No stage scores and drops sentences/tokens of the retrieved context before prompt assembly, and there is no compression-ratio metric.

## What RAG-NIMBF would need
- Pipeline stage between reranking and prompting: config key `context_compressor: <none | <model id>>` (+ `context_token_budget`).
- `benchmark/context_compression.py` with a `Compressor` protocol (`compress(query, documents, budget) -> documents`).
- Logged token counts before/after compression next to existing metrics so the quality-vs-budget trade-off is visible.

## Estimated effort
Small–medium (~3–5 days): one protocol + adapter class + config wiring + tests, following the same shape as the earlier trim-1 new-axis proposal (hf-caveman-so/trim-1, W45).
