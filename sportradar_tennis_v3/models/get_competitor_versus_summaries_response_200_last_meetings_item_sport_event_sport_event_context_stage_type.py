from enum import Enum


class GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStageType(str, Enum):
    CUP = "cup"
    LEAGUE = "league"

    def __str__(self) -> str:
        return str(self.value)
