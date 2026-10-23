# Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference

- **arXiv:** https://arxiv.org/abs/2610.30611
- **Score:** 7/10 (A: 2, B: 2, C: 1, D: 2, E: 0) — PrimeKG benchmark + ablations; training-free; code availability unclear (C=1)
- **Axis:** New-Techniques

## Core idea
SGUR: training-free agentic framework aligning a query graph with candidate hypothesis graphs via prior-weighted partial matching and active information-gain node querying to prune the candidate space.

## Key results (verbatim quotes)
> "starting from only two observed symptoms, SGUR achieves 92.5% Hit@3, outperforming the strongest Graph-RAG baseline by 9.4 percentage points while using approximately 5x fewer tokens" (Abstract)

## RAG-NIMBF relevance
Agentic active graph-querying loop - not expressible in RAG-NIMBF (new axis: agentic/active retrieval). Weekly-fit candidate.
