---
id: hf-OpenMed_EmbeddingGemma2-BiomedicalEvidence-270M-v2
title: "OpenMed EmbeddingGemma2-BiomedicalEvidence 270M v2"
authors: [OpenMed]
year: 2026
score: 8
rubric: {A: 1, B: 1, C: 2, D: 2, E: 2}
axis: [Embedding]
status: screened
screened: 2026-11-23
source: https://huggingface.co/OpenMed/EmbeddingGemma2-BiomedicalEvidence-270M-v2
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/hf-OpenMed_EmbeddingGemma2-BiomedicalEvidence-270M-v2/summary.md
tags: [rag-radar, Embedding]
---
# OpenMed EmbeddingGemma2-BiomedicalEvidence 270M v2

**Axis:** [[Embedding]] · **Score:** 8/10 · [HF model card](https://huggingface.co/OpenMed/EmbeddingGemma2-BiomedicalEvidence-270M-v2) · no PDF (HF model)

## Core idea
271M biomedical fine-tune of google/embeddinggemma-2 for English medical question→answer retrieval; 768-dim, 512 tokens, CPU-capable, Apache-2.0, sentence-transformers.

## Results
> "NDCG@10 91.76", "Recall@10 95.79" (model card, MedQuAD held-out dev, 1,966 questions)

Own numbers, no external baselines on the card.

## Rubric
A 1 · B 1 · C 2 · D 2 · E 2 — biomedical domain fine-tune (A max 1), unverified own numbers, open weights, CPU, SentenceTransformer-loadable.

## Relevance for RAG-NIMBF
`embedding_models: huggingface:OpenMed/EmbeddingGemma2-BiomedicalEvidence-270M-v2` — one-axis-changed candidate for a medical-corpus experiment.

## Status log
- 2026-11-23 screened
