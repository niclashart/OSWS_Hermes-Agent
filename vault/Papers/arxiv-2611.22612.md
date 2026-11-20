---
id: arxiv-2611.22612
title: "Right Diagnosis, Unsafe Route: Auditing Clinical AI Decision Trajectories and Corrective Oversight for Validity and Potential Harm"
authors: [Guanqiao Chen, Wei Jiang, Shu Zhang, Qian Lin, Guanxu Yu, Siran Li, Chunhui Wang, Tianyu Shi]
year: 2026
score: 7
rubric: {A: 2, B: 2, C: 1, D: 1, E: 1}
axis: [Evaluation]
status: screened
screened: 2026-11-20
source: https://arxiv.org/abs/2611.22612
pdf: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22612/paper.pdf
summary: https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22612/summary.md
tags: [rag-radar, evaluation]
---
# Right Diagnosis, Unsafe Route

**Axis:** [[New-Techniques]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2611.22612) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/arxiv-2611.22612/paper.pdf)

## Core idea
Stepwise evaluation of agentic/clinical AI systems with patient safety as the target: a trajectory audit replays cases checkpoint by checkpoint and rates every intermediate decision for potential harm and clinical validity (LLM judge + physician reference standard); an oversight audit branches at the first error and measures whether corrective feedback repairs it and what new harm it introduces.

## Results
> "55.2% of hospital trajectories reaching an acceptable final diagnosis passed through a decision with moderate or severe potential harm and 24.8% through a clinically unacceptable one; the harm rates were 76.2% on MIMIC-IV and 39.6% on ASCENT." (Abstract)
> "Structured corrections resolved 73.6% of first errors versus 24.8% after bare rejection, yet new potentially unsafe decisions followed 30.2% of corrections versus 19.7% of rejections" (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 1 · E 1 — new stepwise-safety evaluation protocol, 3 sources with physician calibration; no public harness code; judge is frontier-API class; needs a new RAG-NIMBF benchmark stage.

## Relevance for RAG-NIMBF
Not expressible today: RAG-NIMBF scores final answers only. Would need stepwise replay mode + per-step judge metric + branch-at-error correction harness (see [[New-Techniques]]).

## Status log
- 2026-11-20 screened
