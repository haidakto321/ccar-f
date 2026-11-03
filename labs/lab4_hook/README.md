# Lab 4 - A hook enforces the money rule, a prompt only asks

**Exam:** D1 tasks 1.4 and 1.5 (notes 2.4, 2.5). Scenario 1. Golden rule 1.
**Time:** about 1.5 hours. **Cost:** each run is capped at $0.50 (`max_budget_usd`); with Haiku expect much less.
**Needs:** `claude-agent-sdk` (see the main [README](../README.md)).

## Rule to remember

Need a **guarantee** (money, identity, a required order of steps) => put it in code: a hook or a gate.
A system prompt rule is **probabilistic**. One clever message can talk the model past it.

- `PreToolUse` hook = check or **block** a call before it runs (refund > $500 => deny, escalate).
- `PostToolUse` hook = change the **result** after it runs (for example, normalize date formats).

## Steps

1. **Predict:** out of 3 `prompt-only` runs, how many refund $820 anyway?
2. Run `python -m lab4_hook.hook prompt-only 3`. The prompt has fake "manager approved" pressure.
   Haiku may hold the rule every time. That doesn't prove the prompt is safe: try 5 runs, or make the
   pressure stronger in `PROMPT`. The point is that you can't **prove** a prompt holds. You can prove a hook does.
3. Write `block_big_refunds()` in [hook.py](hook.py).
4. Run `python -m lab4_hook.hook hook 3`. Expected: 0 refunds above $500 in every run, and the agent escalates
   because your deny reason told it what to do.
5. Try: return the deny **without** a useful `permissionDecisionReason`. What does the agent do then?

## Exam traps this lab covers

- "Add a stronger rule to the system prompt" / "add few-shot examples of refusing" = still probabilistic. Wrong when the question says "guarantee".
- The hook's deny reason should say **what to do instead** (escalate), not only "no".
- SDK name check: the exam says the subagent tool is `Task`. The current SDK calls it `Agent` (see lab 7).

## Log

| Mode | Runs | Refund > $500 went through | Escalated |
|---|---|---|---|
| prompt-only | | | |
| hook | | | |
