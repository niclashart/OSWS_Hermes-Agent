# Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document QA (2610.35542)

**Score:** 7/10 (A:2 B:2 C:1 D:1 E:1) · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.35542)

## Core idea
HyperDoc builds a document hypergraph capturing structural, logical and cross-modal relations among multimodal document elements, then performs adaptive cost-aware hyperedge selection under an input budget to pick evidence for a downstream VLM.

## Key results (verbatim quotes)
> "HyperDoc constructs a document hypergraph to explicitly capture structural, logical, and cross-modal relationships among multimodal document elements. Over this structured evidence space, HyperDoc performs adaptive cost-aware hyperedge selection based on query intent and input budget." (Abstract)

## Rubric justification
New graph-based RAG technique (A=2), three benchmarks vs SOTA baselines (B=2), code availability unclear (C=1), VLM-based pipeline heavy for 24 GB (D=1), new component needed (E=1).

## Affected axis
Not expressible: multimodal evidence selection over a hypergraph needs new config keys (evidence unit, budget-aware selector) and a document-parser + VLM adapter.
