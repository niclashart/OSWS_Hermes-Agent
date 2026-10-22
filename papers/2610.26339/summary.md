# Large-Scale Biomedical RAG: Corpus Scaling, Document Representation, Efficiency (arXiv:2610.26339)

## Core idea
Controlled large-scale evaluation of corpus scale, document representation (abstract vs flat full-text vs hierarchical full-text), and reranking for biomedical RAG, measuring retrieval latency and index storage as operational cost.

## Results
> "RAG improved three of four model configurations across the external benchmarks, with mean gains of up to 9.6 percentage points, and improved all four configurations on the held-out test set by 10.2-30.3 points" (Abstract). > "Hierarchical representation matched or outperformed flat full-text retrieval in most end-to-end comparisons while requiring 67% fewer indexed units and 44-56% less storage" (Abstract). CC BY-NC-ND 4.0.

## Rubric
A 2 · B 2 · C 1 · D 2 · E 0 — document representation + corpus scale as evaluation variables; 5 external benchmarks; NC-ND license; runnable; no representation/scale slot in NIMBF config.

## Relevance for RAG-NIMBF
Candidate new axis: document representation (abstract / flat / hierarchical); corpus size as explicit experiment variable (dataset adapter parameter).
