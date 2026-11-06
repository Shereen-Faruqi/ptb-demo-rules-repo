from shop.notify import build_headers


def test_build_headers_has_authorization():
    """Check that build_headers includes an Authorization header."""
    assert "Authorization" in build_headers()
