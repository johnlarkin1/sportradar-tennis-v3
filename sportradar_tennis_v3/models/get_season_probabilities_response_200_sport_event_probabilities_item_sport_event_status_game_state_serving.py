from enum import Enum


class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventStatusGameStateServing(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
