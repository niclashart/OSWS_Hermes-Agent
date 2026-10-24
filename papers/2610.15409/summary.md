# CoverSynth: Coverage-Guided Generation of Retrieval Evaluation Sets

**Axis:** [[Datasets]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.15409) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/2610.15409/paper.pdf)

## Core idea
Generator for corpus-grounded retrieval evaluation sets with explicit coverage, reliability, and difficulty objectives; deterministic checks locate evidence quotes in sources, model-based checks validate ground truth. Includes an assessment framework for evaluation sets.

## Results
> "91% of human-generated queries can be answered by all members on a panel of 12 retrieval systems, compared to only 12% of CoverSynth-generated queries." (Abstract)
> "12 of 12 within-harness model contrasts have positive nominal 95% intervals on generated sets, compared with 4 of 12 on human sets." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — new dataset/evaluation-set methodology scored against Datasets/Evaluation axes; five public corpora, strong discriminability evidence; no code license stated; LLM-based generation runs on API models; needs a new dataset adapter.

## Relevance for RAG-NIMBF
Could register a CoverSynth-generated evaluation set as a `dataset.name` adapter, but generation pipeline itself is a new component.

## Status log
- 2026-10-24 screened
