from enum import Enum


class GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItemPlayersItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
