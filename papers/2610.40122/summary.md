# 2610.40122 — xPRT: Cross-Passage Retrieval Pretraining

**Score:** 7/10 · **Axis:** Embedding · [arXiv](https://arxiv.org/abs/2610.40122) · [HTML](https://arxiv.org/html/2610.40122)

## Core idea
xPRT is an unsupervised retrieval-pretraining objective that learns from cross-passage structure within a document: anchors (passages closest to the document embedding) plus their most-related siblings give contrastive and reconstruction signals, instead of random spans. Continued pretraining with fixed corpus/schedule outperforms five strong objectives on MTEB English v2.

## Key results (verbatim quotes)
> "Across diverse tasks spanning all task types, we observe that xPRT consistently outperforms the strongest baseline by 3.2% on an average." (Abstract)

## Rubric score with justification
A 2 (new embedding pretraining objective; Embedding axis material via resulting model) · B 2 (MTEB English v2 vs five SOTA objectives, ablations) · C 1 (CC BY-SA 4.0 text; checkpoint release not confirmed) · D 2 (public checkpoint scale pretraining) · E 0 (training loop; only the final model would be pluggable)

## Affected axis
Embedding: The technique itself (continued pretraining) is not expressible in RAG-NIMBF, but if the checkpoint is released it becomes a sentence-transformers/<hf-id> embedding value. Track for the Embedding axis.
