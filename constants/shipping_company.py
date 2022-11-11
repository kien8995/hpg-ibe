from enum import Enum, unique


@unique
class ShippingCompany(Enum):
    MAERSK = "maersk"
    COSCO = "cosco"
    MSC = "MSC"
