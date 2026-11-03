"""Fake support backend for the labs. Pure Python: no API calls, no real money.

Labs expose these functions to Claude as tools. Failures are raised as ToolError,
so each lab can choose how to report them back to the model (see lab 3).
"""
import json
from datetime import date

from .config import DATA_DIR

# Fixed "today" so the 30-day refund rule gives the same answer on every run.
TODAY = date(2026, 11, 3)
REFUND_WINDOW_DAYS = 30


def _load(name: str):
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))


CUSTOMERS: list[dict] = _load("customers.json")
ORDERS: list[dict] = _load("orders.json")

# What actually happened during a run, so labs can count what slipped through.
REFUND_LOG: list[dict] = []
ESCALATIONS: list[dict] = []

# Failure injection (lab 3). Example: FAILURES["lookup_order"] = "timeout"
#   "timeout"    - the first call fails (transient), a retry works
#   "permission" - every call fails: this agent role may not use the tool
FAILURES: dict[str, str] = {}
_failed_once: set[str] = set()


class ToolError(Exception):
    """A tool failure that carries what a structured error needs."""

    def __init__(self, category: str, message: str, retryable: bool, **details):
        super().__init__(message)
        self.category = category  # transient | validation | business | permission
        self.message = message
        self.retryable = retryable
        self.details = details  # optional: suggestion, customer_message


def reset() -> None:
    """Start a run from clean data: reload orders, clear logs and injected failures."""
    ORDERS[:] = _load("orders.json")
    REFUND_LOG.clear()
    ESCALATIONS.clear()
    FAILURES.clear()
    _failed_once.clear()


def _maybe_fail(tool_name: str) -> None:
    mode = FAILURES.get(tool_name)
    if mode == "timeout" and tool_name not in _failed_once:
        _failed_once.add(tool_name)
        raise ToolError("transient", f"{tool_name}: backend timed out after 5s", retryable=True,
                        suggestion="Retry the same call once.")
    if mode == "permission":
        raise ToolError("permission", f"{tool_name}: this agent role is not allowed to use this tool",
                        retryable=False, suggestion="Escalate to a human agent.")


def _find_order(order_id: str) -> dict:
    for order in ORDERS:
        if order["order_id"] == order_id.strip().upper():
            return order
    raise ToolError("validation", f"No order with id {order_id}", retryable=False,
                    suggestion="Ask the customer to check the order number, or use list_orders.")


def get_customer(email: str | None = None, customer_id: str | None = None) -> dict:
    _maybe_fail("get_customer")
    if not email and not customer_id:
        raise ToolError("validation", "Give an email or a customer_id", retryable=False)
    for customer in CUSTOMERS:
        if email and customer["email"].lower() == email.strip().lower():
            return customer
        if customer_id and customer["customer_id"] == customer_id.strip().upper():
            return customer
    raise ToolError("validation", "No customer matches that email or id", retryable=False,
                    suggestion="Ask the customer to check the email address.")


def search_customers(name: str) -> list[dict]:
    """Partial name match. An empty list is a valid answer, not an error."""
    _maybe_fail("search_customers")
    needle = name.strip().lower()
    return [
        {"customer_id": c["customer_id"], "name": c["name"], "email": c["email"]}
        for c in CUSTOMERS
        if needle in c["name"].lower()
    ]


def lookup_order(order_id: str) -> dict:
    _maybe_fail("lookup_order")
    return _find_order(order_id)


def list_orders(customer_id: str) -> list[dict]:
    """Short rows for one customer. An empty list means the customer has no orders."""
    _maybe_fail("list_orders")
    return [
        {"order_id": o["order_id"], "ordered_on": o["ordered_on"], "total": o["total"], "status": o["status"]}
        for o in ORDERS
        if o["customer_id"] == customer_id.strip().upper()
    ]


def process_refund(order_id: str, amount: float, reason: str) -> dict:
    # No refund limit check here on purpose: lab 4 shows where that rule belongs.
    _maybe_fail("process_refund")
    order = _find_order(order_id)
    if order["status"] != "delivered":
        raise ToolError("business", f"Order {order['order_id']} is not delivered yet (status: {order['status']})",
                        retryable=False,
                        customer_message="We can refund an order after it is delivered.")
    days = (TODAY - date.fromisoformat(order["delivered_on"])).days
    if days > REFUND_WINDOW_DAYS:
        raise ToolError("business", f"Refund window passed: delivered {days} days ago, limit {REFUND_WINDOW_DAYS}",
                        retryable=False,
                        customer_message=f"Refunds are possible within {REFUND_WINDOW_DAYS} days of delivery. "
                                         f"This order was delivered {days} days ago.",
                        suggestion="Do not retry. Explain the policy, offer escalation if the customer disagrees.")
    left = round(order["total"] - order["refunded_amount"], 2)
    if amount <= 0 or amount > left:
        raise ToolError("validation", f"Amount must be more than 0 and at most {left} (already refunded: "
                                      f"{order['refunded_amount']})", retryable=False)
    order["refunded_amount"] = round(order["refunded_amount"] + amount, 2)
    entry = {"refund_id": f"R{len(REFUND_LOG) + 1:03d}", "order_id": order["order_id"],
             "amount": amount, "reason": reason}
    REFUND_LOG.append(entry)
    return {**entry, "status": "refunded"}


def escalate_to_human(customer_id: str, reason: str, summary: str) -> dict:
    _maybe_fail("escalate_to_human")
    ticket = {"ticket_id": f"H{len(ESCALATIONS) + 1:03d}", "customer_id": customer_id,
              "reason": reason, "summary": summary}
    ESCALATIONS.append(ticket)
    return {"ticket_id": ticket["ticket_id"], "status": "queued for a human agent"}
