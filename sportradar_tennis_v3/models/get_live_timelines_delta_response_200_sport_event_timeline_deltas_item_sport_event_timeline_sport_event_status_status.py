from enum import Enum


class GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusStatus(str, Enum):
    CANCELLED = "cancelled"
    CLOSED = "closed"
    DELAYED = "delayed"
    ENDED = "ended"
    INTERRUPTED = "interrupted"
    LIVE = "live"
    NOT_STARTED = "not_started"
    POSTPONED = "postponed"
    STARTED = "started"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
