from typing import Any

from modules.msc.response.schedule.vessel import Vessel


class ScheduleDetail:
    def __init__(self):
        self.leg_sequence = 0
        self.single_leg_only = False
        self.last_leg = False
        self.departure_voyage_no = ""
        self.departure_port_un_code = ""
        self.departure_port_id = ""
        self.departure_port_name = ""
        self.departure_equipment_handling_facility_name = ""
        self.estimated_departure_time = ""
        self.estimated_departure_time_formatted = ""
        self.estimated_arrival_time = ""
        self.arrival_port_port_id = ""
        self.arrival_port_name = ""
        self.arrival_equipment_handling_facility_name = ""
        self.estimated_arrival_time_formatted = ""
        self.co2_foot_print = ""
        self.maritime_service_name = ""
        self.vessel: Vessel = Vessel()

    @staticmethod
    def of(data: Any):
        schedule_detail = ScheduleDetail()

        schedule_detail.leg_sequence = data.LegSequence
        schedule_detail.single_leg_only = data.SingleLegOnly
        schedule_detail.last_leg = data.LastLeg
        schedule_detail.departure_voyage_no = data.DepartureVoyageNo
        schedule_detail.departure_port_un_code = data.DeparturePortUNCode
        schedule_detail.departure_port_id = data.DeparturePortId
        schedule_detail.departure_port_name = data.DeparturePortName
        schedule_detail.departure_equipment_handling_facility_name = data.DepartureEquipmentHandlingFacilityName
        schedule_detail.estimated_departure_time = data.EstimatedDepartureTime
        schedule_detail.estimated_departure_time_formatted = data.EstimatedDepartureTimeFormatted
        schedule_detail.estimated_arrival_time = data.EstimatedArrivalTime
        schedule_detail.estimated_arrival_time_formatted = data.EstimatedArrivalTimeFormatted
        schedule_detail.arrival_port_port_id = data.ArrivalPortPortId
        schedule_detail.arrival_port_name = data.ArrivalPortName
        schedule_detail.arrival_equipment_handling_facility_name = data.ArrivalEquipmentHandlingFacilityName
        schedule_detail.co2_foot_print = data.CO2FootPrint
        schedule_detail.maritime_service_name = data.MaritimeServiceName
        schedule_detail.vessel = Vessel.of(data.Vessel)

        return schedule_detail
