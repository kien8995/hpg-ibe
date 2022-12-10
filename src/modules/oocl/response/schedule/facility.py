"""
    Facility response model
"""
from typing import Any


class Facility:
    """
        Facility model class
    """
    def __init__(self):
        self.id = ""
        self.type = ""
        self.code = ""
        self.name = ""

    @staticmethod
    def of(data: Any) -> 'Facility':
        """mapping data to Facility

        Args:
            data (Any): data object

        Returns:
            Facility: mapping result
        """
        facility = Facility()
        facility.id = data.ID
        if hasattr(data, 'Type'):
            facility.type = data.Type
        facility.code = data.Code
        facility.name = data.Name

        return facility
