from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistics_surface import StatisticsSurface
    from ..models.surface import Surface


T = TypeVar("T", bound="Period")


@_attrs_define
class Period:
    """
    Attributes:
        statistics (Union[Unset, StatisticsSurface]):
        surfaces (Union[Unset, List['Surface']]):
        year (Union[Unset, int]):
    """

    statistics: Union[Unset, "StatisticsSurface"] = UNSET
    surfaces: Union[Unset, List["Surface"]] = UNSET
    year: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        surfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.surfaces, Unset):
            surfaces = []
            for surfaces_item_data in self.surfaces:
                surfaces_item = surfaces_item_data.to_dict()
                surfaces.append(surfaces_item)

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if surfaces is not UNSET:
            field_dict["surfaces"] = surfaces
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.statistics_surface import StatisticsSurface
        from ..models.surface import Surface

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, StatisticsSurface]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = StatisticsSurface.from_dict(_statistics)

        surfaces = []
        _surfaces = d.pop("surfaces", UNSET)
        for surfaces_item_data in _surfaces or []:
            surfaces_item = Surface.from_dict(surfaces_item_data)

            surfaces.append(surfaces_item)

        year = d.pop("year", UNSET)

        period = cls(
            statistics=statistics,
            surfaces=surfaces,
            year=year,
        )

        return period
