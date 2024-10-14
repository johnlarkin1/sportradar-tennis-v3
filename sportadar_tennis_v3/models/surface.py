from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.enum_surface_type import EnumSurfaceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistics_surface import StatisticsSurface


T = TypeVar("T", bound="Surface")


@_attrs_define
class Surface:
    """
    Attributes:
        statistics (Union[Unset, StatisticsSurface]):
        type (Union[Unset, EnumSurfaceType]):
    """

    statistics: Union[Unset, "StatisticsSurface"] = UNSET
    type: Union[Unset, EnumSurfaceType] = UNSET

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
        from ..models.statistics_surface import StatisticsSurface

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, StatisticsSurface]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = StatisticsSurface.from_dict(_statistics)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EnumSurfaceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EnumSurfaceType(_type)

        surface = cls(
            statistics=statistics,
            type=type,
        )

        return surface
