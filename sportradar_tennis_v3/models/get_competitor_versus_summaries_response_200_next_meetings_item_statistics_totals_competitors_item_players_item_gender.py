from enum import Enum


class GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotalsCompetitorsItemPlayersItemGender(
    str, Enum
):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
