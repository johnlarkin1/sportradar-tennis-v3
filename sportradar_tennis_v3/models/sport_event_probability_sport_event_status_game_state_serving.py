from enum import Enum


class SportEventProbabilitySportEventStatusGameStateServing(str, Enum):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
