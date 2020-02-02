import os

from ..cache import LRUCache

APP_SECRET = os.getenv('APP_SECRET')
SERVER_SECRET = os.getenv('SERVER_SECRET')
BROKER_URL = 'amqp://guest@localhost//'
CACHE_MAX_CAPACITY = int(os.getenv('CACHE_MAX_CAPACITY'))
CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION'))

KAFKA_HOST = os.getenv('KAFKA_HOST')
KAFKA_PORT = os.getenv('KAFKA_PORT')
KAFKA_TOPIC = f'dlru_{APP_SECRET}'
KAFKA_TOPIC_SERVER = f'dlru_{SERVER_SECRET}'


cache = LRUCache(CACHE_MAX_CAPACITY, CACHE_EXPIRATION)

