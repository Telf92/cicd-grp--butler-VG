from pingurl.models import WatchedUrl, PingData

watched_urls = {}
pings = {}
next_id = 0

def add_watched_url(watched_url: WatchedUrl):
    if not isinstance(watched_url, WatchedUrl):
        raise ValueError("watched_url must be a WatchedUrl instance")

    if (watched_url.url_id is not None):
        raise ValueError("url_id must be None")
    global next_id

    watched_url.url_id = next_id

    next_id += 1

    watched_urls[watched_url.url_id] = watched_url

    return watched_url.url_id

def delete_url(url_id):
    if not isinstance(url_id, int):
        raise ValueError("url_id must be an integer")
    
    if url_id not in watched_urls:
        raise ItemNotFoundError("url_id not found")

    del watched_urls[url_id]

def get_url_data(url_id):
    return jsonify({'message': 'Good'}), 201

def get_url_ids():
    return list(watched_urls.keys())

def get_stats():
    return {'watchedUrls': len(watched_urls), 'pings': len(pings)}

class ItemNotFoundError(Exception):
    def __init__(self, id, message="Watched URL with the given urlId was not found."):
        self.id = id
        self.message = message
        super().__init__(self.message)
