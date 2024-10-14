from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.period_surfaces_item_type import PeriodSurfacesItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.period_surfaces_item_statistics import PeriodSurfacesItemStatistics


T = TypeVar("T", bound="PeriodSurfacesItem")


@_attrs_define
class PeriodSurfacesItem:
    """
    Attributes:
        statistics (Union[Unset, PeriodSurfacesItemStatistics]):
        type (Union[Unset, PeriodSurfacesItemType]):
    """

    statistics: Union[Unset, "PeriodSurfacesItemStatistics"] = UNSET
    type: Union[Unset, PeriodSurfacesItemType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.period_surfaces_item_statistics import PeriodSurfacesItemStatistics

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, PeriodSurfacesItemStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = PeriodSurfacesItemStatistics.from_dict(_statistics)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PeriodSurfacesItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PeriodSurfacesItemType(_type)

        period_surfaces_item = cls(
            statistics=statistics,
            type=type,
        )

        return period_surfaces_item
