from enum import Enum


class GetScheduleLiveSummariesResponse200SummariesItemSportEventChildrenItemCompetitorsItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
