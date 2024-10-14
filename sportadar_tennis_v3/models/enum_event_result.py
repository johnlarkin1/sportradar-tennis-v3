from enum import Enum


class EnumEventResult(str, Enum):
    ACE = "ace"
    DOUBLE_FAULT = "double_fault"
    RECEIVER_WON = "receiver_won"
    SERVER_WON = "server_won"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
