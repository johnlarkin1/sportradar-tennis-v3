from enum import Enum


class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemName(str, Enum):
    VALUE_0 = "2way"
    VALUE_1 = "3way"

    def __str__(self) -> str:
        return str(self.value)
