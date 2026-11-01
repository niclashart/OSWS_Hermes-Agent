# VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M — model summary

- **Type:** HF embedder (ColBERT / late interaction), 115M params (67.4M active), apache-2.0
- **Slot:** `embedding_models: huggingface:VAGOsolutions/SauerkrautLM-MoEdernColBERT-115M`
- **mteb:** (none in card)

## Core idea
MoEdernBERT: a ModernBERT-style encoder with mixture-of-experts MLP (2 of 8 GeGLU experts + 1 shared expert per layer), hash embeddings (factorized token embeddings), and gated short convolutions, trained as a multilingual ColBERT retriever for de/en/es/nl/fr/it/pt with 32k-token documents.

## Reported results (quotes from model card)
- "Ahead of 2.7× larger granite-311m-multilingual-r2 on all 11 benchmarks in the overview."
- "German retrieval ahead of models up to 5× larger. MKQA de→en 0.731 vs. 0.671 for Qwen3-Embedding-0.6B."
- "German legal texts: ahead of 8B models and commercial APIs. LegalQuAD 0.851 vs. 0.772† for Nemotron-3-Embed-8B."
- "Long documents up to 32k tokens. LongEmbed 90.1, ahead of the 7B–14B models on the public LongEmbed leaderboard."
- "1,132 documents per second on one GPU" (8× Qwen3-Embedding-0.6B throughput).
Numbers are the vendor's own measurements († = public MTEB, not measured by them).

## Rubric
A 2 — beats Qwen3-Embedding-0.6B / granite baselines; German + multilingual + long context at 1/5 size.
B 1 — own benchmark numbers with named baselines, not independently verified.
C 2 — apache-2.0 weights, sentence-transformers library.
D 2 — 115M params, trivially consumer GPU.
E 1 — late interaction (ColBERT): not loadable as a plain `SentenceTransformer` dense embedder in RAG-NIMBF → new provider.

## Affected axis
Embedding (ColBERT variant — currently not expressible, see `new-axis.md` path in weekly fit check).
