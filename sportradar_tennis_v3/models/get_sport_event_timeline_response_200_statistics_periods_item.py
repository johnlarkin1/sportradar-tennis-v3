from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_event_timeline_response_200_statistics_periods_item_competitors_item import (
        GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItem,
    )


T = TypeVar("T", bound="GetSportEventTimelineResponse200StatisticsPeriodsItem")


@_attrs_define
class GetSportEventTimelineResponse200StatisticsPeriodsItem:
    """
    Attributes:
        competitors (Union[Unset, List['GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItem']]):
        number (Union[Unset, int]):
    """

    competitors: Union[Unset, List["GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItem"]] = UNSET
    number: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_event_timeline_response_200_statistics_periods_item_competitors_item import (
            GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItem,
        )

        d = src_dict.copy()
        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = GetSportEventTimelineResponse200StatisticsPeriodsItemCompetitorsItem.from_dict(
                competitors_item_data
            )

            competitors.append(competitors_item)

        number = d.pop("number", UNSET)

        get_sport_event_timeline_response_200_statistics_periods_item = cls(
            competitors=competitors,
            number=number,
        )

        return get_sport_event_timeline_response_200_statistics_periods_item
