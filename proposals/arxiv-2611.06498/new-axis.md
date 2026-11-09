# New-axis proposal — arXiv:2611.06498

**Paper:** "Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation" (arXiv:2611.06498) — vault note [[arxiv-2611.06498]], screened 2026-11-05, score 8/10.

## What the paper shows
Signed knowledge packs for offline/edge RAG prove who published the pack but not that precomputed vectors encode the signed text ("text-vector integrity gap"). The paper derives the "margin law" and proposes exact verification of quantisation codes. Quote (Abstract / Sec. 5.5): "on a Raspberry Pi 5 running a local language model, such an attack lowers correct answers from 0.75 to 0.39"; verified quantisation codes "accepted every honest vector in our samples on three platforms and left the publisher no choice."

## Why not expressible in RAG-NIMBF today
RAG-NIMBF computes embeddings itself from the corpus (no precomputed-vector ingestion), so the attack surface (a publisher controlling vectors) does not exist in the benchmark — and neither does the defense. There is no axis for ingestion-trust modes or integrity verification, and no security metric (hijack rate).

## What RAG-NIMBF would need
- Ingestion mode that accepts external/precomputed vector packs (`ingestion_method` extension with a `precomputed` value + trust flags).
- Security evaluation mode: inject tampered vectors at a target rate and report answer-hijack rate alongside standard metrics; deterministic reproduction of the margin-law estimate from retrieval-margin distributions.

## Estimated effort
Medium (~1 week for a minimal tamper-injection + hijack-rate metric on the existing index path). Relevant mainly if RAG-NIMBF grows an offline/edge deployment scenario.
