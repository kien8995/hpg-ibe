"""
    ScheduleDetail response model
"""
from typing import Any


class ScheduleDetail:
    """
        ScheduleDetail model class
    """
    def __init__(self):
        self.component_id = ""
        self.type = ""
        self.sequence = ""
        self.transit_time_in_minute = ""
        self.cy = ""
        self.door = ""
        self.cargo_cutoff_gmt_date_time = ""
        self.cargo_availability_gmt_date_time = ""
        self.cargo_cutoff_local_date_time = ""
        self.cargo_availability_local_date_time = ""
        self.from_etd_gmt_date_time = ""
        self.from_eta_gmt_date_time = ""
        self.to_etd_gmt_date_time = ""
        self.to_eta_gmt_date_time = ""
        self.from_etd_local_date_time = ""
        self.from_eta_local_date_time = ""
        self.to_etd_local_date_time = ""
        self.to_eta_local_date_time = ""
        self.service = ""
        self.loading_svvd = ""
        self.loading_svvd_call_number = ""
        self.discharge_svvd = ""
        self.discharge_svvd_call_number = ""
        self.origin_facility_timezone_name = ""
        self.destination_facility_timezone_name = ""
        self.vessel_name = ""
        self.external_voyage_reference = ""

    @staticmethod
    def of(data: Any) -> 'ScheduleDetail':
        """mapping data to ScheduleDetail

        Args:
            data (Any): data object

        Returns:
            ScheduleDetail: mapping result
        """
        schedule_detail = ScheduleDetail()
        schedule_detail.component_id = data.ComponentId
        schedule_detail.type = data.Type
        schedule_detail.sequence = data.Sequence

        return schedule_detail
