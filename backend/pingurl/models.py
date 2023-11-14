from datetime import datetime, timedelta
import validators

class WatchedUrl:
    def __init__(self, activate_at: datetime, force: bool, period_sec: int, url: str, url_id: int = None):
        if not isinstance(activate_at, datetime):
            raise ValueError("activate_at must be a datetime instance")
        if not isinstance(force, bool):
            raise ValueError("force must be a boolean")
        if not isinstance(period_sec, int) or period_sec <= 0:
            raise ValueError("period_sec must be a positive integer")
        if not isinstance(url, str) or not validators.url(url):
            raise ValueError("url must be a valid URL string")
        if not (isinstance(url_id, int) or url_id is None):
            raise ValueError("url_id must be an integer")

        self.activate_at = activate_at
        self.force = force
        self.period_sec = period_sec
        self.url = url
        self.url_id = url_id

    def to_dict(self):
        return {
            "activateAt": self.activate_at.isoformat(),
            "force": self.force,
            "periodSec": self.period_sec,
            "url": self.url,
            "urlId": self.url_id
        }

    def __repr__(self):
        return f"WatchedUrl({self.activate_at}, {self.force}, {self.period_sec}, {self.url}, {self.url_id})"

    __str__ = __repr__

class PingData:
    def __init__(self, url_id: int, pinged_at: datetime, response_time: timedelta, status_code: int):
        if not isinstance(url_id, int):
            raise ValueError("url_id must be an integer")
        if not isinstance(pinged_at, datetime):
            raise ValueError("pinged_at must be a datetime instance")
        if not isinstance(response_time, timedelta):
            raise ValueError("response_time must be a timedelta instance")
        if not isinstance(status_code, int):
            raise ValueError("status_code must be an integer")

        self.url_id = url_id
        self.pinged_at = pinged_at
        self.response_time = response_time
        self.status_code = status_code

    def to_dict(self):
        return {
            "urlId": self.url_id,
            "pingedAt": self.pinged_at.isoformat(),
            "responseTime": self.response_time.total_seconds(),
            "statusCode": self.status_code
        }

    def __repr__(self):
        return f"PingData({self.url_id}, {self.pinged_at}, {self.response_time}, {self.status_code})"

    __str__ = __repr__
