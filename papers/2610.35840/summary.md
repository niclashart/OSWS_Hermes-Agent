# ACARE: Agent-Context-Aware Reranker for Iterative Search (2610.35840)

**Score:** 7/10 (A:2 B:2 C:1 D:2 E:0) · **Axis:** Reranking · [arXiv](https://arxiv.org/abs/2610.35840)

## Core idea
ACARe is a compact 4B LLM reranker that scores documents against the agent-generated sub-query together with the broader task and agent reasoning context, improving retrieval quality in agentic/iterative search while reducing the number of searches.

## Key results (verbatim quotes)
> "Across multiple benchmarks and agent families, ACARe improves retrieval quality over its base reranker while reducing search effort." (Abstract)

## Rubric justification
Clear new reranking option (A=2), multi-benchmark evidence (B=2), model announced but code not yet released (C=1), 4B model runs on consumer GPU (D=2), needs agentic search loop integration (E=0).

## Affected axis
The reranker itself could be a `matrix.reranker_models` value once weights ship, but its context-aware use presupposes an iterative agentic search loop that RAG-NIMBF cannot express; new axis candidate (agentic retrieval context).
