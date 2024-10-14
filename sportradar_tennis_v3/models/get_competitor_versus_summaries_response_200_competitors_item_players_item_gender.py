from enum import Enum


class GetCompetitorVersusSummariesResponse200CompetitorsItemPlayersItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
