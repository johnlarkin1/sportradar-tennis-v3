from enum import Enum


class GetCompetitorProfileResponse200CompetitorRankingsItemCompetitorGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
