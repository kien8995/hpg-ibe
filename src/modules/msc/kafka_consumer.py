"""
    msc's kafka consumer
"""
import json
import sys

from kafka import KafkaConsumer

from config import app_config
from constants import ShippingCompany
from event_store.models import ScheduleInput, ScheduleOutput
from event_store import get_kafka_consumer, publish_to_result
from modules.msc import search_schedules
from modules.msc.request import ScheduleRequest
from modules.msc.response import ScheduleResponse
from utils.json_util import is_json

DEFAULT_TOPIC = app_config['modules']['msc']['consumer-topic']
POLL_TIMEOUT_MS = app_config['modules']['msc']['poll-timeout-ms']


def main(args: list[str]):
    """get and subscribe kafka consumer

    Args:
        args (list[str]): kafka topic
    """
    try:
        print(args[0])
        kafka_topic = args[0]
    except Exception as _:
        print("Failed to set topic")

    consumer = get_kafka_consumer(kafka_topic)
    subscribe(consumer)
    consumer.close()


def subscribe(consumer: KafkaConsumer):
    """subscribe kafka consumer

    Args:
        consumer (KafkaConsumer): kafka consumer
    """
    while True:
        try:
            message_pack = consumer.poll(timeout_ms=POLL_TIMEOUT_MS)

            for _, messages in message_pack.items():
                for message in messages:
                    # print("%s:%d:%d: key=%s value=%s" % (tp.topic, tp.partition,
                    #                                      message.offset, message.key,
                    #                                      message.value))
                    key = message.key.decode("utf-8")
                    value = message.value.decode("utf-8")

                    # print(key, value)

                    if not is_json(value):
                        continue

                    data = ScheduleInput.of(value)

                    # print(f"Message Received: {key}: {data.type}, {data.dep}, {data.arr}, {data.date}")

                    schedule_request = ScheduleRequest()
                    schedule_request.from_port_id = data.dep
                    schedule_request.to_port_id = data.arr
                    schedule_request.from_date = data.date

                    schedules = search_schedules(schedule_request)
                    # schedule_output = _map_schedules_to_output(schedules)

                    # schedules_json = jsonpickle.encode(schedule_output, unpicklable=False)
                    schedules_json_str = json.dumps(schedules)
                    # print(schedules_json_str)

                    publish_to_result(key, schedules_json_str)
        except Exception as ex:
            print('Exception in subscribing')
            print(str(ex))
            continue


def _map_schedules_to_output(schedules: ScheduleResponse) -> ScheduleOutput:
    schedule_output = ScheduleOutput()
    schedule_output.type = str(ShippingCompany.MSC)

    for _, val in enumerate(schedules.schedules):
        schedule = ScheduleOutput.Schedule()
        schedule.transit_time = val.transit_time
        schedule.from_departure.site_name = val.from_location.port_name
        schedule.to_destination.site_name = val.to_location.port_name

        schedule_output.schedules.append(schedule)

    return schedule_output


if __name__ == "__main__":
    topic = sys.argv[1:]
    if topic is None or len(topic) == 0:
        topic = [DEFAULT_TOPIC]

    main(topic)
