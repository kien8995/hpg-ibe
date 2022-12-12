"""
    ScheduleResponse response model
"""
import json
from types import SimpleNamespace as Namespace

from modules.cosco.response.schedule.schedule import Schedule


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

        for _, val in enumerate(parents):
            children_1 = list(filter(lambda x, val=val:
                                x.transitTime == val.transitTime
                                and x.cargoNature == val.cargoNature
                                and x.legSequence > 1, children
                            )
                     )
            children_1.sort(key=lambda x: x.legSequence)
            result = []
            for _, e in enumerate(children_1):
                if not result:
                    if val.pod == e.pol and e.legSequence == 2:
                        result.append(e)
                else:
                    if result[-1].pod == e.pol and e.legSequence == result[-1].legSequence + 1:
                        result.append(e)
            val.legs = result

        for _, val in enumerate(parents):
            schedule = Schedule.of(val)
            response.schedules.append(schedule)

        return response
