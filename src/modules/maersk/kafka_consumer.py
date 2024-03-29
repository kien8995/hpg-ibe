"""
    maersk's kafka consumer
"""
import json
import sys
import jsonpickle

from kafka import KafkaConsumer

from config import app_config
from constants import ShippingCompany
from event_store.models import ScheduleInput, ScheduleOutput
from event_store import get_kafka_consumer, publish_to_result
from modules.maersk import search_schedules
from modules.maersk.request import ScheduleRequest
from modules.maersk.response import ScheduleResponse
from utils.json_util import is_json

DEFAULT_TOPIC = app_config['modules']['maersk']['consumer-topic']
POLL_TIMEOUT_MS = app_config['modules']['maersk']['poll-timeout-ms']


def main(args: list[str]):
    """get and subscribe kafka topic

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
                    schedule_request.from_departure = data.dep
                    schedule_request.to_destination = data.arr
                    schedule_request.date = data.date
                    schedule_request.number_of_weeks = data.number_of_weeks

                    schedules = search_schedules(schedule_request)
                    schedule_output = _map_schedules_to_output(schedules)

                    schedules_json = jsonpickle.encode(schedule_output, unpicklable=False)
                    schedules_json_str = json.dumps(schedules_json)
                    # print(schedules_json_str)

                    publish_to_result(key, schedules_json_str)
        except Exception as ex:
            print('Exception in subscribing')
            print(str(ex))
            continue


def _map_schedules_to_output(schedules: ScheduleResponse) -> ScheduleOutput:
    schedule_output = ScheduleOutput()
    schedule_output.type = str(ShippingCompany.MAERSK)

    for _, val in enumerate(schedules.schedules):
        schedule = ScheduleOutput.Schedule()
        schedule.transit_time = val.transit_time
        schedule.from_departure.date = val.from_location.date
        schedule.from_departure.time = val.from_location.time
        schedule.from_departure.city_name = val.from_location.city_name
        schedule.from_departure.country_code = val.from_location.country_code
        schedule.from_departure.country_name = val.from_location.country_name
        schedule.from_departure.region_code = val.from_location.region_code
        schedule.from_departure.region_name = val.from_location.region_name
        schedule.from_departure.site_name = val.from_location.site_name

        schedule.to_destination.date = val.to_location.date
        schedule.to_destination.time = val.to_location.time
        schedule.to_destination.city_name = val.to_location.city_name
        schedule.to_destination.country_code = val.to_location.country_code
        schedule.to_destination.country_name = val.to_location.country_name
        schedule.to_destination.region_code = val.to_location.region_code
        schedule.to_destination.region_name = val.to_location.region_name
        schedule.to_destination.site_name = val.to_location.site_name

        schedule_output.schedules.append(schedule)

    return schedule_output


if __name__ == "__main__":
    topic = sys.argv[1:]
    if topic is None or len(topic) == 0:
        topic = [DEFAULT_TOPIC]

    main(topic)
