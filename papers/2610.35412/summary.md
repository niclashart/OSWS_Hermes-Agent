# Read the Route: Attention-Steered Hypergraph Retrieval for Multi-hop RAG (2610.35412)

**Score:** 7/10 (A:2 B:2 C:1 D:2 E:0) · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.35412)

## Core idea
HyperAddress resolves implicit entity references with attention "addressing heads" in a single forward pass, then runs Personalized PageRank on a description-labelled hypergraph for multi-hop retrieval without any query-time generation.

## Key results (verbatim quotes)
> "HyperAddress outperforms the strongest baseline by 3.5 points of Recall@5 and 7.4 points of All@5 on average, with gains that grow with the number of hops. It answers more than twice as fast and builds its index at half the cost." (Abstract / Results)

## Rubric justification
Novel attention-steered graph retrieval (A=2), three multi-hop benchmarks with strong gains (B=2), no code release found (C=1), retrieval via PageRank is cheap at query time (D=2), graph RAG not expressible (E=0).

## Affected axis
Graph RAG is explicitly not expressible today; this adds a hypergraph + attention-steered PPR variant to the New-Techniques evidence pile.
