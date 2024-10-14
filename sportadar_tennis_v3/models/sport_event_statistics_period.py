from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_event_statistics_period_competitors_item import SportEventStatisticsPeriodCompetitorsItem


T = TypeVar("T", bound="SportEventStatisticsPeriod")


@_attrs_define
class SportEventStatisticsPeriod:
    """
    Attributes:
        competitors (Union[Unset, List['SportEventStatisticsPeriodCompetitorsItem']]):
        number (Union[Unset, int]):
    """

    competitors: Union[Unset, List["SportEventStatisticsPeriodCompetitorsItem"]] = UNSET
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
        from ..models.sport_event_statistics_period_competitors_item import SportEventStatisticsPeriodCompetitorsItem

        d = src_dict.copy()
        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = SportEventStatisticsPeriodCompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        number = d.pop("number", UNSET)

        sport_event_statistics_period = cls(
            competitors=competitors,
            number=number,
        )

        return sport_event_statistics_period
