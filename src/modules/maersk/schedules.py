"""
    maersk's schedule function
"""
import requests

from modules.maersk.request import ScheduleRequest
from modules.maersk.response import ScheduleResponse


def search_schedules(schedule_request: ScheduleRequest) -> ScheduleResponse:
    """search schedule

    Args:
        request (ScheduleRequest): schedule request

    Returns:
        ScheduleResponse: schedule response
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        'from': schedule_request.from_departure,
        'to': schedule_request.to_destination,
        'containerIsoCode': schedule_request.container_iso_code,
        'fromServiceMode': schedule_request.from_service_mode,
        'toServiceMode': schedule_request.to_service_mode,
        'numberOfWeeks': schedule_request.number_of_weeks,
        'dateType': schedule_request.date_type,
        'date': schedule_request.date,
        'vesselFlag': schedule_request.vessel_flag,
        'cargoType': schedule_request.cargo_type,
        'containerType': schedule_request.container_type,
        'containerLength': schedule_request.container_length,
        'brandCode': schedule_request.brand_code
    }

    response = requests.request(
        'GET',
        'https://api.maersk.com/oceanProducts/maeu/futureschedules',
        headers=headers,
        params=params,
        timeout=10
    )

    result = ScheduleResponse()
    if response.status_code == 200:
        result = ScheduleResponse.of(response.text)

    return result


if __name__ == '__main__':
    request = ScheduleRequest()
    request.from_departure = '2GZ03V8AX8T5O'
    request.to_destination = '3AJMN274REBUN'
    request.container_iso_code = '42G1'
    request.from_service_mode = 'CY'
    request.to_service_mode = 'CY'
    request.number_of_weeks = 4
    request.date_type = 'D'
    request.date = '2022-09-05'
    request.vessel_flag = None
    request.cargo_type = 'DRY'
    request.container_type = 'DRY'
    request.container_length = 40
    request.brand_code = 'maeu'

    search_schedules(request)
