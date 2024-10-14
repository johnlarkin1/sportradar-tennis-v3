from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSportEventsRemovedResponse200SportEventsRemovedItem")


@_attrs_define
class GetSportEventsRemovedResponse200SportEventsRemovedItem:
    """
    Attributes:
        id (Union[Unset, str]):
        replaced_by (Union[Unset, str]): Sport Event URN (sr:sport_event:x)
    """

    id: Union[Unset, str] = UNSET
    replaced_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        replaced_by = self.replaced_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if replaced_by is not UNSET:
            field_dict["replaced_by"] = replaced_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        replaced_by = d.pop("replaced_by", UNSET)

        get_sport_events_removed_response_200_sport_events_removed_item = cls(
            id=id,
            replaced_by=replaced_by,
        )

        get_sport_events_removed_response_200_sport_events_removed_item.additional_properties = d
        return get_sport_events_removed_response_200_sport_events_removed_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
