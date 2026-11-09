# New-axis proposal — arXiv:2611.09807

**Paper:** "Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation" (arXiv:2611.09807) — vault note [[arxiv-2611.09807]], screened 2026-11-09, score 8/10.

## What the paper shows
Instead of retrieving from the raw transcript, each conversational turn is compacted into atomic facts held in a two-tier store (working + archive) with decay/reinforcement weights. Quote (Abstract): "compaction scores 71.4 per cent against 64.6, a lead of 6.8 points (p = 5.5e-08) at 34 per cent fewer prompt tokens" on LoCoMo.

## Why not expressible in RAG-NIMBF today
RAG-NIMBF has no memory-lifecycle axis: there is no stage that transforms conversation history into a compacted/weighted store before retrieval, and no config knobs for compaction, decay or reinforcement. The paper's approach replaces the retrieval corpus, not a retrieval parameter.

## What RAG-NIMBF would need
- Config key `conversational_memory: <none | transcript-rag | compaction>` (+ `memory_tier_count`, `memory_decay`, `memory_reinforcement` as sub-knobs).
- New component between the dataset and the retriever that maintains the store across a conversation and serves it as either retrieval corpus or prompt context; paired-evaluation mode (same questions to both arms, McNemar on discordant pairs) matches the paper's design and would be a new comparison mode beside `retrieval_mode: retrieval|direct`.

## Estimated effort
Large (~2–3 weeks): stateful multi-turn evaluation is new to the framework (current benchmarks are single-turn); the compaction component itself is a prompt pipeline and is consumer-feasible, but the paired-comparison harness is the real work.
