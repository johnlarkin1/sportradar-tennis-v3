from enum import Enum


class GetStreamEventsResponse200Type0PayloadSportEventStatusGameStateServing(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
