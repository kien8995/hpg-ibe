from kafka import KafkaProducer
from config import app_config

DEFAULT_SERVER = app_config['kafka']['producer']['default-server']


def publish_message(topic: str, key: str, message: str):
    producer = get_kafka_producer()
    publish(producer, topic, key, message)


def publish(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print(f"Publish Successful ({key}, {value}) -> {topic_name}")
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def get_kafka_producer(servers=None):
    if servers is None:
        servers = DEFAULT_SERVER

    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=servers, api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
