# GINGER: Spicing Up Graph-Based Vector Search (arXiv-2611.08306)

**Core idea.** Open-source C++ ANNS library from Google combining a new two-level quantizer (Nested TurboQuant, NTQ: 4-bit graph navigation + higher-precision reranking in one representation), graph compression via reordering plus a StreamVByte-based lossless codec (AdaptiveGap), and search optimizations (PCA projection, candidate prefiltering, beam management).

**Key results.**
> "This representation achieves near floating point precision with 2.6× less memory." (Abstract)
> "At 95% recall, Ginger speeds up query throughput by an average of 1.8× over each dataset's fastest competitor and by at least 2.3× over any single library." (Abstract)
> "We also compress the size of our proximity graphs by up to 2.5× without impacting query throughput." (Abstract)
Ablations show 12-bit NTQ achieves near-float brute-force recall; AdaptiveGap+reordering cuts graph storage from ~34–89 bits/edge (CSR/flat) to ~13–18 bits/edge at equal QPS (Sec. 6, Tables 3–4).

**Rubric.** A 1 (vector-store/index internals — retrieval efficiency, not a RAG technique axis) · B 2 (6 large datasets, many library baselines, ablations) · C 2 (open-source C++, CC BY 4.0 paper) · D 2 (CPU library, consumer-feasible) · E 0 (index codec — RAG-NIMBF uses chroma/lancedb backends; no config slot for the ANNS library) = **7/10, relevant** (efficiency reference for Vector-Store axis).

**Affected axis:** Vector-Store (informational; not expressible as a config value).

**Source:** https://arxiv.org/abs/2611.08306
