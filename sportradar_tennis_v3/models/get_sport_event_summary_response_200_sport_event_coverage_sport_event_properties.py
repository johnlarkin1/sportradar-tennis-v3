from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_sport_event_summary_response_200_sport_event_coverage_sport_event_properties_scores import (
    GetSportEventSummaryResponse200SportEventCoverageSportEventPropertiesScores,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSportEventSummaryResponse200SportEventCoverageSportEventProperties")


@_attrs_define
class GetSportEventSummaryResponse200SportEventCoverageSportEventProperties:
    """
    Attributes:
        detailed_serve_outcomes (Union[Unset, bool]):
        enhanced_stats (Union[Unset, bool]): If true, the following statistics are available: 'backhand_errors',
            'backhand_unforced_errors', 'backhand_winners', 'forehand_errors', 'forehand_unforced_errors',
            'forehand_winners', 'groundstroke_errors', 'groundstroke_unforced_errors', 'overhead_stroke_errors',
            'overhead_stroke_winners', 'overhead_stroke_unforced_errors', 'return_errors', 'return_winners',
            'service_points_won', 'volley_winners' 'lob_winners', 'lob_unforced_errors', 'aces', 'double_faults',
            'max_points_in_a_row', 'breakpoints_won', 'total_breakpoints', 'first_serve_points_won',
            'second_serve_points_won', 'points_won', 'max_games_in_a_row', 'games_won', 'tiebreaks_won',
            'first_serve_successful', 'second_serve_successful', 'service_points_won', 'service_points_lost',
            'service_games_won', 'groundstroke_winners', 'volley_unforced_errors' If false: 'aces', 'double_faults',
            'max_points_in_a_row', 'breakpoints_won', 'total_breakpoints', 'first_serve_points_won',
            'second_serve_points_won', 'points_won', 'max_games_in_a_row', 'games_won', 'tiebreaks_won',
            'first_serve_successful', 'second_serve_successful', 'service_points_won', 'service_points_lost',
            'service_games_won',
        play_by_play (Union[Unset, bool]):
        scores (Union[Unset, GetSportEventSummaryResponse200SportEventCoverageSportEventPropertiesScores]):
    """

    detailed_serve_outcomes: Union[Unset, bool] = UNSET
    enhanced_stats: Union[Unset, bool] = UNSET
    play_by_play: Union[Unset, bool] = UNSET
    scores: Union[Unset, GetSportEventSummaryResponse200SportEventCoverageSportEventPropertiesScores] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        detailed_serve_outcomes = self.detailed_serve_outcomes

        enhanced_stats = self.enhanced_stats

        play_by_play = self.play_by_play

        scores: Union[Unset, str] = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detailed_serve_outcomes is not UNSET:
            field_dict["detailed_serve_outcomes"] = detailed_serve_outcomes
        if enhanced_stats is not UNSET:
            field_dict["enhanced_stats"] = enhanced_stats
        if play_by_play is not UNSET:
            field_dict["play_by_play"] = play_by_play
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        detailed_serve_outcomes = d.pop("detailed_serve_outcomes", UNSET)

        enhanced_stats = d.pop("enhanced_stats", UNSET)

        play_by_play = d.pop("play_by_play", UNSET)

        _scores = d.pop("scores", UNSET)
        scores: Union[Unset, GetSportEventSummaryResponse200SportEventCoverageSportEventPropertiesScores]
        if isinstance(_scores, Unset):
            scores = UNSET
        else:
            scores = GetSportEventSummaryResponse200SportEventCoverageSportEventPropertiesScores(_scores)

        get_sport_event_summary_response_200_sport_event_coverage_sport_event_properties = cls(
            detailed_serve_outcomes=detailed_serve_outcomes,
            enhanced_stats=enhanced_stats,
            play_by_play=play_by_play,
            scores=scores,
        )

        get_sport_event_summary_response_200_sport_event_coverage_sport_event_properties.additional_properties = d
        return get_sport_event_summary_response_200_sport_event_coverage_sport_event_properties

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
