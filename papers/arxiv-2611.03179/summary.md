# Every Clause Counts: Instruction-Following Reranking by Multiplying Small, Answerable Questions

- arXiv: https://arxiv.org/abs/2611.03179
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (2, 2, 1, 2, 1)
- Axis: Reranking

## Core idea
DMReranker: zero-shot reranker that splits an instructed query into typed clauses answered by a small judge model; answer probabilities are multiplied into one score, obeying instructions like 'beginners only' without training.

## Key results (verbatim quotes)
> "DMReranker reaches a macro WISE of 50.9 over all six InfoSearch dimensions while keeping original-mode nDCG@10 at 82.9." (Abstract)

## Rubric justification
A=2: instruction-conditioned reranking = new Reranking option; B=2 InfoSearch benchmark vs GPT-4o listwise; C=1 no code release mentioned; D=2 small judge model; E=1 LLM-based reranker = new provider, not a CrossEncoder slot.

## RAG-NIMBF relevance
Maps to the **Reranking** axis; see vault note.
