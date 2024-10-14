from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_event_competitor_statistics_statistics import SportEventCompetitorStatisticsStatistics


T = TypeVar("T", bound="SportEventCompetitorStatistics")


@_attrs_define
class SportEventCompetitorStatistics:
    """
    Attributes:
        statistics (Union[Unset, SportEventCompetitorStatisticsStatistics]):
    """

    statistics: Union[Unset, "SportEventCompetitorStatisticsStatistics"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sport_event_competitor_statistics_statistics import SportEventCompetitorStatisticsStatistics

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SportEventCompetitorStatisticsStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SportEventCompetitorStatisticsStatistics.from_dict(_statistics)

        sport_event_competitor_statistics = cls(
            statistics=statistics,
        )

        sport_event_competitor_statistics.additional_properties = d
        return sport_event_competitor_statistics

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
