from shop.pricing import apply_discount, describe_discount


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0


def test_describe_discount():
    assert describe_discount(10) == "10% off"
