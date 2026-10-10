"""
inmemory store
"""


class InMemoryStore:
    def __init__(self, limit=1000):
        self.limit = limit
        self.store = {}

    def get(self, key):
        return self.store.get(key, None)

    def set(self, key, value):
        self.store[key] = value

    def delete(self, key):
        del self.store[key]
