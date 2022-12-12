"""
    cosco's test producer
"""
import uuid

from config import app_config
from event_store.producer import get_kafka_producer, publish

DEFAULT_TOPIC = app_config['modules']['cosco']['consumer-topic']


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


if __name__ == "__main__":
    GUID = str(uuid.uuid4())
    DATA = """
    {
       "type": "cosco",
       "dep_id": "738872886234414",
       "dep": "Ho Chi Minh, ,Ho Chi Minh,Vietnam,VNHCM",
       "arr_id": "738872886265409",
       "arr": "Helsinki, ,Uusimaa,Finland,FIHEL",
       "date": "2022-12-13"
    }
    """
    main([DEFAULT_TOPIC, GUID, DATA])
