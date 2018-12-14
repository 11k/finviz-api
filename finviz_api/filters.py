from enum import Enum

class MarketCap(Enum):
    OVER_300_MIL = "cap_smallover"
    OVER_2_BIL = "cap_midover"

class Price(Enum):
    UNDER_20 = "sh_price_u20"
    FROM_5_TO_20 = "sh_price_5to20"

class Country(Enum):
    USA = "geo_usa"

class Sort(Enum):
    CHANGE = "change"

    def desc(self):
        return "-" + self.value

    def asc(self):
        return self.value

