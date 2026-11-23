# New axis proposal — Right Diagnosis, Unsafe Route: Auditing Clinical AI Decision Trajectories (arxiv-2611.22612)

- Paper: https://arxiv.org/abs/2611.22612
- Verdict: **not expressible** in RAG-NIMBF today.

## What RAG-NIMBF would need
Stepwise trajectory audit (per-checkpoint harm ratings) + corrective-oversight branching for agentic systems. RAG-NIMBF benchmarks single-pass RAG, not agentic decision trajectories. Needs: trajectory logging + per-step LLM-judge metric and intervention branches in the MCP agentic mode. Effort: L.
