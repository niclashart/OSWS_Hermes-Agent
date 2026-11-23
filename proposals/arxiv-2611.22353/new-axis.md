# New axis proposal — NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval (arxiv-2611.22353)

- Paper: https://arxiv.org/abs/2611.22353
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Adversarial non-semantic string probes that outrank judged-relevant passages. Not a config axis: needs a probe-corpus dataset adapter (jsonl works for the corpus, but the QRP-rank metric does not exist). Needs: custom metric 'QRP outranked by probe (rank gap)' plus probe-injection dataset mode. Effort: M.
