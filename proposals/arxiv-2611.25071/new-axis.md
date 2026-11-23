# New axis proposal — FinVeriQA: Financial Research Agents for Question Answering (arxiv-2611.25071)

- Paper: https://arxiv.org/abs/2611.25071
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Multi-agent financial QA with routing, tool use and provenance-aware verification; key finding: verification must be independent of the writing context. RAG-NIMBF has agentic MCP mode but no independent-verifier stage or provenance metric. Needs: `verifier` component (separate context) + custom metric provenance-violation rate. Effort: M.
