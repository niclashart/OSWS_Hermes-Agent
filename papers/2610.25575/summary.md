# Benchmark for Structured Retrieval-Augmented Generation in Perovskite Photovoltaics (arXiv:2610.25575)

## Core idea
Quantitative QA benchmark for materials-science literature: 755 ground-truth answers computed from 45,441 measured device records; compares six retrieval architectures over 158,274 passages against read-only SQL execution over the structured table, using an open 14B model on a single 24 GB GPU.

## Results
> "standard passage retrieval tops out at 16-23% accuracy (compared to 1.6-6.5% zero-shot). In contrast, equipping the language model with read-only SQL execution over the structured device table elevates accuracy to 51.5% on historical and 50.8% on prospective literature -- a 33.01.8 percentage-point advantage over hybrid text retrieval" (Abstract). "Aggregate queries ... prove virtually unsolvable via text retrieval alone" (Abstract).

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — text-vs-SQL structured retrieval benchmark; verified ground truth; open 24 GB GPU setup; no SQL-adapter slot in NIMBF.

## Relevance for RAG-NIMBF
Candidate new retrieval mode (`structured`/SQL) or RAG-System adapter; benchmark as dataset adapter candidate.
