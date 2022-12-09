"""
    Transport
"""
from typing import Any


class Transport:
    """Transport
    """
    def __init__(self):
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any) -> 'Transport':
        transport = Transport()
        transport.code = data.Code
        transport.name = data.Name

        return transport
