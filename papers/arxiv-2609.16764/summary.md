# RECTIFY: An Interactive Workbench for Post-Evaluation RAG Diagnosis, Repair, and Verification

**arXiv:** https://arxiv.org/abs/2609.16764 · **Score:** 7/10 (A2 B1 C2 D2 E0) · **Axis:** Evaluation · **Screened:** 2026-10-26

## Core idea
Open-source workbench that routes evaluated RAG failures into repair families/slices and generates editable repair cards with sandbox reruns.

## Key results (verbatim quotes)
- "BM25 mainly triggers noisy-retrieval repairs, while dense and hybrid retrieval leave smaller sets of multi-part underretrieval and underused-evidence cases." (Abstract)
- "RECTIFY is publicly available as an open-source Streamlit workbench" (Abstract)

## Rubric justification
- A=2: post-evaluation repair workflow is a new Evaluation-axis option
- B=1: controlled benchmark across BM25/dense/hybrid, but no accuracy gains claimed
- C=2: publicly available open-source workbench
- D=2: Streamlit app on standard hardware
- E=0: workflow tool, not a config value

## RAG-NIMBF fit
Partially relevant to Evaluation axis as external tooling; no config change possible (E=0).
