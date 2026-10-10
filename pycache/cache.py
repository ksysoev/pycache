"""
Cache package
"""


class Cache:
    """
    Cache class
    """

    def __init__(self, storage):
        self.store = storage

    def cache(self, key, generator):
        data = self.store.get(key)

        if data != None:
            return data

        data = generator()

        self.store.set(key, data)

        return data

    def invalidate(self, key):
        self.store.delete(key)
