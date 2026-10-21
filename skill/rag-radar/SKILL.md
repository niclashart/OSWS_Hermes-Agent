---
name: rag-radar
description: Screen new RAG research for RAG-NIMBF — score with rubric, summarise relevant papers, maintain the Obsidian vault, propose config.yaml experiments in a weekly fit check, write monthly gap reports.
version: 1.0.0
author: Niclas Hart
metadata:
  hermes:
    tags: [research, rag, arxiv, obsidian]
---

# RAG Radar

Working directory: `/opt/data/osws` (git repo `niclashart/OSWS_Hermes-Agent`).
Read `AGENTS.md` there first; its hard rules override everything below.
References (read before scoring / proposing):
- `reference/rubric.md` — scoring rubric, threshold 7/10
- `reference/nimbf-capabilities.md` — what RAG-NIMBF can express (axes, YAML keys, values)
- `reference/full-grid-example.yaml` — real RAG-NIMBF config schema
- `reference/proposal-template.yaml` — template for proposals
- `vault/Templates/paper-note.md` — template for vault notes

## Mode 1 — Daily screening (job `radar-daily`)
1. Read every line of `state/inbox.jsonl`.
2. For each item: score A–E per rubric, using title + abstract (fetch the arXiv abstract page if the abstract is empty).
3. Append one row per item to `screening.csv`:
   `date,id,source,title,score,A,B,C,D,E,decision,reason` (date `YYYY-MM-DD`, title in double quotes,
   decision `relevant` or `logged`).
4. For each item with score >= 7 that is an arXiv paper:
   - verify ID via `https://export.arxiv.org/api/query?id_list=<arxiv-id>` (title must match),
   - download `https://arxiv.org/pdf/<arxiv-id>` to `papers/<id>/paper.pdf`,
   - read the PDF (at least abstract, method, results) and write `papers/<id>/summary.md`:
     core idea, key results as verbatim quotes with section, rubric score with justification per criterion,
     affected axis (name from `nimbf-capabilities.md`) or `New-Techniques`,
   - create `vault/Papers/<id>.md` from the template (`status: screened`, links to GitHub, **no PDF**),
   - append `- [[<id>]] — <one-line idea> (<score>)` to `vault/Axes/<Axis>.md`.
   GitHub releases with score >= 7: no PDF, only `papers/<id>/summary.md` + vault note.
5. Truncate `state/inbox.jsonl` to empty.
6. `git add -A && git commit -m "screen: <n> items (<k> relevant)" && git pull --rebase && git push`.
7. Final answer (sent to Telegram): number screened, list of relevant items with score and one line each. Nothing else.

## Mode 2 — Weekly fit check (job `radar-weekly`)
1. Candidates: vault notes with `status: screened` whose `screened` date is within the last 7 days.
2. For each candidate decide with `nimbf-capabilities.md`:
   - **expressible** → `proposals/<id>/config.yaml` from `proposal-template.yaml`: change exactly ONE axis
     (baseline vs. variant), keep everything else single-valued, fill the HYPOTHESIS header with a falsifiable,
     quantitative claim derived from the paper's reported numbers (metric, threshold in pp, dataset). Use only
     values listed as supported. Set vault note `status: proposed`.
   - **new technique, not expressible** → `proposals/<id>/new-axis.md`: what RAG-NIMBF would need
     (new config key, component, adapter), estimated effort. Set `status: fit`.
   - **not useful after all** → set `status: rejected` with one-line reason in the status log.
3. Vault status edits are committed on `main` (`note: weekly status`).
4. Proposals: `git checkout -b proposal/<YYYY-Www>` from `main`, add only `proposals/`, commit
   (`proposal: <ids>`), `git push -u origin proposal/<YYYY-Www>`, then `git checkout main`.
5. Final answer: list of proposals with hypothesis, list of rejects with reason, and the compare link
   `https://github.com/niclashart/OSWS_Hermes-Agent/compare/main...proposal/<YYYY-Www>?expand=1`.
   If there are no candidates, answer only `RAG Radar weekly: no candidates.`

## Mode 3 — Monthly gap report (job `radar-monthly`)
1. Inputs: `screening.csv` rows and vault notes of the previous calendar month, plus `vault/Axes/New-Techniques.md`.
2. Write `reports/<YYYY-MM>-gap.md` and a copy `vault/Reports/<YYYY-MM>-gap.md`:
   - counts (screened / relevant / proposed / merged),
   - per axis: what is new in the literature, what RAG-NIMBF already covers, what is missing,
   - **Gaps** — techniques with evidence but no RAG-NIMBF support, ranked by evidence × feasibility,
   - suggested sentences for Related Work and Future Work of the next RAG-NIMBF paper, each with arXiv citation.
3. Commit on `main` (`report: <YYYY-MM>`), push. Final answer: the Gaps list.

## Quality rules
- Never cite a paper not present in `screening.csv` / `papers/`.
- If unsure whether a technique is expressible, treat it as not expressible (`new-axis.md`).
- Keep summaries short (<= 300 words). No marketing language.
