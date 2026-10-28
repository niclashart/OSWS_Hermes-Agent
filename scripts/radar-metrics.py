#!/opt/hermes/.venv/bin/python3
"""RAG Radar self-evaluation (Hermes cron pre-script of radar-weekly, no LLM).

Computes the radar's own metrics for the last 7 days and writes one row per ISO week
to metrics/weekly.csv (re-runs replace the row of the same week):
collected items, skipped runs (wakeAgent=false), screened/relevant items, proposals,
acceptance rate (proposals merged into main), LLM tokens and estimated cost.
Stdout is injected into the radar-weekly prompt.
"""
import csv
import datetime as dt
import json
import os
import subprocess

REPO = os.environ.get("RADAR_REPO", "/opt/data/osws")
HERMES = os.environ.get("HERMES_HOME", "/opt/data")
RUNS = os.path.join(REPO, "state", "runs.jsonl")
SCREENING = os.path.join(REPO, "screening.csv")
OUT = os.path.join(REPO, "metrics", "weekly.csv")
JOBS = os.path.join(HERMES, "cron", "jobs.json")
USAGE = os.path.join(HERMES, "cron", "usage_audit.jsonl")
PRICES = os.path.join(HERMES, "models_dev_cache.json")
PROVIDER = os.environ.get("RADAR_PROVIDER", "zai")

FIELDS = [
    "week", "from", "to", "collector_runs", "skipped_runs", "skip_rate", "collected",
    "screened", "relevant", "relevant_rate", "proposed_week", "proposed_total",
    "accepted_total", "acceptance_rate", "llm_runs", "prompt_tokens",
    "completion_tokens", "cost_usd",
]


def git(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args], check=True, capture_output=True, text=True
    ).stdout


def ts(s):
    t = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)


def rate(num, den):
    return round(num / den, 3) if den else ""


def collector_stats(start, end):
    runs = skipped = collected = 0
    if os.path.exists(RUNS):
        for line in open(RUNS):
            if not line.strip():
                continue
            r = json.loads(line)
            if start <= ts(r["ts"]) < end:
                runs += 1
                skipped += not r["woke"]
                collected += r["new"]
    return runs, skipped, collected


def screening_stats(start, end):
    screened = relevant = 0
    with open(SCREENING, newline="") as f:
        for row in csv.DictReader(f):
            try:
                d = dt.date.fromisoformat(row["date"])
            except (TypeError, ValueError):
                continue
            if start.date() <= d < end.date():
                screened += 1
                relevant += row["decision"] == "relevant"
    return screened, relevant


def proposal_ids(ref):
    ids = set()
    for path in git("ls-tree", "-r", "--name-only", ref, "--", "proposals").split():
        parts = path.split("/")
        if len(parts) == 3:
            ids.add(parts[1])
    return ids


def proposal_stats(week):
    """Proposals live on proposal/<YYYY-Www> branches; accepted = merged into main."""
    accepted = proposal_ids("origin/main")
    branches = git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/proposal/").split()
    proposed, this_week = set(accepted), set()
    for b in branches:
        ids = proposal_ids(b)
        proposed |= ids
        if b.endswith(week):
            this_week = ids
    return len(this_week), len(proposed), len(accepted)


def llm_stats(start, end):
    jobs = json.load(open(JOBS))["jobs"]
    radar = {j["id"] for j in jobs if j["name"].startswith("radar-")}
    try:
        cost = json.load(open(PRICES))[PROVIDER]["models"]
    except (OSError, KeyError, ValueError):
        cost = {}
    runs = prompt = completion = 0
    usd = 0.0
    priced = True
    for line in open(USAGE):
        u = json.loads(line)
        if u["job_id"] not in radar or not start <= ts(u["ts"]) < end:
            continue
        runs += 1
        prompt += u["prompt_tokens"]
        completion += u["completion_tokens"]
        price = cost.get(u.get("model") or "", {}).get("cost")
        if price:
            # List price per 1M tokens; cached input is billed lower, so this is an upper bound.
            usd += (u["prompt_tokens"] * price["input"] + u["completion_tokens"] * price["output"]) / 1e6
        else:
            priced = False
    return runs, prompt, completion, round(usd, 2) if priced else ""


def write_row(row):
    rows = []
    if os.path.exists(OUT):
        with open(OUT, newline="") as f:
            rows = [r for r in csv.DictReader(f) if r["week"] != row["week"]]
    rows.append(row)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["week"]))


def main():
    git("pull", "-q", "--rebase", "--autostash")
    git("fetch", "-q", "--prune", "origin")
    end = dt.datetime.now(dt.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - dt.timedelta(days=7)
    y, w, _ = (end - dt.timedelta(days=1)).isocalendar()
    week = f"{y}-W{w:02d}"

    runs, skipped, collected = collector_stats(start, end)
    screened, relevant = screening_stats(start, end)
    proposed_week, proposed_total, accepted = proposal_stats(week)
    llm_runs, prompt, completion, usd = llm_stats(start, end)
    row = {
        "week": week, "from": start.date().isoformat(),
        "to": (end - dt.timedelta(days=1)).date().isoformat(),
        "collector_runs": runs, "skipped_runs": skipped, "skip_rate": rate(skipped, runs),
        "collected": collected, "screened": screened, "relevant": relevant,
        "relevant_rate": rate(relevant, screened), "proposed_week": proposed_week,
        "proposed_total": proposed_total, "accepted_total": accepted,
        "acceptance_rate": rate(accepted, proposed_total), "llm_runs": llm_runs,
        "prompt_tokens": prompt, "completion_tokens": completion, "cost_usd": usd,
    }
    write_row(row)

    print(f"RAG Radar self-evaluation {week} ({row['from']}..{row['to']}), written to metrics/weekly.csv:")
    for k in FIELDS[3:]:
        print(f"- {k}: {row[k] if row[k] != '' else 'n/a'}")


if __name__ == "__main__":
    main()
