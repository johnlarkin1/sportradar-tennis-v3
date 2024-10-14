from enum import Enum


class GetSeasonStandingsResponse200StandingsItemGroupsItemStageType(str, Enum):
    CUP = "cup"
    LEAGUE = "league"

    def __str__(self) -> str:
        return str(self.value)
