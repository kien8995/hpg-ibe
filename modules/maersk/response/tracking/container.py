from typing import Any

from modules.maersk.response.tracking.latest import Latest
from modules.maersk.response.tracking.location import Location


class Container:
    def __init__(self):
        self.container_num = ""
        self.container_size = ""
        self.container_type = ""
        self.eta_final_delivery = ""
        self.iso_code = ""
        self.latest: Latest = Latest()
        self.locations: list[Location] = []
        self.operator = ""
        self.status = ""

    @staticmethod
    def of(data: Any):
        container = Container()
        container.container_num = data.container_num
        container.container_size = data.container_size
        container.container_type = data.container_type
        container.eta_final_delivery = data.eta_final_delivery
        container.iso_code = data.iso_code
        container.latest = Latest.of(data.latest)

        if hasattr(data, 'locations'):
            for index, val in enumerate(data.locations):
                container.locations.append(Location.of(val))

        container.operator = data.operator
        container.status = data.status

        return container
