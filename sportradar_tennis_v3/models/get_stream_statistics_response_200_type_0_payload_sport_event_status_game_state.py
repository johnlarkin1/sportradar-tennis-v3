from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_stream_statistics_response_200_type_0_payload_sport_event_status_game_state_advantage import (
    GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateAdvantage,
)
from ..models.get_stream_statistics_response_200_type_0_payload_sport_event_status_game_state_last_point_result import (
    GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateLastPointResult,
)
from ..models.get_stream_statistics_response_200_type_0_payload_sport_event_status_game_state_point_type import (
    GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStatePointType,
)
from ..models.get_stream_statistics_response_200_type_0_payload_sport_event_status_game_state_serving import (
    GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateServing,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameState")


@_attrs_define
class GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameState:
    """
    Attributes:
        advantage (Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateAdvantage]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        last_point_result (Union[Unset,
            GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateLastPointResult]):
        point_type (Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStatePointType]):
        serving (Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateServing]):
        tie_break (Union[Unset, bool]):
    """

    advantage: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateAdvantage] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    last_point_result: Union[
        Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateLastPointResult
    ] = UNSET
    point_type: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStatePointType] = UNSET
    serving: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateServing] = UNSET
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
        advantage: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateAdvantage]
        if isinstance(_advantage, Unset):
            advantage = UNSET
        else:
            advantage = GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateAdvantage(_advantage)

        away_score = d.pop("away_score", UNSET)

        home_score = d.pop("home_score", UNSET)

        _last_point_result = d.pop("last_point_result", UNSET)
        last_point_result: Union[
            Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateLastPointResult
        ]
        if isinstance(_last_point_result, Unset):
            last_point_result = UNSET
        else:
            last_point_result = GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateLastPointResult(
                _last_point_result
            )

        _point_type = d.pop("point_type", UNSET)
        point_type: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStatePointType]
        if isinstance(_point_type, Unset):
            point_type = UNSET
        else:
            point_type = GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStatePointType(_point_type)

        _serving = d.pop("serving", UNSET)
        serving: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateServing]
        if isinstance(_serving, Unset):
            serving = UNSET
        else:
            serving = GetStreamStatisticsResponse200Type0PayloadSportEventStatusGameStateServing(_serving)

        tie_break = d.pop("tie_break", UNSET)

        get_stream_statistics_response_200_type_0_payload_sport_event_status_game_state = cls(
            advantage=advantage,
            away_score=away_score,
            home_score=home_score,
            last_point_result=last_point_result,
            point_type=point_type,
            serving=serving,
            tie_break=tie_break,
        )

        return get_stream_statistics_response_200_type_0_payload_sport_event_status_game_state
