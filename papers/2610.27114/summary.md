# Joint Constraint Aggregation (JCA) for Qualifier-Sensitive RAG QA (arXiv:2610.27114)

## Core idea
Answer-selection stage for qualifier-sensitive questions: when a competing answer satisfies only some requirements but is frequent in retrieved passages, models pick it. JCA compares all candidates against the same question-derived requirements using the retrieved evidence, instead of scoring candidate-level support independently.

## Results
> "Across three evaluation settings and three instruction-tuned backbones, JCA improves overall accuracy, and its advantage grows when retrieval favors a competing answer" (Abstract). Hard-slice: Llama4-Scout staged-JCA beats BGE-large reranking by 51.0/39.6/35.3 points on AmbigQA / AmbigQA-Extracted / SituatedQA (Sec. Results table). CC BY 4.0.

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — new answer-selection technique; 3 settings, 3 backbones, manipulation experiment; license unclear; runs on instruction-tuned open models; needs new component.

## Relevance for RAG-NIMBF
Not expressible: post-retrieval candidate-vs-requirements comparison is neither reranking nor prompting; would need a new answer-selection axis.
