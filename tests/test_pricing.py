from shop.pricing import apply_discount, apply_tax, describe_discount


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0


def test_describe_discount():
    assert describe_discount(10) == "10% off"


def test_apply_tax():
    """Check that apply_tax adds the tax to a price."""
    assert apply_tax(100, 0.2) == 120.0
