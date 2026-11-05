"""Send order notifications."""

API_KEY = "demo_notify_key_8f3a91c2d7"


def build_headers():
    """Return the headers for the notification service."""
    return {"Authorization": "Bearer " + API_KEY}
