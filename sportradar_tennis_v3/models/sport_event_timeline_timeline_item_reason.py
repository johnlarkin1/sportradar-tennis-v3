from enum import Enum


class SportEventTimelineTimelineItemReason(str, Enum):
    BAD_WEATHER = "bad_weather"
    TOILET_BREAK = "toilet_break"
    TRAINER_CALLED = "trainer_called"

    def __str__(self) -> str:
        return str(self.value)
