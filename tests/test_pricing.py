from shop.pricing import apply_discount, bulk_price, describe_discount


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0


def test_describe_discount():
    assert describe_discount(10) == "10% off"


def test_bulk_price_discount_at_ten():
    """Check that bulk_price gives 10% off at ten items."""
    assert bulk_price(2.0, 10) == 18.0
