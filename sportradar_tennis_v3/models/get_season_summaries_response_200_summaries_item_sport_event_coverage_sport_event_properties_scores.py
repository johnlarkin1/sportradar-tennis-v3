from enum import Enum


class GetSeasonSummariesResponse200SummariesItemSportEventCoverageSportEventPropertiesScores(str, Enum):
    LIVE = "live"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
