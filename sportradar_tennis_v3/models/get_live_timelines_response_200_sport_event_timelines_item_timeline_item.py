import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item_competitor import (
    GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemCompetitor,
)
from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item_reason import (
    GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemReason,
)
from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item_result import (
    GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemResult,
)
from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item_server import (
    GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemServer,
)
from ..models.get_live_timelines_response_200_sport_event_timelines_item_timeline_item_type import (
    GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem")


@_attrs_define
class GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItem:
    """
    Attributes:
        id (int):
        time (datetime.datetime):
        type (GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemType):
        away_score (Union[Unset, int]):
        competitor (Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemCompetitor]):
        first_serve_fault (Union[Unset, bool]):
        home_score (Union[Unset, int]):
        period (Union[Unset, str]): Period number.
        period_name (Union[Unset, str]):
        reason (Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemReason]):
        result (Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemResult]):
        server (Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemServer]):
        updated (Union[Unset, bool]):
        updated_time (Union[Unset, datetime.datetime]):
    """

    id: int
    time: datetime.datetime
    type: GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemType
    away_score: Union[Unset, int] = UNSET
    competitor: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemCompetitor] = UNSET
    first_serve_fault: Union[Unset, bool] = UNSET
    home_score: Union[Unset, int] = UNSET
    period: Union[Unset, str] = UNSET
    period_name: Union[Unset, str] = UNSET
    reason: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemReason] = UNSET
    result: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemResult] = UNSET
    server: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemServer] = UNSET
    updated: Union[Unset, bool] = UNSET
    updated_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        time = self.time.isoformat()

        type = self.type.value

        away_score = self.away_score

        competitor: Union[Unset, str] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.value

        first_serve_fault = self.first_serve_fault

        home_score = self.home_score

        period = self.period

        period_name = self.period_name

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        server: Union[Unset, str] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.value

        updated = self.updated

        updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "time": time,
                "type": type,
            }
        )
        if away_score is not UNSET:
            field_dict["away_score"] = away_score
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if first_serve_fault is not UNSET:
            field_dict["first_serve_fault"] = first_serve_fault
        if home_score is not UNSET:
            field_dict["home_score"] = home_score
        if period is not UNSET:
            field_dict["period"] = period
        if period_name is not UNSET:
            field_dict["period_name"] = period_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if result is not UNSET:
            field_dict["result"] = result
        if server is not UNSET:
            field_dict["server"] = server
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_time is not UNSET:
            field_dict["updated_time"] = updated_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        time = isoparse(d.pop("time"))

        type = GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemType(d.pop("type"))

        away_score = d.pop("away_score", UNSET)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemCompetitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemCompetitor(_competitor)

        first_serve_fault = d.pop("first_serve_fault", UNSET)

        home_score = d.pop("home_score", UNSET)

        period = d.pop("period", UNSET)

        period_name = d.pop("period_name", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemReason(_reason)

        _result = d.pop("result", UNSET)
        result: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemResult(_result)

        _server = d.pop("server", UNSET)
        server: Union[Unset, GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemServer]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = GetLiveTimelinesResponse200SportEventTimelinesItemTimelineItemServer(_server)

        updated = d.pop("updated", UNSET)

        _updated_time = d.pop("updated_time", UNSET)
        updated_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        get_live_timelines_response_200_sport_event_timelines_item_timeline_item = cls(
            id=id,
            time=time,
            type=type,
            away_score=away_score,
            competitor=competitor,
            first_serve_fault=first_serve_fault,
            home_score=home_score,
            period=period,
            period_name=period_name,
            reason=reason,
            result=result,
            server=server,
            updated=updated,
            updated_time=updated_time,
        )

        return get_live_timelines_response_200_sport_event_timelines_item_timeline_item
