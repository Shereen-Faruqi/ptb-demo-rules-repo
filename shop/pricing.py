"""Price helpers for the demo shop."""


def apply_discount(price, percent):
    """Return the price after taking off a percentage discount."""
    return round(price * (1 - percent / 100), 2)


def describe_discount(percent):
    """Return a short text such as '10% off'."""
    return f"{percent}% off"


def apply_tax(price, rate):
    """Return the price with tax added; rate is a fraction such as 0.2."""
    return round(price * (1 + rate), 2)
