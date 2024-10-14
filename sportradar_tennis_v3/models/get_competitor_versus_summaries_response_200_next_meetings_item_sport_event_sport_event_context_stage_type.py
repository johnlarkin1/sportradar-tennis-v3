from enum import Enum


class GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventSportEventContextStageType(str, Enum):
    CUP = "cup"
    LEAGUE = "league"

    def __str__(self) -> str:
        return str(self.value)
