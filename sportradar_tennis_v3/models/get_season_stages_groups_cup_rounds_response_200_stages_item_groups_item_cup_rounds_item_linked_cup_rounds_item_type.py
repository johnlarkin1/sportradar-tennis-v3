from enum import Enum


class GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItemType(str, Enum):
    CHILD = "child"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
