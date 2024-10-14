from enum import Enum


class SportEventSportEventContextRoundName(str, Enum):
    FINAL = "final"
    QUALIFICATION = "qualification"
    QUALIFICATION_FINAL = "qualification_final"
    QUALIFICATION_ROUND_1 = "qualification_round_1"
    QUALIFICATION_ROUND_2 = "qualification_round_2"
    QUARTERFINAL = "quarterfinal"
    ROUND_1 = "round_1"
    ROUND_2 = "round_2"
    ROUND_3 = "round_3"
    ROUND_OF_128 = "round_of_128"
    ROUND_OF_16 = "round_of_16"
    ROUND_OF_256 = "round_of_256"
    ROUND_OF_32 = "round_of_32"
    ROUND_OF_64 = "round_of_64"
    SEMIFINAL = "semifinal"
    VALUE_15 = "3rd_place_playoff"
    VALUE_16 = "3rd_place_final"
    VALUE_17 = "5th_place_final"
    VALUE_18 = "7th_place_final"

    def __str__(self) -> str:
        return str(self.value)
