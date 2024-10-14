import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_event_timeline_response_200_sport_event import GetSportEventTimelineResponse200SportEvent
    from ..models.get_sport_event_timeline_response_200_sport_event_status import (
        GetSportEventTimelineResponse200SportEventStatus,
    )
    from ..models.get_sport_event_timeline_response_200_statistics import GetSportEventTimelineResponse200Statistics
    from ..models.get_sport_event_timeline_response_200_timeline_item import (
        GetSportEventTimelineResponse200TimelineItem,
    )


T = TypeVar("T", bound="GetSportEventTimelineResponse200")


@_attrs_define
class GetSportEventTimelineResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_event (Union[Unset, GetSportEventTimelineResponse200SportEvent]):
        sport_event_status (Union[Unset, GetSportEventTimelineResponse200SportEventStatus]):
        statistics (Union[Unset, GetSportEventTimelineResponse200Statistics]):
        timeline (Union[Unset, List['GetSportEventTimelineResponse200TimelineItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_event: Union[Unset, "GetSportEventTimelineResponse200SportEvent"] = UNSET
    sport_event_status: Union[Unset, "GetSportEventTimelineResponse200SportEventStatus"] = UNSET
    statistics: Union[Unset, "GetSportEventTimelineResponse200Statistics"] = UNSET
    timeline: Union[Unset, List["GetSportEventTimelineResponse200TimelineItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event, Unset):
            sport_event = self.sport_event.to_dict()

        sport_event_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_status, Unset):
            sport_event_status = self.sport_event_status.to_dict()

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        timeline: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.timeline, Unset):
            timeline = []
            for timeline_item_data in self.timeline:
                timeline_item = timeline_item_data.to_dict()
                timeline.append(timeline_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_event is not UNSET:
            field_dict["sport_event"] = sport_event
        if sport_event_status is not UNSET:
            field_dict["sport_event_status"] = sport_event_status
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if timeline is not UNSET:
            field_dict["timeline"] = timeline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_event_timeline_response_200_sport_event import (
            GetSportEventTimelineResponse200SportEvent,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_status import (
            GetSportEventTimelineResponse200SportEventStatus,
        )
        from ..models.get_sport_event_timeline_response_200_statistics import GetSportEventTimelineResponse200Statistics
        from ..models.get_sport_event_timeline_response_200_timeline_item import (
            GetSportEventTimelineResponse200TimelineItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        _sport_event = d.pop("sport_event", UNSET)
        sport_event: Union[Unset, GetSportEventTimelineResponse200SportEvent]
        if isinstance(_sport_event, Unset):
            sport_event = UNSET
        else:
            sport_event = GetSportEventTimelineResponse200SportEvent.from_dict(_sport_event)

        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, GetSportEventTimelineResponse200SportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = GetSportEventTimelineResponse200SportEventStatus.from_dict(_sport_event_status)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetSportEventTimelineResponse200Statistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetSportEventTimelineResponse200Statistics.from_dict(_statistics)

        timeline = []
        _timeline = d.pop("timeline", UNSET)
        for timeline_item_data in _timeline or []:
            timeline_item = GetSportEventTimelineResponse200TimelineItem.from_dict(timeline_item_data)

            timeline.append(timeline_item)

        get_sport_event_timeline_response_200 = cls(
            generated_at=generated_at,
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            statistics=statistics,
            timeline=timeline,
        )

        get_sport_event_timeline_response_200.additional_properties = d
        return get_sport_event_timeline_response_200

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
