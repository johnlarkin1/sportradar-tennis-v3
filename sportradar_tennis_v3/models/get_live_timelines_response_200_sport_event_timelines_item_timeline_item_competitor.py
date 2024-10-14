from enum import Enum


class GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemCompetitor(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
