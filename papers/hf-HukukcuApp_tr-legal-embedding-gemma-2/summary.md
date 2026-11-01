# HukukcuApp/tr-legal-embedding-gemma-2 — model summary

- **Type:** HF embedder (dense, single-vector), 271M params, 768-d, license: gemma
- **Slot:** `embedding_models: huggingface:HukukcuApp/tr-legal-embedding-gemma-2`
- **mteb:** (none)

## Core idea
Turkish legal-domain fine-tune of google/embeddinggemma-2 for case-law retrieval (dispute → precedent matching in Yargıtay decisions), trained on 118,078 legal triplets with BM25 hard-negative mining.

## Reported results (quotes from model card)
- Card reports metrics top-1/top-5/top-10 accuracy, MRR, nDCG, but no baseline comparisons in the visible card text.
- "118.078 adet içtihadi üçlü (triplet) ile fine-tune edilmiştir" — trained on 118,078 case-law triplets.
- "BM25 tabanlı zor negatif madenciliği" — BM25-based hard-negative mining; twin decisions with cosine ≥ 0.88 excluded from the negative pool.

## Rubric
A 1 — domain-specific (legal) fine-tune for a single non-English, non-German language → A max 1 per rubric.
B 1 — own unverified numbers, no baselines named.
C 1 — Gemma license, not an open license (MIT/Apache/CC-BY).
D 2 — 271M params, trivial to run.
E 2 — loadable via sentence-transformers (`SentenceTransformer`).

## Affected axis
Embedding (domain-specific value; niche — Turkish law; unlikely fit-check candidate).
