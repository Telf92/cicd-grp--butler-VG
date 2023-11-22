#from unittest.mock import patch, MagicMock
#from pingurl.models import PingData
#from pingurl.business import add_watched_url
#from datetime import datetime, timedelta
#from pingurl.models import WatchedUrl
# import PingData

#@patch("pingurl.ping.send_ping")
#@patch("pingurl.persistance.add_watched_url")
#@patch("pingurl.persistance.add_ping_data")
#@patch("pingurl.schedule.add")
#def test_add_watched_url_with_mocked_ping(mock_ping, mock_add_watched_url, mock_add_ping_data, schedule_add):
#    time = datetime.now()
#    # Set up the mock response
#    mock_ping_response = PingData(
#        time,
    #     timedelta(seconds=1),
    #     200,
    # )
    # mock_ping.return_value = mock_ping_response

    # mock_add_watched_url_respond = 5
    # mock_add_watched_url.return_value = mock_add_watched_url_respond

    # watched_url = WatchedUrl(
    #     time,
    #     True,
    #     1,
    #     "https://example.com",
    # )
    # #    mock_ping.return_value = mock_response
    # assert mock_add_watched_url_respond == add_watched_url(watched_url)
