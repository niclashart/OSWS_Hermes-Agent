# Beyond the Context Window: An Adaptive Entropy-Based Routing Framework for Hybrid Retrieval and Long-Context Language Models (2609.35831)

**Score: 8/10** · [arXiv](https://arxiv.org/abs/2609.35831) · screened 2026-10-25

## Core idea
EDAR routes each query at inference time either through RAG or full long-context processing, using the predictive entropy of the first generated RAG tokens; threshold tuned on held-out cost/accuracy sweep.

## Key results
> "EDAR retains 97.4% of the accuracy of the pure long-context baseline while reducing total token expenditure by 70.7%, escalating only 18.2% of incoming queries." (Results)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 = 8 — A2 · B2 · C1 · D2 · E1 — two long-context benchmarks plus held-out hallucination correlation (r=0.85); no code released; runs on small models; needs a routing component.

## Affected axis
New-Techniques

## Relevance for RAG-NIMBF
Long-context vs RAG trade-offs are explicitly listed as not expressible in RAG-NIMBF → `new-axis.md`.
