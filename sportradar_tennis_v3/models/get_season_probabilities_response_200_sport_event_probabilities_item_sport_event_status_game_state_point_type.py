from enum import Enum


class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventStatusGameStatePointType(str, Enum):
    BREAK = "break"
    GAME = "game"
    MATCH = "match"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
