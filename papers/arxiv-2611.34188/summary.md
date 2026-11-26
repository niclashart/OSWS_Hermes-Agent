# MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance

**Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.34188) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.34188/paper.pdf)

## Core idea
Training-free defense against indirect prompt injection in RAG: instead of detecting attacks, maximize relevance — score retrieved passages by mutual information / embedding variance under the query and drop or down-rank injected ones. The mechanism doubles as a query-conditioned reranker. Also introduces the long-context benchmark LC-Inj-SQuAD (~4,032 words per context).

## Results
> "Across all four, MINE achieves the best accuracy–security trade-off among training-free defenses. It is also the only defense that stays usable against a fully adaptive attacker, generalizes to agent tool-call injection, and achieves the lowest inference latency on long contexts." (Abstract)
> "we introduce LC-Inj-SQuAD, a long-context benchmark with an average of 4,032 words per context" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new RAG-security technique + benchmark (A); four datasets incl. adaptive-attack eval (B); paper CC BY 4.0, code repo referenced (LukeChen-go/indirect-pia-detection) but license unverified (C); embedding-based, training-free, consumer-GPU feasible (D); needs a new guardrail/reranker component in RAG-NIMBF, not a config slot (E).

## Relevance for RAG-NIMBF
Not expressible today: no guardrail / prompt-injection-defense axis; the security benchmark (LC-Inj-SQuAD) would need a dataset adapter. Candidate for `new-axis.md` in the weekly fit check.

## Status log
- 2026-11-26 screened
