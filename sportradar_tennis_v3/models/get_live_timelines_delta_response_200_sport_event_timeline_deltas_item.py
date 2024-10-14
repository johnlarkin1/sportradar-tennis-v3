from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline import (
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimeline,
    )


T = TypeVar("T", bound="GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem")


@_attrs_define
class GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItem:
    """
    Attributes:
        sport_event_timeline (Union[Unset,
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimeline]):
    """

    sport_event_timeline: Union[
        Unset, "GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimeline"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sport_event_timeline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_timeline, Unset):
            sport_event_timeline = self.sport_event_timeline.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sport_event_timeline is not UNSET:
            field_dict["sport_event_timeline"] = sport_event_timeline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline import (
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimeline,
        )

        d = src_dict.copy()
        _sport_event_timeline = d.pop("sport_event_timeline", UNSET)
        sport_event_timeline: Union[
            Unset, GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimeline
        ]
        if isinstance(_sport_event_timeline, Unset):
            sport_event_timeline = UNSET
        else:
            sport_event_timeline = (
                GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimeline.from_dict(
                    _sport_event_timeline
                )
            )

        get_live_timelines_delta_response_200_sport_event_timeline_deltas_item = cls(
            sport_event_timeline=sport_event_timeline,
        )

        get_live_timelines_delta_response_200_sport_event_timeline_deltas_item.additional_properties = d
        return get_live_timelines_delta_response_200_sport_event_timeline_deltas_item

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
