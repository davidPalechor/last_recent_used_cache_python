# Distributed LRU Cache

This is a lite implementation of a Distributed Last Recently Used (LRU) cache.

This module is for academic purposes only and is not meant to be deployed to production in any way.
## Dependencies
- [Apache Kafka 2.4.0](https://kafka.apache.org/)

## Initial Steps

### Initiating Kafka

- Go to Kafka installation directory 

    `cd /usr/local/kafka/`
- Before starting Kafka you should first start a Zookeeper instance by running

    `bin/zookeeper-server-start.sh config/zookeeper.properties`
- Start Kafka by running

    `bin/kafka-server-start.sh config/server.properties`
    
### Creating Topics

- In order to create a topic, run

    `bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic dlru_server`
    
    where `dlru_server` is the name of the topic
    
    See [Create a Topic](https://kafka.apache.org/quickstart#quickstart_createtopic) for more information.
    
- Start a consumer

    `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic dlru_server`
    
    See [Start a consumer](https://kafka.apache.org/quickstart#quickstart_consume) for more.    

- Start a producer

    `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic dlru_2223323342`

    See [Send some messages](https://kafka.apache.org/quickstart#quickstart_send) for more.

## Needed Environment Variables

In order to the library to work properly, you will have to export some environment variables. eg.

```bash
export CACHE_EXPIRATION=5000
export CACHE_MAX_CAPACITY=50
export APP_SECRET=2223323342
export KAFKA_HOST=localhost
export KAFKA_PORT=9092
export SERVER_SECRET=server
```

## Usage
- Import distributed cache package and make a new client

```python
from lru_cache.cache import DistributedCache

client = DistributedCache.new_client()
```

- To start processing and sending messages do:

```python
client.serve()
```

### Methods

- Via Kafka producer send a json-like message indicating the action to be triggered (default is `get`), the key to be stored and the data associated to it (required for `put` method) 

#### Get

```shell script
>{"key": 1}
```

This method will send the response through a kafka message again like:

```shell script
lorem ipsum
```
### Put

```shell script
>{"action": "put", "key": 1, "data": "lorem ipsum"}    
>{"action": "put", "key": 2, "data": "dolor sit amet"} 
>{"action": "put", "key": 3, "data": "consectetur adipiscing elit"} 
>{"action": "put", "key": 4, "data": "Vestibulum lobortis"} 
```

