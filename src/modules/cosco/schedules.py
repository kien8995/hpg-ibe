"""
    cosco's schedule function
"""
import requests

from modules.cosco.request import ScheduleRequest
from modules.cosco.response import ScheduleResponse


def search_schedules(schedule_request: ScheduleRequest) -> ScheduleResponse:
    """search schedule

    Args:
        schedule_request (ScheduleRequest): schedule request

    Returns:
        ScheduleResponse: schedule response
    """
    json_data = {
        'fromDate': schedule_request.from_date,
        'pickup': 'B',
        'delivery': 'B',
        'estimateDate': 'D',
        'toDate': schedule_request.to_date,
        'originCityUuid': schedule_request.origin_city_uuid,
        'destinationCityUuid': schedule_request.destination_city_uuid,
        'originCity': schedule_request.origin_city,
        'destinationCity': schedule_request.destination_city,
        'cargoNature': 'All',
    }

    response = requests.post(
        'https://elines.coscoshipping.com/ebschedule/public/purpoShipmentWs',
        json=json_data,
        timeout=10
    )

    result = ScheduleResponse()
    if response.status_code == 200:
        result = ScheduleResponse.of(response.text)

    return result


if __name__ == '__main__':
    request = ScheduleRequest()
    request.from_date = '2022-12-03'
    request.to_date = '2022-12-30'
    request.origin_city_uuid = '738872886234414'
    request.destination_city_uuid = '738872886265409'
    request.origin_city = 'Ho Chi Minh, ,Ho Chi Minh,Vietnam,VNHCM'
    request.destination_city = 'Helsinki, ,Uusimaa,Finland,FIHEL'

    search_schedules(request)
