from enum import Enum


class StandingType(str, Enum):
    AWAY = "away"
    FIRST_HALF_AWAY = "first_half_away"
    FIRST_HALF_HOME = "first_half_home"
    FIRST_HALF_TOTAL = "first_half_total"
    HOME = "home"
    SECOND_HALF_AWAY = "second_half_away"
    SECOND_HALF_HOME = "second_half_home"
    SECOND_HALF_TOTAL = "second_half_total"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
