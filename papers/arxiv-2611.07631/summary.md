# MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents (arXiv-2611.07631)

**Core idea.** Training-free agent-memory lifecycle: (1) judge-gated consolidation — an LLM-judge ensemble certifies merges as lossless before compressing memory (with token-coverage and length gates); (2) retrospective attribution — after each query, estimate which retrieved memories supported the answer and update retrieval priority; plus a UCB exploration bonus for under-exposed memories.

**Key results.**
> "On 1,905 deduplicated LoCoMo QA pairs, the full retrieval stack improves evidence recall@5 by 11.92 percentage points over bare cosine, with confidence-gated feedback adding 1.50 points overall without reference answers or reranker training" (Abstract, Sec. 4)
> "Judge-gated merge changes the recall of text-based evidence from 58.82% to 59.08%, reduces the active store by 1.42%, and incurs 0 observed losses in 100 independently audited merges, with a one-sided 95% upper loss-rate bound of 2.95%." (Abstract)

**Rubric.** A 2 (new RAG technique: agent memory with retrieval-priority feedback — beyond existing axes) · B 2 (LoCoMo + LongMemEval-S, system baselines, bootstrap, ablations RQ1–RQ4) · C 1 (training-free, prompts given; code release not confirmed) · D 2 (local small LLM judge ensemble, consumer-feasible) · E 1 (memory lifecycle + attribution feedback = new component, not a config value) = **8/10, relevant**.

**Affected axis:** New-Techniques (memory lifecycle, retrospective retrieval feedback).

**Source:** https://arxiv.org/abs/2611.07631
