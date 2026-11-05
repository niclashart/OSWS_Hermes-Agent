# New-axis proposal — arXiv:2610.37826 (DeFT-RAG)

**Paper:** "DeFT-RAG: Incrementally Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers" (arXiv:2610.37826) — vault note [[2610.37826]], screened 2026-10-30, score 7/10.

## What the paper shows
Decomposes multi-hop questions incrementally into self-contained sub-questions whose answers are cached and reused across questions. Quote (from vault note / abstract evidence): outperforms existing decomposition-based RAG on multi-hop QA while cutting repeated retrieval/generation through answer reuse.

## Why not expressible in RAG-NIMBF today
Query decomposition and multi-hop loops are explicit gaps: RAG-NIMBF has only HyDE (`retrieval_use_hyde`) and iterative multi-hop follow-up queries (`retrieval_multihop`). DeFT-RAG adds two things neither covers:

1. **Incremental decomposition with self-contained sub-questions** fed back into retrieval — beyond the follow-up-query mechanism in two ways: sub-questions are self-contained (no pronoun/coreference dependence on the parent) and the decomposition is a tree, not a linear chain.
2. **A cross-question answer cache** — sub-question/answer pairs are stored and reused when later questions hit the same sub-problem. RAG-NIMBF benchmarks every question independently and statelessly; no cache axis exists.

## What RAG-NIMBF would need
- New config keys: `query_decomposition: <none | incremental-selfcontained>` (with `decomposition_max_depth`, `decomposition_llm`), reusing the multi-hop merge path.
- New component: an optional benchmark-level sub-question/answer cache (`settings.subq_cache_enabled`) keyed by normalized sub-question text, with cache hits reported as a metric (reuse rate) so the cost trade-off is measurable.

## Estimated effort
Medium (~1–2 weeks): decomposition mode extends the existing multi-hop loop; the cache is a new stateful component with metric wiring and tests. Feasibility caveat: D/E in the rubric reflect that the paper's own pipeline is not released (E=0), so this proposal would follow the method description, not a reference implementation.
