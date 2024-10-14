from enum import Enum


class GetScheduleSummariesResponse200SummariesItemSportEventChildrenItemCompetitorsItemPlayersItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
