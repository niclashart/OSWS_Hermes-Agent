# Yaldat/Yalda-Embedding — model card summary

- Source: https://huggingface.co/Yaldat/Yalda-Embedding
- Score: 7/10 · Axis: Embedding · HF model (no PDF per rules)

## Model card facts
- Fine-tune of Qwen3-Embedding-0.6B; >1M Persian query-document pairs + relational knowledge distillation from F2LLM-v2-8B.
- 595,776,512 parameters, 1024-dim embeddings, 512-token input, last-token pooling, cosine similarity. License: Apache 2.0.
- sentence-transformers loadable (`SentenceTransformer("Yaldat/Yalda-Embedding")`).

## Reported numbers (verbatim quotes, model card)
> "Yalda achieves **state-of-the-art performance among the evaluated 0.6B models** on eight Persian retrieval tasks from FaMTEB. Its reported mean is **0.5488**, compared with **0.4713** for its Qwen3-0.6B initialization and **0.5563** for Qwen3-Embedding-4B."

> "It offers competitive retrieval performance against the 4B reference while retaining the 0.6B model's inference footprint."

No separate `mteb` leaderboard link in the card.

## Rubric
A 1 (domain fine-tune, non-German non-English) · B 2 (FaMTEB with baselines) · C 2 (Apache 2.0, open data/code) · D 2 (0.6B) · E 2 (sentence-transformers)

## RAG-NIMBF slot
`embedding_models: huggingface:Yaldat/Yalda-Embedding`
