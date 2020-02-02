import json
import logging
import threading as th

from kafka import KafkaConsumer
from kafka import KafkaProducer

from ..config import config

logging.basicConfig(level=logging.INFO)


class PubSub:
    def __init__(self):
        self.consumer = KafkaConsumer(config.KAFKA_TOPIC,
                                      bootstrap_servers=[f'{config.KAFKA_HOST}:{config.KAFKA_PORT}'])

        self.producer = KafkaProducer(bootstrap_servers=[f'{config.KAFKA_HOST}:{config.KAFKA_PORT}'])
        self.cache = config.cache
        self.logger = logging.getLogger('PubSub')
        self.logger.setLevel(logging.INFO)

    def consume(self):
        """Consume and processes kafka messages
        """
        _ACTIONS = {
            'get': self.cache.get,
            'put': self.cache.put_in_cache
        }
        for msg in self.consumer:
            try:
                json_data = json.loads(msg.value.decode('utf-8'))
                self.logger.info(f'processing message: {json_data}')
                action = json_data.get('action', 'get')
                if json_data.get('key'):
                    args = [json_data.get('key')]
                    if json_data.get('data'):
                        args.append(json_data['data'])

                    response = _ACTIONS.get(action)(*args)
                    if response:
                        self.send(data=response)

            except json.decoder.JSONDecodeError:
                self.logger.info('not valid json')
            else:
                self.logger.info('Unknown error')
            finally:
                pass

    def send(self, topic: str = config.KAFKA_TOPIC_SERVER, data=None):
        """Sends a message through a kafka topic

        Args:
            data: Information to be sent back to server
            topic: Topic that will be used to send the data (default: config.KAFKA_TOPIC_SERVER)
        """
        if isinstance(data, dict):
            self.producer.send(topic, json.dumps(data))
        elif isinstance(data, str):
            self.producer.send(topic, data.encode())
        elif isinstance(data, bytes):
            self.producer.send(topic, data)
        else:
            self.logger('not valid data type')

    def serve(self):
        t = th.Thread(target=self.consume)
        t.start()
