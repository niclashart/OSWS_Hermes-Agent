# OpenMed/EmbeddingGemma2-BiomedicalEvidence-270M-v2 — Summary

## Core idea
Domain fine-tune of google/embeddinggemma-2 (271M params, Apache-2.0, 768-dim, 512-token max input) for
English medical question→answer retrieval. Runs on CPU. Uses task prefixes (`task: search result | query:`
for questions, `title: none | text: ` for answers), float32/bfloat16 only.

## Key results (model card, held-out MedQuAD dev split: 1,966 questions / 15,139 answers)
> "NDCG@10 91.76" (model-index, Medical FAQ answer retrieval)
> "Recall@10 95.79" / "MRR@10 91.12" / "Recall@1 82.95" (model-index)

Own unverified numbers on one in-domain dataset; no comparison against bge-m3, nomic-embed-text,
embeddinggemma-2 base, or other general-purpose embedders on the card.

## Rubric
A 1 · B 1 · C 2 · D 2 · E 2 — A=1: domain-specific fine-tune (biomedical, English) → max 1 per rubric note;
B=1: own unverified numbers, no external baselines; C=2: Apache-2.0 weights, sentence-transformers;
D=2: 271M, CPU; E=2: loadable via SentenceTransformer.

## Affected axis
Embedding — `embedding_models: huggingface:OpenMed/EmbeddingGemma2-BiomedicalEvidence-270M-v2`
(candidate value for a medical-corpus variant; weak evidence, logged candidate not priority).
