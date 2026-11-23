# New axis proposal — Deal With It: On Better Schedules for Listwise Reranking (arxiv-2611.22392)

- Paper: https://arxiv.org/abs/2611.22392
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Dealing schedules for listwise LLM rerankers (repair queries 59% -> 14%, quality unchanged). RAG-NIMBF reranking supports only cross-encoders; listwise LLM reranking is listed as not expressible. Needs: `reranker_kind: cross-encoder|listwise-llm` plus schedule config key (deal window/interval). Effort: M.
