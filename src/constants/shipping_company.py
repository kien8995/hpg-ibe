from enum import Enum, unique


@unique
class ShippingCompany(Enum):
    MAERSK = "maersk"
    COSCO = "cosco"
    MSC = "msc"
    OOCL = "oocl"

    def __str__(self):
        return str(self.value)
