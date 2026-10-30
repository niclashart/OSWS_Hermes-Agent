# 2610.40314 — Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG

**Score:** 8/10 · **Axis:** Query-Transformation · [arXiv](https://arxiv.org/abs/2610.40314) · [HTML](https://arxiv.org/html/2610.40314)

## Core idea
Coverage-aware retrieval for multi-aspect questions: decompose the query into subquestions, rank candidates with a coverage-trained bi-encoder, predict a document x subquestion coverage matrix with a cross-encoder, and select by greedy maximum-marginal coverage. A grounded self-feedback loop then asks the model to re-generate using evidence it underused in its first answer.

## Key results (verbatim quotes)
> "On TREC RAG 2024, our approach improves $\alpha$-nDCG@10, which rewards newly covered nuggets and discounts redundant evidence, from $0.625$ to $0.702$" (Sec. 1/Abstract (TREC RAG 2024))

## Rubric score with justification
A 2 (query decomposition + coverage selection + self-feedback loop; not expressible) · B 2 (TREC RAG 2024, oracle comparisons, ablations) · C 1 (license CC BY; code release not stated in HTML) · D 2 (bi/cross-encoder scale) · E 0 (needs decomposition + coverage-matrix + multi-pass loop)

## Affected axis
Query-Transformation: New technique: subquestion decomposition and coverage-maximizing selection are explicitly listed as not expressible (query decomposition, multi-hop loops). Candidates for new-axis.md: 'coverage_aware_selection' and 'self_feedback_passes'.
