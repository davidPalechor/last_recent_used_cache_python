#!/usr/bin/python
# from .cache import LRUCache
from .config import app


@app.task
def publish(key, data):
    print(f'{key} {data}')
