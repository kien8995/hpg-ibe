"""
    result producer
"""
import sys
from config import app_config
from event_store.producer import get_kafka_producer, publish

RESULT_TOPIC = app_config['kafka']['producer']['result-topic']


def main(args: list[str]):
    """publish kafka message

    Args:
        args (list[str]): data list
    """
    try:
        topic = args[0]
        key = args[1]
        message = args[2]
    except Exception as _:
        print("Failed to set topic, key, or message")

    producer = get_kafka_producer()
    publish(producer, topic, key, message)


def publish_to_result(key: str, message: str):
    """publish kafka message to result topic

    Args:
        key (str): topic name
        message (str): topic message
    """
    producer = get_kafka_producer()
    publish(producer, RESULT_TOPIC, key, message)


if __name__ == "__main__":
    main(sys.argv[1:])
