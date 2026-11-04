# Dhārā Bench: An Evidence-Oriented Retrieval Benchmark for Indian Knowledge Systems

- arXiv: https://arxiv.org/abs/2611.03196
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (1, 2, 2, 2, 1)
- Axis: Datasets

## Core idea
Retrieval benchmark for Indian Knowledge Systems: 325 questions, 60k chunks, 7,578 relevance links, plus conjugate groups that score complete multi-passage evidence sets, with a fixed Pyserini BM25 baseline.

## Key results (verbatim quotes)
> "BM25 achieves MRR@20 of 0.315, Recall@10 of 0.182, and nDCG@10 of 0.205. On the group-annotated subset, complete-evidence scores are CE_Recall@20 = 0.294 and CE_MRR@20 = 0.141." (Abstract)

## Rubric justification
A=1: domain-specific dataset (Datasets axis); B=2 large annotated corpus + baseline; C=2 code CC BY 4.0; D=2 CPU; E=1 needs a jsonl/hf-generic adapter with group-level metrics not in RAG-NIMBF.

## RAG-NIMBF relevance
Maps to the **Datasets** axis; see vault note.
