"""SQL text for the demo shop."""


def build_orders_query(customer_id):
    """Return the SQL text that lists one customer's orders."""
    return "SELECT id, total FROM orders WHERE customer_id = " + str(customer_id)
