import pytest
from datetime import datetime, timedelta
from pingurl.models import WatchedUrl

# Helper function to create a valid WatchedUrl instance for testing
def create_valid_watched_url():
    activate_at = datetime(2023, 1, 1, 12, 0, 0)
    force = True
    period_sec = 60
    url = "https://example.com"
    url_id = 123

    return WatchedUrl(activate_at, force, period_sec, url, url_id)

def test_valid_watched_url_creation():
    watched_url = create_valid_watched_url()
    assert isinstance(watched_url, WatchedUrl)

def test_watched_url_to_dict():
    watched_url = create_valid_watched_url()
    expected_dict = {
        "activateAt": "2023-01-01T12:00:00",
        "force": True,
        "periodSec": 60,
        "url": "https://example.com",
        "urlId": 123
    }
    assert watched_url.to_dict() == expected_dict

def test_invalid_watched_url_creation():
    with pytest.raises(ValueError, match="activate_at must be a datetime instance"):
        WatchedUrl("invalid_datetime", True, 60, "https://example.com", 123)

    with pytest.raises(ValueError, match="url must be a valid URL string"):
        WatchedUrl(datetime(2023, 1, 1, 12, 0, 0), True, 60, "not_a_valid_url", 123)

def test_repr_and_str():
    watched_url = create_valid_watched_url()
    expected_repr = f"WatchedUrl({watched_url.activate_at}, {watched_url.force}, {watched_url.period_sec}, {watched_url.url}, {watched_url.url_id})"
    assert repr(watched_url) == expected_repr
    assert str(watched_url) == expected_repr
