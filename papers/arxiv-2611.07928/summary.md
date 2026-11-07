# ZeroRAG: Adaptive Semantic Peer Routing for Decentralized RAG (arXiv-2611.07928)

**Core idea.** Decentralized retrieval layer for RAG: documents stay with owning peers; each peer keeps only neighbor advertisements and a query-routing cache. Queries take a best-first walk over a self-organizing semantic overlay — no DHT, no central coordinator.

**Key results.**
> "ZeroRAG approaches the recall and end-to-end RAG answer accuracy of a centralized document store, without any global index, and 99% of queries locate the best supporting document in at most 13 peer contacts." (Sec. 4/Summary)
> "We find that ZeroRAG outperforms baselines in terms of recall and required network messages, approaches the recall and LLM answer accuracy of a centralized document store, self-heals after catastrophic peer failures, and scales to 100 000 peers." (Abstract)

**Rubric.** A 2 (new RAG technique: decentralized/P2P retrieval — clearly not an existing axis) · B 2 (3 real-world workloads, 2 decentralized baselines + centralized baseline, ablations) · C 1 (Middleware '26 paper, code release not stated in abstract) · D 1 (multi-peer deployment, not a consumer-GPU concern) · E 0 (requires a network of peer nodes — framework redesign, not an adapter) = **7/10, relevant** (New-Techniques; architectural, low integration priority).

**Affected axis:** New-Techniques (decentralized retrieval topology).

**Source:** https://arxiv.org/abs/2611.07928
