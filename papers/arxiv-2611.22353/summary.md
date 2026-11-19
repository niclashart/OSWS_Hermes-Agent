# NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval (2611.22353)

Score: 8/10 (A 2, B 2, C 1, D 2, E 1)

## Core idea
Non-semantic strings outrank relevant passages in dense retrievers (semanticity gap probe).

## Key result (verbatim)
> "Across five BEIR-style datasets and three popular single-vector retrievers, these strings frequently outscore the retriever's own best judged query-relevant passage (QRP), and often rank first in the full corpus." (Abstract)

## Rubric justification
new evaluation probe for dense retrievers; 5 BEIR datasets; C=1; black-box probe runs cheap (D=2); evaluation-side integration (E=1)

## Affected axis
Evaluation: Evaluation axis: could become a custom retrieval metric (semanticity-gap probe) via custom_retrieval_metrics_mode / custom_metrics; needs new metric implementation.
