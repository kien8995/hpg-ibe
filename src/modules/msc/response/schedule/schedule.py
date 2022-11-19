from typing import Any

from modules.msc.response.schedule.location import Location
from modules.msc.response.schedule.schedule_detail import ScheduleDetail


class Schedule:
    def __init__(self):
        self.transit_time = ""
        self.transit_time_hours = ""
        self.estimated_departure_date = ""
        self.estimated_departure_date_formatted = ""
        self.estimated_arrival_date = ""
        self.estimated_arrival_date_formatted = ""
        self.vessel_name = ""
        self.departure_voyage_no = ""
        self.from_location: Location = Location()
        self.to_location: Location = Location()
        self.schedule_details: list[ScheduleDetail] = []

    @staticmethod
    def of(data: Any):
        schedule = Schedule()

        schedule.transit_time = data.TotalTransitTime
        schedule.transit_time_hours = data.TotalTransitTimeHours
        schedule.estimated_departure_date = data.EstimatedDepartureDate
        schedule.estimated_departure_date_formatted = data.EstimatedDepartureDateFormatted
        schedule.estimated_arrival_date = data.EstimatedArrivalDate
        schedule.estimated_arrival_date_formatted = data.EstimatedArrivalDateFormatted
        schedule.vessel_name = data.VesselName
        schedule.departure_voyage_no = data.DepartureVoyageNo

        for index, val in enumerate(data.RouteScheduleLegDetails):
            schedule_detail = ScheduleDetail.of(val)
            schedule.schedule_details.append(schedule_detail)

        return schedule

