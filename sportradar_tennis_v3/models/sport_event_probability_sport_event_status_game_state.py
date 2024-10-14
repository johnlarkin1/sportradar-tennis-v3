from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.sport_event_probability_sport_event_status_game_state_advantage import (
    SportEventProbabilitySportEventStatusGameStateAdvantage,
)
from ..models.sport_event_probability_sport_event_status_game_state_last_point_result import (
    SportEventProbabilitySportEventStatusGameStateLastPointResult,
)
from ..models.sport_event_probability_sport_event_status_game_state_point_type import (
    SportEventProbabilitySportEventStatusGameStatePointType,
)
from ..models.sport_event_probability_sport_event_status_game_state_serving import (
    SportEventProbabilitySportEventStatusGameStateServing,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SportEventProbabilitySportEventStatusGameState")


@_attrs_define
class SportEventProbabilitySportEventStatusGameState:
    """
    Attributes:
        advantage (Union[Unset, SportEventProbabilitySportEventStatusGameStateAdvantage]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        last_point_result (Union[Unset, SportEventProbabilitySportEventStatusGameStateLastPointResult]):
        point_type (Union[Unset, SportEventProbabilitySportEventStatusGameStatePointType]):
        serving (Union[Unset, SportEventProbabilitySportEventStatusGameStateServing]):
        tie_break (Union[Unset, bool]):
    """

    advantage: Union[Unset, SportEventProbabilitySportEventStatusGameStateAdvantage] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    last_point_result: Union[Unset, SportEventProbabilitySportEventStatusGameStateLastPointResult] = UNSET
    point_type: Union[Unset, SportEventProbabilitySportEventStatusGameStatePointType] = UNSET
    serving: Union[Unset, SportEventProbabilitySportEventStatusGameStateServing] = UNSET
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
        advantage: Union[Unset, SportEventProbabilitySportEventStatusGameStateAdvantage]
        if isinstance(_advantage, Unset):
            advantage = UNSET
        else:
            advantage = SportEventProbabilitySportEventStatusGameStateAdvantage(_advantage)

        away_score = d.pop("away_score", UNSET)

        home_score = d.pop("home_score", UNSET)

        _last_point_result = d.pop("last_point_result", UNSET)
        last_point_result: Union[Unset, SportEventProbabilitySportEventStatusGameStateLastPointResult]
        if isinstance(_last_point_result, Unset):
            last_point_result = UNSET
        else:
            last_point_result = SportEventProbabilitySportEventStatusGameStateLastPointResult(_last_point_result)

        _point_type = d.pop("point_type", UNSET)
        point_type: Union[Unset, SportEventProbabilitySportEventStatusGameStatePointType]
        if isinstance(_point_type, Unset):
            point_type = UNSET
        else:
            point_type = SportEventProbabilitySportEventStatusGameStatePointType(_point_type)

        _serving = d.pop("serving", UNSET)
        serving: Union[Unset, SportEventProbabilitySportEventStatusGameStateServing]
        if isinstance(_serving, Unset):
            serving = UNSET
        else:
            serving = SportEventProbabilitySportEventStatusGameStateServing(_serving)

        tie_break = d.pop("tie_break", UNSET)

        sport_event_probability_sport_event_status_game_state = cls(
            advantage=advantage,
            away_score=away_score,
            home_score=home_score,
            last_point_result=last_point_result,
            point_type=point_type,
            serving=serving,
            tie_break=tie_break,
        )

        return sport_event_probability_sport_event_status_game_state
