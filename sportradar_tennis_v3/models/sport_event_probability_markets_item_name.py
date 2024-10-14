from enum import Enum


class SportEventProbabilityMarketsItemName(str, Enum):
    VALUE_0 = "2way"
    VALUE_1 = "3way"

    def __str__(self) -> str:
        return str(self.value)
