from enum import Enum


class GetStreamEventsEventIdItem(str, Enum):
    BALL_POSITION = "ball_position"
    DECIDING_TEAM = "deciding_team"
    FIRST_SERVE = "first_serve"
    MATCH_CALLED = "match_called"
    MATCH_ENDED = "match_ended"
    MATCH_RESUMED = "match_resumed"
    MATCH_STARTED = "match_started"
    MATCH_SUSPENDED = "match_suspended"
    PERIOD_SCORE = "period_score"
    PERIOD_START = "period_start"
    POINT = "point"
    SERVICE_FAULT = "service_fault"
    STATS_UPDATE = "stats_update"
    TIE_BREAK_POINTS = "tie_break_points"

    def __str__(self) -> str:
        return str(self.value)
