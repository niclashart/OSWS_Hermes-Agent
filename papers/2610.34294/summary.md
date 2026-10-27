# Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation (2610.34294)

**Score:** 7/10 (A:2 B:2 C:1 D:2 E:1) · **Axis:** New-Techniques · [arXiv](https://arxiv.org/abs/2610.34294)

## Core idea
Shows stance poisoning with factually correct but one-sided retrieved documents shifts RAG output stance monotonically with poisoning share, and proposes a Stance-Balancing Middleware (stance detection + fixed 2+2+1 balancing + debiasing prompt) between retriever and generator.

## Key results (verbatim quotes)
> "Across all eight concentration-direction settings, the complete method reduced the magnitude of stance deviation by an estimated 0.106 to 0.350; the six settings at poisoning shares of 11.9%-18.9% remained significant after Holm adjustment (adjusted p <= 0.009)." (Abstract / Results)

## Rubric justification
New retriever-generator middleware axis (A=2), 4 models, concentration sweeps, statistical correction (B=2), no code found (C=1), ~1.5% GPU overhead for detection (D=2), new post-retrieval component (E=1).

## Affected axis
Not expressible: a stance-balancing / document-diversity post-retrieval filter is a new axis between Retrieval and Prompting.
