---
name: rag-radar
description: Screen new RAG research for RAG-NIMBF — score with rubric, summarise relevant papers, maintain the Obsidian vault, propose config.yaml experiments in a weekly fit check, propose code for RAG-NIMBF and Enterprise_RAG_Blueprint in a weekly implementation check, write monthly gap reports.
version: 1.1.0
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

## Runtime constraints (cron, no user present)
- Do NOT install packages (`pip`, `uv`, `apt`) and do NOT run inline scripts (`python -c`, `sh -c`, `node -e`);
  they are blocked in cron and waste memory on this 4 GB VPS.
- Do NOT use the browser tool. Use plain HTTP fetches (web/extract tool or `curl`) only.
- Read paper full text from the arXiv HTML version `https://arxiv.org/html/<arxiv-id>`;
  if it does not exist, use the abstract only. Never parse PDFs.
- Download PDFs with a single command: `curl -sSfL -o papers/<id>/paper.pdf https://arxiv.org/pdf/<arxiv-id>`.
- Process at most 30 inbox items per run; leave the rest in the inbox for the next run.

## Mode 1 — Daily screening (job `radar-daily`)
1. Read the first 30 lines of `state/inbox.jsonl`.
2. For each item: score A–E per rubric, using title + abstract (fetch the arXiv abstract page if the abstract is empty).
3. Append one row per item to `screening.csv`:
   `date,id,source,title,score,A,B,C,D,E,decision,reason` (date `YYYY-MM-DD`, title in double quotes,
   decision `relevant` or `logged`).
4. For each item with score >= 7 that is an arXiv paper:
   - verify ID via `https://export.arxiv.org/api/query?id_list=<arxiv-id>` (title must match),
   - download the PDF with `curl` (see runtime constraints) to `papers/<id>/paper.pdf`,
   - read `https://arxiv.org/html/<arxiv-id>` (at least abstract, method, results) and write `papers/<id>/summary.md`:
     core idea, key results as verbatim quotes with section, rubric score with justification per criterion,
     affected axis (name from `nimbf-capabilities.md`) or `New-Techniques`,
   - create `vault/Papers/<id>.md` from the template (`status: screened`, links to GitHub, **no PDF**),
   - append `- [[<id>]] — <one-line idea> (<score>)` to `vault/Axes/<Axis>.md`.
   GitHub releases with score >= 7: no PDF, only `papers/<id>/summary.md` + vault note.
5. Remove the processed lines from `state/inbox.jsonl` (keep unprocessed ones).
6. `git add -A && git commit -m "screen: <n> items (<k> relevant)" && git pull --rebase && git push`.
7. Final answer (sent to Telegram): number screened, list of relevant items with score and one line each. Nothing else.

## Mode 2 — Weekly fit check (job `radar-weekly`)
0. The pre-script `radar-metrics.py` has already pulled, written this week's row to `metrics/weekly.csv`
   and printed the self-evaluation metrics above. Do not edit `metrics/` yourself.
1. Candidates: vault notes with `status: screened` whose `screened` date is within the last 7 days.
2. For each candidate decide with `nimbf-capabilities.md`:
   - **expressible** → `proposals/<id>/config.yaml` from `proposal-template.yaml`: change exactly ONE axis
     (baseline vs. variant), keep everything else single-valued, fill the HYPOTHESIS header with a falsifiable,
     quantitative claim derived from the paper's reported numbers (metric, threshold in pp, dataset). Use only
     values listed as supported. Set vault note `status: proposed`.
   - **new technique, not expressible** → `proposals/<id>/new-axis.md`: what RAG-NIMBF would need
     (new config key, component, adapter), estimated effort. Set `status: fit`.
   - **not useful after all** → set `status: rejected` with one-line reason in the status log.
3. Vault status edits and `metrics/weekly.csv` are committed on `main` (`note: weekly status`).
4. Proposals: `git checkout -b proposal/<YYYY-Www>` from `main`, add only `proposals/`, commit
   (`proposal: <ids>`), `git push -u origin proposal/<YYYY-Www>`, then `git checkout main`.
5. Final answer: list of proposals with hypothesis, list of rejects with reason, and the compare link
   `https://github.com/niclashart/OSWS_Hermes-Agent/compare/main...proposal/<YYYY-Www>?expand=1`.
   If there are no candidates, answer `RAG Radar weekly: no candidates.` instead of these lists.
   Always end the answer with one line `Self-eval <week>: collected <n>, skipped <s>/<runs> runs,
   relevant <relevant>/<screened>, accepted <accepted_total>/<proposed_total>, cost $<cost_usd>`
   (values from the pre-script output, `n/a` where missing).

## Mode 3 — Monthly gap report (job `radar-monthly`)
1. Inputs: `screening.csv` rows and vault notes of the previous calendar month, plus `vault/Axes/New-Techniques.md`.
2. Write `reports/<YYYY-MM>-gap.md` and a copy `vault/Reports/<YYYY-MM>-gap.md`:
   - counts (screened / relevant / proposed / merged),
   - **Self-evaluation** — the rows of `metrics/weekly.csv` for that month as a table, plus month totals
     (collected, skip rate, relevant rate, acceptance rate, tokens, cost),
   - per axis: what is new in the literature, what RAG-NIMBF already covers, what is missing,
   - **Gaps** — techniques with evidence but no RAG-NIMBF support, ranked by evidence × feasibility,
   - suggested sentences for Related Work and Future Work of the next RAG-NIMBF paper, each with arXiv citation.
3. Commit on `main` (`report: <YYYY-MM>`), push. Final answer: the Gaps list.

## Mode 4 — Weekly implementation check (job `radar-impl`)
Goal: for papers that are **very useful**, check whether RAG-NIMBF (benchmarking framework) or
Enterprise_RAG_Blueprint (the RAG system) already has the functionality; if not, propose concrete code.
0. The pre-script `radar-impl.py` has already pulled, selected the candidates (score >= 8 or `status: fit`,
   screened in the last 7 days, not checked before) and refreshed read-only mirrors in `.cache/repos/`.
   Its output above lists the candidates and the current state of both repos:
   RAG-NIMBF `main` only; Enterprise_RAG_Blueprint `main` plus every other branch (files differing from `main`).
1. For each candidate read `papers/<id>/summary.md` (and `https://arxiv.org/html/<arxiv-id>` for method details).
   Decide per repo whether it is relevant at all: RAG-NIMBF = something to benchmark/evaluate (new axis value,
   component, metric, dataset adapter); Blueprint = something the production RAG system should do
   (loader/chunking, retriever, reranking, query refinement, guardrails, chain, API, frontend).
2. Existence check per relevant repo — search before you propose, and record the commands you ran:
   - `git -C .cache/repos/<repo> grep -n -i -E '<2-4 technique terms>' <ref> -- '*.py' '*.j2' '*.yaml'`
   - `git -C .cache/repos/<repo> show <ref>:<path>` to read the hits and the files you would change.
   RAG-NIMBF: ref `main` only. Blueprint: `main` **and** each branch from the pre-script output.
   Verdict per repo: `exists` (where, file:line), `partial` (what is missing), `missing`, or `not-applicable`.
3. Write a full proposal only if the verdict is `missing` or `partial` **and** the paper's evidence is strong
   (quantitative gain over a relevant baseline, feasible on consumer GPU / Ollama). At most 3 full proposals per run,
   best evidence first; the rest get the existence check plus a one-line reason. Skip when `exists`.
4. One file per paper: `implementations/<YYYY-Www>/<id>.md` with this structure:
   ```
   ---
   paper: <id>
   week: <YYYY-Www>
   rag-nimbf: {verdict: <exists|partial|missing|not-applicable>, ref: main@<sha>}
   blueprint: {verdict: <...>, ref: <branch>@<sha>}
   ---
   # <title>
   ## Why — evidence (verbatim quote with section, arXiv link)
   ## Existence check — table: repo | ref@sha | verdict | evidence (file:line) | commands run
   ## Proposal: RAG-NIMBF            (omit section if not proposed)
   ### Design — where it plugs in (module, adapter, registry, config key), data flow, defaults
   ### Files — for each file:
   #### NEW `<path>`      → complete file content in a fenced code block
   #### MODIFY `<path>`   → unified diff (```diff, --- a/<path> +++ b/<path>) against the stated ref
   ### Setup — YAML/config snippet (e.g. experiments/<name>.yaml), env vars, requirements, docker-compose
   ### Tests — complete pytest file following the repo's tests/ conventions
   ### Effort & risks — S/M/L, open questions
   ## Proposal: Enterprise_RAG_Blueprint   (same subsections; state the base branch, e.g. main or a branch
      that already contains related work such as feat/mcp-integration)
   ```
   Code rules: base every diff on the real file content from `git show <ref>:<path>` (never guess context lines);
   reuse the repo's existing interfaces, naming and config style; only open-licensed dependencies;
   mark the file header line `Draft generated by RAG Radar — untested, review before applying.`
5. `implementations/<YYYY-Www>/README.md`: table of all candidates (id, title, verdict per repo, proposed yes/no,
   one-line reason).
6. Append to each candidate's vault note status log: `- <YYYY-MM-DD> impl-check: NIMBF <verdict>, Blueprint <verdict>`;
   commit on `main` (`note: impl check`), push.
7. `git checkout -b impl/<YYYY-Www>` from `main`, add only `implementations/`, commit (`impl: <ids>`),
   `git push -u origin impl/<YYYY-Www>`, then `git checkout main`.
8. Final answer (Telegram, German): per proposal one block — paper + score, target repo(s), verdict, what gets
   added (files), effort; then the skipped candidates with reason; then the compare link
   `https://github.com/niclashart/OSWS_Hermes-Agent/compare/main...impl/<YYYY-Www>?expand=1`.
   If no proposal was written, answer `RAG Radar impl: nichts Neues — <n> geprüft, alles vorhanden/nicht relevant.`
   plus the README table as short lines, and still push the branch.

## Quality rules
- Never cite a paper not present in `screening.csv` / `papers/`.
- If unsure whether a technique is expressible, treat it as not expressible (`new-axis.md`).
- Keep summaries short (<= 300 words). No marketing language.
