# The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation over Curated Corpora (2609.24885)

**Score: 9/10** · [arXiv](https://arxiv.org/abs/2609.24885) · screened 2026-10-25

## Core idea
Introduces a copy baseline ('copy ceiling') and exposure accounting for RAG evaluation: if verbatim copying of shown context already achieves recall 0.964, a model below it proves little. Decouples what a recall score establishes from whether reasoning occurred.

## Key results
> "Across ten models, grounding raised target-name recall from 0.265 unaided to about 0.92. A copy baseline, the recall a verbatim copy of the shown context already achieves, scores 0.964, and every model sits 0.022 to 0.067 below it." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 2 = 9 — A2 · B2 · C1 · D2 · E2 — ten models plus production paired study; public corpus; method is an evaluation-metric add-on (small plug-in).

## Affected axis
Evaluation

## Relevance for RAG-NIMBF
Fits `custom_metrics_*` / Evaluation axis: a copy-baseline and exposure-accounting metric is a small custom metric in RAG-NIMBF evaluations.
