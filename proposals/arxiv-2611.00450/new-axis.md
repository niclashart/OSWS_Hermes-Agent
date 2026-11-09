# New-axis proposal — arXiv:2611.00450

**Paper:** "From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory" (arXiv:2611.00450, ResMem) — vault note [[arxiv-2611.00450]], screened 2026-11-04, score 8/10.

## What the paper shows
Retrieved evidence is distilled offline into a parametric memory (adapter) that predicts an additive logit residual at inference. Quote (Abstract): "ResMem reduces the storage retained for teacher construction by 94.7% compared with the evaluated kNN pipeline. Across five question answering datasets, ResMem raises mean token F1 from 32.83% for the frozen LLM to 34.48%."

## Why not expressible in RAG-NIMBF today
This replaces the retrieval stage entirely with trained parameters inside the generator — "fine-tuned or trained retrievers" are explicitly listed as not expressible. A RAG-NIMBF grid can only compare retrieval-time components; there is no axis for "model with baked-in retrieval memory vs. runtime retrieval" as a single comparison arm.

## What RAG-NIMBF would need
- Config key `parametric_memory: <none | <adapter id>>` on the generator side: wraps an `ollama:`/`openai:` model with a LoRA-style adapter trained offline from a corpus.
- A training-time helper (outside benchmark runs) that builds the adapter from a corpus + teacher; hard rule "never trigger benchmark runs" keeps this out of the run matrix, so it would be a documented offline step.
- Evaluation: existing pipeline works unchanged (answers come from the wrapped model), but token/storage accounting needs a memory-size metric.

## Estimated effort
Large: adapter training pipeline, model-loading plumbing in `benchmark/providers.py`, and storage metrics. Research-only interest until gains (here +1.65 F1) justify the complexity.
