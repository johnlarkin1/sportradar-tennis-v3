from enum import Enum


class SeasonBracketsStageType(str, Enum):
    CUP = "cup"
    LEAGUE = "league"

    def __str__(self) -> str:
        return str(self.value)
