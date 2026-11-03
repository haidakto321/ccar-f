"""Reference agentic loop for the Messages API labs.

This is the answer to lab 1. Write your own loop there first, then compare.
"""
import json

from .config import MAX_TOKENS, MODEL
from .support_tools import ErrorFormatter, execute_tool, structured_error


def text_of(response) -> str:
    return "\n".join(block.text for block in response.content if block.type == "text")


def run_loop(client, user_msg: str, tools: list[dict], system: str | None = None,
             error_formatter: ErrorFormatter = structured_error, max_turns: int = 15, verbose: bool = True):
    """Call Claude until it stops asking for tools.

    Returns (final_text, messages, tool_calls) where tool_calls is a list of
    {"name", "input", "is_error"} dicts, handy for checking what the agent did.
    """
    messages = [{"role": "user", "content": user_msg}]
    tool_calls = []
    # max_turns is only a safety net. The real stop signal is stop_reason.
    for _ in range(max_turns):
        kwargs = {"model": MODEL, "max_tokens": MAX_TOKENS, "tools": tools, "messages": messages}
        if system:
            kwargs["system"] = system
        response = client.messages.create(**kwargs)
        # Append the whole content (thinking + text + tool_use), not only the text
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "tool_use":
            results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue
                content, is_error = execute_tool(block.name, block.input, error_formatter)
                tool_calls.append({"name": block.name, "input": block.input, "is_error": is_error})
                if verbose:
                    print(f"  -> {block.name}({json.dumps(block.input)})")
                    print(f"  <- {'ERROR ' if is_error else ''}{content[:300]}")
                result = {"type": "tool_result", "tool_use_id": block.id, "content": content}
                if is_error:
                    result["is_error"] = True
                results.append(result)
            # All results of one turn go back in ONE user message
            messages.append({"role": "user", "content": results})
            continue

        # end_turn = done. max_tokens / refusal = stopped early, also no tool calls left to run.
        if response.stop_reason != "end_turn" and verbose:
            print(f"  [loop] stopped early: stop_reason={response.stop_reason}")
        return text_of(response), messages, tool_calls

    print(f"  [loop] hit the max_turns={max_turns} safety cap")
    return "", messages, tool_calls
