# New-axis proposal — arXiv:2611.02387

**Paper:** "EviCast: Forecasting Retrieval Gains Through Shared Response Calibration" (arXiv:2611.02387) — vault note [[arxiv-2611.02387]], screened 2026-11-04, score 8/10.

## What the paper shows
Forecasts the end-to-end net utility of RAG configurations before deployment by calibrating against shared responses. Quote (Abstract): "EviCast correctly decides all 14 HotpotQA retrieval configurations with a forecast error of 2.75 F1 points while reducing diagnostic generation calls by 80%."

## Why not expressible in RAG-NIMBF today
This is a *meta-evaluation* method: predicting which grid configurations are worth running, rather than a retrievable pipeline component. RAG-NIMBF's matrix executes all combinations; there is no mechanism to forecast scores per configuration or prune the grid by predicted utility before spending run budget.

## What RAG-NIMBF would need
- A grid-pruning front-end: config key `matrix_pruning: <none | forecast>` in the orchestration layer (`benchmark/orchestration/matrix.py`) that scores candidate combos with a calibrated predictor and runs only the top-k.
- Reporting: predicted vs. measured score per configuration to validate the forecaster on past runs.

## Estimated effort
Medium: isolated to orchestration (no benchmark-code changes); predictor training uses historical run results. Value grows with matrix size — currently marginal for the small grids used here.
