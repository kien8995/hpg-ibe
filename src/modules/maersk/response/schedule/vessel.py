"""
    Vessel response model
"""
from typing import Any

import requests


class Vessel:
    """
        Vessel model class
    """
    def __init__(self):
        self.code = ""
        self.name = ""
        self.build_year = ""
        self.call_sign = ""
        self.capacity_teu = ""
        self.class_name = ""
        self.flag_code = ""
        self.flag_name = ""
        self.imo_number = ""
        self.long_name = ""

    @staticmethod
    def of(data: Any) -> 'Vessel':
        """mapping data to Vessel

        Args:
            data (Any): data object

        Returns:
            Vessel: mapping result
        """
        vessel = Vessel()
        vessel.code = data.code
        vessel.name = data.name

        # get vessel detail
        response = requests.request(
            'GET',
            f'https://api.maersk.com/vessels?maerskCode={data.code}',
            timeout=10
        )
        vessel_detail = response.json()

        if response.status_code == 200:
            vessel.build_year = vessel_detail["buildYear"]
            vessel.call_sign = vessel_detail["callSign"]
            vessel.capacity_teu = vessel_detail["capacityTeu"]
            vessel.class_name = vessel_detail["class"]
            vessel.flag_code = vessel_detail["flagCode"]
            vessel.flag_name = vessel_detail["flagName"]
            vessel.imo_number = vessel_detail["imoNumber"]
            vessel.long_name = vessel_detail["longName"]

        return vessel
