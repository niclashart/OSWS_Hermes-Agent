# Which Code Changes Need Re-embedding? CIPBench and the Limits of Multi-Signal Index Maintenance (2610.25108)

**Score: 8/10** · [arXiv](https://arxiv.org/abs/2610.25108) · screened 2026-10-25

## Core idea
CIPBench scores index-maintenance policies for repository RAG under a strict pre-embedding information boundary: which changed code units need new embeddings. Unchanged units can be skipped at nearly half the embedding cost with no retrieval risk.

## Key results
> "What pays off is not ranking but filtering: units whose text is unchanged from the indexed state can be skipped with no risk and, in the most reversion-heavy project, at nearly half the embedding cost." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 = 8 — A2 · B2 · C1 · D2 · E1 — 10 repos across 3 languages; benchmark formalized; no persistent code release confirmed; incremental indexing is outside NIMBF's static-index axes.

## Affected axis
New-Techniques

## Relevance for RAG-NIMBF
Index maintenance / incremental re-embedding is a new dimension RAG-NIMBF lacks → `new-axis.md`.
