from enum import Enum


class BaseSummarySportEventSportEventContextModeBestOf(str, Enum):
    VALUE_0 = "3"
    VALUE_1 = "5"

    def __str__(self) -> str:
        return str(self.value)
