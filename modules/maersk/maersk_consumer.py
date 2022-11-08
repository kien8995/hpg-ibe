import json
import sys
import jsonpickle

from kafka import KafkaConsumer
from event_store.models import ScheduleInput
from event_store.models.schedule_output import ScheduleOutput
from event_store.producer import publish_to_result
from event_store.consumer import get_kafka_consumer
from modules.maersk import search_schedules
from modules.maersk.request.schedule_request import ScheduleRequest
from utils.json_util import is_json

DEFAULT_TOPIC = "search_MAERSK"


def main(args: list[str]):
    global topic
    try:
        print(args[0])
        topic = args[0]
    except Exception as ex:
        print("Failed to set topic")

    consumer = get_kafka_consumer(topic)
    subscribe(consumer)
    consumer.close()


def subscribe(consumer: KafkaConsumer):
    while True:
        try:
            message_pack = consumer.poll(timeout_ms=500)

            for tp, messages in message_pack.items():
                for message in messages:
                    print("%s:%d:%d: key=%s value=%s" % (tp.topic, tp.partition,
                                                         message.offset, message.key,
                                                         message.value))
                    key = message.key.decode("utf-8")
                    value = message.value.decode("utf-8")

                    # print(key, value)

                    if not is_json(value):
                        continue

                    data = ScheduleInput.of(value)

                    print(f"Message Received: {key}: {data.type}, {data.dep}, {data.arr}, {data.date}")

                    scheduleRequest = ScheduleRequest()
                    scheduleRequest.from_departure = data.dep
                    scheduleRequest.to_destination = data.arr
                    scheduleRequest.date = data.date

                    schedules = search_schedules(scheduleRequest)

                    schedule_output = ScheduleOutput()
                    schedule_output.type = "maersk"

                    schedules_json = jsonpickle.encode(schedule_output, unpicklable=False)
                    schedules_json_str = json.dumps(schedules_json)
                    print(schedules_json_str)

                    # publish_to_result(key, schedules_json_str)
            continue
        except Exception as ex:
            print('Exception in subscribing')
            print(str(ex))
            break


if __name__ == "__main__":
    topic = sys.argv[1:]
    if topic is None or len(topic) == 0:
        topic = [DEFAULT_TOPIC]

    main(topic)
