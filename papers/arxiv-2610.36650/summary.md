# TACO-Graph: Automated Construction of Text-Attributed Graphs (arXiv-2610.36650)

## Core idea
A decision-tree framework that learns which text-attributed-graph (TAG) construction choices (which entities become nodes, which relations become edges, what text nodes carry) work best for a given dataset and task. It enumerates valid TAG variants, scores each with fast proxy evaluations on small subsets (GNN node-classification accuracy; RAGAS for GraphRAG retrieval), and trains an interpretable decision tree to predict construction quality. Open-source pipeline: https://github.com/AmiriHayes/text_attributed_graphs.

## Results
> "our decision trees predict construction quality on separately drawn evaluation samples with mean Spearman ρ above 0.9 for node classification and above 0.8 for GraphRAG retrieval" (Abstract)

> "while GNN node classification depends heavily on rich textual context, GraphRAG retrieval is driven primarily by relational edge structure here." (Sec. 4.2)

> "the winning constructions shift with the dataset as well as the task." (Sec. 4.1)

Five datasets (citation network, e-commerce, bibliographic); trees reach R² > 0.99 on training scores (Sec. 4.2); best Amazon Sports GraphRAG variant scores 74.2 vs 54.4 for a poor construction (Fig. 3).

## Rubric
A 2 · B 2 · C 2 · D 2 · E 1 — graph-RAG construction search is a clear new technique (graph axis needed); five datasets with strong validation; open-source CC BY 4.0; small-model proxy scoring fits consumer GPU; integration needs a new graph component.

## Relevance for RAG-NIMBF
Graph RAG is not expressible today (see nimbf-capabilities.md) → candidate for `New-Techniques` / a future graph-construction axis (node entity choice, edge semantics, node text policy as config values).

## Status log
- 2026-10-29 screened
