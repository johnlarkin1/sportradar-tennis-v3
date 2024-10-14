from enum import Enum


class GetStreamStatisticsResponse200Type0PayloadStatisticsItemCompetitorsItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
