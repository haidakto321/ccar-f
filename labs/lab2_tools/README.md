# Lab 2 - Tool descriptions and `tool_choice`

**Exam:** D2, tasks 2.1 and 2.3 (notes 3.1, 3.3). Scenario 1 and 4.
**Time:** about 1 hour. **Cost:** cents (8 short calls per run, nothing executed).

## Rules to remember

- Claude picks a tool **from its description**. Wrong tool picked => the cheapest first fix is a better description, not a classifier, a routing layer or a bigger model.
- A good description says: what it does, input format, what it returns, **when to use it instead of the similar tool**.
- `tool_choice`: `auto` = may answer in text. `any` = must call some tool. `{"type": "tool", "name": X}` = must call X.

## Steps

1. **Predict:** score of `vague` out of 8? Which cases will miss?
2. Run `python -m lab2_tools.tools vague` 2 times. Note the score and the misses.
3. Rewrite the 6 descriptions in `MY_TOOLS` in [tools.py](tools.py). Don't open `common/support_tools.py` yet.
4. Run `python -m lab2_tools.tools mine`. Target: 8/8 two runs in a row.
5. Compare with `python -m lab2_tools.tools ref` and the reference text in [common/support_tools.py](../common/support_tools.py).
6. Run `python -m lab2_tools.tools choice`. "Thanks, bye!" needs no tool. What does `any` / forced do with it?

## Note about newer models

On Claude Opus 5.5 and Sonnet 5.5, forced `tool_choice` (`any` / `tool`) returns a 400 error. The script catches it and prints a note. Haiku 5.5 (the lab default) is not on that list, so it should work there. The exam guide (v1.0) still tests `tool_choice` as a concept, so learn it anyway.

## Log

| Run | Score | Misses (which pair got mixed up?) |
|---|---|---|
| vague #1 | | |
| vague #2 | | |
| mine | | |
| ref | | |

| tool_choice | What came back |
|---|---|
| auto | |
| any | |
| forced | |
