# They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs

- arXiv: https://arxiv.org/abs/2611.02587
- Screened: 2026-11-04 · Score: 8/10 · Rubric A-E: (1, 2, 2, 2, 1)
- Axis: Evaluation

## Core idea
Bilingual benchmark (EN/AR) probing five open-weight LLMs on exact Hadith recall without retrieval: no model reproduces the source text exactly; authors argue verified-corpus RAG should be mandatory for such high-stakes recall.

## Key results (verbatim quotes)
> "0% of 30,000 responses achieve both high lexical and high semantic fidelity, i.e., an exact, verifiable match to the source text." (Abstract)

## Rubric justification
A=1: direct-mode (no-retrieval) hallucination evaluation, supports the retrieval_mode: direct baseline (Evaluation); B=2 30k scored responses; C=2 code public; D=2 small local models; E=1 evaluation protocol, not a config value.

## RAG-NIMBF relevance
Maps to the **Evaluation** axis; see vault note.
