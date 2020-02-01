#!/usr/bin/python
from lru_cache.src.cache import LRUCache


def main():
    cache = LRUCache(5, 5000)
    cache.put_in_cache(1, 'www.google.com')
    cache.put_in_cache(2, 'www.amazon.com')
    cache.put_in_cache(3, 'www.ebay.com')

    for i in cache.traverse_cache():
        print(i)

if __name__ == '__main__':
    main()
