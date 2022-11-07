import requests

from modules.maersk.request.schedule_request import ScheduleRequest
from modules.maersk.response.schedule.schedule_response import ScheduleResponse


def search_schedules(request: ScheduleRequest) -> ScheduleResponse:
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        'from': request.from_departure,
        'to': request.to_destination,
        'containerIsoCode': request.container_iso_code,
        'fromServiceMode': request.from_service_mode,
        'toServiceMode': request.to_service_mode,
        'numberOfWeeks': request.number_of_weeks,
        'dateType': request.date_type,
        'date': request.date,
        'vesselFlag': request.vessel_flag,
        'cargoType': request.cargo_type,
        'containerType': request.container_type,
        'containerLength': request.container_length,
        'brandCode': request.brand_code
    }

    response = requests.request(
        'GET',
        'https://api.maersk.com/oceanProducts/maeu/futureschedules',
        headers=headers,
        params=params
    )

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
