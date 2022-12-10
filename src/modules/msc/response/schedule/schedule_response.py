"""
    ScheduleResponse response model
"""
import json
from types import SimpleNamespace as Namespace

from modules.msc.response.schedule.schedule import Schedule


class ScheduleResponse:
    """
        ScheduleResponse model class
    """
    def __init__(self):
        self.port_load_id = ""
        self.port_load = ""
        self.port_load_un_code = ""
        self.port_discharge_id = ""
        self.port_discharge = ""
        self.port_discharge_un_code = ""
        self.transit_time = ""
        self.transit_time_hours = ""
        self.co2_foot_print = ""
        self.estimated_departure_time = ""
        self.estimated_departure_time_formatted = ""
        self.loading_service = ""
        self.is_direct_route = False
        self.routing_type = ""
        self.schedules: list[Schedule] = []

    @staticmethod
    def of(json_str: str) -> 'ScheduleResponse':
        """convert json string to ScheduleResponse

        Args:
            json_str (str): json string

        Returns:
            ScheduleResponse: convert result
        """
        data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

        response = ScheduleResponse()
        if not data.IsSuccess:
            return response

        product = data.Data[0]

        response.port_load_id = product.PortOfLoadId
        response.port_load = product.PortOfLoad
        response.port_load_un_code = product.PortOfLoadUnCode
        response.port_discharge_id = product.PortOfDischargeId
        response.port_discharge = product.PortOfDischarge
        response.port_discharge_un_code = product.PortOfDischargeUnCode
        response.transit_time = product.TransitTime
        response.transit_time_hours = product.TransitTimeHours
        response.co2_foot_print = product.CO2FootPrint
        response.estimated_departure_time = product.EstimatedDepartureTime
        response.estimated_departure_time_formatted = product.EstimatedDepartureTimeFormatted
        response.loading_service = product.LoadingService
        response.is_direct_route = product.IsDirectRoute
        response.routing_type = product.RoutingType

        for _, val in enumerate(product.Routes):
            schedule = Schedule.of(val)
            schedule.from_location.port_id = product.PortOfLoadId
            schedule.from_location.port_name = product.PortOfLoad
            schedule.from_location.port_un_code = product.PortOfLoadUnCode

            schedule.to_location.port_id = product.PortOfDischargeId
            schedule.to_location.port_name = product.PortOfDischarge
            schedule.to_location.port_un_code = product.PortOfDischargeUnCode

            response.schedules.append(schedule)

        return response
