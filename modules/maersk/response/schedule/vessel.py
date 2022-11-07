import json
from typing import Any

import requests


class Vessel:
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
    def of(data: Any):
        vessel = Vessel()
        vessel.code = data.code
        vessel.name = data.name

        # get vessel detail
        response = requests.request(
            'GET',
            'https://api.maersk.com/vessels?maerskCode={0}'.format(data.code),
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

