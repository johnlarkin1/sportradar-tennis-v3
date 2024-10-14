from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.enum_competition_status import EnumCompetitionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseInfo")


@_attrs_define
class BaseInfo:
    """
    Attributes:
        competition_status (Union[Unset, EnumCompetitionStatus]):
        venue_reduced_capacity (Union[Unset, bool]):
        venue_reduced_capacity_max (Union[Unset, int]):
    """

    competition_status: Union[Unset, EnumCompetitionStatus] = UNSET
    venue_reduced_capacity: Union[Unset, bool] = UNSET
    venue_reduced_capacity_max: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competition_status: Union[Unset, str] = UNSET
        if not isinstance(self.competition_status, Unset):
            competition_status = self.competition_status.value

        venue_reduced_capacity = self.venue_reduced_capacity

        venue_reduced_capacity_max = self.venue_reduced_capacity_max

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competition_status is not UNSET:
            field_dict["competition_status"] = competition_status
        if venue_reduced_capacity is not UNSET:
            field_dict["venue_reduced_capacity"] = venue_reduced_capacity
        if venue_reduced_capacity_max is not UNSET:
            field_dict["venue_reduced_capacity_max"] = venue_reduced_capacity_max

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _competition_status = d.pop("competition_status", UNSET)
        competition_status: Union[Unset, EnumCompetitionStatus]
        if isinstance(_competition_status, Unset):
            competition_status = UNSET
        else:
            competition_status = EnumCompetitionStatus(_competition_status)

        venue_reduced_capacity = d.pop("venue_reduced_capacity", UNSET)

        venue_reduced_capacity_max = d.pop("venue_reduced_capacity_max", UNSET)

        base_info = cls(
            competition_status=competition_status,
            venue_reduced_capacity=venue_reduced_capacity,
            venue_reduced_capacity_max=venue_reduced_capacity_max,
        )

        return base_info
