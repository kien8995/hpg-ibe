import requests
import json

from modules.cosco.request.cosco_request import CoscoRequest


def search_point_to_point(request: CoscoRequest):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        'cargoNature': request.cargo_nature,
        'delivery': request.delivery,
        'destinationCity': request.destination_city,
        'destinationCityUuid': request.destination_city_uuid,
        'estimateDate': request.estimate_date,
        'fromDate': request.from_date,
        'originCity': request.origin_city,
        'originCityUuid': request.origin_city_uuid,
        'pickup': request.pickup,
        'toDate': request.to_date
    })

    response = requests.request(
        'POST',
        'https://elines.coscoshipping.com/ebschedule/public/purpoShipmentWs',
        headers=headers,
        data=payload
    )
    print(response.json())


if __name__ == '__main__':
    request = CoscoRequest()
    request.cargo_nature = 'All'
    request.delivery = 'B'
    request.destination_city = 'Helsinki, ,Uusimaa,Finland,FIHEL'
    request.destination_city_uuid = '738872886265409'
    request.estimate_date = 'D'
    request.from_date = '2022-10-16'
    request.origin_city = 'Ho Chi Minh, ,Ho Chi Minh,Vietnam,VNHCM'
    request.origin_city_uuid = '738872886234414'
    request.pickup = 'B'
    request.to_date = '2022-11-12'

    search_point_to_point(request)
