import uuid

from config import app_config
from event_store.producer import get_kafka_producer, publish

DEFAULT_TOPIC = app_config['modules']['maersk']['consumer-topic']


def main(args):
    try:
        topic = args[0]
        key = args[1]
        message = args[2]
    except Exception as ex:
        print("Failed to set topic, key, or message")

    producer = get_kafka_producer()
    publish(producer, topic, key, message)


if __name__ == "__main__":
    guid = str(uuid.uuid4())
    data = """
    {
       "type": "maersk",
       "dep": "2GZ03V8AX8T5O",
       "arr": "3AJMN274REBUN",
       "date": "2022-09-05",
       "number_of_weeks": 5
    }
    """
    main([DEFAULT_TOPIC, guid, data])
