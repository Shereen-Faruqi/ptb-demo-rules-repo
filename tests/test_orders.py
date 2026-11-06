from shop.orders import total_for


def test_total_for_no_discount():
    assert total_for([("pen", 2.0), ("book", 8.0)]) == 10.0


def test_total_for_with_discount():
    """Check that total_for applies a percentage discount."""
    assert total_for([("pen", 2.0), ("book", 8.0)], 50) == 5.0
