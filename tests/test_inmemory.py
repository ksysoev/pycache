import unittest

import pycache.inmemory


class TestInMemoryStore(unittest.TestCase):
    def test_get(self):
        store = pycache.inmemory.InMemoryStore()

        store.set("key", "value")

        self.assertEqual(store.get("key"), "value")


if __name__ == "__main__":
    unittest.main()
