"""
    Location response model
"""
import json
from types import SimpleNamespace as Namespace
from typing import Any

import requests


class Location:
    """
        Location model class
    """
    def __init__(self):
        self.date = ""
        self.time = ""
        self.city_name = ""
        self.country_code = ""
        self.country_geo_id = ""
        self.country_name = ""
        self.maersk_geo_location_id = ""
        self.maersk_rkst_code = ""
        self.maersk_rkts_code = ""
        self.region_code = ""
        self.region_name = ""
        self.site_name = ""
        self.timezone_id = ""
        self.type = ""
        self.un_loc_code = ""

    @staticmethod
    def of(data: Any) -> 'Location':
        """mapping data to Location

        Args:
            data (Any): data object

        Returns:
            Location: mapping result
        """
        location = Location()
        location.date = data.date
        location.time = data.time

        # get location detail
        response = requests.request(
            'GET',
            f'https://api.maersk.com/locations/{data.siteGeoId}',
            timeout=10
        )
        location_detail = json.loads(response.text, object_hook=lambda d: Namespace(**d))

        location.city_name = location_detail.cityName
        location.country_code = location_detail.countryCode
        location.country_geo_id = location_detail.countryGeoId
        location.country_name = location_detail.countryName
        location.maersk_geo_location_id = location_detail.maerskGeoLocationId
        location.maersk_rkst_code = location_detail.maerskRkstCode
        location.maersk_rkts_code = location_detail.maerskRktsCode
        location.region_code = location_detail.regionCode
        location.region_name = location_detail.regionName
        location.site_name = location_detail.siteName
        location.timezone_id = location_detail.timezoneId
        location.type = location_detail.type
        location.un_loc_code = location_detail.unLocCode

        return location
