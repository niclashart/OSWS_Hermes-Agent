# From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries

- **arXiv:** https://arxiv.org/abs/2610.31467
- **Score:** 7/10 (A: 2, B: 2, C: 1, D: 2, E: 0) — grounding-constraint prompting with faithfulness-vs-evidence evaluation; no public code found
- **Axis:** New-Techniques

## Core idea
Constrained-generation framework combining structured evidence conditioning with RAG for patient-facing health summaries; evaluated with NLI, atomic factuality and readability across three LLMs and 4,500 summaries.

## Key results (verbatim quotes)
> "explicit grounding constraints consistently improve clinical alignment, particularly by improving uncertainty preservation and, once faithfulness is evaluated against retrieved evidence, generally preserving or improving faithfulness, while effects on omission remain model-dependent" (Abstract)

## RAG-NIMBF relevance
Not expressible: prompt-based constrained generation stage between retrieval and answering has no NIMBF config key. Candidate for new-axis.md in weekly fit check.
