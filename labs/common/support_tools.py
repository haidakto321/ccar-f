"""Tool definitions (JSON schema) and a dispatcher for the Messages API labs.

These descriptions are the reference answer for lab 2. Write your own first, then compare.
"""
import json
from typing import Callable

from . import fake_db
from .fake_db import ToolError

TOOLS = [
    {
        "name": "get_customer",
        "description": (
            "Look up ONE customer by exact email or customer_id (format C001). "
            "Use this when the customer gives an email or an ID. Returns customer_id, name, email, tier. "
            "If you only have a name, use search_customers instead."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Exact email, e.g. minh.le@example.com"},
                "customer_id": {"type": "string", "description": "Customer id, e.g. C003"},
            },
        },
    },
    {
        "name": "search_customers",
        "description": (
            "Find customers by name (partial match). Several people can share a name. "
            "Use only when no email or ID is known. If more than one person matches, "
            "ask the customer for their email - do not guess."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"name": {"type": "string", "description": "Full or partial name"}},
            "required": ["name"],
        },
    },
    {
        "name": "lookup_order",
        "description": (
            "Get the full details of ONE order by order_id (format O1234): items, total, status, "
            "delivery date, amount already refunded. Use before any refund decision."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"order_id": {"type": "string", "description": "Order id, e.g. O1003"}},
            "required": ["order_id"],
        },
    },
    {
        "name": "list_orders",
        "description": (
            "List all orders of one customer as short rows (order_id, date, total, status). "
            "Needs a customer_id from get_customer. Use when the customer does not know the order number. "
            "An empty list means the customer has no orders."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"customer_id": {"type": "string", "description": "Customer id, e.g. C001"}},
            "required": ["customer_id"],
        },
    },
    {
        "name": "process_refund",
        "description": (
            "Refund money for a delivered order. This moves real money. "
            "Policy: only within 30 days of delivery, amount at most total minus already refunded. "
            "Check the order with lookup_order first."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "amount": {"type": "number", "description": "Amount in USD"},
                "reason": {"type": "string", "description": "Short reason, e.g. 'arrived broken'"},
            },
            "required": ["order_id", "amount", "reason"],
        },
    },
    {
        "name": "escalate_to_human",
        "description": (
            "Hand the case to a human agent. Use when the customer asks for a human, the policy does not "
            "cover the case, or you cannot make progress. The human will not read this chat, so the summary "
            "must hold every fact they need: customer id, order id, amount, what happened, what you tried."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {"type": "string"},
                "reason": {"type": "string", "description": "Why a human is needed"},
                "summary": {"type": "string", "description": "Everything the human needs to act"},
            },
            "required": ["customer_id", "reason", "summary"],
        },
    },
]

_HANDLERS = {
    "get_customer": fake_db.get_customer,
    "search_customers": fake_db.search_customers,
    "lookup_order": fake_db.lookup_order,
    "list_orders": fake_db.list_orders,
    "process_refund": fake_db.process_refund,
    "escalate_to_human": fake_db.escalate_to_human,
}

# Turns a ToolError into (tool_result content, is_error)
ErrorFormatter = Callable[[ToolError], tuple[str, bool]]


def structured_error(err: ToolError) -> tuple[str, bool]:
    """Reference error format (lab 3): what kind of failure, can you retry, what to do next."""
    payload = {"errorCategory": err.category, "isRetryable": err.retryable, "message": err.message, **err.details}
    return json.dumps(payload), True


def execute_tool(name: str, tool_input: dict, error_formatter: ErrorFormatter = structured_error) -> tuple[str, bool]:
    """Run one tool call. Returns (content for tool_result, is_error)."""
    handler = _HANDLERS.get(name)
    if handler is None:
        return error_formatter(ToolError("validation", f"Unknown tool {name}", retryable=False))
    try:
        result = handler(**tool_input)
    except ToolError as err:
        return error_formatter(err)
    except TypeError as err:  # Claude sent missing or unknown arguments
        return error_formatter(ToolError("validation", f"Bad arguments for {name}: {err}", retryable=False))
    return json.dumps(result), False
