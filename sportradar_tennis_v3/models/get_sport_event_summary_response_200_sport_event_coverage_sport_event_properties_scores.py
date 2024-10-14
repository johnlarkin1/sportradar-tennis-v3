from enum import Enum


class GetSportEventSummaryResponse200SportEventCoverageSportEventPropertiesScores(str, Enum):
    LIVE = "live"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
