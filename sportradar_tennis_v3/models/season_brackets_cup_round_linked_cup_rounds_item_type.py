from enum import Enum


class SeasonBracketsCupRoundLinkedCupRoundsItemType(str, Enum):
    CHILD = "child"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
