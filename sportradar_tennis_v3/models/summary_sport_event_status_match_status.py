from enum import Enum


class SummarySportEventStatusMatchStatus(str, Enum):
    ABANDONED = "abandoned"
    CANCELLED = "cancelled"
    DEFAULTED = "defaulted"
    ENDED = "ended"
    INTERRUPTED = "interrupted"
    MATCH_ABOUT_TO_START = "match_about_to_start"
    NOT_STARTED = "not_started"
    POSTPONED = "postponed"
    RETIRED = "retired"
    STARTED = "started"
    START_DELAYED = "start_delayed"
    SUSPENDED = "suspended"
    VALUE_10 = "3rd_set"
    VALUE_11 = "4th_set"
    VALUE_12 = "5th_set"
    VALUE_8 = "1st_set"
    VALUE_9 = "2nd_set"
    WALKOVER = "walkover"

    def __str__(self) -> str:
        return str(self.value)
