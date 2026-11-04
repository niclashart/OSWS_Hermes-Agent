# From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory

- arXiv: https://arxiv.org/abs/2611.00450
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (2, 2, 2, 2, 0)
- Axis: New-Techniques

## Core idea
ResMem: distills retrieved evidence offline into a parametric memory that predicts an additive logit residual; cuts teacher-construction storage 94.7% vs kNN and breaks 21% fewer correct answers than a kNN-trained memory.

## Key results (verbatim quotes)
> "ResMem reduces the storage retained for teacher construction by 94.7% compared with the evaluated kNN pipeline. Across five question answering datasets, ResMem raises mean token F1 from 32.83% for the frozen LLM to 34.48%." (Abstract)

## Rubric justification
A=2: retrieval-to-parametric-memory; B=2 five QA datasets; C=2 code + HF weights (MIT/Apache family); D=2 7B Mistral quantized; E=0: requires a training loop — not expressible as a RAG-NIMBF config value.

## RAG-NIMBF relevance
Not expressible as a single config value — new technique (see New-Techniques / New-Techniques).
