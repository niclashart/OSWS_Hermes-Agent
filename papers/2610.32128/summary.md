# From Noisy Retrieval to Decision Evidence: Silver Evidence Demonstrations for In-Context Learning (2610.32128)

**Score:** 7/10 (A:2 B:2 C:1 D:2 E:1) · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.32128)

## Core idea
Replaces raw retrieved passages in ICL demonstrations with LLM-generated, target-conditioned silver-evidence summaries, cutting distracting context while preserving decision-relevant signal; one structured call generates evidence then predicts label at test time.

## Key results (verbatim quotes)
> "It also achieves higher mean label accuracy than InstructRAG-style ICL on all four datasets." (Results)

## Rubric justification
New retrieval-output condensation technique (A=2), 4 datasets vs gold-only and InstructRAG ICL (B=2), code availability unclear (C=1), single structured LLM call, small models OK (D=2), new ICL/evidence layer component (E=1).

## Affected axis
Not expressible: demonstration-side evidence condensation is a new layer between Retrieval and Prompting; new-axis candidate.
