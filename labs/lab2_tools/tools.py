"""Lab 2 - Tool descriptions and tool_choice (guide 2.1, 2.3; notes 3.1, 3.3).

Run from the labs folder:
    python -m lab2_tools.tools vague    # near-identical descriptions
    python -m lab2_tools.tools mine     # your descriptions (fill MY_TOOLS first)
    python -m lab2_tools.tools ref      # reference descriptions from common/support_tools.py
    python -m lab2_tools.tools choice   # tool_choice: auto vs any vs forced
"""
import copy
import sys

import anthropic

from common.config import MAX_TOKENS, MODEL, get_client
from common.support_tools import TOOLS as REF_TOOLS


def _with_descriptions(descriptions: dict[str, str]) -> list[dict]:
    """Copy the reference tools (same names and schemas) with other descriptions."""
    tools = copy.deepcopy(REF_TOOLS)
    for tool in tools:
        tool["description"] = descriptions[tool["name"]]
        for prop in tool["input_schema"].get("properties", {}).values():
            prop.pop("description", None)  # field hints would leak the answer
    return tools


# WRONG: two pairs of similar tools with descriptions that don't say which one to pick
VAGUE_TOOLS = _with_descriptions({
    "get_customer": "Find a customer.",
    "search_customers": "Find customers.",
    "lookup_order": "Get order info.",
    "list_orders": "Get orders.",
    "process_refund": "Refund.",
    "escalate_to_human": "Escalate.",
})

# TODO: rewrite each description. Say what it does, what input it needs (with format),
# what it returns, and WHEN to use it instead of the similar tool.
MY_TOOLS = _with_descriptions({
    "get_customer": "Find a customer. Requires the customer's email or ID. Returns customer details. Use this when you have a specific customer in mind.",
    "search_customers": "Find customers. Requires search criteria like name or email. Returns a list of matching customers. Use this when you need to locate customers without a specific ID.",
    "lookup_order": "Get order info. Requires the order ID. Returns order details. Use this when you have a specific order to check.",
    "list_orders": "Get orders. Requires the customer ID. Returns a list of the customer's orders. Use this when you want to see all orders for a customer.",
    "process_refund": "Refund. Requires the order ID and refund amount. Returns confirmation of the refund. Use this when you need to issue a refund for a specific order.",
    "escalate_to_human": "Escalate. Requires context of the issue. Returns confirmation of escalation. Use this when the issue cannot be resolved with the available tools.",
})

# (user message, the tool a careful agent calls first)
CASES = [
    ("My email is minh.le@example.com. What tier is my account?", "get_customer"),
    ("Hi, I'm Alex Tran, can you find my account?", "search_customers"),
    ("Where is order O1006 right now?", "lookup_order"),
    ("Customer C004 wants to see everything they ever bought.", "list_orders"),
    ("Customer id C002 here. Is my account still active?", "get_customer"),
    ("Which items were in order O1004?", "lookup_order"),
    ("Show me the purchase history of customer C001.", "list_orders"),
    ("Look up a customer called Sara.", "search_customers"),
]

SYSTEM = "You are a support agent for an online shop. Use the tools to look things up."


def first_tool(client, tools: list[dict], prompt: str) -> str:
    """One call only: which tool does Claude pick first? Nothing is executed."""
    response = client.messages.create(model=MODEL, max_tokens=MAX_TOKENS, system=SYSTEM, tools=tools,
                                      messages=[{"role": "user", "content": prompt}])
    for block in response.content:
        if block.type == "tool_use":
            return block.name
    return "(no tool)"


def score(tools: list[dict]) -> None:
    client = get_client()
    hits = 0
    for prompt, expected in CASES:
        picked = first_tool(client, tools, prompt)
        ok = picked == expected
        hits += ok
        print(f"{'OK  ' if ok else 'MISS'} want {expected:<17} got {picked:<17} | {prompt}")
    print(f"\nScore: {hits}/{len(CASES)}")


def tool_choice_demo() -> None:
    """Same message, three tool_choice settings."""
    client = get_client()
    prompt = "Thanks, that's all. Bye!"
    settings = {
        "auto": {"type": "auto"},
        "any": {"type": "any"},
        "forced get_customer": {"type": "tool", "name": "get_customer"},
    }
    for label, choice in settings.items():
        try:
            response = client.messages.create(
                model=MODEL, max_tokens=MAX_TOKENS, system=SYSTEM, tools=REF_TOOLS,
                messages=[{"role": "user", "content": prompt}], tool_choice=choice,
                # Forced tool use does not work together with thinking, so turn thinking off here
                thinking={"type": "disabled"},
            )
        except anthropic.BadRequestError as err:
            print(f"[{label}] 400 from the API: {err.message}")
            print("    The newest Opus / Sonnet models reject forced tool_choice. The exam still tests the idea.")
            continue
        kinds = [b.name if b.type == "tool_use" else b.type for b in response.content]
        print(f"[{label}] stop_reason={response.stop_reason} blocks={kinds}")


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "vague"
    if mode == "choice":
        tool_choice_demo()
        return
    tools = {"vague": VAGUE_TOOLS, "mine": MY_TOOLS, "ref": REF_TOOLS}.get(mode)
    if tools is None:
        sys.exit("usage: python -m lab2_tools.tools [vague|mine|ref|choice]")
    print(f"== {mode} descriptions, model {MODEL} ==")
    score(tools)


if __name__ == "__main__":
    main()
