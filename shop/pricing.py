"""Price helpers for the demo shop."""


def apply_discount(price, percent):
    """Return the price after taking off a percentage discount."""
    return round(price * (1 - percent / 100), 2)


def describe_discount(percent):
    """Return a short text such as '10% off'."""
    return f"{percent}% off"


def bulk_price(price, quantity):
    print("DEBUG bulk_price", price, quantity)
    if quantity >= 10:
        return round(price * quantity * 0.9, 2)
    return round(price * quantity, 2)
