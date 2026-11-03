# Lab 1 - Agentic loop on `stop_reason`

**Exam:** D1, task 1.1 (notes 2.1). Scenario 1 (support agent).
**Time:** about 1 hour. **Cost:** a few cents with Haiku.

## Rule to remember

Keep calling Claude while `stop_reason == "tool_use"`. Stop on `"end_turn"`.
Wrong stop signals: Claude wrote some text, Claude said "done", a fixed turn count.
A turn cap is OK only as a **safety net**, never as the main stop signal.

## Steps

1. **Predict first.** Write in the table below what each wrong mode will print.
2. Run the two wrong modes. Run each 2-3 times: model output changes between runs.
   ```bash
   python -m lab1_loop.loop wrong-text
   python -m lab1_loop.loop wrong-turns
   ```
   Look for: a final answer like "Let me check that" with no data, or an answer cut in the middle of the task.
3. Fill TODO 1-4 in `right_loop()` in [loop.py](loop.py). Don't open `common/agent_loop.py` yet: it is the answer.
4. Run `python -m lab1_loop.loop right`. You should see `get_customer` -> `list_orders` -> `lookup_order` (maybe in a different order), then a full answer: O1001, $129, refund possible (delivered 2026-10-20, within 30 days).
5. Compare your loop with [common/agent_loop.py](../common/agent_loop.py).

## Break it more (optional)

- In your loop, append only `text_of(response)` as the assistant turn, not the whole `response.content`. What error do you get? (The `tool_use` block is missing, so the `tool_result` has nothing to match.)
- Send each `tool_result` in its **own** user message instead of one message. Does it still work? The docs say: one message with all results, or Claude learns to stop calling tools in parallel.

## Log

| Mode | My prediction | What happened |
|---|---|---|
| wrong-text | | |
| wrong-turns | | |
| right | | |

Surprise? Add it to `CCAR-F-NOTES.md` section 10.
