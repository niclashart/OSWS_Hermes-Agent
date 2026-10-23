# ULME: Predictive Coupling for Mutually Reinforcing Embedding and Language Modeling

- **arXiv:** https://arxiv.org/abs/2610.30705
- **Score:** 7/10 (A: 2, B: 2, C: 2, D: 2, E: 1) — two model families, eight scales, strong baselines; CC BY 4.0; <=8B fits consumer GPUs
- **Axis:** Embedding

## Core idea
Post-training framework unifying embedding and generation on a causal decoder-only LLM via learnable slot tokens and a stop-gradient predictive loss; released checkpoints 0.5B-8B (Qwen2.5/Qwen3).

## Key results (verbatim quotes)
> "a single ULME checkpoint improves MTEB by 3.3-4.1 points over the strongest open-source baseline, tightens BRIGHT and AdvBench-IR simultaneously, and remains on par with a generation-only fine-tune on standard accuracy benchmarks" (Abstract)

## RAG-NIMBF relevance
ULME checkpoints plug into existing NIMBF slots (Embedding via sentence-transformers/HF id, Generator via OpenAI-compatible endpoint) - enables one-model-both-roles experiment. Weekly-fit candidate.
