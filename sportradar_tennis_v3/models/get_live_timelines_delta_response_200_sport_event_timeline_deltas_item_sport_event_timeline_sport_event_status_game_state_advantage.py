from enum import Enum


class GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateAdvantage(
    str, Enum
):
    AWAY = "away"
    HOME = "home"

    def __str__(self) -> str:
        return str(self.value)
