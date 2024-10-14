from enum import Enum


class GetScheduleLiveSummariesResponse200SummariesItemSportEventStatusGameStateLastPointResult(str, Enum):
    ACE = "ace"
    DOUBLE_FAULT = "double_fault"
    RECEIVER_WINNER = "receiver_winner"
    SERVER_WINNER = "server_winner"

    def __str__(self) -> str:
        return str(self.value)
