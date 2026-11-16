# New-axis proposal — arXiv:2611.13675

**Paper:** "OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation" (arXiv:2611.13675) — vault note [[arxiv-2611.13675]], screened 2026-11-11, score 9/10.

## What the paper shows
Compresses retrieved context in pixel space: render pages as images, encode with a frozen DeepSeek-OCR encoder, distill into 16 query-conditioned prefix tokens for the LLM. Quote (Abstract): "OpticalRAG achieves the best compression-aware accuracy (CAP) on all three benchmarks while injecting only $16$ tokens, and improves the closed-book Qwen2.5-7B-Instruct backbone by $5.17$ points on LongBench-v2."

## Why not expressible in RAG-NIMBF today
Context compression / selection under a token budget is listed as not expressible. OpticalRAG additionally replaces *token* context with visual prefix tokens — RAG-NIMBF's prompt builder only assembles text chunks, has no image-rendering stage, no vision-encoder component, and no prefix-token injection into the LLM call.

## What RAG-NIMBF would need
- Config key `context_compression: none | optical` with `compression_prefix_tokens`, `compression_encoder` (frozen vision encoder provider).
- New stage between retrieval and generation: document rendering + encoder + query-conditioned compressor (~30.7M params, MIT-licensed code/weights).
- Metric: compression-aware accuracy (accuracy per injected token).

## Estimated effort
Large (~2–3 weeks): the prefix-token injection also requires touching the LLM provider layer (transformers-based generation with embeds input, not Ollama chat API). Feasible on consumer GPU quantized, but integration is invasive.
