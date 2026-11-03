"""Lab 6 - Extraction pipeline: schema, validation + retry, batch (guide 4.3-4.5, 5.5; notes 5.3-5.5, 6.5).

Run from the labs folder:
    python -m lab6_extract.extract wrong      # strict non-null schema - watch it invent values
    python -m lab6_extract.extract mine       # your nullable schema (fill MY_SCHEMA first)
    python -m lab6_extract.extract validate   # your schema + validate() + retry with feedback
    python -m lab6_extract.extract batch      # same requests through the Message Batches API
"""
import copy
import json
import sys
import time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

from common.config import DATA_DIR, MAX_TOKENS, MODEL, get_client

RECEIPTS_DIR = DATA_DIR / "receipts"
EXPECTED = {k: v for k, v in json.loads((RECEIPTS_DIR / "expected.json").read_text(encoding="utf-8")).items()
            if not k.startswith("_")}
COMPARED_FIELDS = ["date", "currency", "total", "tax_id", "payment_method"]

PROMPT = "Extract this receipt by calling record_receipt. Dates as YYYY-MM-DD.\n\n<receipt>\n{text}\n</receipt>"

# WRONG: every field is a required non-null value, so the model must fill it even when the
# receipt doesn't say it (no date, no tax id, no currency) - it will invent something.
WRONG_SCHEMA = {
    "type": "object",
    "properties": {
        "vendor": {"type": "string"},
        "date": {"type": "string", "description": "YYYY-MM-DD"},
        "currency": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"name": {"type": "string"}, "qty": {"type": "number"},
                               "unit_price": {"type": "number"}},
                "required": ["name", "qty", "unit_price"],
            },
        },
        "subtotal": {"type": "number"},
        "tax": {"type": "number"},
        "total": {"type": "number"},
        "tax_id": {"type": "string"},
        "payment_method": {"type": "string"},
    },
    "required": ["vendor", "date", "currency", "items", "subtotal", "tax", "total", "tax_id", "payment_method"],
}

# TODO: fix the schema.
#   - nullable where a receipt may not print the value: {"type": ["string", "null"]}
#   - currency: enum ["USD", "EUR", "VND", "other", null] + currency_detail (nullable) for "other"
#   - payment_method: enum ["card", "cash", "bank_transfer", "other", "unclear"]
#   - field descriptions that say "null if the receipt does not show it"
MY_SCHEMA = copy.deepcopy(WRONG_SCHEMA)


def record_tool(schema: dict) -> dict:
    return {"name": "record_receipt", "description": "Record the fields of one receipt.", "input_schema": schema}


def request_params(text: str, schema: dict, extra_messages: list | None = None) -> dict:
    messages = [{"role": "user", "content": PROMPT.format(text=text)}] + (extra_messages or [])
    # Forced tool_choice guarantees a record_receipt call. It doesn't work with thinking, so thinking is off.
    return {"model": MODEL, "max_tokens": MAX_TOKENS, "tools": [record_tool(schema)], "messages": messages,
            "tool_choice": {"type": "tool", "name": "record_receipt"}, "thinking": {"type": "disabled"}}


def tool_input(message) -> dict | None:
    return next((b.input for b in message.content if b.type == "tool_use"), None)


def extract_one(client, text: str, schema: dict) -> dict | None:
    return tool_input(client.messages.create(**request_params(text, schema)))


def validate(data: dict) -> list[str]:
    """Semantic checks a schema can't do. Returns a list of problems (empty = OK)."""
    problems = []
    # TODO: add checks, for example:
    #   - sum of qty * unit_price matches subtotal (or total - tax when subtotal is null), within 0.01
    #   - subtotal + tax (null tax = 0) matches total, within 0.01
    #   - date is null or matches YYYY-MM-DD
    #   - currency "other" => currency_detail is not null
    return problems


def extract_with_retry(client, text: str, schema: dict, max_retries: int = 1) -> tuple[dict | None, list[str]]:
    """Extract, validate, and on failure send the problems back once. Returns (data, problems left)."""
    data = extract_one(client, text, schema)
    problems = validate(data) if data else ["no tool call"]
    # TODO: while problems and retries left:
    #   send the same request again plus two extra messages: the assistant turn with the
    #   tool_use, and a user turn with a tool_result (is_error true) that lists the problems
    #   and says "fix only if the receipt supports it; otherwise keep what is printed".
    #   Use request_params(text, schema, extra_messages=[...]).
    return data, problems


def compare(results: dict[str, dict | None]) -> None:
    """Score against expected.json and count invented values (expected null, got a value)."""
    correct = total = invented = 0
    for rid, expected in EXPECTED.items():
        got = results.get(rid) or {}
        for field in COMPARED_FIELDS:
            total += 1
            want, have = expected.get(field), got.get(field)
            if isinstance(want, (int, float)) and isinstance(have, (int, float)):
                ok = abs(want - have) < 0.01
            else:
                ok = str(want).lower() == str(have).lower()
            correct += ok
            if want is None and have not in (None, ""):
                invented += 1
                print(f"  INVENTED {rid}.{field} = {have!r}")
            elif not ok:
                print(f"  wrong    {rid}.{field}: want {want!r}, got {have!r}")
    print(f"\nField accuracy: {correct}/{total}. Invented values: {invented}.")


def receipts() -> dict[str, str]:
    return {p.stem: p.read_text(encoding="utf-8") for p in sorted(RECEIPTS_DIR.glob("r*.txt"))}


def run_sync(schema: dict, use_retry: bool) -> None:
    client = get_client()
    results = {}
    for rid, text in receipts().items():
        if use_retry:
            data, problems = extract_with_retry(client, text, schema)
            if problems:
                print(f"  {rid}: still failing after retry => send to human review: {problems}")
        else:
            data = extract_one(client, text, schema)
        results[rid] = data
        print(f"{rid}: {json.dumps(data)[:160]}")
    compare(results)


def run_batch(schema: dict) -> None:
    """Message Batches API: 50% cheaper, up to 24 h, no latency promise. Fine here: nobody waits."""
    client = get_client()
    texts = receipts()
    batch = client.messages.batches.create(requests=[
        Request(custom_id=rid, params=MessageCreateParamsNonStreaming(**request_params(text, schema)))
        for rid, text in texts.items()
    ])
    print(f"batch {batch.id} created, polling every 30 s (most batches finish within an hour)")
    while (batch := client.messages.batches.retrieve(batch.id)).processing_status != "ended":
        print(f"  {batch.processing_status}: {batch.request_counts.processing} still processing")
        time.sleep(30)
    results, failed = {}, []
    # Results come back in any order: always key them by custom_id, never by position
    for item in client.messages.batches.results(batch.id):
        if item.result.type == "succeeded":
            results[item.custom_id] = tool_input(item.result.message)
        else:
            failed.append(item.custom_id)
    print(f"succeeded: {len(results)}, failed: {failed}")
    # TODO: resubmit ONLY the failed custom_ids (a new, smaller batch), not the whole set
    compare(results)


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        if mode == "wrong":
            run_sync(WRONG_SCHEMA, use_retry=False)
        elif mode == "mine":
            run_sync(MY_SCHEMA, use_retry=False)
        elif mode == "validate":
            run_sync(MY_SCHEMA, use_retry=True)
        elif mode == "batch":
            run_batch(MY_SCHEMA)
        else:
            sys.exit("usage: python -m lab6_extract.extract [wrong|mine|validate|batch]")
    except anthropic.BadRequestError as err:
        sys.exit(f"400 from the API: {err.message}\n"
                 "If it is about tool_choice: this model rejects forced tool_choice. Remove tool_choice "
                 "and thinking from request_params() and rely on the prompt.")


if __name__ == "__main__":
    main()
