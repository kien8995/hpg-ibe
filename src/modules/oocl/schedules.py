import json

import requests

from modules.oocl.request import ScheduleRequest
from modules.oocl.response import ScheduleResponse


def get_cs_token(app_key: str) -> str:
    headers = {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"'
    }

    params = {
        'appKey': app_key,
        'captchaType': 'blockPuzzle',
    }

    response = requests.get('https://cs-captcha.cargosmart.com/captcha/public/get', params=params, headers=headers)
    data_raw = response.text[1:-2]
    data_json = json.loads(data_raw)

    return data_json['repData']['token']


def search_schedules(request: ScheduleRequest) -> ScheduleResponse:
    app_key = '1dc597b617744cb49c97e20b523931e1'
    cs_token = get_cs_token(app_key)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
    }

    json_data = {
        'date': request.date,
        'displayDate': '',
        'transhipment_Port': None,
        'port_of_Load': None,
        'port_of_Discharge': None,
        'sailing': 'sailing.from',
        'weeks': request.number_of_weeks,
        'transhipment_PortId': None,
        'service': None,
        'port_of_LoadId': None,
        'port_of_DischargeId': None,
        'origin_Haulage': 'cy',
        'destination_Haulage': 'cy',
        'cargo_Nature': 'dry',
        'originId': request.from_departure,
        'originCountryCode': '',
        'destinationCountryCode': '',
        'destinationId': request.to_destination,
        'origin': '',
        'destination': '',
        'showCaptcha': 'false',
        'csToken': cs_token,
        'appKey': app_key,
        'weeksSymbol': '+',
    }

    response = requests.post('http://moc.oocl.com/nj_prs_wss/mocss/secured/supportData/nsso/searchHubToHubRoute',
                             headers=headers, json=json_data)

    result = ScheduleResponse()
    if response.status_code == 200:
        result = ScheduleResponse.of(response.text)

    return result


if __name__ == '__main__':
    request = ScheduleRequest()
    request.date = '2022-11-17'
    request.from_departure = '461798104035121'
    request.to_destination = '461802935876817'
    request.number_of_weeks = '4'

    search_schedules(request)
