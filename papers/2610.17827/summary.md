# CSEG: Benchmarking and Training Reward Models for Cross-Source Evidence Grounding in Search Agents

**Axis:** [[Evaluation]] · **Score:** 7/10 · [arXiv](https://arxiv.org/abs/2610.17827) · [PDF](https://github.com/niclashart/OSWS_Hermes-Agent/blob/main/papers/2610.17827/paper.pdf)

## Core idea
Evaluation framework (CSEG) with a six-layer decision tree judging how search-agent answers map back to retrieved evidence, including source independence and conflicting-evidence adjudication. Ships CSEG-Bench (1,160 verified trajectories) and a trainable reward model (CSEG-RM).

## Results
> "CSEG-RM reaches 83.9% exact accuracy and lies on the accuracy–cost Pareto frontier among open-weight judges." (Sec. 5.3)
> "CSEG-RM raises the independently judged mean label from 2.83 to 4.19, and the proportion of trajectories with labels 5–7 from 19.1% to 40.2%." (Sec. 5.3)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — benchmark/reward model for grounding evaluation; CC BY 4.0 license; needs dedicated judging setup and reward-model training, not a plug-in config value.

## Relevance for RAG-NIMBF
A candidate additional LLM-judge metric family under the Evaluation axis, but the six-layer trajectory judging requires components (trajectory logger, reward model) RAG-NIMBF does not have.

## Status log
- 2026-10-24 screened
