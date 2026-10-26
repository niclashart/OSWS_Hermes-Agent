# Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented Software Vulnerability Detection

**arXiv:** https://arxiv.org/abs/2609.37669 · **Score:** 7/10 (A1 B2 C2 D2 E0) · **Axis:** Evaluation · **Screened:** 2026-10-26

## Core idea
Unified open-weight benchmark of six RAG4SVD systems with component-level analysis; oracle retrieval still leaves pairwise accuracy at 0.51.

## Key results (verbatim quotes)
- "oracle knowledge raises retrieval to near-optimal, yet performance remains low (0.51 pairwise accuracy)" (Abstract)
- "published RAG4SVD performance does not transfer under a controlled open-weight evaluation" (Abstract)

## Rubric justification
- A=1: component-level RAG evaluation aligns with axis decomposition but is SVD-domain-specific
- B=2: six systems, common dataset/metrics/model pool, oracle-knowledge ablation
- C=2: open-weight setting, reproduction package
- D=2: open-weight models
- E=0: SVD task not among registered datasets

## RAG-NIMBF fit
Domain benchmark, not directly expressible; useful evidence that component-level evaluation (NIMBF-style) matters.
