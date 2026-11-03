"""Lab 5 - Handoff summary: free text vs tool_use + JSON schema (guide 4.3, 5.1, 5.2; notes 5.3, 6.1, 6.2).

Run from the labs folder:
    python -m lab5_handoff.handoff free-text   # "write a summary" - check which facts get lost
    python -m lab5_handoff.handoff schema      # your submit_handoff schema (fill the TODO first)
"""
import json
import sys

import anthropic

from common.config import DATA_DIR, MAX_TOKENS, MODEL, get_client

TRANSCRIPT = (DATA_DIR / "transcripts" / "case_long.txt").read_text(encoding="utf-8")

# Facts the human agent needs. Each is (label, any of these strings must appear).
REQUIRED_FACTS = [
    ("customer id", ["C003"]),
    ("order id", ["O1003"]),
    ("amount", ["820"]),
    ("root cause", ["crack", "shipping damage", "damaged in shipping"]),
    ("photos received", ["photo"]),
    ("replacement out of stock", ["out of stock", "no stock"]),
    ("customer wants full refund", ["full refund", "refund of $820", "refund $820", "money back"]),
    ("refund to original card", ["card"]),
    ("free return label", ["return label", "return shipping", "free return"]),
]
# A fact from the chat that does NOT belong in the handoff (old order, no problem)
NOISE = "O0999"

INSTRUCTION = (
    "You are an AI support agent. The chat below is being handed to a human agent. "
    "The human will NOT read the chat."
)

# TODO: finish the schema. Add the fields a human needs to act without the chat, for example:
#   amount_usd (number), root_cause, category (enum incl. "other") + category_detail (nullable),
#   what_was_tried, customer_wants, recommended_action.
# strict: true means every property must be listed in "required". Make a field optional by
# allowing null, e.g. {"type": ["string", "null"]}. additionalProperties must be false.
HANDOFF_TOOL = {
    "name": "submit_handoff",
    "description": "Submit the case for the human agent. They will not read the chat, so put every fact they need here.",
    "strict": True,
    "input_schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "customer_id": {"type": "string"},
            "order_id": {"type": ["string", "null"]},
        },
        "required": ["customer_id", "order_id"],
    },
}


def check(text: str) -> None:
    """Print which required facts made it into the handoff."""
    lower = text.lower()
    found = 0
    for label, options in REQUIRED_FACTS:
        ok = any(opt.lower() in lower for opt in options)
        found += ok
        print(f"  {'OK  ' if ok else 'LOST'} {label}")
    print(f"  facts kept: {found}/{len(REQUIRED_FACTS)}")
    if NOISE.lower() in lower:
        print(f"  NOISE: the old order {NOISE} leaked into the handoff")


def free_text(client) -> None:
    response = client.messages.create(
        model=MODEL, max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": f"{INSTRUCTION}\nWrite a short handoff summary.\n\n{TRANSCRIPT}"}],
    )
    text = "\n".join(b.text for b in response.content if b.type == "text")
    print(text)
    check(text)


def with_schema(client) -> None:
    messages = [{"role": "user", "content": f"{INSTRUCTION}\nCall submit_handoff.\n\n{TRANSCRIPT}"}]
    try:
        # Forced tool_choice guarantees a submit_handoff call. It doesn't work with thinking, so thinking is off.
        response = client.messages.create(
            model=MODEL, max_tokens=MAX_TOKENS, tools=[HANDOFF_TOOL], messages=messages,
            tool_choice={"type": "tool", "name": "submit_handoff"}, thinking={"type": "disabled"},
        )
    except anthropic.BadRequestError as err:
        # Newest Opus / Sonnet reject forced tool_choice: fall back to auto + the instruction above
        print(f"  forced tool_choice rejected ({err.message}), retrying with auto")
        response = client.messages.create(model=MODEL, max_tokens=MAX_TOKENS, tools=[HANDOFF_TOOL],
                                          messages=messages)
    calls = [b for b in response.content if b.type == "tool_use"]
    if not calls:
        print("  no submit_handoff call came back")
        return
    handoff = calls[0].input
    print(json.dumps(handoff, indent=2))
    check(json.dumps(handoff))


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    modes = {"free-text": free_text, "schema": with_schema}
    if mode not in modes:
        sys.exit("usage: python -m lab5_handoff.handoff [free-text|schema]")
    modes[mode](get_client())


if __name__ == "__main__":
    main()
