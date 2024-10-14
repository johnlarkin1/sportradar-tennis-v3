from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.base_summary_sport_event_status_game_state_advantage import BaseSummarySportEventStatusGameStateAdvantage
from ..models.base_summary_sport_event_status_game_state_last_point_result import (
    BaseSummarySportEventStatusGameStateLastPointResult,
)
from ..models.base_summary_sport_event_status_game_state_point_type import BaseSummarySportEventStatusGameStatePointType
from ..models.base_summary_sport_event_status_game_state_serving import BaseSummarySportEventStatusGameStateServing
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseSummarySportEventStatusGameState")


@_attrs_define
class BaseSummarySportEventStatusGameState:
    """
    Attributes:
        advantage (Union[Unset, BaseSummarySportEventStatusGameStateAdvantage]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        last_point_result (Union[Unset, BaseSummarySportEventStatusGameStateLastPointResult]):
        point_type (Union[Unset, BaseSummarySportEventStatusGameStatePointType]):
        serving (Union[Unset, BaseSummarySportEventStatusGameStateServing]):
        tie_break (Union[Unset, bool]):
    """

    advantage: Union[Unset, BaseSummarySportEventStatusGameStateAdvantage] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    last_point_result: Union[Unset, BaseSummarySportEventStatusGameStateLastPointResult] = UNSET
    point_type: Union[Unset, BaseSummarySportEventStatusGameStatePointType] = UNSET
    serving: Union[Unset, BaseSummarySportEventStatusGameStateServing] = UNSET
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
        advantage: Union[Unset, BaseSummarySportEventStatusGameStateAdvantage]
        if isinstance(_advantage, Unset):
            advantage = UNSET
        else:
            advantage = BaseSummarySportEventStatusGameStateAdvantage(_advantage)

        away_score = d.pop("away_score", UNSET)

        home_score = d.pop("home_score", UNSET)

        _last_point_result = d.pop("last_point_result", UNSET)
        last_point_result: Union[Unset, BaseSummarySportEventStatusGameStateLastPointResult]
        if isinstance(_last_point_result, Unset):
            last_point_result = UNSET
        else:
            last_point_result = BaseSummarySportEventStatusGameStateLastPointResult(_last_point_result)

        _point_type = d.pop("point_type", UNSET)
        point_type: Union[Unset, BaseSummarySportEventStatusGameStatePointType]
        if isinstance(_point_type, Unset):
            point_type = UNSET
        else:
            point_type = BaseSummarySportEventStatusGameStatePointType(_point_type)

        _serving = d.pop("serving", UNSET)
        serving: Union[Unset, BaseSummarySportEventStatusGameStateServing]
        if isinstance(_serving, Unset):
            serving = UNSET
        else:
            serving = BaseSummarySportEventStatusGameStateServing(_serving)

        tie_break = d.pop("tie_break", UNSET)

        base_summary_sport_event_status_game_state = cls(
            advantage=advantage,
            away_score=away_score,
            home_score=home_score,
            last_point_result=last_point_result,
            point_type=point_type,
            serving=serving,
            tie_break=tie_break,
        )

        return base_summary_sport_event_status_game_state
