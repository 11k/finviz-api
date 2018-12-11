from enum import Enum

class MarketCap(Enum):
    OVER_300_MIL = "cap_smallover"

class Price(Enum):
    UNDER_20 = "sh_price_u20"

class Sort(Enum):
    CHANGE = "change"

    def desc(self):
        return "-" + self.value

    def asc(self):
        return self.value

