# New-axis proposal — arXiv:2611.07631

**Paper:** "MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents" (arXiv:2611.07631) — vault note [[arxiv-2611.07631]], screened 2026-11-07, score 8/10.

## What the paper shows
Training-free agent-memory lifecycle: judge-gated consolidation (LLM-judge ensemble certifies merges as lossless before compressing) and retrospective attribution (after each query, estimate which retrieved memories supported the answer and update retrieval priority, plus a UCB exploration bonus). Quote (Abstract): "the full retrieval stack improves evidence recall@5 by 11.92 percentage points over bare cosine, with confidence-gated feedback adding 1.50 points overall without reference answers or reranker training."

## Why not expressible in RAG-NIMBF today
Two gaps: (1) agent-memory lifecycle (merge/decay/priority) does not exist as an axis; (2) retrieval feedback without reference answers is not expressible — `custom_retrieval_metrics_mode: gold_doc` consumes gold labels, it cannot *produce* ranking updates from answer support. MEMOIR's attribution loop acts on the index between queries, which the benchmark's one-shot retrieval stage cannot represent.

## What RAG-NIMBF would need
- Config key `memory_lifecycle: <none | judge-gated-merge>` and `retrieval_feedback: <none | attribution>` (+ `feedback_rounds`).
- A stateful index component: merge/decay/priority operations over stored memories, plus a post-answer hook that adjusts retrieval priority. Reuses `eval_critic_llm` as judge.
- Multi-round retrieval evaluation mode so the effect of feedback across queries is measurable.

## Estimated effort
Large (~2–3 weeks): stateful benchmark runs and an index mutation API are new infrastructure; the attribution scorer itself is small (local judge ensemble, consumer-feasible).
