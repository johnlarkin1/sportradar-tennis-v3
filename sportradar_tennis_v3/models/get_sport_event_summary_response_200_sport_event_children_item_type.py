from enum import Enum


class GetSportEventSummaryResponse200SportEventChildrenItemType(str, Enum):
    CHILD = "child"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
