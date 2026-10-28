# UCVE: Graph Structured Retrieval for Compliance Validation (arxiv-2610.37323)

**Core idea:** Represents compliance requirement spaces as a Compliance Requirement Graph; edges are learned by reinforcement learning with a violation-detection traversal reward, then retrieval runs as spectral reranking over the graph Laplacian.

**Key result (verbatim):** "UCVE averages 4.3% matched-K recall lift over flat cosine retrieval and consistently outperforms strong retrieval and graph-based baselines" (Abstract)

**Rubric:** A=2 B=2 C=1 D=1 E=1 → 7/10. Graph-structured retrieval, new RAG technique; three compliance domains with strong baselines; code/license unclear; RL edge training adds weight; not expressible in NIMBF.

**Affected axis:** New-Techniques
