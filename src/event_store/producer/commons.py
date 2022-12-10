"""
    kafka's common function
"""
from kafka import KafkaProducer
from config import app_config

DEFAULT_SERVER = app_config['kafka']['producer']['default-server']


def publish_message(topic: str, key: str, message: str):
    """publish a kafka message

    Args:
        topic (str): topic name
        key (str): topic key
        message (str): topic message
    """
    producer = get_kafka_producer()
    publish(producer, topic, key, message)


def publish(producer_instance, topic_name, key, value):
    """publish a kafka message with producer instance

    Args:
        producer_instance (_type_): kafka producer
        topic_name (_type_): topic name
        key (_type_): topic key
        value (_type_): topic message
    """
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print(f"Publish Successful ({key}, {value}) -> {topic_name}")
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def get_kafka_producer(servers: list[str] = None) -> KafkaProducer:
    """get kafka producer

    Args:
        servers (list[str], optional): bootstap server. Defaults to None.

    Returns:
        KafkaProducer: kafka producer
    """
    if servers is None:
        servers = DEFAULT_SERVER

    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=servers, api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    return _producer
