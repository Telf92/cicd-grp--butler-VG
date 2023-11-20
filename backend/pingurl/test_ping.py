from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta, timezone
from pingurl.models import WatchedUrl
from pingurl.ping import send_ping
import requests


@patch("pingurl.ping.requests.get")
def test_send_ping(mock_get):
    # Set up the mock response
    mock_response = MagicMock()
    mock_response.elapsed = timedelta(seconds=1)
    mock_response.status_code = 200
    mock_response.headers = {"Date": "Wed, 21 Oct 2023 07:28:00 GMT"}
    mock_get.return_value = mock_response

    # Define test data
    activate_at = datetime.now()
    force = True
    period_sec = 60
    url = "http://example.com"
    url_id = 1
    watched_url = WatchedUrl(activate_at, force, period_sec, url, url_id)

    # Call the function under test
    ping_data = send_ping(watched_url)

    # Asserts
    assert ping_data.url_id == url_id
    assert ping_data.status_code == 200
    assert isinstance(ping_data.response_time_sec, timedelta)
    expected_pinged_at = datetime(2023, 10, 21, 7, 28, tzinfo=timezone.utc)
    assert ping_data.pinged_at == expected_pinged_at

    # Test for exceptions
    mock_get.side_effect = requests.exceptions.Timeout()
    ping_data_timeout = send_ping(watched_url)
    assert ping_data_timeout.status_code == 503
