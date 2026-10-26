# Smart Content Ingestion for Generative AI Workloads

**arXiv:** https://arxiv.org/abs/2610.07091 · **Score:** 7/10 (A2 B1 C1 D2 E1) · **Axis:** Chunking · **Screened:** 2026-10-26

## Core idea
Explicit configurable ingestion stage: selective OCR routing, structure-aware parent-child chunker (hit@1 68.6%, MRR 0.77) and read-only retrieval evaluator.

## Key results (verbatim quotes)
- "the chunker reaches hit@1 of 68.6%, hit@10 of 92.8% and MRR 0.77 over 25,050 generated questions" (Abstract)
- "content extraction becomes a lifecycle stage in its own right whose errors no downstream retriever or re-ranker can repair" (Abstract)

## Rubric justification
- A=2: structure-aware parent-child chunking is a clear Chunking-axis option
- B=1: hit@1 68.6%, MRR 0.77 on 25,050 generated questions, but single corpus
- C=1: no code release stated
- D=2: deterministic pipeline, consumer hardware
- E=1: parent-child chunking not in supported values

## RAG-NIMBF fit
`parent-child` chunking is not a supported value; candidate new-axis or `semantic` approximation in weekly fit check.
