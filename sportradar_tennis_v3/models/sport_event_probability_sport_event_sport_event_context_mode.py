from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.sport_event_probability_sport_event_sport_event_context_mode_best_of import (
    SportEventProbabilitySportEventSportEventContextModeBestOf,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SportEventProbabilitySportEventSportEventContextMode")


@_attrs_define
class SportEventProbabilitySportEventSportEventContextMode:
    """
    Attributes:
        best_of (Union[Unset, SportEventProbabilitySportEventSportEventContextModeBestOf]):
    """

    best_of: Union[Unset, SportEventProbabilitySportEventSportEventContextModeBestOf] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        best_of: Union[Unset, str] = UNSET
        if not isinstance(self.best_of, Unset):
            best_of = self.best_of.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if best_of is not UNSET:
            field_dict["best_of"] = best_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _best_of = d.pop("best_of", UNSET)
        best_of: Union[Unset, SportEventProbabilitySportEventSportEventContextModeBestOf]
        if isinstance(_best_of, Unset):
            best_of = UNSET
        else:
            best_of = SportEventProbabilitySportEventSportEventContextModeBestOf(_best_of)

        sport_event_probability_sport_event_sport_event_context_mode = cls(
            best_of=best_of,
        )

        return sport_event_probability_sport_event_sport_event_context_mode
