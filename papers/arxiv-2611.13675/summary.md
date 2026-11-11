# OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation

arXiv 2611.13675 · CC BY 4.0 · code MIT (https://github.com/brighterr/OpticalRAG)

## Core idea
Render retrieved documents as page images, encode them with a frozen vision encoder (DeepSeek-OCR DeepEncoder, ~100 visual tokens/page), retrieve visual tokens via a text-to-visual projection ("Encoder-Bridged Retrieval", no contrastive training), and distill them with a cross-attention compressor into as few as 16 query-conditioned prefix tokens fed to the LLM. Compression happens in pixel space instead of token space.

## Key results (verbatim)
> "On LongBench-v2, BAMBOO, and LooGLE-v2, OpticalRAG achieves the best compression-aware accuracy (CAP) on all three benchmarks while injecting only $16$ tokens, and improves the closed-book Qwen2.5-7B-Instruct backbone by $5.17$ points on LongBench-v2." (Abstract)

> "Modern visual encoders can pack the contents of a rendered text page into roughly a hundred visual tokens with little semantic loss" (§1)

## Rubric
A 2 · B 2 · C 2 · D 1 · E 2 — 10/10 → relevant. New compression modality (context-compression axis), 3 benchmarks vs strong baselines (LLMLingua-2, truncation), code+weights MIT, needs frozen DeepSeek-OCR encoder + 7B LLM (runs quantized on consumer GPU, compressor only ~30.7M params).

## Affected axis
New-Techniques — context compression / selection under token budget is not expressible in RAG-NIMBF today (see nimbf-capabilities.md "Not expressible").

## Status log
- 2026-11-11 screened
