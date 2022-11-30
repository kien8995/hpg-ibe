import json
from types import SimpleNamespace as Namespace

from modules.oocl.response.schedule.schedule import Schedule


class ScheduleResponse:
    def __init__(self):
        self.number_of_route_return = 0
        self.nearby = False
        self.schedules: list[Schedule] = []

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        response = ScheduleResponse()
        if not data.success:
            return response

        product = data.data

        response.number_of_route_return = product.numberOfRouteReturn
        response.nearby = product.nearby

        for index, val in enumerate(product.standardRoutes):
            schedule = Schedule.of(val)

            response.schedules.append(schedule)

        return response


