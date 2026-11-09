# Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation

- arXiv: https://arxiv.org/abs/2611.09807
- Score: 8/10 · Axis: New-Techniques · Verified: yes (export.arxiv.org, title match)

## Core idea
Instead of retrieving from the raw transcript, a conversational memory compacts each turn into atomic facts stored in a two-tier store (working + archive) with decay/reinforcement weights. Compared head-to-head with transcript RAG on LoCoMo using a paired design (both arms on all 1,985 questions, McNemar's exact test on the 512 discordant pairs).

## Key results (verbatim)
> "On the four categories comparable work reports, compaction scores 71.4 per cent against 64.6, a lead of 6.8 points (p = 5.5e-08) at 34 per cent fewer prompt tokens." (Abstract / Sec. 5.1, Table 1)

> "The temporal category carries the result. A lead of 25.5 points on 321 questions, with 101 won and 19 lost, is larger than the entire scored-four lead" (Sec. 5.1)

> "Compaction wins where the answer is a value the extractor can compute or normalise once and store ... Transcript retrieval wins where the answer is a phrasing" (Sec. 6)

> "On all five, including the adversarial set comparable work drops, the lead falls to 2.0 and stops being significant, because the baseline leads adversarial by 14.6." (Abstract)

Per-question predictions, scripts and JSON are released: https://github.com/BigBrown10/nmafc-paper (analysis runs without API keys).

## Rubric
A 2 · B 2 · C 2 · D 1 · E 1 — A: new memory-compaction technique, not an existing axis; B: paired eval with significance tests and ablations; C: full code/data release; D: shipped arm uses paid-API inference for ingestion (analysis is CPU-only); E: needs a new memory/ingestion component, not a config value.

## Affected axis
New-Techniques — conversational-memory compaction / tiered fact store is not expressible in RAG-NIMBF (no context-compression or memory-tiering axis).

## Status log
- 2026-11-09 screened
