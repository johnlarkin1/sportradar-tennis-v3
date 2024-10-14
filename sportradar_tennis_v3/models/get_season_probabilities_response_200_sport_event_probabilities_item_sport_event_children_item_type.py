from enum import Enum


class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventChildrenItemType(str, Enum):
    CHILD = "child"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
