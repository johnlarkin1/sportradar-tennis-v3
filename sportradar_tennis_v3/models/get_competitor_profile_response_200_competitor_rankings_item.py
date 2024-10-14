from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_profile_response_200_competitor_rankings_item_competitor import (
        GetCompetitorProfileResponse200CompetitorRankingsItemCompetitor,
    )


T = TypeVar("T", bound="GetCompetitorProfileResponse200CompetitorRankingsItem")


@_attrs_define
class GetCompetitorProfileResponse200CompetitorRankingsItem:
    """
    Attributes:
        competitions_played (Union[Unset, int]):
        competitor (Union[Unset, GetCompetitorProfileResponse200CompetitorRankingsItemCompetitor]):
        competitor_id (Union[Unset, str]):
        movement (Union[Unset, int]):
        name (Union[Unset, str]):
        points (Union[Unset, int]):
        race_ranking (Union[Unset, bool]):
        rank (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    competitions_played: Union[Unset, int] = UNSET
    competitor: Union[Unset, "GetCompetitorProfileResponse200CompetitorRankingsItemCompetitor"] = UNSET
    competitor_id: Union[Unset, str] = UNSET
    movement: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    points: Union[Unset, int] = UNSET
    race_ranking: Union[Unset, bool] = UNSET
    rank: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitions_played = self.competitions_played

        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        competitor_id = self.competitor_id

        movement = self.movement

        name = self.name

        points = self.points

        race_ranking = self.race_ranking

        rank = self.rank

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitions_played is not UNSET:
            field_dict["competitions_played"] = competitions_played
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if competitor_id is not UNSET:
            field_dict["competitor_id"] = competitor_id
        if movement is not UNSET:
            field_dict["movement"] = movement
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if race_ranking is not UNSET:
            field_dict["race_ranking"] = race_ranking
        if rank is not UNSET:
            field_dict["rank"] = rank
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_profile_response_200_competitor_rankings_item_competitor import (
            GetCompetitorProfileResponse200CompetitorRankingsItemCompetitor,
        )

        d = src_dict.copy()
        competitions_played = d.pop("competitions_played", UNSET)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, GetCompetitorProfileResponse200CompetitorRankingsItemCompetitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = GetCompetitorProfileResponse200CompetitorRankingsItemCompetitor.from_dict(_competitor)

        competitor_id = d.pop("competitor_id", UNSET)

        movement = d.pop("movement", UNSET)

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        race_ranking = d.pop("race_ranking", UNSET)

        rank = d.pop("rank", UNSET)

        type = d.pop("type", UNSET)

        get_competitor_profile_response_200_competitor_rankings_item = cls(
            competitions_played=competitions_played,
            competitor=competitor,
            competitor_id=competitor_id,
            movement=movement,
            name=name,
            points=points,
            race_ranking=race_ranking,
            rank=rank,
            type=type,
        )

        return get_competitor_profile_response_200_competitor_rankings_item
