# TriageRAG: Failure-Aware Self-Training for Adapting Retrieval-Augmented Language Models to Specialized Domains (2610.33776)

**Score:** 7/10 (A:2 B:2 C:1 D:1 E:0) · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.33776)

## Core idea
Failure-aware self-training: probes the student with and without retrieved context, triages each self-generated QA pair (known / solved / context-failure / retrieval-failure), and routes each category to targeted training signal including a parametric route.

## Key results (verbatim quotes)
> "TriageRAG outperforms a budget-matched SimRAG by 1.2-6.4 points and is the only method that recovers the closed-book level in every case where retrieval hurts the base model." (Abstract / Results)

## Rubric justification
New domain-adaptation technique (A=2), 11 datasets + CS-Bench, 2 backbones (B=2), code availability unclear (C=1), needs RL/SFT training runs (D=1), requires training loop, not expressible (E=0).

## Affected axis
Not expressible: whole pipeline is a fine-tuning method; would need a training axis. Relevant for New-Techniques evidence only.
