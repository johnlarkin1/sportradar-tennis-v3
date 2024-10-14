from enum import Enum


class GetSportEventSummaryResponse200SportEventSportEventContextStageType(str, Enum):
    CUP = "cup"
    LEAGUE = "league"

    def __str__(self) -> str:
        return str(self.value)
