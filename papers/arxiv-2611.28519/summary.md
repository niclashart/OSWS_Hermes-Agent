# SupportChain: Trace-Calibrated Aggregation of Quote-Grounded Reasoning Chains for Multi-Hop RAG with Small Readers

arXiv: 2611.28519 · Screened: 2026-11-24 · Score: 8/10

## Core idea
Replaces the graph index of multi-hop RAG (HippoRAG 2 style) with an index-free execution scheme: split the question into hops, bind each hop's answer to a quoted sentence from a retrieved passage, score each execution's reliability from its own trace, and merge several executions by answer support and pooled reliability, stopping once support is high enough. Works with a 9B reader.

## Key results
> "With a 9B reader under the HippoRAG~2 protocol, SupportChain reaches 63.0 F1 on MuSiQue, above the best earlier result of 59.2, which used a 20B reader." (Abstract)
> "With the same reader and embedder, it is significantly better than HippoRAG~2 on all five datasets, by up to 17.2 F1, and it builds no index." (Abstract)
> "The reliability model needs only 100 answered training questions." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0
A=2: multi-hop decomposition + trace-calibrated execution merging is a new retrieval/orchestration technique; B=2: five datasets, HippoRAG 2 baseline, ablations (support vs majority voting); C=1: code availability not stated in abstract; D=2: 9B reader, consumer-GPU feasible; E=0: no NIMBF axis covers hop-wise execution with trace-based merging and early stopping — needs framework redesign.

## Affected axis
New-Techniques (multi-hop orchestration, index-free execution merging)

## Status log
- 2026-11-24 screened (score 8)
