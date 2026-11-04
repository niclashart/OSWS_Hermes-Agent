# Do Retrieval Ranking Models Capture Event Order? A Study of Timeline-Constrained Retrieval

- arXiv: https://arxiv.org/abs/2611.04343
- Screened: 2026-11-04 · Score: 7/10 · Rubric A-E: (2, 2, 1, 1, 1)
- Axis: Evaluation

## Core idea
Timeline-constrained retrieval: dense retrievers and rerankers barely beat lexical retrieval when relevance requires matching an ordered sequence of events; an order-preserving reranking method yields large gains on a new disaster-report collection.

## Key results (verbatim quotes)
> "Experiments show that state-of-the-art semantic retrievers and rerankers provide only limited improvements over lexical retrieval, suggesting that their semantic matching capabilities do not reliably capture temporal constraints." (Abstract)

## Rubric justification
A=2: new evaluation protocol + collection for order-sensitive retrieval (Evaluation axis); B=2 controlled study over multiple retrievers and rerankers; C=1 dataset described but license CC BY-SA for paper; D=1 standard models; E=1 new evaluation scenario, no direct config value.

## RAG-NIMBF relevance
Maps to the **Evaluation** axis; see vault note.
