# Lab 6 - Extraction pipeline

**Exam:** D4 tasks 4.3, 4.4, 4.5, D5 task 5.5 (notes 5.3, 5.4, 5.5, 6.5). Scenario 6 (and 5).
**Time:** about 2 hours. **Cost:** cents. The batch run is 50% cheaper but can take up to 24 hours (most finish within an hour).

## Rules to remember

- Value may be missing => **nullable**. Required non-null => the model **invents** a value.
- Schema fixes **syntax**. Totals that don't add up are **semantic** errors => `validate()` + retry with the problem list.
- Retry helps for format / structure mistakes. Retry **can't** help when the info isn't in the document => send to a human.
- Batch API: 50% cheaper, up to 24 h, **no SLA**, no multi-turn tool loop inside one request, match results by `custom_id`, resubmit **only** the failed ones. Use it for work nobody is waiting for.
- 97% overall accuracy can hide one document type at 60%. Measure **per document type and per field**.

## The data

10 receipts in [data/receipts](../data/receipts), ground truth in `expected.json`. Traps on purpose:

| Receipt | Trap |
|---|---|
| r02 | Vietnamese, DD/MM date, VND with `.` as thousands separator |
| r03 | Email, not a receipt. PayPal = `other` |
| r04 | Smudged date, payment illegible => `null` / `unclear` |
| r05 | No date, no currency |
| r06 | JPY is not in the enum => `other` + detail |
| r07 | **Printed total is wrong** (39.00 + 3.12 = 42.12, receipt says 43.12) => retry can't fix it, human review |
| r09 | Markdown table, DD.MM.YYYY |

## Steps

1. **Predict:** how many values will `wrong` invent?
2. Run `python -m lab6_extract.extract wrong`. Count the `INVENTED` lines.
3. Fix `MY_SCHEMA` in [extract.py](extract.py). Run `python -m lab6_extract.extract mine`. Target: 0 invented.
4. Write `validate()` and the retry in `extract_with_retry()`. Run `python -m lab6_extract.extract validate`.
   Expected: r07 still fails after retry and goes to human review. Nothing else fails.
5. Run `python -m lab6_extract.extract batch`. Then write the TODO: resubmit only failed `custom_id`s.
6. Optional: add a `confidence` field per important field (`date`, `total`). Do low-confidence fields match the wrong answers? Self-reported confidence is not reliable until you check it against labeled data (that is what `expected.json` is).

## Log

| Mode | Accuracy | Invented | Notes |
|---|---|---|---|
| wrong | | | |
| mine | | | |
| validate | | | |
| batch | | | time taken: |
