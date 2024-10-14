from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_summaries_response_200_summaries_item_sport_event import (
        GetSeasonSummariesResponse200SummariesItemSportEvent,
    )
    from ..models.get_season_summaries_response_200_summaries_item_sport_event_status import (
        GetSeasonSummariesResponse200SummariesItemSportEventStatus,
    )
    from ..models.get_season_summaries_response_200_summaries_item_statistics import (
        GetSeasonSummariesResponse200SummariesItemStatistics,
    )


T = TypeVar("T", bound="GetSeasonSummariesResponse200SummariesItem")


@_attrs_define
class GetSeasonSummariesResponse200SummariesItem:
    """
    Attributes:
        sport_event (GetSeasonSummariesResponse200SummariesItemSportEvent):
        sport_event_status (GetSeasonSummariesResponse200SummariesItemSportEventStatus):
        statistics (Union[Unset, GetSeasonSummariesResponse200SummariesItemStatistics]):
    """

    sport_event: "GetSeasonSummariesResponse200SummariesItemSportEvent"
    sport_event_status: "GetSeasonSummariesResponse200SummariesItemSportEventStatus"
    statistics: Union[Unset, "GetSeasonSummariesResponse200SummariesItemStatistics"] = UNSET

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
        from ..models.get_season_summaries_response_200_summaries_item_sport_event import (
            GetSeasonSummariesResponse200SummariesItemSportEvent,
        )
        from ..models.get_season_summaries_response_200_summaries_item_sport_event_status import (
            GetSeasonSummariesResponse200SummariesItemSportEventStatus,
        )
        from ..models.get_season_summaries_response_200_summaries_item_statistics import (
            GetSeasonSummariesResponse200SummariesItemStatistics,
        )

        d = src_dict.copy()
        sport_event = GetSeasonSummariesResponse200SummariesItemSportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = GetSeasonSummariesResponse200SummariesItemSportEventStatus.from_dict(
            d.pop("sport_event_status")
        )

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetSeasonSummariesResponse200SummariesItemStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetSeasonSummariesResponse200SummariesItemStatistics.from_dict(_statistics)

        get_season_summaries_response_200_summaries_item = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        return get_season_summaries_response_200_summaries_item
