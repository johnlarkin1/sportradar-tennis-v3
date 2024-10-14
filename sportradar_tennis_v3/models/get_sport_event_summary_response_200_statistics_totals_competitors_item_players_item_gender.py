from enum import Enum


class GetSportEventSummaryResponse200StatisticsTotalsCompetitorsItemPlayersItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
