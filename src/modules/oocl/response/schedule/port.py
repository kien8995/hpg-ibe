from typing import Any


class Port:
    def __init__(self):
        self.id = ""
        self.type = ""
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any):
        port = Port()
        port.id = data.ID
        if hasattr(data, 'Type'):
            port.type = data.Type
        port.code = data.Code
        port.name = data.Name

        return port
