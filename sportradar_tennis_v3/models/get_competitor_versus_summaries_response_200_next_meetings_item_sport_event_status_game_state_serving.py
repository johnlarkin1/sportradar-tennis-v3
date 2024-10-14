from enum import Enum


class GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatusGameStateServing(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
