import uuid
from event_store.producer import get_kafka_producer, publish


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
       "type": "msc",
       "dep": "51",
       "arr": "138",
       "date": "2022-11-16"
    }
    """
    main(['search_MSC', guid, data])
