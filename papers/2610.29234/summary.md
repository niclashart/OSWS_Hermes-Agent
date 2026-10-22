# LMVU: Learning Marginal Viewpoint Utility for Budgeted Evidence Selection (arXiv:2610.29234)

## Core idea
Lightweight ranker that selects evidence under a fixed context budget by maximising marginal viewpoint coverage: at each step it scores candidates by the viewpoints they add to the current selection. Trained with viewpoint annotations from dev splits; at inference no annotations needed. Metrics RVC1/RVC2 measure recovered viewpoint coverage.

## Results
> "Across four viewpoint-annotated benchmarks at a 1,024-token budget, LMVU achieves gains of up to 0.047 and 0.052 points in RVC$_1$ and RVC$_2$, respectively, over the strongest non-oracle baseline for each benchmark and metric, and reaches the exact viewpoint-breadth ceiling on two benchmarks" (Abstract). CC BY 4.0.

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — new budgeted evidence-selection criterion (diversity-aware reranking); 4 benchmarks + oracles; code/license unclear; runs small; needs a trained ranker component.

## Relevance for RAG-NIMBF
Not expressible: reranking axis only supports cross-encoders, not marginal-utility selection policies; would need a new selection component + coverage metric.
