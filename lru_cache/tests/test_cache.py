import unittest

from .context import LRUCache


class TestLRUCache(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache = LRUCache(max_capacity=5)
        self.cache.put_in_cache(1, 'lorem')
        self.cache.put_in_cache(2, 'ipsum')
        self.cache.put_in_cache(3, 'dolor')
        self.cache.put_in_cache(4, 'sit')
        self.cache.put_in_cache(5, 'amet')

    def test_cache_get(self):
        tests = [
            {
                "name": "Get existing item",
                "data": 1,
                "return": 'lorem'
            },
            {
                "name": "Get existing item",
                "data": 2,
                "return": 'ipsum'
            },
            {
                "name": "Get non existing item",
                "data": 6,
                "return": None
            }
        ]

        for test in tests:
            self.assertEqual(test['return'], self.cache.get(test['data']))

    def test_cache_put(self):
        tests = [
            {
                "name": "Put an item",
                "key": 6,
                "data": 'consectetur',
                "return": 'consectetur'
            },
            {
                "name": "Put an item",
                "key": 7,
                "data": 'adipiscing',
                "return": 'adipiscing'
            },
        ]

        for test in tests:
            self.cache.put_in_cache(test['key'], test['data'])
            self.assertEqual(test['return'], self.cache.get(test['key']))


if __name__ == '__main__':
    unittest.main()
