from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_statistics_periods_item_competitors_item import SummaryStatisticsPeriodsItemCompetitorsItem


T = TypeVar("T", bound="SummaryStatisticsPeriodsItem")


@_attrs_define
class SummaryStatisticsPeriodsItem:
    """
    Attributes:
        competitors (Union[Unset, List['SummaryStatisticsPeriodsItemCompetitorsItem']]):
        number (Union[Unset, int]):
    """

    competitors: Union[Unset, List["SummaryStatisticsPeriodsItemCompetitorsItem"]] = UNSET
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
        from ..models.summary_statistics_periods_item_competitors_item import (
            SummaryStatisticsPeriodsItemCompetitorsItem,
        )

        d = src_dict.copy()
        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = SummaryStatisticsPeriodsItemCompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        number = d.pop("number", UNSET)

        summary_statistics_periods_item = cls(
            competitors=competitors,
            number=number,
        )

        return summary_statistics_periods_item
