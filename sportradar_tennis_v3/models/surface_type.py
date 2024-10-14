from enum import Enum


class SurfaceType(str, Enum):
    CARPET_INDOOR = "carpet_indoor"
    GRASS = "grass"
    GREEN_CLAY = "green_clay"
    HARDCOURT_INDOOR = "hardcourt_indoor"
    HARDCOURT_OUTDOOR = "hardcourt_outdoor"
    HARD_COURT = "hard_court"
    RED_CLAY = "red_clay"
    RED_CLAY_INDOOR = "red_clay_indoor"
    SYNTHETIC_GRASS = "synthetic_grass"
    SYNTHETIC_INDOOR = "synthetic_indoor"
    SYNTHETIC_OUTDOOR = "synthetic_outdoor"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
