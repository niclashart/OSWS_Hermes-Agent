# Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking

- **arXiv:** https://arxiv.org/abs/2610.31019
- **Score:** 8/10 (A: 2, B: 2, C: 1, D: 2, E: 1) — 120 bilingual revision pairs, controlled edits, ablations; Steadlith implementation Apache-2.0; frozen dense encoder on consumer GPU
- **Axis:** Chunking

## Core idea
Measures embedding update cost of chunkers under real document revisions: fixed-size chunking recomputes 57-68% of embedding workload per revision, recursive 38-56%, content-defined 43-54%, while evidence recall differs by less than 2pp.

## Key results (verbatim quotes)
> "fixed-size chunking recomputes 57-68% of its full new-version embedding-input workload, recursive chunking 38-56%, and content-defined chunking 43-54% ... while at these parameters mean evidence recall under a fixed 2048-token retrieval budget differs by less than two percentage points within either language" (Abstract)

## RAG-NIMBF relevance
Update cost is a new evaluation dimension for the Chunking axis; content-defined chunking (Steadlith) pluggable as a new chunking strategy value. Strong weekly-fit candidate.
