from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_game_state_advantage import (
    GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateAdvantage,
)
from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_game_state_last_point_result import (
    GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateLastPointResult,
)
from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_game_state_point_type import (
    GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStatePointType,
)
from ..models.get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_game_state_serving import (
    GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateServing,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameState"
)


@_attrs_define
class GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameState:
    """
    Attributes:
        advantage (Union[Unset, GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEvent
            StatusGameStateAdvantage]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        last_point_result (Union[Unset, GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSp
            ortEventStatusGameStateLastPointResult]):
        point_type (Union[Unset, GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEven
            tStatusGameStatePointType]):
        serving (Union[Unset, GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventSt
            atusGameStateServing]):
        tie_break (Union[Unset, bool]):
    """

    advantage: Union[
        Unset,
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateAdvantage,
    ] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    last_point_result: Union[
        Unset,
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateLastPointResult,
    ] = UNSET
    point_type: Union[
        Unset,
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStatePointType,
    ] = UNSET
    serving: Union[
        Unset,
        GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateServing,
    ] = UNSET
    tie_break: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        advantage: Union[Unset, str] = UNSET
        if not isinstance(self.advantage, Unset):
            advantage = self.advantage.value

        away_score = self.away_score

        home_score = self.home_score

        last_point_result: Union[Unset, str] = UNSET
        if not isinstance(self.last_point_result, Unset):
            last_point_result = self.last_point_result.value

        point_type: Union[Unset, str] = UNSET
        if not isinstance(self.point_type, Unset):
            point_type = self.point_type.value

        serving: Union[Unset, str] = UNSET
        if not isinstance(self.serving, Unset):
            serving = self.serving.value

        tie_break = self.tie_break

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if advantage is not UNSET:
            field_dict["advantage"] = advantage
        if away_score is not UNSET:
            field_dict["away_score"] = away_score
        if home_score is not UNSET:
            field_dict["home_score"] = home_score
        if last_point_result is not UNSET:
            field_dict["last_point_result"] = last_point_result
        if point_type is not UNSET:
            field_dict["point_type"] = point_type
        if serving is not UNSET:
            field_dict["serving"] = serving
        if tie_break is not UNSET:
            field_dict["tie_break"] = tie_break

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _advantage = d.pop("advantage", UNSET)
        advantage: Union[
            Unset,
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateAdvantage,
        ]
        if isinstance(_advantage, Unset):
            advantage = UNSET
        else:
            advantage = GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateAdvantage(
                _advantage
            )

        away_score = d.pop("away_score", UNSET)

        home_score = d.pop("home_score", UNSET)

        _last_point_result = d.pop("last_point_result", UNSET)
        last_point_result: Union[
            Unset,
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateLastPointResult,
        ]
        if isinstance(_last_point_result, Unset):
            last_point_result = UNSET
        else:
            last_point_result = GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateLastPointResult(
                _last_point_result
            )

        _point_type = d.pop("point_type", UNSET)
        point_type: Union[
            Unset,
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStatePointType,
        ]
        if isinstance(_point_type, Unset):
            point_type = UNSET
        else:
            point_type = GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStatePointType(
                _point_type
            )

        _serving = d.pop("serving", UNSET)
        serving: Union[
            Unset,
            GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateServing,
        ]
        if isinstance(_serving, Unset):
            serving = UNSET
        else:
            serving = GetLiveTimelinesDeltaResponse200SportEventTimelineDeltasItemSportEventTimelineSportEventStatusGameStateServing(
                _serving
            )

        tie_break = d.pop("tie_break", UNSET)

        get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_game_state = cls(
            advantage=advantage,
            away_score=away_score,
            home_score=home_score,
            last_point_result=last_point_result,
            point_type=point_type,
            serving=serving,
            tie_break=tie_break,
        )

        return get_live_timelines_delta_response_200_sport_event_timeline_deltas_item_sport_event_timeline_sport_event_status_game_state
