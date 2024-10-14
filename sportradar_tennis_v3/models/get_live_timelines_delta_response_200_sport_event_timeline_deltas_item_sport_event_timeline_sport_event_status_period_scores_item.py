from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_period_scores_item_type import (
    GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusPeriodScoresItemType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusPeriodScoresItem",
)


@_attrs_define
class GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusPeriodScoresItem:
    """
    Attributes:
        away_score (int):
        home_score (int):
        away_tiebreak_score (Union[Unset, int]):
        home_tiebreak_score (Union[Unset, int]):
        number (Union[Unset, int]):
        type (Union[Unset, GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatu
            sPeriodScoresItemType]):
    """

    away_score: int
    home_score: int
    away_tiebreak_score: Union[Unset, int] = UNSET
    home_tiebreak_score: Union[Unset, int] = UNSET
    number: Union[Unset, int] = UNSET
    type: Union[
        Unset,
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusPeriodScoresItemType,
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        away_score = self.away_score

        home_score = self.home_score

        away_tiebreak_score = self.away_tiebreak_score

        home_tiebreak_score = self.home_tiebreak_score

        number = self.number

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "away_score": away_score,
                "home_score": home_score,
            }
        )
        if away_tiebreak_score is not UNSET:
            field_dict["away_tiebreak_score"] = away_tiebreak_score
        if home_tiebreak_score is not UNSET:
            field_dict["home_tiebreak_score"] = home_tiebreak_score
        if number is not UNSET:
            field_dict["number"] = number
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        away_score = d.pop("away_score")

        home_score = d.pop("home_score")

        away_tiebreak_score = d.pop("away_tiebreak_score", UNSET)

        home_tiebreak_score = d.pop("home_tiebreak_score", UNSET)

        number = d.pop("number", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[
            Unset,
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusPeriodScoresItemType,
        ]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusPeriodScoresItemType(
                _type
            )

        get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_period_scores_item = cls(
            away_score=away_score,
            home_score=home_score,
            away_tiebreak_score=away_tiebreak_score,
            home_tiebreak_score=home_tiebreak_score,
            number=number,
            type=type,
        )

        return get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_period_scores_item
