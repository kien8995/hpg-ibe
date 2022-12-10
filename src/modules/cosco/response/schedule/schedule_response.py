"""
    ScheduleResponse response model
"""
import json
from types import SimpleNamespace as Namespace

from modules.cosco.response.schedule.schedule import Schedule


def _find_children_(parent, children):
    return []


class ScheduleResponse:
    """
        ScheduleResponse model class
    """
    def __init__(self):
        self.trace_id = ""
        self.delivery = ""
        self.arrival = False
        self.to_date = ""
        self.origin_city_uuid = ""
        self.pickup = ""
        self.pol = ""
        self.from_date = ""
        self.destination_city = ""
        self.cargo_nature = ""
        self.destination_city_uuid = ""
        self.origin_city = ""
        self.departure = False
        self.data_source = ""
        self.estimate_date = ""
        self.schedules: list[Schedule] = []

    @staticmethod
    def of(json_str: str) -> 'ScheduleResponse':
        """convert json string to ScheduleResponse

        Args:
            json_str (str): json string

        Returns:
            ScheduleResponse: convert result
        """
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        response = ScheduleResponse()
        if not data.code == "200":
            return response

        content = data.data.content
        product = content.data
        condition = content.conditions

        response.trace_id = condition.traceId
        response.delivery = condition.delivery
        response.arrival = condition.arrival
        response.to_date = condition.toDate
        response.origin_city_uuid = condition.originCityUuid
        response.pickup = condition.pickup
        response.pol = condition.pol
        response.from_date = condition.fromDate
        response.destination_city = condition.destinationCity
        response.cargo_nature = condition.cargoNature
        response.destination_city_uuid = condition.destinationCityUuid
        response.origin_city = condition.originCity
        response.departure = condition.departure
        response.data_source = condition.dataSource
        response.estimate_date = condition.estimateDate

        parents = list(filter(lambda x: x.id is not None, product))
        children = list(filter(lambda x: x.id is None, product))

        for index, val in enumerate(parents):
            parents[index].children = _find_children_(val, children)
        #     schedule = Schedule.of(val)
        #
        #     response.schedules.append(schedule)

        return response
