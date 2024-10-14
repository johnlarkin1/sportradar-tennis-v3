from enum import Enum


class GetCompetitorSummariesResponse200SummariesItemSportEventType(str, Enum):
    CHILD = "child"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
