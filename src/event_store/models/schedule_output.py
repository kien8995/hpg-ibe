"""
    schedule output model
"""
from event_store.models.base_message import BaseMessage
from event_store.models.location import Location


class ScheduleOutput(BaseMessage):
    """
        ScheduleOutput model class
    """
    def __init__(self):
        super().__init__()
        self.type = ""
        self.schedules: list[ScheduleOutput.Schedule] = []

    class Schedule:
        """
            Schedule model inner class
        """
        def __init__(self):
            self.transit_time = ""
            self.from_departure: Location = Location()
            self.to_destination: Location = Location()
