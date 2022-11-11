from event_store.models.base_model import BaseModel
from event_store.models.location import Location


class ScheduleOutput(BaseModel):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.schedules: list[ScheduleOutput.Schedule] = []

    class Schedule:
        def __init__(self):
            self.transit_time = ""
            self.from_departure: Location = Location()
            self.to_destination: Location = Location()
