# Lab 5 - Escalation handoff as structured output

**Exam:** D4 task 4.3, D5 tasks 5.1 and 5.2 (notes 5.3, 6.1, 6.2). Scenario 1.
**Time:** about 1 hour. **Cost:** cents.

## Rules to remember

- The human who takes the case has **no transcript**. The handoff must hold: customer id, order id, amount, root cause, what was tried, what the customer wants, the next step.
- Need valid structure every time => `tool_use` + JSON schema. Syntax errors go away. **Wrong facts** (semantic errors) still need validation.
- A field the source may not have => **nullable**, or the model invents a value.
- Open lists => enum with `"other"` + a `detail` field.
- Long chats lose facts in the middle ("lost in the middle"). Key facts go in their own block, not only in a summary.

## The chat

[data/transcripts/case_long.txt](../data/transcripts/case_long.txt): Minh's $820 laptop arrived cracked, a replacement is out of stock, they want a full refund to the card plus a free return label, and they ask for a human. A noise fact on purpose: an old order O0999 that is fine.

## Steps

1. **Predict:** how many of the 9 facts will a free-text summary keep?
2. Run `python -m lab5_handoff.handoff free-text` 2 times. Which facts got lost?
3. Finish `HANDOFF_TOOL` in [handoff.py](handoff.py) (see the TODO). Run `python -m lab5_handoff.handoff schema`.
   Target: 9/9 and no `O0999`.
4. Try a field that is **required and not nullable** for something the chat doesn't say (for example `phone_number`). Does the model invent a number? Then make it nullable and run again.

## Note

The script uses forced `tool_choice` with thinking turned off (they don't work together). Newest Opus / Sonnet
reject forced `tool_choice`. The script then falls back to `auto`. The current API also has structured outputs
(`output_config.format`), but the exam guide v1.0 tests the `tool_use` + schema way.

## Log

| Mode | Facts kept | Lost facts | Noise leaked? |
|---|---|---|---|
| free-text #1 | | | |
| free-text #2 | | | |
| schema | | | |
