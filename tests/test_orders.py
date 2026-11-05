from shop.db import run_query
from shop.orders import find_orders, total_for


def test_total_for_no_discount():
    assert total_for([("pen", 2.0), ("book", 8.0)]) == 10.0


def test_find_orders_returns_rows():
    """Check that find_orders returns the stored rows for a customer."""
    run_query("INSERT INTO orders VALUES (?, ?, ?)", (1, 7, 10.0))
    assert find_orders(7) == [(1, 10.0)]
