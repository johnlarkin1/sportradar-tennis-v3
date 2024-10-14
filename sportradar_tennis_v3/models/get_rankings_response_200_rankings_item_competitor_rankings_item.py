from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_rankings_response_200_rankings_item_competitor_rankings_item_competitor import (
        GetRankingsResponse200RankingsItemCompetitorRankingsItemCompetitor,
    )


T = TypeVar("T", bound="GetRankingsResponse200RankingsItemCompetitorRankingsItem")


@_attrs_define
class GetRankingsResponse200RankingsItemCompetitorRankingsItem:
    """
    Attributes:
        competitions_played (Union[Unset, int]):
        competitor (Union[Unset, GetRankingsResponse200RankingsItemCompetitorRankingsItemCompetitor]):
        movement (Union[Unset, int]):
        points (Union[Unset, int]):
        rank (Union[Unset, int]):
    """

    competitions_played: Union[Unset, int] = UNSET
    competitor: Union[Unset, "GetRankingsResponse200RankingsItemCompetitorRankingsItemCompetitor"] = UNSET
    movement: Union[Unset, int] = UNSET
    points: Union[Unset, int] = UNSET
    rank: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitions_played = self.competitions_played

        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        movement = self.movement

        points = self.points

        rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitions_played is not UNSET:
            field_dict["competitions_played"] = competitions_played
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if movement is not UNSET:
            field_dict["movement"] = movement
        if points is not UNSET:
            field_dict["points"] = points
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_rankings_response_200_rankings_item_competitor_rankings_item_competitor import (
            GetRankingsResponse200RankingsItemCompetitorRankingsItemCompetitor,
        )

        d = src_dict.copy()
        competitions_played = d.pop("competitions_played", UNSET)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, GetRankingsResponse200RankingsItemCompetitorRankingsItemCompetitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = GetRankingsResponse200RankingsItemCompetitorRankingsItemCompetitor.from_dict(_competitor)

        movement = d.pop("movement", UNSET)

        points = d.pop("points", UNSET)

        rank = d.pop("rank", UNSET)

        get_rankings_response_200_rankings_item_competitor_rankings_item = cls(
            competitions_played=competitions_played,
            competitor=competitor,
            movement=movement,
            points=points,
            rank=rank,
        )

        return get_rankings_response_200_rankings_item_competitor_rankings_item
