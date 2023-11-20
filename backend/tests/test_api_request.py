import os
import requests

container_ip = os.environ.get('CONTAINER_IP', 'default_value_if_not_set')

API_URL = f"http://{container_ip}:5001"

# Just made one universal constant that then gets added onto when needed
#API_WATCHED_URL = "http://localhost:5000/watched-urls"
#API_STATS_URL = f"http:{container_ip}:5001/stats"
#API_DELETE_ULR = f"http://{container_ip}:5000/watched-urls/0"


def test_get_watched_url_none():
    assert requests.get(f"{API_URL}/watched-urls", timeout=20).json() == {"urlIds": []}


def test_set_watched_url():
    to_post = {
        "activateAt": "2023-11-06T01:36:28.610Z",
        "force": True,
        "periodSec": 30,
        "url": "https://google.com",
    }
    assert requests.post(f"{API_URL}/watched-urls", json=to_post, timeout=20).json() == {
        "message": "Watched URL added",
        "urlId": 0,
    }


def test_get_watched_url_first():
    assert requests.get(f"{API_URL}/watched-urls", timeout=20).json() == {"urlIds": [0]}


def test_get_stats():
    assert requests.get(f"{API_URL}/stats", timeout=20).json() == {
        "pings": 1,
        "watchedUrls": 1,
    }

def test_delete_url():
    assert requests.delete(f"{API_URL}/watched-urls/0", timeout=20).json() == {
        "message": "Removed watched url with id 0"
    }