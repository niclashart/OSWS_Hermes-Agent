# New-axis proposal — arXiv:2610.38090

**Paper:** "Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a Distilled 4B Student on Ten Engines under Controlled Retrieval" (arXiv:2610.38090) — vault note [[2610.38090]], screened 2026-10-30, score 8/10.

## What the paper shows
Benchmarks 36 scorers for predicting which sources generative answer engines cite, and releases GEO Citation Ranker 4B (LoRA on Qwen3-Reranker-4B, apache-2.0, HF: `citead/geo-citation-ranker-4b`, ~10 GB bf16 on one GPU). Quote (Abstract): "A Qwen3-Reranker-4B fine-tuned with low-rank adapters on teacher labels for other GEO-Bench queries, released as GEO Citation Ranker 4B, reaches 0.542 to 0.549 across three seeds" (citation-share Spearman), beating the 9B zero-shot decision model (0.516).

## Why not expressible in RAG-NIMBF today
Two separate gaps:

1. **The reranker itself is nearly pluggable but not loadable.** The ranker is a PEFT LoRA adapter over Qwen3-Reranker-4B — a causal-LM yes/no log-odds scorer (`predict.py` template), not a `sentence_transformers.CrossEncoder`. `benchmark/reranker.py::get_reranker` supports only `huggingface:` + CrossEncoder, so `reranker_models` cannot load it. A generic Qwen3-Reranker (log-odds) provider would make it (and Qwen3-Reranker-0.6B) usable.
2. **The evaluation target is new.** Citation-share prediction (Spearman against which sources an answer engine cites) is not any existing RAG-NIMBF metric; it presupposes an answer-engine-in-the-loop setup that the framework does not have.

## What RAG-NIMBF would need
- New reranker provider `qwen-reranker` (or generic `peft-logodds`): loads base + LoRA adapter, scores (query, passage) pairs via yes/no logit difference — reuses the existing `Reranker` protocol and `reranker_models` slot unchanged.
- New custom metric `citation_share_spearman` plus a dataset source containing engine-citation labels (citead/geo-citation-benchmark).

## Estimated effort
- Reranker provider: small-medium (~2–3 days: one class in `benchmark/reranker.py`, transformers+peft dependency, tests).
- Citation-share metric + engine-label dataset: medium (~1 week, needs the engine-answer labels as gold).
