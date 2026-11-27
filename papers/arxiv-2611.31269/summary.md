# Reliability of Language-Model Judges for Quantitative Scientific QA (arXiv 2611.31269)

## Core idea
Measures how reliably LLM judges grade quantitative RAG answers when ground truth is computed deterministically from structured records (755 answers from 45,441 perovskite device records). Judges are evaluated with a reference key, with retrieved passages, or unassisted.

## Key results
> "Equipped with the reference key, Claude Opus reproduces ground truth near-perfectly (Cohen's κ = 0.982 ± 0.003) and preserves exact architectural rankings (τ = 1.00)." (Abstract)

> "Withholding the reference causes evaluation fidelity to collapse: frontier agreement drops to κ = 0.557 ± 0.022, and providing retrieved literature passages yields virtually no improvement (κ = 0.576 ± 0.024)." (Abstract)

> "Without reference keys, local judges degrade to near-random agreement (κ = 0.087 and 0.112), inverting the leaderboard to rank a hallucinating closed-book baseline first (τ ≤ 0.20)." (Abstract)

> "absent a reference, the frontier judge accepts 46.6% of erroneous SQL answers, overestimating architecture accuracy as 66.4% against its true 52.6%." (Abstract)

## Rubric score: 7/10
A 2 — judge-reliability protocol (reference-keyed vs. unassisted judging, κ/τ agreement) for the Evaluation axis. B 2 — 4,530 free-text answers, 6 retrieval architectures, 3 judges, 3 regimes. C 1 — arXiv non-exclusive license; no code/data release stated. D 1 — requires a frontier judge and precomputed structured ground truth. E 1 — reference-keyed judging and judge-agreement metrics are not config values; new custom metric/eval mode needed.

## Affected axis
Evaluation (judge-reliability protocol; conclusion: quantitative benchmarks need reference ground truth, not unstructured LLM inspection).

## Relevance for RAG-NIMBF
Supports using deterministic reference answers (`dataset_ground_truth_field`, exact-match-style custom metrics) over LLM judges for quantitative datasets. Judge-agreement measurement (κ against gold labels, judge swap sensitivity) would be a new evaluation mode.
