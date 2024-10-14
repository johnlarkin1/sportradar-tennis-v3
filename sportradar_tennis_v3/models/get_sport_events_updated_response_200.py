import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_events_updated_response_200_sport_events_updated_item import (
        GetSportEventsUpdatedResponse200SportEventsUpdatedItem,
    )


T = TypeVar("T", bound="GetSportEventsUpdatedResponse200")


@_attrs_define
class GetSportEventsUpdatedResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_events_updated (Union[Unset, List['GetSportEventsUpdatedResponse200SportEventsUpdatedItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_events_updated: Union[Unset, List["GetSportEventsUpdatedResponse200SportEventsUpdatedItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_events_updated: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_events_updated, Unset):
            sport_events_updated = []
            for sport_events_updated_item_data in self.sport_events_updated:
                sport_events_updated_item = sport_events_updated_item_data.to_dict()
                sport_events_updated.append(sport_events_updated_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_events_updated is not UNSET:
            field_dict["sport_events_updated"] = sport_events_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_events_updated_response_200_sport_events_updated_item import (
            GetSportEventsUpdatedResponse200SportEventsUpdatedItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        sport_events_updated = []
        _sport_events_updated = d.pop("sport_events_updated", UNSET)
        for sport_events_updated_item_data in _sport_events_updated or []:
            sport_events_updated_item = GetSportEventsUpdatedResponse200SportEventsUpdatedItem.from_dict(
                sport_events_updated_item_data
            )

            sport_events_updated.append(sport_events_updated_item)

        get_sport_events_updated_response_200 = cls(
            generated_at=generated_at,
            sport_events_updated=sport_events_updated,
        )

        return get_sport_events_updated_response_200
