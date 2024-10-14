from enum import Enum


class SportEventProbabilitySportEventCoverageSportEventPropertiesScores(str, Enum):
    LIVE = "live"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
