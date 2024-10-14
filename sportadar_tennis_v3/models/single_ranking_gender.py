from enum import Enum


class SingleRankingGender(str, Enum):
    MEN = "men"
    MIXED = "mixed"
    WOMEN = "women"

    def __str__(self) -> str:
        return str(self.value)
