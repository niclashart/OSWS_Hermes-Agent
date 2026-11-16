# New-axis proposal — arXiv:2611.10405

**Paper:** "Yuanbao-Reranker: Document-Grounded Synthesis and Preference Distillation for Text Reranking" (arXiv:2611.10405) — vault note [[arxiv-2611.10405]], screened 2026-11-11, score 9/10.

## What the paper shows
Qwen3-based dense pointwise reranker family (0.6B/4B/8B, Apache-2.0 weights at `Yuanbao-Search/Yuanbao-Reranker-{0.6B,4B,8B}`). Quote (Abstract): "the 0.6B variant reaches 70.96 Avg. to surpass 1B–4B active-parameter baselines, the 4B variant reaches 73.63 Avg. to outperform the 8B teacher (72.68), and the 8B variant achieves a state-of-the-art 74.21 Avg."

## Why not expressible in RAG-NIMBF today
The `reranker_models` slot accepts only sentence-transformers `CrossEncoder` models. Yuanbao-Reranker is a **causal-LM yes/no scorer**: relevance = softmax over the `yes`/`no` token logits after an instruction-formatted chat prompt (`<Instruct>/<Query>/<Document>` with Qwen3 chat template and an empty `<think>` block — HF model card quickstart). Loading it as a `CrossEncoder` would silently produce garbage; it needs prompt construction plus a decision-token logit head. No LLM-based / generative reranking provider exists in RAG-NIMBF (`nimbf-capabilities.md`: "late interaction (ColBERT) / LLM rerankers = new provider").

## What RAG-NIMBF would need
- New reranker provider `reranker_kind: crossencoder | generative-yes-no` with adapter interface `score(query, docs, instruction) -> list[float]`.
- Config keys `reranker_prompt_instruct` (task instruction string) and `reranker_max_input_tokens` (8,192 context).
- Registry entry for `huggingface:Yuanbao-Search/Yuanbao-Reranker-0.6B` (bf16 safetensors, 0.6B = consumer-GPU friendly).

## Estimated effort
Medium (~3–5 days): a single adapter class reusing the existing `reranker.py` plumbing; the yes/no logit scoring loop is ~50 lines with transformers. No training involved.
