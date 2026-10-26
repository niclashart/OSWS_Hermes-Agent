# Beyond Benchmark Scores: How Synthetic and Authentic Query Distributions Diverge in RAG Evaluation

**arXiv:** https://arxiv.org/abs/2609.14579 · **Score:** 7/10 (A2 B1 C1 D2 E1) · **Axis:** Datasets · **Screened:** 2026-10-26

## Core idea
Synthetic vs authentic query distributions diverge sharply (6.8 vs 15.7 words); configs tuned on synthetic queries lose substantially on authentic traffic.

## Key results (verbatim quotes)
- "authentic queries average 6.8 words versus 15.7 for the synthetic ones, and draw from only 53 unique sources compared to 165" (Abstract)
- "optimizing on synthetic queries selected a higher-latency hybrid retriever" (Abstract)

## Rubric justification
- A=2: motivates authentic-query dataset axis option
- B=1: one case study (university system), clear quantified divergence
- C=1: no code release stated
- D=2: n/a
- E=1: guidance for dataset selection, no new component

## RAG-NIMBF fit
Supports Datasets-axis guidance (synthetic vs authentic splits); partially expressible via dataset choice.
