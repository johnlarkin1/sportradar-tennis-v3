import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.base_summary_sport_event_sport_event_context_stage_phase import (
    BaseSummarySportEventSportEventContextStagePhase,
)
from ..models.base_summary_sport_event_sport_event_context_stage_type import (
    BaseSummarySportEventSportEventContextStageType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseSummarySportEventSportEventContextStage")


@_attrs_define
class BaseSummarySportEventSportEventContextStage:
    """
    Attributes:
        order (int):
        phase (BaseSummarySportEventSportEventContextStagePhase):
        type (BaseSummarySportEventSportEventContextStageType):
        end_date (Union[Unset, datetime.date]):
        start_date (Union[Unset, datetime.date]):
        year (Union[Unset, str]):
    """

    order: int
    phase: BaseSummarySportEventSportEventContextStagePhase
    type: BaseSummarySportEventSportEventContextStageType
    end_date: Union[Unset, datetime.date] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    year: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order = self.order

        phase = self.phase.value

        type = self.type.value

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

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
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order = d.pop("order")

        phase = BaseSummarySportEventSportEventContextStagePhase(d.pop("phase"))

        type = BaseSummarySportEventSportEventContextStageType(d.pop("type"))

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        year = d.pop("year", UNSET)

        base_summary_sport_event_sport_event_context_stage = cls(
            order=order,
            phase=phase,
            type=type,
            end_date=end_date,
            start_date=start_date,
            year=year,
        )

        return base_summary_sport_event_sport_event_context_stage
