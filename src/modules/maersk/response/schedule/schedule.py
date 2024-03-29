"""
    Schedule response model
"""
from typing import Any

from modules.maersk.response.schedule.location import Location
from modules.maersk.response.schedule.schedule_detail import ScheduleDetail
from modules.maersk.response.schedule.vessel import Vessel


class Schedule:
    """
        Schedule model class
    """
    def __init__(self):
        self.transit_time = ""
        self.from_location: Location = Location()
        self.to_location: Location = Location()
        self.vessel: Vessel = Vessel()
        self.schedule_details: list[ScheduleDetail] = []

    @staticmethod
    def of(data: Any) -> 'Schedule':
        """mapping data to Schedule

        Args:
            data (Any): data object

        Returns:
            Schedule: mapping result
        """
        schedule = Schedule()

        schedule.transit_time = data.transitTime
        schedule.from_location = Location.of(data.fromLocation)
        schedule.to_location = Location.of(data.toLocation)
        schedule.vessel = Vessel.of(data.vessel)

        for _, val in enumerate(data.scheduleDetails):
            schedule_detail = ScheduleDetail.of(val)
            schedule.schedule_details.append(schedule_detail)

        return schedule
