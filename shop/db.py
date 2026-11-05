"""A tiny in-memory database for the demo shop."""

import sqlite3

_conn = sqlite3.connect(":memory:")
_conn.execute("CREATE TABLE orders (id INTEGER, customer_id INTEGER, total REAL)")


def run_query(sql, params=()):
    """Run one SQL statement and return all rows."""
    rows = _conn.execute(sql, params).fetchall()
    _conn.commit()
    return rows
