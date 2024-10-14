from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_schedule_live_summaries_response_200_summaries_item_sport_event_sport_event_context_mode_best_of import (
    GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextModeBestOf,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextMode")


@_attrs_define
class GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextMode:
    """
    Attributes:
        best_of (Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextModeBestOf]):
    """

    best_of: Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextModeBestOf] = UNSET

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
        best_of: Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextModeBestOf]
        if isinstance(_best_of, Unset):
            best_of = UNSET
        else:
            best_of = GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextModeBestOf(_best_of)

        get_schedule_live_summaries_response_200_summaries_item_sport_event_sport_event_context_mode = cls(
            best_of=best_of,
        )

        return get_schedule_live_summaries_response_200_summaries_item_sport_event_sport_event_context_mode
