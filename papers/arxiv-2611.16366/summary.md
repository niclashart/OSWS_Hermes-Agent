# CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented Generation using Decision Models

- arXiv/HF id: arxiv-2611.16366
- Score: 7/10 (A 2, B 2, C 1, D 1, E 1)
- Date screened: 2026-11-13
- Axis: New-Techniques
- Source: https://arxiv.org/abs/2611.16366

## Core idea
CURATOR fine-tunes a pretrained decision model to jointly select evidence spans from large candidate pools, keeping per-span decisions context-aware while efficient; targets limited-context RAG.

## Key results (verbatim quotes)
> "CURATOR maintains a strong evidence discrimination capability as the number of candidates increases, generalizes across different tasks and document domains, and improves downstream RAG performance, particularly when the available context is limited." (Abstract)

## Rubric justification
A 2 · B 2 · C 1 · D 1 · E 1 — context compression/selection is explicitly not expressible; multi-task/domain experiments, no code or weights stated; new component + adapter needed.

## RAG-NIMBF fit
Not expressible: RAG-NIMBF has no context-compression/selection axis (listed under 'Not expressible today') → new-axis.md candidate.
