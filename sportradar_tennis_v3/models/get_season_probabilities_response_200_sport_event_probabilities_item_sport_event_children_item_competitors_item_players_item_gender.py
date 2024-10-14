from enum import Enum


class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventChildrenItemCompetitorsItemPlayersItemGender(
    str, Enum
):
    FEMALE = "female"
    MALE = "male"

    def __str__(self) -> str:
        return str(self.value)
