from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummarySportEventSportEventContextGroupsItem")


@_attrs_define
class SummarySportEventSportEventContextGroupsItem:
    """
    Attributes:
        group_name (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    group_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name

        id = self.id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_name = d.pop("group_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        summary_sport_event_sport_event_context_groups_item = cls(
            group_name=group_name,
            id=id,
            name=name,
        )

        return summary_sport_event_sport_event_context_groups_item
