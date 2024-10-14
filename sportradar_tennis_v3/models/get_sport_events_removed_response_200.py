import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_events_removed_response_200_sport_events_removed_item import (
        GetSportEventsRemovedResponse200SportEventsRemovedItem,
    )


T = TypeVar("T", bound="GetSportEventsRemovedResponse200")


@_attrs_define
class GetSportEventsRemovedResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_events_removed (Union[Unset, List['GetSportEventsRemovedResponse200SportEventsRemovedItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_events_removed: Union[Unset, List["GetSportEventsRemovedResponse200SportEventsRemovedItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_events_removed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_events_removed, Unset):
            sport_events_removed = []
            for sport_events_removed_item_data in self.sport_events_removed:
                sport_events_removed_item = sport_events_removed_item_data.to_dict()
                sport_events_removed.append(sport_events_removed_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_events_removed is not UNSET:
            field_dict["sport_events_removed"] = sport_events_removed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_events_removed_response_200_sport_events_removed_item import (
            GetSportEventsRemovedResponse200SportEventsRemovedItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        sport_events_removed = []
        _sport_events_removed = d.pop("sport_events_removed", UNSET)
        for sport_events_removed_item_data in _sport_events_removed or []:
            sport_events_removed_item = GetSportEventsRemovedResponse200SportEventsRemovedItem.from_dict(
                sport_events_removed_item_data
            )

            sport_events_removed.append(sport_events_removed_item)

        get_sport_events_removed_response_200 = cls(
            generated_at=generated_at,
            sport_events_removed=sport_events_removed,
        )

        return get_sport_events_removed_response_200
