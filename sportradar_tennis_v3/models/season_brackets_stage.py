import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_brackets_stage_phase import SeasonBracketsStagePhase
from ..models.season_brackets_stage_type import SeasonBracketsStageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_brackets_stage_groups_item import SeasonBracketsStageGroupsItem


T = TypeVar("T", bound="SeasonBracketsStage")


@_attrs_define
class SeasonBracketsStage:
    """
    Attributes:
        phase (SeasonBracketsStagePhase):
        type (SeasonBracketsStageType):
        end_date (Union[Unset, datetime.date]):
        groups (Union[Unset, List['SeasonBracketsStageGroupsItem']]):
        order (Union[Unset, int]):
        start_date (Union[Unset, datetime.date]):
        year (Union[Unset, str]):
    """

    phase: SeasonBracketsStagePhase
    type: SeasonBracketsStageType
    end_date: Union[Unset, datetime.date] = UNSET
    groups: Union[Unset, List["SeasonBracketsStageGroupsItem"]] = UNSET
    order: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    year: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        order = self.order

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "phase": phase,
                "type": type,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if groups is not UNSET:
            field_dict["groups"] = groups
        if order is not UNSET:
            field_dict["order"] = order
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_brackets_stage_groups_item import SeasonBracketsStageGroupsItem

        d = src_dict.copy()
        phase = SeasonBracketsStagePhase(d.pop("phase"))

        type = SeasonBracketsStageType(d.pop("type"))

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SeasonBracketsStageGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        order = d.pop("order", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        year = d.pop("year", UNSET)

        season_brackets_stage = cls(
            phase=phase,
            type=type,
            end_date=end_date,
            groups=groups,
            order=order,
            start_date=start_date,
            year=year,
        )

        return season_brackets_stage
