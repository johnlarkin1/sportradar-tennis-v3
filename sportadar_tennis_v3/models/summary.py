from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_event import SportEvent
    from ..models.sport_event_statistics import SportEventStatistics
    from ..models.sport_event_status import SportEventStatus


T = TypeVar("T", bound="Summary")


@_attrs_define
class Summary:
    """
    Attributes:
        sport_event (SportEvent):
        sport_event_status (SportEventStatus):
        statistics (Union[Unset, SportEventStatistics]):
    """

    sport_event: "SportEvent"
    sport_event_status: "SportEventStatus"
    statistics: Union[Unset, "SportEventStatistics"] = UNSET

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
        from ..models.sport_event import SportEvent
        from ..models.sport_event_statistics import SportEventStatistics
        from ..models.sport_event_status import SportEventStatus

        d = src_dict.copy()
        sport_event = SportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = SportEventStatus.from_dict(d.pop("sport_event_status"))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SportEventStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SportEventStatistics.from_dict(_statistics)

        summary = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        return summary
