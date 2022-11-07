import json
from typing import Any

from modules.maersk.response.schedule.vessel import Vessel


class Transport:
    def __init__(self):
        self.trade_lane = ""
        self.transport_mode = ""
        self.voyage_number = ""
        self.vessel: Vessel = Vessel()

    @staticmethod
    def of(data: Any):
        transport = Transport()
        transport.trade_lane = data.tradeLane
        transport.transport_mode = data.transportMode
        transport.voyage_number = data.voyageNumber
        transport.vessel = Vessel.of(data.vessel)

        return transport

