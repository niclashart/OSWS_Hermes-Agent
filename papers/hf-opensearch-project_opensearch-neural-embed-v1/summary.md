# opensearch-project/opensearch-neural-embed-v1

- HF id: opensearch-project/opensearch-neural-embed-v1
- Score: 10/10 (A 2, B 2, C 2, D 2, E 2)
- Date screened: 2026-11-13
- Axis: Embedding
- Source: https://huggingface.co/opensearch-project/opensearch-neural-embed-v1
- MTEB: https://github.com/embeddings-benchmark/results/tree/main/results/opensearch-project__opensearch-neural-embed-v1

## Model card facts
598M params, 2048-dim, English, Apache-2.0, sentence-transformers loadable. Distilled (no labeled data) from two teachers into a Qwen3-Embedding-0.6B student; teacher space built by concatenating the leading 1024 dims of each teacher.

## Key results (verbatim quotes)
> "ranks #1 among single-vector dense models under 1B parameters on the MTEB BEIR benchmark (58.37 average NDCG@10 over 15 tasks) and #2 among models under 1B parameters on MTEB(eng, v2) (73.76 Mean (Task)), within 1.5 points of the nearly 13x larger Qwen3-Embedding-8B." (model card)

## Rubric justification
Beats the sub-1B class users already run (bge-m3, Qwen3-Embedding-0.6B); MTEB/BEIR numbers with public per-task results; Apache-2.0 + sentence-transformers; 598M runs easily on consumer GPU; drop-in `huggingface:` slot value.

## Ready-to-use slot
```
embedding_models: huggingface:opensearch-project/opensearch-neural-embed-v1
```
