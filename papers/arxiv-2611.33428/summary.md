# When the Knowledge Runs Out (arXiv 2611.33428)

## Core idea
A part-level evaluation protocol for multi-part questions where the supplied reference material covers only some parts. Each part gets one of six verdicts (correct_answer, answer_plus_claim, correct_withhold, unsupported_claim, unnecessary_withhold, refusal), isolating gap-filling from the subtler failure of adding an unsupported claim to an otherwise correct answer.

## Key results
> "Without an explicit instruction to stay within the material, both models fill most gaps from their own knowledge (unsupported-claim rates of 0.71 and 0.90)." (Abstract)

> "One added sentence instructing them to answer only from the material brings these rates to 0.00 and 0.06" (Abstract) — boundary_accuracy rises to .99/.87 (Table 2, Sec. 4).

> "RAGAS faithfulness is unsuitable for this task because it penalises correct withholding; and a difference between the two models that is clear under one judge disappears when the judge model is replaced." (Abstract, Sec. 5)

## Rubric score: 8/10
A 2 — new evaluation protocol (part-level abstention + added-claim verdict) for the Evaluation axis. B 1 — pilot only: 30 cases, 2 models, 150 responses/run. C 2 — dataset, code, hand labels public; CC BY 4.0. D 2 — llama3.1:8b via Ollama runs locally. E 1 — per-part unsupported-claim rate and boundary accuracy are new custom metrics; the grounded-instruction condition maps to the existing `abstain_strict` prompt template.

## Affected axis
Evaluation (new metrics: per-part unsupported-claim rate, boundary accuracy, answer_plus_claim rate); Prompting (grounded vs. default condition = existing `abstain_strict`).

## Relevance for RAG-NIMBF
The instruction condition is expressible today (`prompt_templates: [default, abstain_strict]`). The verdict metrics are not in RAGAS or the custom-metric set — a new custom metric (LLM-judge per-part verdict over a JSON-labelled dataset) would be needed.
