"""
    Transport response model
"""
from typing import Any


class Transport:
    """Transport model class
    """
    def __init__(self):
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any) -> 'Transport':
        """mapping data to Transport

        Args:
            data (Any): data object

        Returns:
            Transport: mapping result
        """
        transport = Transport()
        transport.code = data.Code
        transport.name = data.Name

        return transport
