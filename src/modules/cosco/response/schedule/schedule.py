from typing import Any

from modules.cosco.response.schedule.schedule_detail import ScheduleDetail


class Schedule:
    def __init__(self):
        self.route_id = ""
        self.transit_time_in_day = ""
        self.schedule_details: list[ScheduleDetail] = []

    @staticmethod
    def of(data: Any):
        schedule = Schedule()
        schedule.route_id = data.id
        schedule.transit_time_in_day = data.transitTime

        for index, val in enumerate(data.Legs):
            schedule_detail = ScheduleDetail.of(val)
            schedule.schedule_details.append(schedule_detail)

        return schedule

