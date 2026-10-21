# OSWS_Hermes-Agent — RAG Radar

Agent-based research monitoring for [RAG-NIMBF](https://github.com/aiengineeringblueprints/RAG-NIMBF),
run by [Hermes Agent](https://hermes-agent.nousresearch.com/docs) on a VPS (see `proposal.pdf`).

```
Collectors → Relevance eval → PDF + summary → weekly fit check → config.yaml (PR) → human review → merge
```

| Path | Content |
|---|---|
| `screening.csv` | every screened item with rubric score (audit trail) |
| `papers/<id>/` | `paper.pdf` + `summary.md` for relevant papers (score >= 7) |
| `proposals/<id>/` | `config.yaml` with hypothesis, or `new-axis.md` — via branch `proposal/<YYYY-Www>` |
| `reports/` | monthly gap reports |
| `vault/` | Obsidian vault (notes only, no PDFs) — open this folder in Obsidian |
| `reference/` | rubric, RAG-NIMBF capabilities, config template |
| `scripts/radar-collect.py` | collector (arXiv, Semantic Scholar, GitHub releases), Hermes pre-script |
| `skill/rag-radar/` | Hermes skill with the methodology |
| `AGENTS.md` | hard rules, injected into every job via `--workdir` |

## Jobs (Hermes cron)
| Job | Schedule (UTC) | What |
|---|---|---|
| `radar-daily` | `0 6 * * *` | collect → score → summaries + vault notes → push to `main` |
| `radar-weekly` | `0 8 * * 1` | fit check → proposals on branch → Telegram compare link |
| `radar-monthly` | `0 9 1 * *` | gap report |

## Review a proposal
Open the compare link from Telegram, create the PR, review hypothesis + config, merge or close.
