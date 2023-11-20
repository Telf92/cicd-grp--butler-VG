from datetime import datetime, timedelta
from pingurl.models import PingData

def test_ping_data():
    pinged_at = datetime.now()
    response_time_sec = timedelta(seconds=1)
    status_code_200 = 200
    status_code_404 = 404

    # Test instantiation and 'ok' method for 200 status code
    ping_data_200 = PingData(pinged_at, response_time_sec, status_code_200)
    assert ping_data_200.pinged_at == pinged_at
    assert ping_data_200.response_time_sec == response_time_sec
    assert ping_data_200.status_code == status_code_200
    assert ping_data_200.ok()

    # Test 'ok' method for 404 status code
    ping_data_404 = PingData(pinged_at, response_time_sec, status_code_404)
    assert not ping_data_404.ok()
