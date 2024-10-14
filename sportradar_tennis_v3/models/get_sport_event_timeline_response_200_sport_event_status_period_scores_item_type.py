from enum import Enum


class GetSportEventTimelineResponse200SportEventStatusPeriodScoresItemType(str, Enum):
    INTERRUPTED = "interrupted"
    SET = "set"
    SUSPENDED = "suspended"
    VALUE_1 = "1st_set"
    VALUE_2 = "2nd_set"
    VALUE_3 = "3rd_set"
    VALUE_4 = "4th_set"
    VALUE_5 = "5th_set"

    def __str__(self) -> str:
        return str(self.value)
