from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.surface_type import SurfaceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.surface_statistics import SurfaceStatistics


T = TypeVar("T", bound="Surface")


@_attrs_define
class Surface:
    """
    Attributes:
        statistics (Union[Unset, SurfaceStatistics]):
        type (Union[Unset, SurfaceType]):
    """

    statistics: Union[Unset, "SurfaceStatistics"] = UNSET
    type: Union[Unset, SurfaceType] = UNSET

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
        from ..models.surface_statistics import SurfaceStatistics

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SurfaceStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SurfaceStatistics.from_dict(_statistics)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SurfaceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SurfaceType(_type)

        surface = cls(
            statistics=statistics,
            type=type,
        )

        return surface
