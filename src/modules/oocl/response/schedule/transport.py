from typing import Any


class Transport:
    def __init__(self):
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any):
        transport = Transport()
        transport.code = data.Code
        transport.name = data.Name

        return transport
