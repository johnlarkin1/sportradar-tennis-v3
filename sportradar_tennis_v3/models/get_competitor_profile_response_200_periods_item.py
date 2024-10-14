from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_profile_response_200_periods_item_statistics import (
        GetCompetitorProfileResponse200PeriodsItemStatistics,
    )
    from ..models.get_competitor_profile_response_200_periods_item_surfaces_item import (
        GetCompetitorProfileResponse200PeriodsItemSurfacesItem,
    )


T = TypeVar("T", bound="GetCompetitorProfileResponse200PeriodsItem")


@_attrs_define
class GetCompetitorProfileResponse200PeriodsItem:
    """
    Attributes:
        statistics (Union[Unset, GetCompetitorProfileResponse200PeriodsItemStatistics]):
        surfaces (Union[Unset, List['GetCompetitorProfileResponse200PeriodsItemSurfacesItem']]):
        year (Union[Unset, int]):
    """

    statistics: Union[Unset, "GetCompetitorProfileResponse200PeriodsItemStatistics"] = UNSET
    surfaces: Union[Unset, List["GetCompetitorProfileResponse200PeriodsItemSurfacesItem"]] = UNSET
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
        from ..models.get_competitor_profile_response_200_periods_item_statistics import (
            GetCompetitorProfileResponse200PeriodsItemStatistics,
        )
        from ..models.get_competitor_profile_response_200_periods_item_surfaces_item import (
            GetCompetitorProfileResponse200PeriodsItemSurfacesItem,
        )

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetCompetitorProfileResponse200PeriodsItemStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetCompetitorProfileResponse200PeriodsItemStatistics.from_dict(_statistics)

        surfaces = []
        _surfaces = d.pop("surfaces", UNSET)
        for surfaces_item_data in _surfaces or []:
            surfaces_item = GetCompetitorProfileResponse200PeriodsItemSurfacesItem.from_dict(surfaces_item_data)

            surfaces.append(surfaces_item)

        year = d.pop("year", UNSET)

        get_competitor_profile_response_200_periods_item = cls(
            statistics=statistics,
            surfaces=surfaces,
            year=year,
        )

        return get_competitor_profile_response_200_periods_item
