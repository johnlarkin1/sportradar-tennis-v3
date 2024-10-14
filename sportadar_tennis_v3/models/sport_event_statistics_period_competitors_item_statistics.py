from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SportEventStatisticsPeriodCompetitorsItemStatistics")


@_attrs_define
class SportEventStatisticsPeriodCompetitorsItemStatistics:
    """
    Attributes:
        aces (Union[Unset, int]):
        backhand_errors (Union[Unset, int]):
        backhand_unforced_errors (Union[Unset, int]):
        backhand_winners (Union[Unset, int]):
        breakpoints_won (Union[Unset, int]):
        double_faults (Union[Unset, int]):
        drop_shot_unforced_errors (Union[Unset, int]):
        drop_shot_winners (Union[Unset, int]):
        first_serve_points_won (Union[Unset, int]):
        first_serve_successful (Union[Unset, int]):
        forehand_errors (Union[Unset, int]):
        forehand_unforced_errors (Union[Unset, int]):
        forehand_winners (Union[Unset, int]):
        games_won (Union[Unset, int]):
        groundstroke_errors (Union[Unset, int]):
        groundstroke_unforced_errors (Union[Unset, int]):
        groundstroke_winners (Union[Unset, int]):
        lob_unforced_errors (Union[Unset, int]):
        lob_winners (Union[Unset, int]):
        max_games_in_a_row (Union[Unset, int]):
        max_points_in_a_row (Union[Unset, int]):
        overhead_stroke_errors (Union[Unset, int]):
        overhead_stroke_unforced_errors (Union[Unset, int]):
        overhead_stroke_winners (Union[Unset, int]):
        points_won (Union[Unset, int]):
        points_won_from_last_10 (Union[Unset, int]):
        return_errors (Union[Unset, int]):
        return_errors_unforced (Union[Unset, int]):
        return_winners (Union[Unset, int]):
        returns_played (Union[Unset, int]):
        second_serve_points_won (Union[Unset, int]):
        second_serve_successful (Union[Unset, int]):
        service_games_won (Union[Unset, int]):
        service_points_lost (Union[Unset, int]):
        service_points_won (Union[Unset, int]):
        tiebreaks_won (Union[Unset, int]):
        total_breakpoints (Union[Unset, int]):
        volley_unforced_errors (Union[Unset, int]):
        volley_winners (Union[Unset, int]):
    """

    aces: Union[Unset, int] = UNSET
    backhand_errors: Union[Unset, int] = UNSET
    backhand_unforced_errors: Union[Unset, int] = UNSET
    backhand_winners: Union[Unset, int] = UNSET
    breakpoints_won: Union[Unset, int] = UNSET
    double_faults: Union[Unset, int] = UNSET
    drop_shot_unforced_errors: Union[Unset, int] = UNSET
    drop_shot_winners: Union[Unset, int] = UNSET
    first_serve_points_won: Union[Unset, int] = UNSET
    first_serve_successful: Union[Unset, int] = UNSET
    forehand_errors: Union[Unset, int] = UNSET
    forehand_unforced_errors: Union[Unset, int] = UNSET
    forehand_winners: Union[Unset, int] = UNSET
    games_won: Union[Unset, int] = UNSET
    groundstroke_errors: Union[Unset, int] = UNSET
    groundstroke_unforced_errors: Union[Unset, int] = UNSET
    groundstroke_winners: Union[Unset, int] = UNSET
    lob_unforced_errors: Union[Unset, int] = UNSET
    lob_winners: Union[Unset, int] = UNSET
    max_games_in_a_row: Union[Unset, int] = UNSET
    max_points_in_a_row: Union[Unset, int] = UNSET
    overhead_stroke_errors: Union[Unset, int] = UNSET
    overhead_stroke_unforced_errors: Union[Unset, int] = UNSET
    overhead_stroke_winners: Union[Unset, int] = UNSET
    points_won: Union[Unset, int] = UNSET
    points_won_from_last_10: Union[Unset, int] = UNSET
    return_errors: Union[Unset, int] = UNSET
    return_errors_unforced: Union[Unset, int] = UNSET
    return_winners: Union[Unset, int] = UNSET
    returns_played: Union[Unset, int] = UNSET
    second_serve_points_won: Union[Unset, int] = UNSET
    second_serve_successful: Union[Unset, int] = UNSET
    service_games_won: Union[Unset, int] = UNSET
    service_points_lost: Union[Unset, int] = UNSET
    service_points_won: Union[Unset, int] = UNSET
    tiebreaks_won: Union[Unset, int] = UNSET
    total_breakpoints: Union[Unset, int] = UNSET
    volley_unforced_errors: Union[Unset, int] = UNSET
    volley_winners: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aces = self.aces

        backhand_errors = self.backhand_errors

        backhand_unforced_errors = self.backhand_unforced_errors

        backhand_winners = self.backhand_winners

        breakpoints_won = self.breakpoints_won

        double_faults = self.double_faults

        drop_shot_unforced_errors = self.drop_shot_unforced_errors

        drop_shot_winners = self.drop_shot_winners

        first_serve_points_won = self.first_serve_points_won

        first_serve_successful = self.first_serve_successful

        forehand_errors = self.forehand_errors

        forehand_unforced_errors = self.forehand_unforced_errors

        forehand_winners = self.forehand_winners

        games_won = self.games_won

        groundstroke_errors = self.groundstroke_errors

        groundstroke_unforced_errors = self.groundstroke_unforced_errors

        groundstroke_winners = self.groundstroke_winners

        lob_unforced_errors = self.lob_unforced_errors

        lob_winners = self.lob_winners

        max_games_in_a_row = self.max_games_in_a_row

        max_points_in_a_row = self.max_points_in_a_row

        overhead_stroke_errors = self.overhead_stroke_errors

        overhead_stroke_unforced_errors = self.overhead_stroke_unforced_errors

        overhead_stroke_winners = self.overhead_stroke_winners

        points_won = self.points_won

        points_won_from_last_10 = self.points_won_from_last_10

        return_errors = self.return_errors

        return_errors_unforced = self.return_errors_unforced

        return_winners = self.return_winners

        returns_played = self.returns_played

        second_serve_points_won = self.second_serve_points_won

        second_serve_successful = self.second_serve_successful

        service_games_won = self.service_games_won

        service_points_lost = self.service_points_lost

        service_points_won = self.service_points_won

        tiebreaks_won = self.tiebreaks_won

        total_breakpoints = self.total_breakpoints

        volley_unforced_errors = self.volley_unforced_errors

        volley_winners = self.volley_winners

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aces is not UNSET:
            field_dict["aces"] = aces
        if backhand_errors is not UNSET:
            field_dict["backhand_errors"] = backhand_errors
        if backhand_unforced_errors is not UNSET:
            field_dict["backhand_unforced_errors"] = backhand_unforced_errors
        if backhand_winners is not UNSET:
            field_dict["backhand_winners"] = backhand_winners
        if breakpoints_won is not UNSET:
            field_dict["breakpoints_won"] = breakpoints_won
        if double_faults is not UNSET:
            field_dict["double_faults"] = double_faults
        if drop_shot_unforced_errors is not UNSET:
            field_dict["drop_shot_unforced_errors"] = drop_shot_unforced_errors
        if drop_shot_winners is not UNSET:
            field_dict["drop_shot_winners"] = drop_shot_winners
        if first_serve_points_won is not UNSET:
            field_dict["first_serve_points_won"] = first_serve_points_won
        if first_serve_successful is not UNSET:
            field_dict["first_serve_successful"] = first_serve_successful
        if forehand_errors is not UNSET:
            field_dict["forehand_errors"] = forehand_errors
        if forehand_unforced_errors is not UNSET:
            field_dict["forehand_unforced_errors"] = forehand_unforced_errors
        if forehand_winners is not UNSET:
            field_dict["forehand_winners"] = forehand_winners
        if games_won is not UNSET:
            field_dict["games_won"] = games_won
        if groundstroke_errors is not UNSET:
            field_dict["groundstroke_errors"] = groundstroke_errors
        if groundstroke_unforced_errors is not UNSET:
            field_dict["groundstroke_unforced_errors"] = groundstroke_unforced_errors
        if groundstroke_winners is not UNSET:
            field_dict["groundstroke_winners"] = groundstroke_winners
        if lob_unforced_errors is not UNSET:
            field_dict["lob_unforced_errors"] = lob_unforced_errors
        if lob_winners is not UNSET:
            field_dict["lob_winners"] = lob_winners
        if max_games_in_a_row is not UNSET:
            field_dict["max_games_in_a_row"] = max_games_in_a_row
        if max_points_in_a_row is not UNSET:
            field_dict["max_points_in_a_row"] = max_points_in_a_row
        if overhead_stroke_errors is not UNSET:
            field_dict["overhead_stroke_errors"] = overhead_stroke_errors
        if overhead_stroke_unforced_errors is not UNSET:
            field_dict["overhead_stroke_unforced_errors"] = overhead_stroke_unforced_errors
        if overhead_stroke_winners is not UNSET:
            field_dict["overhead_stroke_winners"] = overhead_stroke_winners
        if points_won is not UNSET:
            field_dict["points_won"] = points_won
        if points_won_from_last_10 is not UNSET:
            field_dict["points_won_from_last_10"] = points_won_from_last_10
        if return_errors is not UNSET:
            field_dict["return_errors"] = return_errors
        if return_errors_unforced is not UNSET:
            field_dict["return_errors_unforced"] = return_errors_unforced
        if return_winners is not UNSET:
            field_dict["return_winners"] = return_winners
        if returns_played is not UNSET:
            field_dict["returns_played"] = returns_played
        if second_serve_points_won is not UNSET:
            field_dict["second_serve_points_won"] = second_serve_points_won
        if second_serve_successful is not UNSET:
            field_dict["second_serve_successful"] = second_serve_successful
        if service_games_won is not UNSET:
            field_dict["service_games_won"] = service_games_won
        if service_points_lost is not UNSET:
            field_dict["service_points_lost"] = service_points_lost
        if service_points_won is not UNSET:
            field_dict["service_points_won"] = service_points_won
        if tiebreaks_won is not UNSET:
            field_dict["tiebreaks_won"] = tiebreaks_won
        if total_breakpoints is not UNSET:
            field_dict["total_breakpoints"] = total_breakpoints
        if volley_unforced_errors is not UNSET:
            field_dict["volley_unforced_errors"] = volley_unforced_errors
        if volley_winners is not UNSET:
            field_dict["volley_winners"] = volley_winners

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aces = d.pop("aces", UNSET)

        backhand_errors = d.pop("backhand_errors", UNSET)

        backhand_unforced_errors = d.pop("backhand_unforced_errors", UNSET)

        backhand_winners = d.pop("backhand_winners", UNSET)

        breakpoints_won = d.pop("breakpoints_won", UNSET)

        double_faults = d.pop("double_faults", UNSET)

        drop_shot_unforced_errors = d.pop("drop_shot_unforced_errors", UNSET)

        drop_shot_winners = d.pop("drop_shot_winners", UNSET)

        first_serve_points_won = d.pop("first_serve_points_won", UNSET)

        first_serve_successful = d.pop("first_serve_successful", UNSET)

        forehand_errors = d.pop("forehand_errors", UNSET)

        forehand_unforced_errors = d.pop("forehand_unforced_errors", UNSET)

        forehand_winners = d.pop("forehand_winners", UNSET)

        games_won = d.pop("games_won", UNSET)

        groundstroke_errors = d.pop("groundstroke_errors", UNSET)

        groundstroke_unforced_errors = d.pop("groundstroke_unforced_errors", UNSET)

        groundstroke_winners = d.pop("groundstroke_winners", UNSET)

        lob_unforced_errors = d.pop("lob_unforced_errors", UNSET)

        lob_winners = d.pop("lob_winners", UNSET)

        max_games_in_a_row = d.pop("max_games_in_a_row", UNSET)

        max_points_in_a_row = d.pop("max_points_in_a_row", UNSET)

        overhead_stroke_errors = d.pop("overhead_stroke_errors", UNSET)

        overhead_stroke_unforced_errors = d.pop("overhead_stroke_unforced_errors", UNSET)

        overhead_stroke_winners = d.pop("overhead_stroke_winners", UNSET)

        points_won = d.pop("points_won", UNSET)

        points_won_from_last_10 = d.pop("points_won_from_last_10", UNSET)

        return_errors = d.pop("return_errors", UNSET)

        return_errors_unforced = d.pop("return_errors_unforced", UNSET)

        return_winners = d.pop("return_winners", UNSET)

        returns_played = d.pop("returns_played", UNSET)

        second_serve_points_won = d.pop("second_serve_points_won", UNSET)

        second_serve_successful = d.pop("second_serve_successful", UNSET)

        service_games_won = d.pop("service_games_won", UNSET)

        service_points_lost = d.pop("service_points_lost", UNSET)

        service_points_won = d.pop("service_points_won", UNSET)

        tiebreaks_won = d.pop("tiebreaks_won", UNSET)

        total_breakpoints = d.pop("total_breakpoints", UNSET)

        volley_unforced_errors = d.pop("volley_unforced_errors", UNSET)

        volley_winners = d.pop("volley_winners", UNSET)

        sport_event_statistics_period_competitors_item_statistics = cls(
            aces=aces,
            backhand_errors=backhand_errors,
            backhand_unforced_errors=backhand_unforced_errors,
            backhand_winners=backhand_winners,
            breakpoints_won=breakpoints_won,
            double_faults=double_faults,
            drop_shot_unforced_errors=drop_shot_unforced_errors,
            drop_shot_winners=drop_shot_winners,
            first_serve_points_won=first_serve_points_won,
            first_serve_successful=first_serve_successful,
            forehand_errors=forehand_errors,
            forehand_unforced_errors=forehand_unforced_errors,
            forehand_winners=forehand_winners,
            games_won=games_won,
            groundstroke_errors=groundstroke_errors,
            groundstroke_unforced_errors=groundstroke_unforced_errors,
            groundstroke_winners=groundstroke_winners,
            lob_unforced_errors=lob_unforced_errors,
            lob_winners=lob_winners,
            max_games_in_a_row=max_games_in_a_row,
            max_points_in_a_row=max_points_in_a_row,
            overhead_stroke_errors=overhead_stroke_errors,
            overhead_stroke_unforced_errors=overhead_stroke_unforced_errors,
            overhead_stroke_winners=overhead_stroke_winners,
            points_won=points_won,
            points_won_from_last_10=points_won_from_last_10,
            return_errors=return_errors,
            return_errors_unforced=return_errors_unforced,
            return_winners=return_winners,
            returns_played=returns_played,
            second_serve_points_won=second_serve_points_won,
            second_serve_successful=second_serve_successful,
            service_games_won=service_games_won,
            service_points_lost=service_points_lost,
            service_points_won=service_points_won,
            tiebreaks_won=tiebreaks_won,
            total_breakpoints=total_breakpoints,
            volley_unforced_errors=volley_unforced_errors,
            volley_winners=volley_winners,
        )

        sport_event_statistics_period_competitors_item_statistics.additional_properties = d
        return sport_event_statistics_period_competitors_item_statistics

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
