"""
    Vessel response model
"""
from typing import Any


class Vessel:
    """
        Vessel model class
    """
    def __init__(self):
        self.vessel_name = ""
        self.vessel_imo_code = ""
        self.vessel_built_year = ""
        self.vessel_flag = ""

    @staticmethod
    def of(data: Any) -> 'Vessel':
        """mapping data to Vessel

        Args:
            data (Any): data object

        Returns:
            Vessel: mapping result
        """
        vessel = Vessel()
        vessel.vessel_name = data.VesselName
        vessel.vessel_imo_code = data.VesselImoCode
        vessel.vessel_built_year = data.VesselBuiltYear
        vessel.vessel_flag = data.VesselFlag

        return vessel
