# Automated Enrichment Analysis with GraphRAG: Efficient Multi-Database ORA Extraction and Biological Interpretation

- **arXiv:** https://arxiv.org/abs/2610.30710
- **Score:** 7/10 (A: 2, B: 2, C: 2, D: 2, E: 0) — open code (github.com/ggnb367/GBOR-RAG), multiple baselines and ablations, consumer-feasible
- **Axis:** New-Techniques

## Core idea
GBOR-RAG: graph RAG over a multi-database term-gene knowledge graph; prize-collecting subgraph retrieval conditions the LLM, plus a claim-level faithfulness metric for generated interpretations.

## Key results (verbatim quotes)
> "graph-based ORA preserves conventional ORA results with high consistency (mean Pearson r=0.997) while reducing query time by a median of 37x (up to 48x)" (Abstract)

## RAG-NIMBF relevance
Graph RAG not expressible in RAG-NIMBF (no graph adapter). new-axis.md candidate; claim-level faithfulness also an Evaluation-axis extension.
