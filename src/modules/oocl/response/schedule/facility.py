from typing import Any


class Facility:
    def __init__(self):
        self.id = ""
        self.type = ""
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any):
        facility = Facility()
        facility.id = data.ID
        if hasattr(data, 'Type'):
            facility.type = data.Type
        facility.code = data.Code
        facility.name = data.Name

        return facility
