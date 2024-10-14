from enum import Enum


class ProbabilityOutcomeTwoThreeWayName(str, Enum):
    AWAY_TEAM_NEXT_GOAL = "away_team_next_goal"
    AWAY_TEAM_WINNER = "away_team_winner"
    DRAW = "draw"
    HOME_TEAM_NEXT_GOAL = "home_team_next_goal"
    HOME_TEAM_WINNER = "home_team_winner"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
