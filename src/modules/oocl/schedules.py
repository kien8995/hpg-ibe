"""
    oocl's schedule function
"""
import json

import requests

from config import app_config
from modules.oocl.request import ScheduleRequest
from modules.oocl.response import ScheduleResponse

APP_KEY = DEFAULT_TOPIC = app_config['modules']['oocl']['app-key']

def get_cs_token(app_key: str) -> str:
    """get cs token

    Args:
        app_key (str): app key

    Returns:
        str: cs token
    """

    headers = {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"'
    }

    params = {
        'appKey': app_key,
        'captchaType': 'blockPuzzle',
    }

    response = requests.get('https://cs-captcha.cargosmart.com/captcha/public/get',
        params=params,
        headers=headers,
        timeout=10
    )
    data_raw = response.text[1:-2]
    data_json = json.loads(data_raw)

    return data_json['repData']['token']


def search_schedules(schedule_request: ScheduleRequest) -> ScheduleResponse:
    """search schedules

    Args:
        request (ScheduleRequest): schedule request

    Returns:
        ScheduleResponse: schedule response
    """
    cs_token = get_cs_token(APP_KEY)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent':   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/107.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
    }

    json_data = {
        'date': schedule_request.date,
        'displayDate': '',
        'transhipment_Port': None,
        'port_of_Load': None,
        'port_of_Discharge': None,
        'sailing': 'sailing.from',
        'weeks': schedule_request.number_of_weeks,
        'transhipment_PortId': None,
        'service': None,
        'port_of_LoadId': None,
        'port_of_DischargeId': None,
        'origin_Haulage': 'cy',
        'destination_Haulage': 'cy',
        'cargo_Nature': 'dry',
        'originId': schedule_request.from_departure,
        'originCountryCode': '',
        'destinationCountryCode': '',
        'destinationId': schedule_request.to_destination,
        'origin': '',
        'destination': '',
        'showCaptcha': 'false',
        'csToken': cs_token,
        'appKey': APP_KEY,
        'weeksSymbol': '+',
    }

    response = requests.post('http://moc.oocl.com/nj_prs_wss/mocss/secured/supportData/nsso/'
                            'searchHubToHubRoute',
                             headers=headers, json=json_data, timeout=10)

    result = ScheduleResponse()
    if response.status_code == 200:
        result = ScheduleResponse.of(response.text)
        print(response.text)

    return result


if __name__ == '__main__':
    request = ScheduleRequest()
    request.date = '2022-11-17'
    request.from_departure = '461798104035121'
    request.to_destination = '461802935876817'
    request.number_of_weeks = '4'

    search_schedules(request)
