import redis
import hashlib
import json

class Cache:
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)

    def _key(self, query):
        return hashlib.md5(query.encode()).hexdigest()

    def get(self, query):
        result = self.client.get(self._key(query))
        return json.loads(result) if result else None

    def set(self, query, value):
        self.client.set(self._key(query), json.dumps(value), ex=3600)
