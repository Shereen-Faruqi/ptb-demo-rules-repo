"""Export orders for the demo shop."""


def export_orders(orders):
    """Return the orders as CSV text and report how many were exported."""
    lines = ["order_id,total"]
    for order in orders:
        lines.append(f"{order['id']},{order['total']:.2f}")
    print(f"Exported {len(orders)} orders")
    return "\n".join(lines)
