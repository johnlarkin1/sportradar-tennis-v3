import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.enum_phase import EnumPhase
from ..models.enum_stage_type import EnumStageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_stage_group import SeasonStageGroup


T = TypeVar("T", bound="SeasonStage")


@_attrs_define
class SeasonStage:
    """
    Attributes:
        order (int):
        phase (EnumPhase):
        type (EnumStageType):
        end_date (Union[Unset, datetime.date]):
        groups (Union[Unset, List['SeasonStageGroup']]):
        start_date (Union[Unset, datetime.date]):
        year (Union[Unset, str]):
    """

    order: int
    phase: EnumPhase
    type: EnumStageType
    end_date: Union[Unset, datetime.date] = UNSET
    groups: Union[Unset, List["SeasonStageGroup"]] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    year: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order = self.order

        phase = self.phase.value

        type = self.type.value

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "order": order,
                "phase": phase,
                "type": type,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if groups is not UNSET:
            field_dict["groups"] = groups
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_stage_group import SeasonStageGroup

        d = src_dict.copy()
        order = d.pop("order")

        phase = EnumPhase(d.pop("phase"))

        type = EnumStageType(d.pop("type"))

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SeasonStageGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        year = d.pop("year", UNSET)

        season_stage = cls(
            order=order,
            phase=phase,
            type=type,
            end_date=end_date,
            groups=groups,
            start_date=start_date,
            year=year,
        )

        return season_stage
