import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sport_event_timeline_delta_timeline_item_competitor import SportEventTimelineDeltaTimelineItemCompetitor
from ..models.sport_event_timeline_delta_timeline_item_reason import SportEventTimelineDeltaTimelineItemReason
from ..models.sport_event_timeline_delta_timeline_item_result import SportEventTimelineDeltaTimelineItemResult
from ..models.sport_event_timeline_delta_timeline_item_server import SportEventTimelineDeltaTimelineItemServer
from ..models.sport_event_timeline_delta_timeline_item_type import SportEventTimelineDeltaTimelineItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SportEventTimelineDeltaTimelineItem")


@_attrs_define
class SportEventTimelineDeltaTimelineItem:
    """
    Attributes:
        id (int):
        time (datetime.datetime):
        type (SportEventTimelineDeltaTimelineItemType):
        away_score (Union[Unset, int]):
        competitor (Union[Unset, SportEventTimelineDeltaTimelineItemCompetitor]):
        first_serve_fault (Union[Unset, bool]):
        home_score (Union[Unset, int]):
        period (Union[Unset, str]): Period number.
        period_name (Union[Unset, str]):
        reason (Union[Unset, SportEventTimelineDeltaTimelineItemReason]):
        result (Union[Unset, SportEventTimelineDeltaTimelineItemResult]):
        server (Union[Unset, SportEventTimelineDeltaTimelineItemServer]):
        updated (Union[Unset, bool]):
        updated_time (Union[Unset, datetime.datetime]):
    """

    id: int
    time: datetime.datetime
    type: SportEventTimelineDeltaTimelineItemType
    away_score: Union[Unset, int] = UNSET
    competitor: Union[Unset, SportEventTimelineDeltaTimelineItemCompetitor] = UNSET
    first_serve_fault: Union[Unset, bool] = UNSET
    home_score: Union[Unset, int] = UNSET
    period: Union[Unset, str] = UNSET
    period_name: Union[Unset, str] = UNSET
    reason: Union[Unset, SportEventTimelineDeltaTimelineItemReason] = UNSET
    result: Union[Unset, SportEventTimelineDeltaTimelineItemResult] = UNSET
    server: Union[Unset, SportEventTimelineDeltaTimelineItemServer] = UNSET
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

        type = SportEventTimelineDeltaTimelineItemType(d.pop("type"))

        away_score = d.pop("away_score", UNSET)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, SportEventTimelineDeltaTimelineItemCompetitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = SportEventTimelineDeltaTimelineItemCompetitor(_competitor)

        first_serve_fault = d.pop("first_serve_fault", UNSET)

        home_score = d.pop("home_score", UNSET)

        period = d.pop("period", UNSET)

        period_name = d.pop("period_name", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, SportEventTimelineDeltaTimelineItemReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = SportEventTimelineDeltaTimelineItemReason(_reason)

        _result = d.pop("result", UNSET)
        result: Union[Unset, SportEventTimelineDeltaTimelineItemResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = SportEventTimelineDeltaTimelineItemResult(_result)

        _server = d.pop("server", UNSET)
        server: Union[Unset, SportEventTimelineDeltaTimelineItemServer]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = SportEventTimelineDeltaTimelineItemServer(_server)

        updated = d.pop("updated", UNSET)

        _updated_time = d.pop("updated_time", UNSET)
        updated_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        sport_event_timeline_delta_timeline_item = cls(
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

        return sport_event_timeline_delta_timeline_item
