from celery import Celery

BROKER_URL = 'amqp://guest@localhost//'

app = Celery('distributed_cache', broker=BROKER_URL)