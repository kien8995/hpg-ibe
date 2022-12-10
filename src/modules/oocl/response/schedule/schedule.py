"""
    Schedule response model
"""
from typing import Any

from modules.oocl.response.schedule.cargo_container_set import CargoContainerSet
from modules.oocl.response.schedule.schedule_detail import ScheduleDetail


class Schedule:
    """
        Schedule model class
    """
    def __init__(self):
        self.route_id = ""
        self.transit_time_in_minute = ""
        self.cargo_cutoff_gmt_date_time = ""
        self.cargo_availability_gmt_date_time = ""
        self.cargo_cutoff_local_date_time = ""
        self.cargo_availability_local_date_time = ""
        self.cargo_container_set: CargoContainerSet = CargoContainerSet()
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
        schedule.route_id = data.RouteId
        schedule.transit_time_in_minute = data.TransitTimeInMinute
        schedule.cargo_cutoff_gmt_date_time = data.CargoCutoffGmtDateTime.dateStr
        schedule.cargo_availability_gmt_date_time = data.CargoAvailabilityGmtDateTime.dateStr
        schedule.cargo_cutoff_local_date_time = data.CargoCutoffLocalDateTime.dateStr
        schedule.cargo_availability_local_date_time = data.CargoAvailabilityLocalDateTime.dateStr
        schedule.cargo_container_set = CargoContainerSet.of(data.CargoContainerSet)

        for _, val in enumerate(data.Legs):
            schedule_detail = ScheduleDetail.of(val)
            schedule.schedule_details.append(schedule_detail)

        return schedule
