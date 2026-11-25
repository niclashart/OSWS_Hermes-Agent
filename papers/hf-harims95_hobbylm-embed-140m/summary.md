# harims95/hobbylm-embed-140m

**Score:** 7/10 · [HuggingFace](https://huggingface.co/harims95/hobbylm-embed-140m) · [MTEB results](https://github.com/embeddings-benchmark/results/tree/main/results/harims95__hobbylm-embed-140m)

## Model
English sparse-MoE text embedder, trained from scratch: 140M total / 36M active params, 512-dim dense output. Apache-2.0, sentence-transformers loadable, GGUF/MLX/Ollama available.

## Key claims (quotes from model card)
> "62.33 on MTEB(eng, v2), all 41 tasks, scored through the loader merged into the `mteb` package."
> "512 tokens by default; set it to 2,048 and long-document search improves from 36.1 to 49.3 nDCG@10 on LongEmbed."

## Rubric
A 1 · B 2 · C 2 · D 2 · E 2 — card does not show it beating bge-m3/nomic/Qwen3 defaults (A=1); official MTEB numbers with baselines; Apache-2.0 + sentence-transformers; tiny model; slot-ready.

## Relevance for RAG-NIMBF
Ready-to-use slot line: `embedding_models: huggingface:harims95/hobbylm-embed-140m` (compare vs. current default embedder, one axis changed).

## Status log
- 2026-11-25 screened
