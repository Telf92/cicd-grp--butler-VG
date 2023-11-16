import os
import requests

container_ip = os.environ.get('CONTAINER_IP', 'default_value_if_not_set')

API_WATCHED_URL = f"http://{container_ip}:5000/watched-urls"
API_STATS_URL = f"http://{container_ip}:5000/stats"

def test_get_watched_url_none():
    assert requests.get(API_WATCHED_URL, timeout=20).json() == {'urlIds': []}

def test_set_watched_url():
    to_post = {
    "activateAt": "2023-11-06T01:36:28.610Z",
    "force": True,
    "periodSec": 30,
    "url": "https://google.com"
    }
    assert requests.post(API_WATCHED_URL, json=to_post, timeout=20).json() == {"message": "Watched URL added","urlId": 0}

def test_get_watched_url_first():
    assert requests.get(API_WATCHED_URL, timeout=20).json() == {'urlIds': [0]}  

def test_get_stats():
    assert requests.get(API_STATS_URL, timeout=20).json() == {"pings": 1, "watchedUrls": 1}
 