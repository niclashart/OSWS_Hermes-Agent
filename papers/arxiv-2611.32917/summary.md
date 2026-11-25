# SOARS: System One Assisted Reranking for Agentic Search (arxiv-2611.32917)

**Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.32917)

## Core idea
Training-free reranking for deep-search agents: a fast "System One" model estimates calibrated relevance and reranks candidates in a single call at each search step, jointly considering the original question and the agent's sub-query — cutting search calls, latency and cost while improving accuracy.

## Results
> "On BrowseComp-Plus, it improves GPT-5.4 Mini's accuracy from 73.9% to 84.7% while reducing search calls from 23 to 14" (Abstract)
> "Across six LLM backbones on BrowseComp-Plus and WebShaper, SOARS consistently improves answer accuracy and evidence recall while reducing search calls, end-to-end latency, and inference cost." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 0 — LLM-based reranking inside an agentic search loop is a clear new technique; strong multi-backbone experiments; training-free but license CC BY-NC-ND and no code stated; relies on large LLM backbones; not expressible in RAG-NIMBF (LLM reranking = new provider; agentic search loop beyond MCP agentic).

## Relevance for RAG-NIMBF
New-Techniques: LLM reranking provider + per-round reranking in iterative retrieval.

## Status log
- 2026-11-25 screened
