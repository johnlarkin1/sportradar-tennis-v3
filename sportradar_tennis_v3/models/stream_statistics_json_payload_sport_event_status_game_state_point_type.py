from enum import Enum


class StreamStatisticsJsonPayloadSportEventStatusGameStatePointType(str, Enum):
    BREAK = "break"
    GAME = "game"
    MATCH = "match"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
