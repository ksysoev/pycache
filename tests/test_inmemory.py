import unittest

import pycache.inmemory


class TestInMemoryStore(unittest.TestCase):
    def test_get_set(self):
        store = pycache.inmemory.InMemoryStore()

        self.assertEqual(store.get("key"), None)

        store.set("key", "value")

        self.assertEqual(store.get("key"), "value")

    def test_delete(self):
        store = pycache.inmemory.InMemoryStore()

        store.set("key", "value")

        self.assertEqual(store.get("key"), "value")

        store.delete("key")

        self.assertEqual(store.get("key"), None)


if __name__ == "__main__":
    unittest.main()
