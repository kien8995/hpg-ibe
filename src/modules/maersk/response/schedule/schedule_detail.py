from typing import Any

from modules.maersk.response.schedule.location import Location
from modules.maersk.response.schedule.transport import Transport


class ScheduleDetail:
    def __init__(self):
        self.carrier_code = ""
        self.routing_type = ""
        self.service_code = ""
        self.service_name = ""
        self.from_location: Location = Location()
        self.to_location: Location = Location()
        self.transport: Transport = Transport()

    @staticmethod
    def of(data: Any):
        schedule_detail = ScheduleDetail()
        schedule_detail.carrier_code = data.carrierCode
        schedule_detail.routing_type = data.routingType
        schedule_detail.service_code = data.serviceCode
        schedule_detail.service_name = data.serviceName
        schedule_detail.from_location = Location.of(data.fromLocation)
        schedule_detail.to_location = Location.of(data.toLocation)
        schedule_detail.transport = Transport.of(data.transport)

        return schedule_detail

