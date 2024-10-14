from enum import Enum


class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStageType(str, Enum):
    CUP = "cup"
    LEAGUE = "league"

    def __str__(self) -> str:
        return str(self.value)
