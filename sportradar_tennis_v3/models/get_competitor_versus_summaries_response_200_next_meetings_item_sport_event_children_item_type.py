from enum import Enum


class GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventChildrenItemType(str, Enum):
    CHILD = "child"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
