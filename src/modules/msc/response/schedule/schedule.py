from typing import Any

from modules.msc.response.schedule.location import Location


class Schedule:
    def __init__(self):
        self.transit_time = ""
        self.from_location: Location = Location()
        self.to_location: Location = Location()

    @staticmethod
    def of(data: Any):
        schedule = Schedule()

        schedule.transit_time = data.TotalTransitTimeHours

        return schedule

