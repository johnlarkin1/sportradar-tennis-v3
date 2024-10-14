from enum import Enum


class GetSeasonSummariesResponse200SummariesItemSportEventStatusGameStateServing(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
