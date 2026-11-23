# New axis proposal — Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web (arxiv-2611.19900)

- Paper: https://arxiv.org/abs/2611.19900
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Field-verification benchmark with attribution + abstention scoring on live web pages. RAG-NIMBF has `abstain_strict` prompting but no dataset adapter for this benchmark and no attribution-rate metric. Needs: new dataset adapter (web-corpus + fictitious-company probes) and custom metric 'supported-claim rate / abstention correctness'. Effort: M.
