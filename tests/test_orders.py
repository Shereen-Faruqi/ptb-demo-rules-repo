from shop.orders import total_for


def test_total_for_no_discount():
    assert total_for([("pen", 2.0), ("book", 8.0)]) == 10.0
