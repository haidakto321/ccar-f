# Lab 7 (optional) - Coordinator + subagents

**Exam:** D1 tasks 1.2 and 1.3, D5 tasks 5.3 and 5.6 (notes 2.2, 2.3, 6.3, 6.6). Scenario 3 (multi-agent research).
**Time:** about 2 hours. **Cost:** capped at $1.00 per run (`max_budget_usd`).
**Needs:** `claude-agent-sdk`.

## Rules to remember

- A subagent does **not** see the coordinator's conversation. Everything it needs goes **in the prompt** of the Agent call.
- The coordinator needs the subagent tool in `allowedTools`. The exam guide calls it `"Task"`; the current SDK calls it `"Agent"` (the `system:init` tool list still says `Task`).
- Parallel = **several Agent calls in one response**.
- Subagent output: claim + evidence + source + date, so the final report keeps provenance.
- Two sources disagree => keep **both**, with source and date. Don't silently pick one.
- A subagent fails => the coordinator gets a structured error, goes on with partial results, and writes down the coverage gap.

## The knowledge base

[data/kb](../data/kb): our policy (30 days), Q3 support stats (12% of refund requests come on day 31-45),
and two competitor notes that **disagree**: 45 days (2025 marketing note) vs 60 days (2026 help page, electronics 30).

## Steps

1. Run `python -m lab7_multiagent.research wrong`. Look at what the coordinator sends each subagent, and at the `MISS` lines.
2. Fill TODO 1 and 2 in [research.py](research.py). Run `python -m lab7_multiagent.research right`.
   Target: 2 subagents in one response, all checks OK.
3. Break it: in the right version, ask the coordinator to run the subagents one after another. Compare the time in `duration_ms` (print it from `ResultMessage`).
4. Break it more: move `competitor-notes-2026.md` out of `data/kb` for one run (put it back after). Does the report say a source is missing, or does it state 45 days as fact?

## Log

| Mode | What subagents got | Parallel? | Checks OK |
|---|---|---|---|
| wrong | | | |
| right | | | |
