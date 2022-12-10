"""
    Schedule response model
"""
from typing import Any

from modules.cosco.response.schedule.schedule_detail import ScheduleDetail


class Schedule:
    """
        Schedule model class
    """
    def __init__(self):
        self.route_id = ""
        self.transit_time_in_day = ""
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
        schedule.route_id = data.id
        schedule.transit_time_in_day = data.transitTime

        for _, val in enumerate(data.Legs):
            schedule_detail = ScheduleDetail.of(val)
            schedule.schedule_details.append(schedule_detail)

        return schedule
