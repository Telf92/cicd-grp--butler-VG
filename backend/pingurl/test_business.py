from unittest.mock import patch
from pingurl.models import PingData
from pingurl.business import add_watched_url
from datetime import datetime, timedelta
from pingurl.models import WatchedUrl

@patch("pingurl.ping.send_ping")
@patch("pingurl.persistance.add_watched_url", return_value=5)
@patch("pingurl.persistance.add_ping_data")
@patch("pingurl.schedule.add")
def test_add_watched_url(
    send_ping, persist_add_url, persist_add_ping, sched_add
):
    time = datetime.now()

    ping_data = PingData(
        time,
        timedelta(seconds=1),
        200,
    )

    send_ping.return_value = ping_data

    watched_url = WatchedUrl(
        time,
        True,
        1,
        "https://example.com",
    )

    assert add_watched_url(watched_url) == 5

    # assert that the mocks have been called
    send_ping.assert_called_once_with(watched_url)
    # persist_add_url.assert_called_once_with(watched_url)
    # persist_add_ping.assert_called_once_with(ping_data)
    sched_add.assert_called_once_with(watched_url)
