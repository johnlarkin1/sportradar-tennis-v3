from enum import Enum


class GetSportEventTimelineResponse200SportEventSportEventContextStagePhase(str, Enum):
    CONFERENCE = "conference"
    DIVISION = "division"
    FINAL_PHASE = "final_phase"
    GRAND_FINALS = "grand_finals"
    GROUP_PHASE_1 = "group_phase_1"
    KNOCKOUT_STAGE = "knockout_stage"
    MAIN_ROUND_1 = "main_round_1"
    MAIN_ROUND_2 = "main_round_2"
    NONE = "none"
    PLACEMENT_MATCHES = "placement_matches"
    PLAYOFFS = "playoffs"
    PROMOTION_PLAYOFFS = "promotion_playoffs"
    QUALIFICATION = "qualification"
    QUALIFICATION_PLAYOFFS = "qualification_playoffs"
    REGULAR_SEASON = "regular season"
    RELEGATION_PLAYOFFS = "relegation_playoffs"
    STAGE_1 = "stage_1"
    STAGE_1_PLAYOFF = "stage_1_playoff"
    STAGE_2 = "stage_2"
    STAGE_2_PLACEMENT_MATCHES = "stage_2_placement_matches"
    VALUE_0 = "1st_part_of_season_1st_leg"

    def __str__(self) -> str:
        return str(self.value)
