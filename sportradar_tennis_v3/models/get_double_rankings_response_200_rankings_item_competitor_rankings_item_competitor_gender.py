from enum import Enum


class GetDoubleRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
