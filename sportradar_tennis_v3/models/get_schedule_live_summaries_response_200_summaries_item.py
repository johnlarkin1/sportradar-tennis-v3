from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_schedule_live_summaries_response_200_summaries_item_sport_event import (
        GetScheduleLiveSummariesResponse200SummariesItemSportEvent,
    )
    from ..models.get_schedule_live_summaries_response_200_summaries_item_sport_event_status import (
        GetScheduleLiveSummariesResponse200SummariesItemSportEventStatus,
    )
    from ..models.get_schedule_live_summaries_response_200_summaries_item_statistics import (
        GetScheduleLiveSummariesResponse200SummariesItemStatistics,
    )


T = TypeVar("T", bound="GetScheduleLiveSummariesResponse200SummariesItem")


@_attrs_define
class GetScheduleLiveSummariesResponse200SummariesItem:
    """
    Attributes:
        sport_event (GetScheduleLiveSummariesResponse200SummariesItemSportEvent):
        sport_event_status (GetScheduleLiveSummariesResponse200SummariesItemSportEventStatus):
        statistics (Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemStatistics]):
    """

    sport_event: "GetScheduleLiveSummariesResponse200SummariesItemSportEvent"
    sport_event_status: "GetScheduleLiveSummariesResponse200SummariesItemSportEventStatus"
    statistics: Union[Unset, "GetScheduleLiveSummariesResponse200SummariesItemStatistics"] = UNSET

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
        from ..models.get_schedule_live_summaries_response_200_summaries_item_sport_event import (
            GetScheduleLiveSummariesResponse200SummariesItemSportEvent,
        )
        from ..models.get_schedule_live_summaries_response_200_summaries_item_sport_event_status import (
            GetScheduleLiveSummariesResponse200SummariesItemSportEventStatus,
        )
        from ..models.get_schedule_live_summaries_response_200_summaries_item_statistics import (
            GetScheduleLiveSummariesResponse200SummariesItemStatistics,
        )

        d = src_dict.copy()
        sport_event = GetScheduleLiveSummariesResponse200SummariesItemSportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = GetScheduleLiveSummariesResponse200SummariesItemSportEventStatus.from_dict(
            d.pop("sport_event_status")
        )

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetScheduleLiveSummariesResponse200SummariesItemStatistics.from_dict(_statistics)

        get_schedule_live_summaries_response_200_summaries_item = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        return get_schedule_live_summaries_response_200_summaries_item
