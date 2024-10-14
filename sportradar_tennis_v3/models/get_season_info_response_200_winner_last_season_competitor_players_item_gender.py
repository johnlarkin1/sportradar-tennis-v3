from enum import Enum


class GetSeasonInfoResponse200WinnerLastSeasonCompetitorPlayersItemGender(str, Enum):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
