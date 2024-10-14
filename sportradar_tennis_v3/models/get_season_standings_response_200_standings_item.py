from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_season_standings_response_200_standings_item_type import (
    GetSeasonStandingsResponse200StandingsItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_standings_response_200_standings_item_groups_item import (
        GetSeasonStandingsResponse200StandingsItemGroupsItem,
    )


T = TypeVar("T", bound="GetSeasonStandingsResponse200StandingsItem")


@_attrs_define
class GetSeasonStandingsResponse200StandingsItem:
    """
    Attributes:
        type (GetSeasonStandingsResponse200StandingsItemType):
        groups (Union[Unset, List['GetSeasonStandingsResponse200StandingsItemGroupsItem']]):
        round_ (Union[Unset, int]):
        tie_break_rule (Union[Unset, str]):
    """

    type: GetSeasonStandingsResponse200StandingsItemType
    groups: Union[Unset, List["GetSeasonStandingsResponse200StandingsItemGroupsItem"]] = UNSET
    round_: Union[Unset, int] = UNSET
    tie_break_rule: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        round_ = self.round_

        tie_break_rule = self.tie_break_rule

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if round_ is not UNSET:
            field_dict["round"] = round_
        if tie_break_rule is not UNSET:
            field_dict["tie_break_rule"] = tie_break_rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_standings_response_200_standings_item_groups_item import (
            GetSeasonStandingsResponse200StandingsItemGroupsItem,
        )

        d = src_dict.copy()
        type = GetSeasonStandingsResponse200StandingsItemType(d.pop("type"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GetSeasonStandingsResponse200StandingsItemGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        round_ = d.pop("round", UNSET)

        tie_break_rule = d.pop("tie_break_rule", UNSET)

        get_season_standings_response_200_standings_item = cls(
            type=type,
            groups=groups,
            round_=round_,
            tie_break_rule=tie_break_rule,
        )

        return get_season_standings_response_200_standings_item
