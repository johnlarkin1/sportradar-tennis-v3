import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_event_summary_response_200_sport_event import GetSportEventSummaryResponse200SportEvent
    from ..models.get_sport_event_summary_response_200_sport_event_status import (
        GetSportEventSummaryResponse200SportEventStatus,
    )
    from ..models.get_sport_event_summary_response_200_statistics import GetSportEventSummaryResponse200Statistics


T = TypeVar("T", bound="GetSportEventSummaryResponse200")


@_attrs_define
class GetSportEventSummaryResponse200:
    """
    Attributes:
        sport_event (GetSportEventSummaryResponse200SportEvent):
        sport_event_status (GetSportEventSummaryResponse200SportEventStatus):
        generated_at (Union[Unset, datetime.datetime]):
        statistics (Union[Unset, GetSportEventSummaryResponse200Statistics]):
    """

    sport_event: "GetSportEventSummaryResponse200SportEvent"
    sport_event_status: "GetSportEventSummaryResponse200SportEventStatus"
    generated_at: Union[Unset, datetime.datetime] = UNSET
    statistics: Union[Unset, "GetSportEventSummaryResponse200Statistics"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sport_event = self.sport_event.to_dict()

        sport_event_status = self.sport_event_status.to_dict()

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sport_event": sport_event,
                "sport_event_status": sport_event_status,
            }
        )
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_event_summary_response_200_sport_event import GetSportEventSummaryResponse200SportEvent
        from ..models.get_sport_event_summary_response_200_sport_event_status import (
            GetSportEventSummaryResponse200SportEventStatus,
        )
        from ..models.get_sport_event_summary_response_200_statistics import GetSportEventSummaryResponse200Statistics

        d = src_dict.copy()
        sport_event = GetSportEventSummaryResponse200SportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = GetSportEventSummaryResponse200SportEventStatus.from_dict(d.pop("sport_event_status"))

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetSportEventSummaryResponse200Statistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetSportEventSummaryResponse200Statistics.from_dict(_statistics)

        get_sport_event_summary_response_200 = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            generated_at=generated_at,
            statistics=statistics,
        )

        return get_sport_event_summary_response_200
