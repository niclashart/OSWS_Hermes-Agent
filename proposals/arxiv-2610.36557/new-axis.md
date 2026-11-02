# New-axis proposal — arXiv:2610.36557 (QESChunker)

**Paper:** "QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking for RAG" (arXiv:2610.36557) — vault note [[arxiv-2610.36557]], screened 2026-10-28, score 8/10.

## What the paper shows
First supervised chunker: builds document-specific static chunk indices by maximizing question-evidence utility from human- or LLM-generated pairs. Non-overlap is solved exactly by dynamic programming; the overlapping case is monotone submodular, optimized with a (1-1/√e)-approximation greedy. Quote (Abstract): "Across two self-constructed and three public datasets, both variants outperform existing chunking methods in complete-evidence recall in nearly all evaluated settings, under the same overlap regime and a fixed hybrid retriever."

## Why not expressible in RAG-NIMBF today
`matrix.chunking_strategies` values are all fixed algorithms (`recursive`, `token`, `semantic`, …) with global size/overlap parameters. QESChunker is (a) *trained* — it needs a question-evidence pair set to fit the utility model, and (b) *document-specific* — chunk boundaries are computed per document from that model, not from a global rule. Both are outside the current Chunking axis: there is no training axis and no mechanism for a chunker that requires a fitted artifact plus per-document inference.

## What RAG-NIMBF would need
- New chunking-strategy value `supervised` in `benchmark/chunking.py` plus new settings: `chunker_model_path` (fitted artifact), `chunker_pairs_dataset` (training/held-out QA pairs), `chunker_overlap: none | soft`, `chunker_top_chunks_per_doc`.
- Either a training mode (`benchmark_stage: chunker-training`) or the convention that the artifact ships pre-trained; a training loop inside the benchmark is out of scope and would be a larger change.
- Note: code availability/license is unclear (C=1) — before implementing, confirm the release; otherwise reimplement the DP objective from the paper (Apache/MIT, feasible: DP + greedy are simple).

## Estimated effort
Medium (~1 week if using released code, ~2 weeks for own reimplementation): new strategy class + artifact loading + config keys + tests. Blocked on C=1 (license clarity) — re-run this fit check once the release is confirmed.
