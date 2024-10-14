from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics")


@_attrs_define
class GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics:
    """
    Attributes:
        competitions_played (Union[Unset, int]):
        competitions_won (Union[Unset, int]):
        matches_played (Union[Unset, int]):
        matches_won (Union[Unset, int]):
    """

    competitions_played: Union[Unset, int] = UNSET
    competitions_won: Union[Unset, int] = UNSET
    matches_played: Union[Unset, int] = UNSET
    matches_won: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitions_played = self.competitions_played

        competitions_won = self.competitions_won

        matches_played = self.matches_played

        matches_won = self.matches_won

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitions_played is not UNSET:
            field_dict["competitions_played"] = competitions_played
        if competitions_won is not UNSET:
            field_dict["competitions_won"] = competitions_won
        if matches_played is not UNSET:
            field_dict["matches_played"] = matches_played
        if matches_won is not UNSET:
            field_dict["matches_won"] = matches_won

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        competitions_played = d.pop("competitions_played", UNSET)

        competitions_won = d.pop("competitions_won", UNSET)

        matches_played = d.pop("matches_played", UNSET)

        matches_won = d.pop("matches_won", UNSET)

        get_competitor_profile_response_200_periods_item_surfaces_item_statistics = cls(
            competitions_played=competitions_played,
            competitions_won=competitions_won,
            matches_played=matches_played,
            matches_won=matches_won,
        )

        return get_competitor_profile_response_200_periods_item_surfaces_item_statistics
