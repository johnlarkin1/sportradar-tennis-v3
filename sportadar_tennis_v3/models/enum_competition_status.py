from enum import Enum


class EnumCompetitionStatus(str, Enum):
    CANCELLED = "cancelled"
    CLOSED = "closed"
    COMPLETED = "completed"
    DELAYED = "delayed"
    IN_PROGRESS = "in_progress"
    POSTPONED = "postponed"
    RESCHEDULED = "rescheduled"
    SCHEDULED = "scheduled"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
