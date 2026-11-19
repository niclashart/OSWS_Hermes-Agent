# UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval (2611.20758)

Score: 7/10 (A 1, B 2, C 1, D 2, E 1)

## Core idea
Unified hybrid dense-sparse graph index: dynamic query weights without index rebuild.

## Key result (verbatim)
> "In the mixed-weight setting, UniGraph delivers 27.6%~52.3% higher QPS than the fastest baseline on each dataset at Recall@100 >= 0.95." (Abstract)

## Rubric justification
hybrid graph index for vector store axis; strong QPS results; C=1; runs standard hardware (D=2); needs new backend (E=1)

## Affected axis
Vector-Store: Vector-Store axis supports chroma/lancedb only; a hybrid-graph index would be a new vector_db_backend value.
