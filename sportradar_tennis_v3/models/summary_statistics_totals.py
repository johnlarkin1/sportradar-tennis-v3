from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_statistics_totals_competitors_item import SummaryStatisticsTotalsCompetitorsItem


T = TypeVar("T", bound="SummaryStatisticsTotals")


@_attrs_define
class SummaryStatisticsTotals:
    """
    Attributes:
        competitors (Union[Unset, List['SummaryStatisticsTotalsCompetitorsItem']]):
    """

    competitors: Union[Unset, List["SummaryStatisticsTotalsCompetitorsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitors is not UNSET:
            field_dict["competitors"] = competitors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.summary_statistics_totals_competitors_item import SummaryStatisticsTotalsCompetitorsItem

        d = src_dict.copy()
        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = SummaryStatisticsTotalsCompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        summary_statistics_totals = cls(
            competitors=competitors,
        )

        return summary_statistics_totals
