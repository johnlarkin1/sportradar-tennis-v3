import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_timelines_response_200_sport_event_timelines_item_sport_event_status import (
        GetLiveTimelinesResponse200SportEventTimelinesItemSportEventStatus,
    )
    from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item import (
        GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem,
    )


T = TypeVar("T", bound="GetLiveTimelinesResponse200SportEventTimelinesItem")


@_attrs_define
class GetLiveTimelinesResponse200SportEventTimelinesItem:
    """
    Attributes:
        id (Union[Unset, str]): Sport Event URN (sr:sport_event:x)
        sport_event_status (Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemSportEventStatus]):
        start_time (Union[Unset, datetime.datetime]):
        timeline (Union[Unset, List['GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem']]):
    """

    id: Union[Unset, str] = UNSET
    sport_event_status: Union[Unset, "GetLiveTimelinesResponse200SportEventTimelinesItemSportEventStatus"] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    timeline: Union[Unset, List["GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        sport_event_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_status, Unset):
            sport_event_status = self.sport_event_status.to_dict()

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        timeline: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.timeline, Unset):
            timeline = []
            for timeline_item_data in self.timeline:
                timeline_item = timeline_item_data.to_dict()
                timeline.append(timeline_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sport_event_status is not UNSET:
            field_dict["sport_event_status"] = sport_event_status
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if timeline is not UNSET:
            field_dict["timeline"] = timeline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_live_timelines_response_200_sport_event_timelines_item_sport_event_status import (
            GetLiveTimelinesResponse200SportEventTimelinesItemSportEventStatus,
        )
        from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item import (
            GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemSportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = GetLiveTimelinesResponse200SportEventTimelinesItemSportEventStatus.from_dict(
                _sport_event_status
            )

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        timeline = []
        _timeline = d.pop("timeline", UNSET)
        for timeline_item_data in _timeline or []:
            timeline_item = GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem.from_dict(timeline_item_data)

            timeline.append(timeline_item)

        get_live_timelines_response_200_sport_event_timelines_item = cls(
            id=id,
            sport_event_status=sport_event_status,
            start_time=start_time,
            timeline=timeline,
        )

        return get_live_timelines_response_200_sport_event_timelines_item
