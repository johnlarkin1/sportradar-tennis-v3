from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_stream_events_response_200_type_0_payload_sport_event_status_match_status import (
    GetStreamEventsResponse200Type0PayloadSportEventStatusMatchStatus,
)
from ..models.get_stream_events_response_200_type_0_payload_sport_event_status_status import (
    GetStreamEventsResponse200Type0PayloadSportEventStatusStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_stream_events_response_200_type_0_payload_sport_event_status_game_state import (
        GetStreamEventsResponse200Type0PayloadSportEventStatusGameState,
    )
    from ..models.get_stream_events_response_200_type_0_payload_sport_event_status_period_scores_item import (
        GetStreamEventsResponse200Type0PayloadSportEventStatusPeriodScoresItem,
    )


T = TypeVar("T", bound="GetStreamEventsResponse200Type0PayloadSportEventStatus")


@_attrs_define
class GetStreamEventsResponse200Type0PayloadSportEventStatus:
    """
    Attributes:
        status (GetStreamEventsResponse200Type0PayloadSportEventStatusStatus):
        away_normaltime_score (Union[Unset, int]):
        away_overtime_score (Union[Unset, int]):
        away_score (Union[Unset, int]):
        decided_by_fed (Union[Unset, bool]):
        game_state (Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatusGameState]):
        home_normaltime_score (Union[Unset, int]):
        home_overtime_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        match_status (Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatusMatchStatus]):
        period_scores (Union[Unset, List['GetStreamEventsResponse200Type0PayloadSportEventStatusPeriodScoresItem']]):
        scout_abandoned (Union[Unset, bool]): Scout has abandoned the match, no further updates.
        winner_id (Union[Unset, str]): Competitor URN (sr:competitor:x)
        winning_reason (Union[Unset, str]):
    """

    status: GetStreamEventsResponse200Type0PayloadSportEventStatusStatus
    away_normaltime_score: Union[Unset, int] = UNSET
    away_overtime_score: Union[Unset, int] = UNSET
    away_score: Union[Unset, int] = UNSET
    decided_by_fed: Union[Unset, bool] = UNSET
    game_state: Union[Unset, "GetStreamEventsResponse200Type0PayloadSportEventStatusGameState"] = UNSET
    home_normaltime_score: Union[Unset, int] = UNSET
    home_overtime_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    match_status: Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatusMatchStatus] = UNSET
    period_scores: Union[Unset, List["GetStreamEventsResponse200Type0PayloadSportEventStatusPeriodScoresItem"]] = UNSET
    scout_abandoned: Union[Unset, bool] = UNSET
    winner_id: Union[Unset, str] = UNSET
    winning_reason: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        away_normaltime_score = self.away_normaltime_score

        away_overtime_score = self.away_overtime_score

        away_score = self.away_score

        decided_by_fed = self.decided_by_fed

        game_state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_state, Unset):
            game_state = self.game_state.to_dict()

        home_normaltime_score = self.home_normaltime_score

        home_overtime_score = self.home_overtime_score

        home_score = self.home_score

        match_status: Union[Unset, str] = UNSET
        if not isinstance(self.match_status, Unset):
            match_status = self.match_status.value

        period_scores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.period_scores, Unset):
            period_scores = []
            for period_scores_item_data in self.period_scores:
                period_scores_item = period_scores_item_data.to_dict()
                period_scores.append(period_scores_item)

        scout_abandoned = self.scout_abandoned

        winner_id = self.winner_id

        winning_reason = self.winning_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
            }
        )
        if away_normaltime_score is not UNSET:
            field_dict["away_normaltime_score"] = away_normaltime_score
        if away_overtime_score is not UNSET:
            field_dict["away_overtime_score"] = away_overtime_score
        if away_score is not UNSET:
            field_dict["away_score"] = away_score
        if decided_by_fed is not UNSET:
            field_dict["decided_by_fed"] = decided_by_fed
        if game_state is not UNSET:
            field_dict["game_state"] = game_state
        if home_normaltime_score is not UNSET:
            field_dict["home_normaltime_score"] = home_normaltime_score
        if home_overtime_score is not UNSET:
            field_dict["home_overtime_score"] = home_overtime_score
        if home_score is not UNSET:
            field_dict["home_score"] = home_score
        if match_status is not UNSET:
            field_dict["match_status"] = match_status
        if period_scores is not UNSET:
            field_dict["period_scores"] = period_scores
        if scout_abandoned is not UNSET:
            field_dict["scout_abandoned"] = scout_abandoned
        if winner_id is not UNSET:
            field_dict["winner_id"] = winner_id
        if winning_reason is not UNSET:
            field_dict["winning_reason"] = winning_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_stream_events_response_200_type_0_payload_sport_event_status_game_state import (
            GetStreamEventsResponse200Type0PayloadSportEventStatusGameState,
        )
        from ..models.get_stream_events_response_200_type_0_payload_sport_event_status_period_scores_item import (
            GetStreamEventsResponse200Type0PayloadSportEventStatusPeriodScoresItem,
        )

        d = src_dict.copy()
        status = GetStreamEventsResponse200Type0PayloadSportEventStatusStatus(d.pop("status"))

        away_normaltime_score = d.pop("away_normaltime_score", UNSET)

        away_overtime_score = d.pop("away_overtime_score", UNSET)

        away_score = d.pop("away_score", UNSET)

        decided_by_fed = d.pop("decided_by_fed", UNSET)

        _game_state = d.pop("game_state", UNSET)
        game_state: Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatusGameState]
        if isinstance(_game_state, Unset):
            game_state = UNSET
        else:
            game_state = GetStreamEventsResponse200Type0PayloadSportEventStatusGameState.from_dict(_game_state)

        home_normaltime_score = d.pop("home_normaltime_score", UNSET)

        home_overtime_score = d.pop("home_overtime_score", UNSET)

        home_score = d.pop("home_score", UNSET)

        _match_status = d.pop("match_status", UNSET)
        match_status: Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatusMatchStatus]
        if isinstance(_match_status, Unset):
            match_status = UNSET
        else:
            match_status = GetStreamEventsResponse200Type0PayloadSportEventStatusMatchStatus(_match_status)

        period_scores = []
        _period_scores = d.pop("period_scores", UNSET)
        for period_scores_item_data in _period_scores or []:
            period_scores_item = GetStreamEventsResponse200Type0PayloadSportEventStatusPeriodScoresItem.from_dict(
                period_scores_item_data
            )

            period_scores.append(period_scores_item)

        scout_abandoned = d.pop("scout_abandoned", UNSET)

        winner_id = d.pop("winner_id", UNSET)

        winning_reason = d.pop("winning_reason", UNSET)

        get_stream_events_response_200_type_0_payload_sport_event_status = cls(
            status=status,
            away_normaltime_score=away_normaltime_score,
            away_overtime_score=away_overtime_score,
            away_score=away_score,
            decided_by_fed=decided_by_fed,
            game_state=game_state,
            home_normaltime_score=home_normaltime_score,
            home_overtime_score=home_overtime_score,
            home_score=home_score,
            match_status=match_status,
            period_scores=period_scores,
            scout_abandoned=scout_abandoned,
            winner_id=winner_id,
            winning_reason=winning_reason,
        )

        return get_stream_events_response_200_type_0_payload_sport_event_status
