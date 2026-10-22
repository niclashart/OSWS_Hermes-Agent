# DeclineCraft: A RAG Abstention Benchmark (arXiv:2610.28340)

## Core idea
Dynamic abstention benchmark: unanswerable questions target Minecraft feature additions after a corpus cut-off (with parametric-exposure audits), so later cut-offs keep it valid for future models. Measures Correct Abstention Rate (CAR), Answerable Attempt Rate, and Answer Accuracy across 27 LLMs.

## Results
> "single-shot retrieval significantly raises CAR in 38 of 40 configurations (model and thinking setting) versus no retrieval" and "Iterative RAG ... significantly lowers CAR versus single-shot RAG in 30 of 40 configurations (mean 46.4%), with little change in Answer Accuracy (68.5% to 69.3%)" (Abstract). "Adding query rewriting and reranking to hybrid (dense & sparse) retrieval lowers CAR for all 12 models tested." Code: https://github.com/Thakur-Atharva/declinecraft-benchmark, CC BY 4.0.

## Rubric
A 2 · B 2 · C 2 · D 2 · E 0 — new abstention evaluation dataset/metric; 27 models, ablations; open code; consumer-GPU; CAR metric has no NIMBF adapter yet.

## Relevance for RAG-NIMBF
Candidate dataset adapter + `custom_metrics` (CAR) in the Evaluation axis; iterative-RAG finding touches the not-yet-expressible agentic loop.
