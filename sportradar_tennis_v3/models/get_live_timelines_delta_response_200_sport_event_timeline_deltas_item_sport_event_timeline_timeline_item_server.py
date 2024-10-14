from enum import Enum


class GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineTimelineItemServer(str, Enum):
    AWAY = "away"
    HOME = "home"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
