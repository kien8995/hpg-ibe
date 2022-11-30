from typing import Any


class CargoContainerSet:
    def __init__(self):
        self.cargo_natures: list[str] = []
        self.cntr_types: list[str] = []
        self.cntr_sizes: list[str] = []

    @staticmethod
    def of(data: Any):
        cargoContainerSet = CargoContainerSet()
        cargoContainerSet.cargo_natures = data.CargoNatures
        cargoContainerSet.cntr_types = data.CntrTypes
        cargoContainerSet.cntr_sizes = data.CntrSizes

        return cargoContainerSet
