from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_sport_event import SummarySportEvent
    from ..models.summary_sport_event_status import SummarySportEventStatus
    from ..models.summary_statistics import SummaryStatistics


T = TypeVar("T", bound="Summary")


@_attrs_define
class Summary:
    """
    Attributes:
        sport_event (SummarySportEvent):
        sport_event_status (SummarySportEventStatus):
        statistics (Union[Unset, SummaryStatistics]):
    """

    sport_event: "SummarySportEvent"
    sport_event_status: "SummarySportEventStatus"
    statistics: Union[Unset, "SummaryStatistics"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sport_event = self.sport_event.to_dict()

        sport_event_status = self.sport_event_status.to_dict()

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
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summary_sport_event import SummarySportEvent
        from ..models.summary_sport_event_status import SummarySportEventStatus
        from ..models.summary_statistics import SummaryStatistics

        d = src_dict.copy()
        sport_event = SummarySportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = SummarySportEventStatus.from_dict(d.pop("sport_event_status"))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SummaryStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SummaryStatistics.from_dict(_statistics)

        summary = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        return summary
