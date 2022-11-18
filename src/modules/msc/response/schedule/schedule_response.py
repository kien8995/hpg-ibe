import json
from types import SimpleNamespace as Namespace

from modules.msc.response.schedule.schedule import Schedule


class ScheduleResponse:
    def __init__(self):
        self.schedules: list[Schedule] = []

    @staticmethod
    def of(json_str: str):
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        response = ScheduleResponse()
        if not data.IsSuccess:
            return response

        product = data.Data[0]

        for index, val in enumerate(product.Routes):
            schedule = Schedule.of(val)
            schedule.from_location.port_id = product.PortOfLoadId
            schedule.from_location.port_name = product.PortOfLoad
            schedule.from_location.port_un_code = product.PortOfLoadUnCode

            schedule.to_location.port_id = product.PortOfDischargeId
            schedule.to_location.port_name = product.PortOfDischarge
            schedule.to_location.port_un_code = product.PortOfDischargeUnCode

            response.schedules.append(schedule)

        return response


