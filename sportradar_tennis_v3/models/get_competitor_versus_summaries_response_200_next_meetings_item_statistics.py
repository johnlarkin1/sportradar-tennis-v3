from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_statistics_periods_item import (
        GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsPeriodsItem,
    )
    from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_statistics_totals import (
        GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotals,
    )


T = TypeVar("T", bound="GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics")


@_attrs_define
class GetCompetitorVersusSummariesResponse200NextMeetingsItemStatistics:
    """
    Attributes:
        periods (Union[Unset, List['GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsPeriodsItem']]):
        totals (Union[Unset, GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotals]):
    """

    periods: Union[Unset, List["GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsPeriodsItem"]] = UNSET
    totals: Union[Unset, "GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotals"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periods is not UNSET:
            field_dict["periods"] = periods
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_statistics_periods_item import (
            GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsPeriodsItem,
        )
        from ..models.get_competitor_versus_summaries_response_200_next_meetings_item_statistics_totals import (
            GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotals,
        )

        d = src_dict.copy()
        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsPeriodsItem.from_dict(
                periods_item_data
            )

            periods.append(periods_item)

        _totals = d.pop("totals", UNSET)
        totals: Union[Unset, GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotals]
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = GetCompetitorVersusSummariesResponse200NextMeetingsItemStatisticsTotals.from_dict(_totals)

        get_competitor_versus_summaries_response_200_next_meetings_item_statistics = cls(
            periods=periods,
            totals=totals,
        )

        get_competitor_versus_summaries_response_200_next_meetings_item_statistics.additional_properties = d
        return get_competitor_versus_summaries_response_200_next_meetings_item_statistics

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
