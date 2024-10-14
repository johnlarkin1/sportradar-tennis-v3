from enum import Enum


class GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
