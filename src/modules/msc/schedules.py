"""
    msc's schedule function
"""
from typing import Any
import requests

from modules.msc.request import ScheduleRequest


def search_schedules(schedule_request: ScheduleRequest) -> Any:
    """search schedule

    Args:
        request (ScheduleRequest): request data

    Returns:
        ScheduleResponse: response data
    """

    cookies = {
        'SC_ANALYTICS_GLOBAL_COOKIE': 'eebaeaddb41d4b0da98b70502e2a2057|False',
        'currentAgency': '2736',
        'currentLocation': 'VN',
        'msccargo#lang': 'en',
    }

    headers = {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'FromDate': schedule_request.from_date,
        'fromPortId': schedule_request.from_port_id,
        'toPortId': schedule_request.to_port_id,
        'isDirectRouteOnly': False,
        'language': 'en',
    }

    response = requests.post('https://www.msc.com/api/feature/tools/SearchSailingRoutes',
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10
    )

    # result = ScheduleResponse()
    if response.status_code == 200:
        # result = ScheduleResponse.of(response.text)
        return response.json()

    return '{}'


if __name__ == '__main__':
    request = ScheduleRequest()
    request.from_date = '2022-11-16'
    request.from_port_id = '51'
    request.to_port_id = '138'

    search_schedules(request)
