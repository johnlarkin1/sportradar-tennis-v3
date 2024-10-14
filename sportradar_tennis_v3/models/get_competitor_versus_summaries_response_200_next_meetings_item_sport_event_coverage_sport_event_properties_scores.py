from enum import Enum


class GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventCoverageSportEventPropertiesScores(str, Enum):
    LIVE = "live"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
