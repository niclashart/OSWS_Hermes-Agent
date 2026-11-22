# Agentic AI Ecosystem for Cross-Project Knowledge (Water Governance & Climate Resilience)

arXiv 2611.26398 · screened 2026-11-22 · score 7/10 (A2 B1 C1 D2 E1)

## Core idea
Agentic RAG over heterogeneous EU-project documentation: hierarchical section trees + structured metadata, two domain-fine-tuned embedding models (water, climate), and a ReAct-style controller that "iteratively orchestrates retrieval actions by allocating retrieval budget across domain collections and accumulating evidence until a stopping criterion is met."

## Key results (verbatim quotes, abstract)
- "the proposed approach improves Mean Reciprocal Rank by 26.7% (relative) compared to a single-domain embedding baseline, indicating more consistent retrieval of relevant evidence."
- Retrieval is supported by "two domain-specific embedding models fine-tuned on domain data (water and climate)."

## Rubric justification
- A=2: retrieval-budget allocation + evidence-sufficiency stopping — agentic technique beyond NIMBF's axes.
- B=1: one retrieval benchmark over the project corpus, single baseline.
- C=1: no code/weights link stated.
- D=2: fine-tuned domain embedders run on consumer hardware.
- E=1: budgeted multi-collection agentic loop needs a new component; embedders themselves are pluggable.

## Affected axis
New-Techniques (agentic budgeted retrieval with stopping criterion).
