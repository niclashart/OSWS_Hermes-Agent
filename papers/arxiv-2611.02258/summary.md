# Beyond Binary Detection: Type-Aware Hallucination Analysis in Financial QA (arXiv-2611.02258)

**Core idea.** Studies hallucination detection at subtype level on PHANTOM (SEC-filings long-context benchmark): diagnoses an LLM detector per hallucination type, then proposes a two-stage hierarchical detector (first binary, then subtype) with an enhanced prompt.

**Key results.**
> "The detector reaches 80.2% binary accuracy but only 44.7% subtype accuracy, never assigns two of the nine categories, and misses between 5.3% and 46.8% of hallucinations depending on category" (Abstract)
> "we propose a two-stage hierarchical detector … raising binary accuracy to 95.6% and subtype accuracy to 56.1%" (Abstract; Sec. 4.2: reasoning_errors 68.3→94.7, entity 72.9→92.3)
> "The results show that type-level evaluation exposes detector weaknesses that aggregate metrics conceal." (Abstract)

**Rubric.** A 2 (new evaluation capability: type-level hallucination metrics — beyond RAGAS faithfulness) · B 2 (PHANTOM, 15,443 paired answers, per-category analysis) · C 1 (benchmark-based; detector prompts described, code/release not clearly stated) · D 2 (LLM-judge prompts, runs via API or small local model) · E 1 (new custom metric: hallucination-subtype classification — needs a new custom metric, not just config) = **8/10, relevant**.

**Affected axis:** Evaluation (hallucination-subtype metrics beyond RAGAS faithfulness — not expressible today).

**Source:** https://arxiv.org/abs/2611.02258
