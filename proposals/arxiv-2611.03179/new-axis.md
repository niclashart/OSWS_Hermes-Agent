# New-axis proposal — arXiv:2611.03179

**Paper:** "Every Clause Counts: Instruction-Following Reranking by Multiplying Small, Answerable Questions" (arXiv:2611.03179, DMReranker) — vault note [[arxiv-2611.03179]], screened 2026-11-04, score 8/10.

## What the paper shows
A zero-shot reranker that splits an instructed query into typed clauses, each answered yes/no by a small judge model; clause answer probabilities are multiplied into one ranking score, so instructions like "beginners only" are obeyed without training. Quote (Abstract): "DMReranker reaches a macro WISE of 50.9 over all six InfoSearch dimensions while keeping original-mode nDCG@10 at 82.9."

## Why not expressible in RAG-NIMBF today
`reranker_models` accepts only cross-encoders; a clause-decomposition + judge-probability pipeline is an LLM-based reranker (explicitly a new provider). Additionally, the *instructed-query* dimension — evaluating whether retrieval obeys query constraints — has no axis: RAG-NIMBF's prompt templates act on generation, not on retrieval-time instruction following.

## What RAG-NIMBF would need
- Reranker provider kind `llm-clause` in `benchmark/reranker.py` (decompose query via LLM, judge clauses per candidate, aggregate scores); reuses existing LLM providers.
- Evaluation option: an instruction-following metric (clause-satisfaction rate) reported alongside nDCG@k — fits the custom-metric plugin mechanism.

## Estimated effort
Medium (~1 week): provider class + one custom metric + tests; judge can run on a small local model (consumer-feasible, zero-shot — no training).
