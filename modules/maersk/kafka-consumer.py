import json
import sys

import jsonpickle
from kafka import KafkaConsumer
from types import SimpleNamespace as Namespace
from kafka_server import publish_result
from modules.maersk import search_schedules
from modules.maersk.request.schedule_request import ScheduleRequest

DEFAULT_SERVER = "localhost:9092"
DEFAULT_TOPIC = "search_maersk"


def main(args):
    try:
        topic = args[0]
    except Exception as ex:
        print("Failed to set topic")

    consumer = get_kafka_consumer(topic)
    subscribe(consumer)


def subscribe(consumer_instance):
    try:
        for event in consumer_instance:
            key = event.key.decode("utf-8")
            value = event.value.decode("utf-8")
            data = json.loads(value, object_hook=lambda d: Namespace(**d))

            print(f"Message Received: {key}: {data.guid}, {data.dep}, {data.arr}, {data.date}, {data.carrier}")
            scheduleRequest = ScheduleRequest()
            scheduleRequest.from_departure = data.dep
            scheduleRequest.to_destination = data.arr
            scheduleRequest.date = data.date

            schedules = search_schedules(scheduleRequest)
            schedules_json = jsonpickle.encode(schedules, unpicklable=False)
            schedules_json_str = json.dumps(schedules_json)
            print(schedules_json_str)
            # publish_result(key, schedules_json_str)
        consumer_instance.close()
    except Exception as ex:
        print('Exception in subscribing')
        print(str(ex))


def get_kafka_consumer(topic_name, servers=None):
    if servers is None:
        servers = [DEFAULT_SERVER]

    _consumer = None
    try:
        _consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest', bootstrap_servers=servers,
                                  api_version=(0, 10), consumer_timeout_ms=10000)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _consumer


if __name__ == "__main__":
    topic = sys.argv[1:]
    if topic is None:
        topic = [DEFAULT_TOPIC]

    main(topic)
