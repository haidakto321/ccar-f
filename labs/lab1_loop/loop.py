"""Lab 1 - Agentic loop driven by stop_reason (guide task 1.1, notes 2.1).

Run from the labs folder:
    python -m lab1_loop.loop wrong-text    # stops as soon as Claude writes any text
    python -m lab1_loop.loop wrong-turns   # stops after a fixed number of calls
    python -m lab1_loop.loop right         # your loop (fill the TODOs first)
"""
import json
import sys

from common.config import MAX_TOKENS, MODEL, get_client
from common.support_tools import TOOLS, execute_tool

SYSTEM = "You are a support agent for an online shop. Use the tools to look things up. Never guess order data."
PROMPT = (
    "Hi, I'm alex.tran@example.com. My headphones arrived broken. "
    "Which order was it, what did I pay, and can I still get a refund?"
)


def call_claude(client, messages):
    return client.messages.create(model=MODEL, max_tokens=MAX_TOKENS, system=SYSTEM, tools=TOOLS, messages=messages)


def run_tools(response) -> list[dict]:
    """Run every tool_use block in a response. Returns tool_result blocks for ONE user message."""
    results = []
    for block in response.content:
        if block.type != "tool_use":
            continue
        content, is_error = execute_tool(block.name, block.input)
        print(f"  -> {block.name}({json.dumps(block.input)}) {'ERROR' if is_error else 'ok'}")
        result = {"type": "tool_result", "tool_use_id": block.id, "content": content}
        if is_error:
            result["is_error"] = True
        results.append(result)
    return results


def text_of(response) -> str:
    return "\n".join(block.text for block in response.content if block.type == "text")


# --- WRONG 1: stop as soon as Claude writes text -----------------------------
def wrong_stop_on_text(client) -> str:
    messages = [{"role": "user", "content": PROMPT}]
    while True:
        response = call_claude(client, messages)
        print(f"  [stop_reason={response.stop_reason}]")
        messages.append({"role": "assistant", "content": response.content})
        if text_of(response):  # BUG: "Let me check that for you" is text too
            return text_of(response)
        messages.append({"role": "user", "content": run_tools(response)})


# --- WRONG 2: fixed number of turns ------------------------------------------
def wrong_fixed_turns(client, turns: int = 2) -> str:
    messages = [{"role": "user", "content": PROMPT}]
    response = None
    for _ in range(turns):  # BUG: the counter decides when to stop, not Claude
        response = call_claude(client, messages)
        print(f"  [stop_reason={response.stop_reason}]")
        messages.append({"role": "assistant", "content": response.content})
        results = run_tools(response)
        if not results:
            break
        messages.append({"role": "user", "content": results})
    return text_of(response)  # may be mid-task when the counter runs out


# --- RIGHT: your loop ---------------------------------------------------------
def right_loop(client) -> str:
    messages = [{"role": "user", "content": PROMPT}]
    while True:
        response = call_claude(client, messages)
        print(f"  [stop_reason={response.stop_reason}]")
        # TODO 1: append the assistant turn - the whole response.content, not only the text
        # TODO 2: stop_reason == "tool_use" -> run_tools(response), append ONE user message with all results, loop
        # TODO 3: stop_reason == "end_turn" -> return text_of(response)
        # TODO 4: anything else (max_tokens, refusal) -> print the reason and return what you have
        raise NotImplementedError("Lab 1: fill TODO 1-4 in right_loop()")


MODES = {"wrong-text": wrong_stop_on_text, "wrong-turns": wrong_fixed_turns, "right": right_loop}


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "right"
    if mode not in MODES:
        sys.exit(f"usage: python -m lab1_loop.loop [{'|'.join(MODES)}]")
    print(f"== {mode} ==\nUSER: {PROMPT}\n")
    answer = MODES[mode](get_client())
    print(f"\nFINAL ANSWER:\n{answer or '(empty)'}")


if __name__ == "__main__":
    main()
