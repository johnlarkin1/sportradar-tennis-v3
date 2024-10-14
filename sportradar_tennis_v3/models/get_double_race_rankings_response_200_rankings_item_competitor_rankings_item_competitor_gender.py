from enum import Enum


class GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
