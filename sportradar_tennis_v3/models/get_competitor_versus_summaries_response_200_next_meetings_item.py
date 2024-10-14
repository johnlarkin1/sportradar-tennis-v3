from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_sport_event import (
        GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEvent,
    )
    from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_sport_event_status import (
        GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatus,
    )
    from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_statistics import (
        GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics,
    )


T = TypeVar("T", bound="GetCompetitorVersusSummariesResponse200NextMeetingsItem")


@_attrs_define
class GetCompetitorVersusSummariesResponse200NextMeetingsItem:
    """
    Attributes:
        sport_event (GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEvent):
        sport_event_status (GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatus):
        statistics (Union[Unset, GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics]):
    """

    sport_event: "GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEvent"
    sport_event_status: "GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatus"
    statistics: Union[Unset, "GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics"] = UNSET

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
        from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_sport_event import (
            GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEvent,
        )
        from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_sport_event_status import (
            GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatus,
        )
        from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_statistics import (
            GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics,
        )

        d = src_dict.copy()
        sport_event = GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = GetCompetitorVersusSummariesResponse200NextMeetingsItemSportEventStatus.from_dict(
            d.pop("sport_event_status")
        )

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics.from_dict(_statistics)

        get_competitor_versus_summaries_response_200_next_meetings_item = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        return get_competitor_versus_summaries_response_200_next_meetings_item
