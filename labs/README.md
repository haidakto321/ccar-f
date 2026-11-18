# CCAR-F labs - learn by building, then breaking

Small hands-on labs for the Claude Certified Architect - Foundations exam (guide v1.0).
One fake online shop (customers, orders, refunds) runs through all of them. No real data, no real money.

**The method:** in each lab you first run the **wrong** design (the kind of answer the exam uses as a trap),
watch it fail, then build the **right** one. Predict the result before every run: predicting is the exam skill.

## Labs

| Lab | Topic | Exam (notes section) | SDK | Time |
|---|---|---|---|---|
| 0 | Claude Code config on real repos (below) | D3 (4.x) | none | 1 evening |
| [1](lab1_loop/README.md) | Agentic loop on `stop_reason` | D1 1.1 (2.1) | anthropic | 1 h |
| [2](lab2_tools/README.md) | Tool descriptions, `tool_choice` | D2 2.1, 2.3 (3.1, 3.3) | anthropic | 1 h |
| [3](lab3_errors/README.md) | Structured errors, empty vs failed | D2 2.2, D5 5.3 (3.2, 6.3) | anthropic | 1-1.5 h |
| [4](lab4_hook/README.md) | Hook vs prompt for the $500 rule | D1 1.4, 1.5 (2.4, 2.5) | claude-agent-sdk | 1.5 h |
| [5](lab5_handoff/README.md) | Escalation handoff with a schema | D4 4.3, D5 5.1, 5.2 (5.3, 6.1, 6.2) | anthropic | 1 h |
| [6](lab6_extract/README.md) | Extraction: nullable, validate + retry, batch | D4 4.3-4.5, D5 5.5 (5.3-5.5, 6.5) | anthropic | 2 h |
| [7](lab7_multiagent/README.md) | Coordinator + subagents, provenance (optional) | D1 1.2, 1.3, D5 5.3, 5.6 (2.2, 2.3, 6.3, 6.6) | claude-agent-sdk | 2 h |

Suggested order: week 1 = lab 0 + labs 1-3, week 2 = labs 4-6, week 3 = lab 7 + mock exams.

## Setup (one time)

You need Python 3.10+ (you have 3.12) and an API key from [console.anthropic.com](https://console.anthropic.com).
The API is billed separately from a claude.ai plan: **Pro includes no API credits** (Max, Ultra and Team include
monthly API credits). Ask your company first, it may already have a Console workspace or credits. Otherwise buy the
smallest top-up, turn auto-reload off and set a spend limit. With the default model (Haiku 5.5) every lab costs cents.
Lab 0 needs no key: it runs on your Pro login.

Git Bash, from the repo root:

```bash
cd labs
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
```

PowerShell: same, but activate with `.venv\Scripts\Activate.ps1` and copy with `Copy-Item .env.example .env`.

Then open `labs/.env` and paste your key after `ANTHROPIC_API_KEY=`. **`labs/.env` is git-ignored. Never commit it** (this repo is on GitHub).

> ⚠️ **Keep the key in `labs/.env` only. Never set `ANTHROPIC_API_KEY` globally** (Windows environment variables,
> `~/.bashrc`, PowerShell profile). When it is set, Claude Code uses the key instead of your Pro login and you pay
> API prices for your normal Claude Code work. The labs load `labs/.env` inside the Python process only, so your
> terminal and Claude Code stay on Pro. Check with `echo $ANTHROPIC_API_KEY` (Git Bash) or
> `$env:ANTHROPIC_API_KEY` (PowerShell): it should print nothing.

Run every lab **from the `labs` folder**, as a module:

```bash
python -m lab1_loop.loop wrong-text
```

## Rules of the game

- `TODO` in a lab file = your part. The script raises `NotImplementedError` until you fill it.
- `common/` holds the **reference answers** (the loop, tool descriptions, structured errors). Open it **after** you try.
- `common/fake_db.py` is the fake backend. `fake_db.reset()` gives clean data for each run.
- Each lab README ends with a **Log** table. Fill it. Anything that surprised you goes into `CCAR-F-NOTES.md` section 10, like a mock-test mistake.
- Models are probabilistic: run each wrong mode 2-3 times before you decide what it does.

## Lab 0 - Claude Code configuration (no code to write)

D3 is 20% of the exam and you already use Claude Code every day. Map what you have to exam rules:

| Look at | Exam topic (notes) |
|---|---|
| `~/.claude/CLAUDE.md` + any `@<file>.md` import in it | CLAUDE.md hierarchy: user level = only you, teammates don't get it (4.1) |
| `~/.claude/settings.json` hooks (UserPromptSubmit, SessionStart with `compact`) | hooks are certain, a prompt is not (2.5) |
| A skill's `SKILL.md` frontmatter (any installed skill) | `context: fork`, `allowed-tools`, `argument-hint`; skill = on demand, CLAUDE.md = always (4.2) |
| `/memory` in a session | which memory files are loaded (4.1) |

Then, on a **throwaway branch** of a real repo, try the team-level setup:

- `.claude/rules/api.md` with `paths:` for the controller folder. Check it loads only when you edit a matching file (4.3).
- A project skill in `.claude/skills/` with `context: fork` and `allowed-tools` (4.2).
- `.mcp.json` with a `${ENV_VAR}` for a secret, plus a personal server in `~/.claude.json`. Check both load (3.4).
- Plan mode vs direct on 3 tasks: a one-file fix, a multi-file migration, a feature with several designs (4.4).
- `claude -p "review this diff" --output-format json --json-schema '<schema>'` as a CI step (4.6).

Delete the branch after. Write one line per item in the notes: "this = which exam rule".

## Folder map

```
labs/
  common/          config, fake backend, tool definitions, reference loop (answer key)
  data/            customers, orders, receipts (+ expected.json), chat transcript, knowledge base
  lab1_loop/ ... lab7_multiagent/   one folder per lab: README + script
  implementation-notes.md           decisions and trade-offs made while building the labs
```
