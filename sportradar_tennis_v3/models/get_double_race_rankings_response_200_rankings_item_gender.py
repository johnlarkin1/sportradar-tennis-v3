from enum import Enum


class GetDoubleRaceRankingsResponse200RankingsItemGender(str, Enum):
    MEN = "men"
    MIXED = "mixed"
    WOMEN = "women"

    def __str__(self) -> str:
        return str(self.value)
