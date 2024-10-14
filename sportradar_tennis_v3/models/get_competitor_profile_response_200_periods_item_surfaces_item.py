from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_competitor_profile_response_200_periods_item_surfaces_item_type import (
    GetCompetitorProfileResponse200PeriodsItemSurfacesItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_profile_response_200_periods_item_surfaces_item_statistics import (
        GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics,
    )


T = TypeVar("T", bound="GetCompetitorProfileResponse200PeriodsItemSurfacesItem")


@_attrs_define
class GetCompetitorProfileResponse200PeriodsItemSurfacesItem:
    """
    Attributes:
        statistics (Union[Unset, GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics]):
        type (Union[Unset, GetCompetitorProfileResponse200PeriodsItemSurfacesItemType]):
    """

    statistics: Union[Unset, "GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics"] = UNSET
    type: Union[Unset, GetCompetitorProfileResponse200PeriodsItemSurfacesItemType] = UNSET

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
        from ..models.get_competitor_profile_response_200_periods_item_surfaces_item_statistics import (
            GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics,
        )

        d = src_dict.copy()
        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetCompetitorProfileResponse200PeriodsItemSurfacesItemStatistics.from_dict(_statistics)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetCompetitorProfileResponse200PeriodsItemSurfacesItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetCompetitorProfileResponse200PeriodsItemSurfacesItemType(_type)

        get_competitor_profile_response_200_periods_item_surfaces_item = cls(
            statistics=statistics,
            type=type,
        )

        return get_competitor_profile_response_200_periods_item_surfaces_item
