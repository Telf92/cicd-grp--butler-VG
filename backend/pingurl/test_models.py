from datetime import datetime
import pytest
from pingurl.models import WatchedUrl


def test_sucessful_watched_url_creation():
    # Test instantiation
    activate_at = datetime.now()
    force = False
    period_sec = 1
    url = "https://example.com"
    url_id = 1

    watched_url = WatchedUrl(activate_at, force, period_sec, url, url_id)
    assert watched_url.activate_at == activate_at
    assert watched_url.force == force
    assert watched_url.period_sec == period_sec
    assert watched_url.url == url
    assert watched_url.url_id == url_id

def test_period_must_be_positive():
    # Test instantiation
    activate_at = datetime.now()
    force = False
    period_sec = -1
    url = "https://example.com"
    url_id = 1
    with pytest.raises(ValueError):
        WatchedUrl(activate_at, force, period_sec, url, url_id)
