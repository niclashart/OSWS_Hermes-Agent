# CA-RAG: Constraint-Aligned Retrieval for Structurally Faithful Long-Form Generation

**Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.33497) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.33497/paper.pdf)

## Core idea
Retrieval conditioning for compliance-sensitive long-form generation: augment section-specific queries with ontology-derived structural constraints and policy-grounded knowledge-graph relations before evidence selection, so retrieved evidence supports mandatory clauses, not just semantic relevance.

## Results
> "At $k=6$, CA-RAG increases Precision@$k$ from $0.5268$ to $0.5692$, pooled Recall@$k$ from $0.5402$ to $0.5950$, and F1@$k$ from $0.5389$ to $0.5672$ over standard RAG." (Abstract / Sec. 5.1)
> "these gains cannot be attributed to prompting or decoding and provide direct evidence that structural conditioning changes evidence selection before generation" (Sec. 5.1)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new query-transformation/retrieval technique, knowledge-graph grounded (A); three domains, manual evidence annotation, ablations (B); CC BY 4.0, no public code found (C); needs ontology + KG per domain, feasible but domain setup heavy (D); query rewriting beyond HyDE/multi-hop not expressible in RAG-NIMBF (E).

## Relevance for RAG-NIMBF
Not expressible today: constraint-aligned query expansion (ontology/KG terms) is not HyDE or multi-hop follow-up; needs a new query-transformation value. Candidate for `new-axis.md`.

## Status log
- 2026-11-26 screened
