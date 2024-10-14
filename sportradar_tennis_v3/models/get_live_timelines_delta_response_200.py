import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item import (
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem,
    )


T = TypeVar("T", bound="GetLiveTimelinesDeltaResponse200")


@_attrs_define
class GetLiveTimelinesDeltaResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_event_timeline_deltas (Union[Unset,
            List['GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_event_timeline_deltas: Union[Unset, List["GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem"]] = (
        UNSET
    )

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_event_timeline_deltas: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_event_timeline_deltas, Unset):
            sport_event_timeline_deltas = []
            for sport_event_timeline_deltas_item_data in self.sport_event_timeline_deltas:
                sport_event_timeline_deltas_item = sport_event_timeline_deltas_item_data.to_dict()
                sport_event_timeline_deltas.append(sport_event_timeline_deltas_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_event_timeline_deltas is not UNSET:
            field_dict["sport_event_timeline_deltas"] = sport_event_timeline_deltas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item import (
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        sport_event_timeline_deltas = []
        _sport_event_timeline_deltas = d.pop("sport_event_timeline_deltas", UNSET)
        for sport_event_timeline_deltas_item_data in _sport_event_timeline_deltas or []:
            sport_event_timeline_deltas_item = GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem.from_dict(
                sport_event_timeline_deltas_item_data
            )

            sport_event_timeline_deltas.append(sport_event_timeline_deltas_item)

        get_live_timelines_delta_response_200 = cls(
            generated_at=generated_at,
            sport_event_timeline_deltas=sport_event_timeline_deltas,
        )

        return get_live_timelines_delta_response_200
