"""
    Port response model
"""
from typing import Any


class Port:
    """
        Port model class
    """
    def __init__(self):
        self.id = ""
        self.type = ""
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any) -> 'Port':
        """mapping data to Port

        Args:
            data (Any): data object

        Returns:
            Port: mapping result
        """
        port = Port()
        port.id = data.ID
        if hasattr(data, 'Type'):
            port.type = data.Type
        port.code = data.Code
        port.name = data.Name

        return port
