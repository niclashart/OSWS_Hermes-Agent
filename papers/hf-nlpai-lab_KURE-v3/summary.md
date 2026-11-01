# nlpai-lab/KURE-v3 — model summary

- **Type:** HF embedder (dense single-vector), 1.1B params, 2048-d (Matryoshka 256–2048), apache-2.0
- **Slot:** `embedding_models: huggingface:nlpai-lab/KURE-v3`
- **mteb:** https://github.com/embeddings-benchmark/results/tree/main/results/nlpai-lab__KURE-v3

## Core idea
Korean–English bilingual dense retriever based on nvidia/Nemotron-3-Embed-1B-BF16. Single 2048-d cosine vector, Matryoshka-trained (256/512/1024/2048 dims), 8,192-token context, dedicated `encode_query` / `encode_document` prompts. Also served via an OpenAI-compatible API (kure.kullm.ai).

## Reported results (quotes from model card)
- "With 1.1B parameters, it averages **0.8027** nDCG@10 on MTEB(kor, v2) Retrieval."
- "It outperforms 8B dense models such as comsat-embed-ko-8b-preview and Qwen3-Embedding-8B."
- "Matryoshka embeddings: trained at 2,048, 1,024, 512 and 256 dimensions, so vectors can be truncated."
MTEB(kor) results page exists (mteb link).

## Rubric
A 1 — Korean-specific model; beats Qwen3-Embedding-8B but only on MTEB(kor), not on the German/English setups RAG-NIMBF runs.
B 2 — MTEB leaderboard results with named baselines + mteb results link.
C 2 — apache-2.0 weights, sentence-transformers.
D 2 — 1.1B params, consumer GPU / CPU.
E 2 — plain sentence-transformers `SentenceTransformer` usage (encode_query/encode_document helpers).

## Affected axis
Embedding (expressible, E=2 — candidate for a one-axis proposal if Korean data is ever added; German/English default comparison not meaningful).
