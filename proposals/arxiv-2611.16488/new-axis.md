# New-axis proposal — arXiv:2611.16488

**Paper:** "Active Learning of Approximate LLM Ranking for Energy-Efficient Retrieval of Long Queries" (arXiv:2611.16488) — vault note [[arxiv-2611.16488]], screened 2026-11-13, score 7/10.

## What the paper shows
LAAM inserts a lightweight learned predictor between semantic retrieval and LLM reranking; active learning labels only the most informative documents with the LLM. Quote (Abstract): "LAAM achieves 87% of average P@10 achieved by DeepSeek's reranking (0.459 vs. 0.526), while requiring only 3.3% of the per-query energy consumption."

## Why not expressible in RAG-NIMBF today
Two gaps: (1) LLM-based reranking itself is a missing provider ("late interaction (ColBERT) / LLM rerankers = new provider"), and LAAM adds a *learned filter in front of it* with an active-learning training loop — no such component or energy-budget axis exists. (2) Per-query energy is reported, but the Efficiency axis measures LLM load/runtime/token cost, not retrieval-stage joules.

## What RAG-NIMBF would need
- New reranker provider `reranker_kind: llm` plus a filter component `rerank_prefilter: none | learned-approx` with `prefilter_keep_fraction`.
- Energy metric for the reranking path (per-query kWh or CO2e) in the efficiency monitor.
- Caveat: needs a proprietary LLM (DeepSeek v3) as teacher and trained predictor weights (no code released, C=1) — not consumer-GPU reproducible until weights are published.

## Estimated effort
Large (~2 weeks): two new components plus an energy meter; reproducibility is blocked on released artifacts, so defer until code/weights appear.
