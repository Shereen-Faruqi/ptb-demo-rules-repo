"""Order helpers for the demo shop."""

from shop.pricing import apply_discount


def total_for(items, discount_percent=0):
    """Return the order total for a list of (name, price) pairs."""
    subtotal = sum(price for _name, price in items)
    print("debug subtotal", subtotal)
    return apply_discount(subtotal, discount_percent)
