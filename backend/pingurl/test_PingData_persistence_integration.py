from datetime import datetime, timedelta
from pingurl.models import WatchedUrl, PingData
from pingurl.persistance import add_watched_url, add_ping_data, get_url_data


def test_ping_data_creation_and_retrieval():
    # Create and add WatchedUrl
    activate_at = datetime.now()
    force = True
    period_sec = 60
    url = "http://example.com"
    watched_url = WatchedUrl(activate_at, force, period_sec, url)
    url_id = add_watched_url(watched_url)

    # Create and add PingData
    pinged_at = datetime.now()
    response_time_sec = timedelta(seconds=1)
    status_code = 200
    ping_data = PingData(pinged_at, response_time_sec, status_code, url_id)
    add_ping_data(ping_data)

    # Retrieve and assert
    url_data = get_url_data(url_id)
    assert len(url_data["pings"]) == 1
    assert url_data["pings"][0]["statusCode"] == status_code
    assert url_data["pings"][0]["responseTimeSec"] == response_time_sec.total_seconds()
