# New-axis proposal — arXiv:2611.16366

**Paper:** "CURATOR: Scalable Fine-grained Evidence Selection for RAG using Decision Models" (arXiv:2611.16366) — vault note [[arxiv-2611.16366]], screened 2026-11-13, score 7/10.

## What the paper shows
A fine-tuned decision model jointly selects evidence spans from large candidate pools for context-limited RAG. Quote (Abstract): "CURATOR maintains a strong evidence discrimination capability as the number of candidates increases … and improves downstream RAG performance, particularly when the available context is limited."

## Why not expressible in RAG-NIMBF today
Context compression / selection under a token budget is listed as not expressible. CURATOR operates at *span* granularity between reranking and prompting — RAG-NIMBF's pipeline passes whole chunks to the prompt builder and has no span-selection component or candidate-pool-size axis.

## What RAG-NIMBF would need
- Config key `context_selection: none | decision-model` with `context_token_budget` and candidate-pool size knob.
- New post-retrieval component hosting the decision model; span-level bookkeeping so gold-span metrics can still be computed.
- No public code or weights stated (C=1) — requires training a decision model or contacting authors, raising effort.

## Estimated effort
Large (~2+ weeks): component + budget protocol similar to the CoRA-Bench proposal (arXiv:2611.10238); a shared `context_selection` axis would cover both. Evidence is qualitative in the abstract; wait for code before prioritizing.
