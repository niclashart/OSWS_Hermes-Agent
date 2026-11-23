# New axis proposal — StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching (arxiv-2611.22766)

- Paper: https://arxiv.org/abs/2611.22766
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Diffusion-based latent stitching of retrieved chunks into one compact context. Context compression/selection under a token budget is explicitly not expressible. Needs: new `context_compression` config key + latent-stitching provider between retrieval and generation. Effort: L.
