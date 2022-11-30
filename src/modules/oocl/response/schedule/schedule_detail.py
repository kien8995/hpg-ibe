from typing import Any

from modules.oocl.response.schedule.facility import Facility
from modules.oocl.response.schedule.port import Port
from modules.oocl.response.schedule.transport import Transport


class ScheduleDetail:
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
        self.origin_facility: Facility = Facility()
        self.destination_facility: Facility = Facility()
        self.origin_labelled_facility: Facility = Facility()
        self.destination_labelled_facility: Facility = Facility()
        self.city: Facility = Facility()
        self.transport_mode: Transport = Transport()
        self.loading_port: Port = Port()
        self.discharge_port: Port = Port()

    @staticmethod
    def of(data: Any):
        schedule_detail = ScheduleDetail()
        schedule_detail.component_id = data.ComponentId
        schedule_detail.type = data.Type
        schedule_detail.sequence = data.Sequence
        if hasattr(data, 'TransitTimeInMinute'):
            schedule_detail.transit_time_in_minute = data.TransitTimeInMinute
        if hasattr(data, 'CY'):
            schedule_detail.cy = data.CY
        if hasattr(data, 'Door'):
            schedule_detail.door = data.Door
        if hasattr(data, 'CargoCutoffGmtDateTime'):
            schedule_detail.cargo_cutoff_gmt_date_time = data.CargoCutoffGmtDateTime.dateStr
        if hasattr(data, 'CargoAvailabilityGmtDateTime'):
            schedule_detail.cargo_cutoff_gmt_date_time = data.CargoAvailabilityGmtDateTime.dateStr
        schedule_detail.cargo_cutoff_local_date_time = data.CargoCutoffLocalDateTime.dateStr
        schedule_detail.cargo_availability_local_date_time = data.CargoAvailabilityLocalDateTime.dateStr
        if hasattr(data, 'FromETDGmtDateTime'):
            schedule_detail.from_etd_gmt_date_time = data.FromETDGmtDateTime.dateStr
        if hasattr(data, 'FromETAGmtDateTime'):
            schedule_detail.from_eta_gmt_date_time = data.FromETAGmtDateTime.dateStr
        if hasattr(data, 'ToETDGmtDateTime'):
            schedule_detail.to_etd_gmt_date_time = data.ToETDGmtDateTime.dateStr
        if hasattr(data, 'ToETAGmtDateTime'):
            schedule_detail.to_eta_gmt_date_time = data.ToETAGmtDateTime.dateStr
        if hasattr(data, 'FromETDLocalDateTime'):
            schedule_detail.from_etd_local_date_time = data.FromETDLocalDateTime.dateStr
        if hasattr(data, 'FromETALocalDateTime'):
            schedule_detail.from_eta_local_date_time = data.FromETALocalDateTime.dateStr
        if hasattr(data, 'ToETDLocalDateTime'):
            schedule_detail.to_etd_local_date_time = data.ToETDLocalDateTime.dateStr
        if hasattr(data, 'ToETALocalDateTime'):
            schedule_detail.to_eta_local_date_time = data.ToETALocalDateTime.dateStr
        if hasattr(data, 'Service'):
            schedule_detail.service = data.Service
        if hasattr(data, 'LoadingSvvd'):
            schedule_detail.loading_svvd = data.LoadingSvvd
        if hasattr(data, 'LoadingSvvdCallNumber'):
            schedule_detail.loading_svvd_call_number = data.LoadingSvvdCallNumber
        if hasattr(data, 'DischargeSvvd'):
            schedule_detail.discharge_svvd = data.DischargeSvvd
        if hasattr(data, 'DischargeSvvdCallNumber'):
            schedule_detail.discharge_svvd_call_number = data.DischargeSvvdCallNumber
        schedule_detail.origin_facility_timezone_name = data.OriginFacilityTimezoneName
        schedule_detail.destination_facility_timezone_name = data.DestinationFacilityTimezoneName
        if hasattr(data, 'VesselName'):
            schedule_detail.vessel_name = data.VesselName
        if hasattr(data, 'ExternalVoyageReference'):
            schedule_detail.external_voyage_reference = data.ExternalVoyageReference
        schedule_detail.origin_facility = Facility.of(data.OriginFacility)
        schedule_detail.destination_facility = Facility.of(data.DestinationFacility)
        if hasattr(data, 'OriginLabelledFacility'):
            schedule_detail.origin_labelled_facility = Facility.of(data.OriginLabelledFacility)
        if hasattr(data, 'DestinationLabelledFacility'):
            schedule_detail.destination_labelled_facility = Facility.of(data.DestinationLabelledFacility)
        if hasattr(data, 'City'):
            schedule_detail.city = Facility.of(data.City)
        if hasattr(data, 'LoadingPort'):
            schedule_detail.loading_port = Port.of(data.LoadingPort)
        if hasattr(data, 'DischargePort'):
            schedule_detail.discharge_port = Port.of(data.DischargePort)

        return schedule_detail
