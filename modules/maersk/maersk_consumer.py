import json
import sys
import jsonpickle

from kafka import KafkaConsumer
from event_store.models import ScheduleRequest
from event_store.models.schedule_response import ScheduleResponse
from event_store.producer import publish_to_result
from event_store.consumer import get_kafka_consumer
from modules.maersk import search_schedules
from modules.maersk.request.schedule_request import ScheduleRequest

DEFAULT_TOPIC = "search_maersk"


def main(args):
    try:
        topic = args[0]
    except Exception as ex:
        print("Failed to set topic")

    consumer = get_kafka_consumer(topic)
    subscribe(consumer)


def subscribe(consumer_instance: KafkaConsumer):
    try:
        for event in consumer_instance:
            key = event.key.decode("utf-8")
            value = event.value.decode("utf-8")

            data = ScheduleRequest.of(value)

            print(f"Message Received: {key}: {data.guid}, {data.dep}, {data.arr}, {data.date}, {data.carrier}")
            scheduleRequest = ScheduleRequest()
            scheduleRequest.from_departure = data.dep
            scheduleRequest.to_destination = data.arr
            scheduleRequest.date = data.date

            schedules = search_schedules(scheduleRequest)

            scheduleResponse = ScheduleResponse()

            schedules_json = jsonpickle.encode(scheduleResponse, unpicklable=False)
            schedules_json_str = json.dumps(schedules_json)
            print(schedules_json_str)

            # publish_to_result(key, schedules_json_str)
        consumer_instance.close()
    except Exception as ex:
        print('Exception in subscribing')
        print(str(ex))


if __name__ == "__main__":
    topic = sys.argv[1:]
    if topic is None:
        topic = [DEFAULT_TOPIC]

    main(topic)
