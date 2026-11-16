# New-axis proposal — arXiv:2611.10335

**Paper:** "Two-Sided Conformal Evidence Sets for Retrieval-Augmented Generation" (arXiv:2611.10335) — vault note [[arxiv-2611.10335]], screened 2026-11-11, score 7/10.

## What the paper shows
Conformal Evidence Sets (CES): separate support and refutation passage sets with finite-sample coverage guarantees. Quote (Abstract): "CES closely tracks nominal coverage across α∈{0.05,0.10,0.15,0.20,0.30}, with maximum deviations of 3.0 percentage points for support and 5.4 for refutation."

## Why not expressible in RAG-NIMBF today
CES is a calibrated post-retrieval component plus a coverage metric — neither exists. RAG-NIMBF's retrieval metrics (hit@k, nDCG@k, RAGAS context precision/recall) measure ranking quality, not distribution-free coverage of a selected evidence set at a chosen risk level α, and there is no refutation-detection concept.

## What RAG-NIMBF would need
- New post-retrieval component `evidence_set: none | conformal-2sided` with knob `conformal_alpha`.
- New metrics: empirical support/refutation coverage and set size, evaluated across α sweeps (a new matrix axis `conformal_alphas`).
- Calibration-split handling in the evaluation harness (exchangeability requirement).

## Estimated effort
Medium (~1 week): the statistics are closed-form; effort goes into the calibration/eval split plumbing and the α-sweep reporting. No public reference code exists (C=1), so implementation is from the paper's description.
