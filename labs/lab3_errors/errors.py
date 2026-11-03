"""Lab 3 - Structured tool errors (guide 2.2, 5.3; notes 3.2, 6.3).

Run from the labs folder:
    python -m lab3_errors.errors empty   [scenario]   # failure looks like "no data"
    python -m lab3_errors.errors generic [scenario]   # just "Error"
    python -m lab3_errors.errors mine    [scenario]   # your structured error (fill the TODO first)
    python -m lab3_errors.errors ref     [scenario]   # reference from common/support_tools.py
Scenarios: transient, business, empty, all (default).
"""
import sys

from common import fake_db
from common.agent_loop import run_loop
from common.config import get_client
from common.fake_db import ToolError
from common.support_tools import TOOLS, structured_error

SYSTEM = (
    "You are a support agent for an online shop. Use the tools. "
    "Be honest about anything you could not check."
)

# name: (failures to inject, customer message, what a good agent does)
SCENARIOS = {
    "transient": (
        {"lookup_order": "timeout"},
        "What's the status of order O1001?",
        "retries lookup_order once, then answers: delivered 2026-10-20",
    ),
    "business": (
        {},
        "I'm alex.tran@example.com. Please refund my keyboard, order O1002, full amount.",
        "does NOT retry the refund, explains the 30-day policy, may offer a human",
    ),
    "empty": (
        {"list_orders": "timeout"},
        "I'm hoa.pham@example.com. Do I have any orders with you?",
        "sees the failure, retries, finds O1006 (shipped). Never says 'you have no orders'",
    ),
}


def empty_error(err: ToolError) -> tuple[str, bool]:
    return "[]", False  # WRONG: a failure that looks like a successful empty result


def generic_error(err: ToolError) -> tuple[str, bool]:
    return "Error: operation failed", True  # WRONG: no way to tell retry from stop


def my_structured_error(err: ToolError) -> tuple[str, bool]:
    # TODO: return (json_text, True). Include at least: the category (err.category),
    # whether a retry can help (err.retryable), what happened (err.message), and what to
    # do next or tell the customer (err.details may hold suggestion / customer_message).
    raise NotImplementedError("Lab 3: write my_structured_error()")


STYLES = {"empty": empty_error, "generic": generic_error, "mine": my_structured_error, "ref": structured_error}


def run_scenario(client, name: str, formatter) -> None:
    failures, prompt, good = SCENARIOS[name]
    fake_db.reset()
    fake_db.FAILURES.update(failures)
    print(f"\n=== {name} === injected: {failures or 'none'}")
    print(f"USER: {prompt}")
    answer, _, calls = run_loop(client, prompt, TOOLS, system=SYSTEM, error_formatter=formatter)
    print(f"AGENT: {answer}")
    print(f"tool calls: {[c['name'] for c in calls]} | refunds done: {len(fake_db.REFUND_LOG)}")
    print(f"good behavior would be: {good}")


def main() -> None:
    style = sys.argv[1] if len(sys.argv) > 1 else ""
    which = sys.argv[2] if len(sys.argv) > 2 else "all"
    if style not in STYLES or (which != "all" and which not in SCENARIOS):
        sys.exit("usage: python -m lab3_errors.errors [empty|generic|mine|ref] [transient|business|empty|all]")
    client = get_client()
    for name in SCENARIOS if which == "all" else [which]:
        run_scenario(client, name, STYLES[style])


if __name__ == "__main__":
    main()
