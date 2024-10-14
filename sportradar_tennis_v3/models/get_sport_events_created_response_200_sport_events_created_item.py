import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSportEventsCreatedResponse200SportEventsCreatedItem")


@_attrs_define
class GetSportEventsCreatedResponse200SportEventsCreatedItem:
    """
    Attributes:
        active_season (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
    """

    active_season: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_season = self.active_season

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_season is not UNSET:
            field_dict["active_season"] = active_season
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active_season = d.pop("active_season", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        get_sport_events_created_response_200_sport_events_created_item = cls(
            active_season=active_season,
            created_at=created_at,
            id=id,
        )

        get_sport_events_created_response_200_sport_events_created_item.additional_properties = d
        return get_sport_events_created_response_200_sport_events_created_item

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
