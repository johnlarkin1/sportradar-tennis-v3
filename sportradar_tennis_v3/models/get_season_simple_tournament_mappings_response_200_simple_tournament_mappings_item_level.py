from enum import Enum


class GetSeasonSimpleTournamentMappingsResponse200SimpleTournamentMappingsItemLevel(str, Enum):
    ATP_1000 = "atp_1000"
    ATP_250 = "atp_250"
    ATP_500 = "atp_500"
    ATP_NEXT_GENERATION = "atp_next_generation"
    ATP_WORLD_TOUR_FINALS = "atp_world_tour_finals"
    GRAND_SLAM = "grand_slam"
    WTA_1000 = "wta_1000"
    WTA_125 = "wta_125"
    WTA_250 = "wta_250"
    WTA_500 = "wta_500"
    WTA_CHAMPIONSHIPS = "wta_championships"
    WTA_ELITE_TROPHY = "wta_elite_trophy"
    WTA_INTERNATIONAL = "wta_international"
    WTA_MASTER = "wta_master"
    WTA_PREMIER = "wta_premier"

    def __str__(self) -> str:
        return str(self.value)
