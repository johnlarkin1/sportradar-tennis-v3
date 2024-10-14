from enum import Enum


class GetCompetitorSummariesResponse200SummariesItemStatisticsPeriodsItemCompetitorsItemPlayersItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
