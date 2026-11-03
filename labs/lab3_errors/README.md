# Lab 3 - Structured tool errors

**Exam:** D2 task 2.2, D5 task 5.3 (notes 3.2, 6.3). Scenario 1 and 3.
**Time:** about 1-1.5 hours. **Cost:** cents.

## Rules to remember

- An error tells the agent **what kind** of failure (transient / validation / business / permission), **if a retry can help**, and **what to do next**.
- Only **transient** errors are worth a retry. Business rule => don't retry, explain to the customer.
- **Access failure != empty result.** "Could not load orders" and "has no orders" must look different to the model.
- Wrong answers on the exam: a generic "Error", returning an empty result as if it worked, stopping the whole workflow on one failure.

## The 3 scenarios

| Scenario | What breaks | Good agent |
|---|---|---|
| transient | `lookup_order` times out once | retries once, then answers |
| business | O1002 delivered 93 days ago, policy is 30 | no retry, explains policy |
| empty | `list_orders` times out once | notices it, retries, finds O1006 |

## Steps

1. **Predict** each cell of the log table before you run it.
2. Run the two wrong styles:
   ```bash
   python -m lab3_errors.errors empty
   python -m lab3_errors.errors generic
   ```
   Look for: "you have no orders" (false!), or the agent giving up / retrying something that can never work.
3. Write `my_structured_error()` in [errors.py](errors.py). Run `python -m lab3_errors.errors mine`.
4. Compare with `ref` and with `structured_error()` in [common/support_tools.py](../common/support_tools.py).

## Break it more (optional)

- Set `fake_db.FAILURES["process_refund"] = "permission"` in a scenario. Does the agent escalate?
- Change `isRetryable` to `true` for the business error. Does the agent now retry a refund that can never pass?

## Log

| Scenario | empty | generic | mine |
|---|---|---|---|
| transient | | | |
| business | | | |
| empty | | | |
