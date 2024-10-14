import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_events_created_response_200_sport_events_created_item import (
        GetSportEventsCreatedResponse200SportEventsCreatedItem,
    )


T = TypeVar("T", bound="GetSportEventsCreatedResponse200")


@_attrs_define
class GetSportEventsCreatedResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_events_created (Union[Unset, List['GetSportEventsCreatedResponse200SportEventsCreatedItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_events_created: Union[Unset, List["GetSportEventsCreatedResponse200SportEventsCreatedItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_events_created: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_events_created, Unset):
            sport_events_created = []
            for sport_events_created_item_data in self.sport_events_created:
                sport_events_created_item = sport_events_created_item_data.to_dict()
                sport_events_created.append(sport_events_created_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_events_created is not UNSET:
            field_dict["sport_events_created"] = sport_events_created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_events_created_response_200_sport_events_created_item import (
            GetSportEventsCreatedResponse200SportEventsCreatedItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        sport_events_created = []
        _sport_events_created = d.pop("sport_events_created", UNSET)
        for sport_events_created_item_data in _sport_events_created or []:
            sport_events_created_item = GetSportEventsCreatedResponse200SportEventsCreatedItem.from_dict(
                sport_events_created_item_data
            )

            sport_events_created.append(sport_events_created_item)

        get_sport_events_created_response_200 = cls(
            generated_at=generated_at,
            sport_events_created=sport_events_created,
        )

        return get_sport_events_created_response_200
