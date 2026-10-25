# Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation (2609.38222)

**Score: 8/10** · [arXiv](https://arxiv.org/abs/2609.38222) · screened 2026-10-25

## Core idea
Split-conformal claim filtering applied to multi-hop RAG: drops unsupported claims at a calibrated target, raising fully-supported responses from 55.6–76.0% to 95.8–97.2% at the 95% target, at the cost of heavy claim retention loss.

## Key results
> "At the 95% target, this rate ranges from 95.80% to 97.20%, compared with 55.60%-76.03% without filtering. However, the improvement is strongly selective: only 4.41%-31.09% of generated claims are retained and 9.70%-51.40% of responses remain non-empty at the 95% target." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 = 8 — A2 · B2 · C1 · D2 · E1 — six multi-hop model-dataset configs plus single-hop reference; conformal filtering is a post-generation component NIMBF lacks.

## Affected axis
New-Techniques

## Relevance for RAG-NIMBF
Not expressible: no post-generation claim-filtering stage in RAG-NIMBF → `new-axis.md`.
