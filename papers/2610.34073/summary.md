# Memory Tax: Dissecting the Net Value of Agent Memory (2610.34073)

**Score:** 7/10 (A:2 B:2 C:1 D:2 E:1) · **Axis:** Evaluation · [arXiv](https://arxiv.org/abs/2610.34073)

## Core idea
Large-scale evaluation showing many dedicated memory systems underperform naive RAG over raw history; decomposes memory net value into memory benefit vs memory tax (losses from reorganization obscuring evidence).

## Key results (verbatim quotes)
> "Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underperform naive RAG in many cases, indicating a negative net value." (Abstract)

## Rubric justification
Evaluation framework with new comparison target (A=2), multi-benchmark multi-backbone (B=2), code promised (C=1), RAG reference baseline feasible (D=2), evaluation methodology contribution (E=1).

## Affected axis
Evaluation axis: motivates a `direct`-retrieval-over-history baseline for memory comparisons; NIMBF already has `retrieval_mode: direct` but not a memory-vs-RAG comparison axis.
