# FrontiersMind/EmbeddingNandi-150M

**Model card:** https://huggingface.co/FrontiersMind/EmbeddingNandi-150M (HF, 2026-11-19)
**Params:** 146M · **License:** Apache-2.0 · **Base:** NandiBERT-150M (28L, 768d, GQA, QK-norm, SwiGLU)
**Source:** hf-model:embedder · **Ready-to-use slot:** `embedding_models: huggingface:FrontiersMind/EmbeddingNandi-150M`
**mteb link:** none (card reports own MTEB library runs, v2.26.19)

## Core idea
Compact long-context multilingual embedder: English + 13 Indic languages + Arabic/Indonesian/Malay, 16,384-token window (long docs embedded whole, no chunking), Matryoshka truncation to 768/512/256/128 dims. sentence-transformers loadable (`trust_remote_code=True`, custom `encode_query`/`encode_document` prompts).

## Key results (verbatim quotes)
> "Mean task scores on MTEB(eng, v2) (41 tasks), MTEB(Code, v1) (12 tasks) and MTEB(Indic, v1) (20 tasks)" — EmbeddingNandi-150M: 65.85 / **75.80** / **74.33**, Average **71.99**; UltraBERT-Embed-150M: 67.24 / 73.30 / 42.16, avg 60.90; granite-embedding-english-r2: 62.84 / 57.22 / 32.85, avg 50.97. (Benchmark Results)

> "EmbeddingNandi-150M is trained with Matryoshka Representation Learning, so the 768-dimensional vector can be shortened by keeping only its first values." (Matryoshka Dimension Truncation)

Caveat: on MTEB(eng, v2) Retrieval it scores 49.75 vs UltraBERT 57.20 — the English-retrieval edge comes from Code/Indic, not English retrieval.

## Rubric
- **A 2** — clear capability add: 16K long context + 14-language coverage at 146M, beats same-size granite/UltraBERT on MTEB averages.
- **B 2** — MTEB results with named same-size baselines, evaluated with the open MTEB library.
- **C 2** — Apache-2.0 weights, open evaluation stack.
- **D 2** — 146M params, trivially consumer-GPU.
- **E 2** — sentence-transformers `SentenceTransformer` loadable (trust_remote_code) → plain `huggingface:` slot value.

**Total: 8/10 → relevant**

## Affected axis
Embedding — directly expressible as `embedding_models: huggingface:FrontiersMind/EmbeddingNandi-150M`.

## Status log
- 2026-11-28 screened (HF model: no PDF; summary from model card)
