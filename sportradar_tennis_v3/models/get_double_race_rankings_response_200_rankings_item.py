from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_double_race_rankings_response_200_rankings_item_gender import (
    GetDoubleRaceRankingsResponse200RankingsItemGender,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_double_race_rankings_response_200_rankings_item_competitor_rankings_item import (
        GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItem,
    )


T = TypeVar("T", bound="GetDoubleRaceRankingsResponse200RankingsItem")


@_attrs_define
class GetDoubleRaceRankingsResponse200RankingsItem:
    """
    Attributes:
        competitor_rankings (Union[Unset, List['GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItem']]):
        gender (Union[Unset, GetDoubleRaceRankingsResponse200RankingsItemGender]):
        name (Union[Unset, str]):
        type_id (Union[Unset, int]):
        week (Union[Unset, int]):
        year (Union[Unset, int]):
    """

    competitor_rankings: Union[Unset, List["GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItem"]] = (
        UNSET
    )
    gender: Union[Unset, GetDoubleRaceRankingsResponse200RankingsItemGender] = UNSET
    name: Union[Unset, str] = UNSET
    type_id: Union[Unset, int] = UNSET
    week: Union[Unset, int] = UNSET
    year: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitor_rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitor_rankings, Unset):
            competitor_rankings = []
            for competitor_rankings_item_data in self.competitor_rankings:
                competitor_rankings_item = competitor_rankings_item_data.to_dict()
                competitor_rankings.append(competitor_rankings_item)

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        name = self.name

        type_id = self.type_id

        week = self.week

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitor_rankings is not UNSET:
            field_dict["competitor_rankings"] = competitor_rankings
        if gender is not UNSET:
            field_dict["gender"] = gender
        if name is not UNSET:
            field_dict["name"] = name
        if type_id is not UNSET:
            field_dict["type_id"] = type_id
        if week is not UNSET:
            field_dict["week"] = week
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_double_race_rankings_response_200_rankings_item_competitor_rankings_item import (
            GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItem,
        )

        d = src_dict.copy()
        competitor_rankings = []
        _competitor_rankings = d.pop("competitor_rankings", UNSET)
        for competitor_rankings_item_data in _competitor_rankings or []:
            competitor_rankings_item = GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItem.from_dict(
                competitor_rankings_item_data
            )

            competitor_rankings.append(competitor_rankings_item)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, GetDoubleRaceRankingsResponse200RankingsItemGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = GetDoubleRaceRankingsResponse200RankingsItemGender(_gender)

        name = d.pop("name", UNSET)

        type_id = d.pop("type_id", UNSET)

        week = d.pop("week", UNSET)

        year = d.pop("year", UNSET)

        get_double_race_rankings_response_200_rankings_item = cls(
            competitor_rankings=competitor_rankings,
            gender=gender,
            name=name,
            type_id=type_id,
            week=week,
            year=year,
        )

        return get_double_race_rankings_response_200_rankings_item
