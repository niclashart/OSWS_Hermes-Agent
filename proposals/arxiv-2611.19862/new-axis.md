# New axis proposal — Bioformer-RetroMAE: retrieval-oriented pretraining of a compact biomedical language model for literature search (arxiv-2611.19862)

- Paper: https://arxiv.org/abs/2611.19862
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Retrieval-oriented domain pretraining of an embedder. The resulting model would plug into `embedding_models` only if published as a sentence-transformers checkpoint; the technique itself (domain-adaptive retroMAE pretraining) is a trained retriever, which RAG-NIMBF cannot benchmark. Needs: embedding-model registry entry for arbitrary HF checkpoints with domain prefix handling + optional 'pretrained retriever' axis documentation. Effort: S (registry) — value limited.
