# VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M — model summary

- **Type:** HF embedder (ColBERT / late interaction), 27M params (12.3M active), apache-2.0
- **Slot:** `embedding_models: huggingface:VAGOsolutions/SauerkrautLM-MoEdernColBERT-27M`
- **mteb:** (none in card)

## Core idea
Smallest member of the MoEdernColBERT family: MoEdernBERT encoder (2 transformer layers, hidden 640, hash embeddings, MoE MLP, gated convolutions) trained as multilingual ColBERT retriever for seven European languages, up to 32k tokens via sliding-window attention.

## Reported results (quotes from model card)
- "Ahead of 3.6× larger granite-97m-multilingual-r2 on all 11 benchmarks in the overview."
- "4.3× the throughput of granite-97m-multilingual-r2 and 47× that of Qwen3-Embedding-0.6B: 6,708 documents per second on one GPU."
- "German retrieval ahead of models up to 22× larger. MKQA de→en 0.690 vs. 0.671 for Qwen3-Embedding-0.6B."
- "German legal texts: ahead of 8B models and commercial APIs. LegalQuAD 0.796 vs. 0.772† for Nemotron-3-Embed-8B."
- "Long documents up to 32k tokens. LongEmbed 86.9, ahead of the 7B–14B models on the public LongEmbed leaderboard."
Numbers are the vendor's own measurements († = public MTEB, not measured by them).

## Rubric
A 2 — beats granite-97m and Qwen3-Embedding-0.6B on German/multilingual retrieval at 1/22 the size.
B 1 — own benchmark numbers with named baselines, not independently verified.
C 2 — apache-2.0 weights, sentence-transformers library.
D 2 — 27M params, runs anywhere including CPU.
E 1 — late interaction (ColBERT): not a plain dense `SentenceTransformer` → new provider in RAG-NIMBF.

## Affected axis
Embedding (ColBERT variant — not expressible today; new-axis candidate).
