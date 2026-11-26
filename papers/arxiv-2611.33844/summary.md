# When Rerankers Work Together: Better and Faster Reranking without Joint Training

**Score:** 8/10 · [arXiv](https://arxiv.org/abs/2611.33844) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33844/paper.pdf)

## Core idea
Systematic study of heterogeneous reranker cascades composed *without* joint training: lightweight trained coarse scorers (Cache-Pointwise, Cache-Shapley — cacheable representations, linear-time inference) placed before strong rerankers (CrossEncoder, Provence, ColBERTv2) prune candidates cheaply, improving accuracy and speed at matched budgets.

## Results
> "On NoLiMa 32K with Gemma, inserting these scorers before CrossEncoder or Provence improves answer accuracy by 4.02-9.43 percentage points while accelerating online pruning by 1.57-1.88x relative to the corresponding reranker alone." (Abstract)
> "Cache-Pointwise composed with ColBERTv2 through reciprocal rank fusion improves accuracy by 4.60 points at 1.36x speedup over direct ColBERTv2." (Abstract)
> "a cascade can outperform its final reranker alone while underperforming its coarse selector alone" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new multistage-reranking technique on an existing axis (A); NoLiMa + 2WikiMultiHopQA, ablations, stage-removal references (B); CC BY 4.0, no public code repo found (C); small scorers + open rerankers, consumer-GPU feasible (D); cascade/stage-order not expressible — RAG-NIMBF supports a single reranker slot (E).

## Relevance for RAG-NIMBF
Not expressible today: `reranker_models` is a single cross-encoder slot; no multi-stage cascade, candidate budgets per stage, or RRF fusion of rerankers. Candidate for `new-axis.md`.

## Status log
- 2026-11-26 screened
