from enum import Enum


class StreamEventsPayloadSportEventStatusGameStateAdvantage(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
