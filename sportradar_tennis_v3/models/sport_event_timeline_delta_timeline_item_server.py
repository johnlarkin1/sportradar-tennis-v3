from enum import Enum


class SportEventTimelineDeltaTimelineItemServer(str, Enum):
    AWAY = "away"
    HOME = "home"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
