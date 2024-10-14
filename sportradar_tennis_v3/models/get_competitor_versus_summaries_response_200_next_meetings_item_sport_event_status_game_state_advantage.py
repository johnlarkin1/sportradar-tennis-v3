from enum import Enum


class GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatusGameStateAdvantage(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
