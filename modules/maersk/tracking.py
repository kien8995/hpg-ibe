import requests

from modules.maersk.request.tracking_request import TrackingRequest
from modules.maersk.response.tracking.tracking_response import TrackingResponse


def search_tracking(request: TrackingRequest) -> TrackingResponse:
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.request(
        'GET',
        'https://api.maersk.com/track/{0}?operator={1}'.format(request.tracking_code, request.operator),
        headers=headers
    )

    result = TrackingResponse()
    if response.status_code == 200:
        result = TrackingResponse.of(response.text)

    return result


if __name__ == '__main__':
    request = TrackingRequest()
    request.tracking_code = 'MNBU9066300'
    request.operator = 'MAEU'

    search_tracking(request)
