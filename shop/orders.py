"""Order helpers for the demo shop."""

from shop.db import run_query
from shop.pricing import apply_discount
from shop.queries import build_orders_query


def total_for(items, discount_percent=0):
    """Return the order total for a list of (name, price) pairs."""
    subtotal = sum(price for _name, price in items)
    return apply_discount(subtotal, discount_percent)


def find_orders(customer_id):
    """Return the stored orders for one customer."""
    return run_query(build_orders_query(customer_id))
