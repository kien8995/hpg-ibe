"""
    maersk's tracking function
"""
import requests

from modules.maersk.request import TrackingRequest
from modules.maersk.response.tracking import TrackingResponse


def search_tracking(tracking_request: TrackingRequest) -> TrackingResponse:
    """tracking data

    Args:
        request (TrackingRequest): tracking data request

    Returns:
        TrackingResponse: tracking data response
    """
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.request(
        'GET',
        f'https://api.maersk.com/track/{tracking_request.tracking_code}?operator={tracking_request.operator}',
        headers=headers,
        timeout=10
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
