from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeasonStandingsResponse200StandingsItemGroupsItemStandingsItemCommentsItem")


@_attrs_define
class GetSeasonStandingsResponse200StandingsItemGroupsItemStandingsItemCommentsItem:
    """
    Attributes:
        text (Union[Unset, str]):  Example: 1 point deducted due to decision by FA.
    """

    text: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        get_season_standings_response_200_standings_item_groups_item_standings_item_comments_item = cls(
            text=text,
        )

        return get_season_standings_response_200_standings_item_groups_item_standings_item_comments_item
