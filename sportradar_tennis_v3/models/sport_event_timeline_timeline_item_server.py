from enum import Enum


class SportEventTimelineTimelineItemServer(str, Enum):
    AWAY = "away"
    HOME = "home"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
