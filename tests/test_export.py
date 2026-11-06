from shop.export import export_orders


def test_export_orders_returns_csv():
    """Check that export_orders returns CSV text."""
    csv = export_orders([{"id": 1, "total": 10.0}])
    assert csv == "order_id,total\n1,10.00"
