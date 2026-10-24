# The Anatomy of a Blind Spot: What an LLM Judge Must Be Shown, and How Much

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.15938) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/2610.15938/paper.pdf)

## Core idea
Treats the LLM judge as a regulator and varies only what the judge is shown across seven benchmarks. Findings: what the judge sees matters more than which judge; judges denied the source/constraints cause revision loops that degrade systems below baseline.

## Results
> "When a system revised its answers on feedback from a judge denied the material they had to respect, it ended below its starting point on instruction following and question answering." (Abstract)
> "About a tenth of the source did almost all of its work, and a small entailment graph matched an LLM judge at finding errors in grounded text." (Abstract)

## Rubric
A 2 · B 2 · C 1 · D 2 · E 1 — directly scores the Evaluation axis (LLM-judge input design); seven benchmarks, pre-registered predictions; no code release stated; runs on API judges; input configuration of judge is not a RAG-NIMBF config key today.

## Relevance for RAG-NIMBF
Informs `settings.eval_critic_*` prompt/input design; a judge-input axis would be a small new config key.

## Status log
- 2026-10-24 screened
