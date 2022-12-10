"""
    Event response model
"""
from typing import Any


class Event:
    """
        Event model class
    """
    def __init__(self):
        self.actfor = ""
        self.activity = ""
        self.actual_time = ""
        self.is_cancelled = False
        self.is_current = False
        self.rkem_move = ""
        self.stempty = False
        self.vessel_name = ""
        self.vessel_num = ""
        self.voyage_num = ""

    @staticmethod
    def of(data: Any) -> 'Event':
        """mapping data to Event

        Args:
            data (Any): data object

        Returns:
            Event: mapping result
        """
        event = Event()
        event.actfor = data.actfor
        event.activity = data.activity
        if hasattr(data, 'actual_time'):
            event.actual_time = data.actual_time
        if hasattr(data, 'is_cancelled'):
            event.is_cancelled = data.is_cancelled
        event.is_current = data.is_current
        if hasattr(data, 'rkem_move'):
            event.rkem_move = data.rkem_move
        event.stempty = data.stempty
        event.vessel_name = data.vessel_name
        event.vessel_num = data.vessel_num
        event.voyage_num = data.voyage_num

        return event
