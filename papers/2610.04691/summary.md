# RAGStress: A controlled benchmark for evaluating retrieval-augmented generation under knowledge-base degradation (2610.04691)

**Score: 8/10** · [arXiv](https://arxiv.org/abs/2610.04691) · screened 2026-10-25

## Core idea
Controlled benchmark stress-testing RAG under systematic KB corruption: 4 corruption types × 3 severity levels over 182,546 MMLU-derived documents, 52,500 evaluations. Artifact bundle with generation scripts and corruption prompts.

## Key results
> "RAGStress reveals that clean retrieval can mask robustness differences, semantic-fidelity corruptions are substantially more harmful than signal-utility perturbations, no-retrieval accuracy does not predict corrupted-retrieval robustness, and mixed-KB accuracy should not be treated as worst-case robustness." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 = 8 — A2 · B2 · C1 · D2 · E1 — massive controlled design, open artifact bundle; robustness-corrupted dataset variants need a new dataset adapter.

## Affected axis
Datasets

## Relevance for RAG-NIMBF
Maps to the Datasets axis as a corruption-dimension adapter candidate (`dataset.name`); not directly loadable today → weekly fit check.
