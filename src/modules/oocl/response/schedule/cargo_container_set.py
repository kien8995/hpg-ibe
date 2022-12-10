"""
    CargoContainerSet response model
"""
from typing import Any


class CargoContainerSet:
    """
        CargoContainerSet model class
    """
    def __init__(self):
        self.cargo_natures: list[str] = []
        self.cntr_types: list[str] = []
        self.cntr_sizes: list[str] = []

    @staticmethod
    def of(data: Any) -> 'CargoContainerSet':
        """mapping data to CargoContainerSet

        Args:
            data (Any): data object

        Returns:
            CargoContainerSet: mapping result
        """
        cargo_container_set = CargoContainerSet()
        cargo_container_set.cargo_natures = data.CargoNatures
        cargo_container_set.cntr_types = data.CntrTypes
        cargo_container_set.cntr_sizes = data.CntrSizes

        return cargo_container_set
