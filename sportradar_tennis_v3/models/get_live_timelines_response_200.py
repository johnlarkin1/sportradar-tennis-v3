import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_timelines_response_200_sport_event_timelines_item import (
        GetLiveTimelinesResponse200SportEventTimelinesItem,
    )


T = TypeVar("T", bound="GetLiveTimelinesResponse200")


@_attrs_define
class GetLiveTimelinesResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_event_timelines (Union[Unset, List['GetLiveTimelinesResponse200SportEventTimelinesItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_event_timelines: Union[Unset, List["GetLiveTimelinesResponse200SportEventTimelinesItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_event_timelines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_event_timelines, Unset):
            sport_event_timelines = []
            for sport_event_timelines_item_data in self.sport_event_timelines:
                sport_event_timelines_item = sport_event_timelines_item_data.to_dict()
                sport_event_timelines.append(sport_event_timelines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_event_timelines is not UNSET:
            field_dict["sport_event_timelines"] = sport_event_timelines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_live_timelines_response_200_sport_event_timelines_item import (
            GetLiveTimelinesResponse200SportEventTimelinesItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        sport_event_timelines = []
        _sport_event_timelines = d.pop("sport_event_timelines", UNSET)
        for sport_event_timelines_item_data in _sport_event_timelines or []:
            sport_event_timelines_item = GetLiveTimelinesResponse200SportEventTimelinesItem.from_dict(
                sport_event_timelines_item_data
            )

            sport_event_timelines.append(sport_event_timelines_item)

        get_live_timelines_response_200 = cls(
            generated_at=generated_at,
            sport_event_timelines=sport_event_timelines,
        )

        return get_live_timelines_response_200
