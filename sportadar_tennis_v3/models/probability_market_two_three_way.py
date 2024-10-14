import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.probability_market_two_three_way_name import ProbabilityMarketTwoThreeWayName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.probability_outcome_two_three_way import ProbabilityOutcomeTwoThreeWay


T = TypeVar("T", bound="ProbabilityMarketTwoThreeWay")


@_attrs_define
class ProbabilityMarketTwoThreeWay:
    """
    Attributes:
        name (ProbabilityMarketTwoThreeWayName):
        outcomes (List['ProbabilityOutcomeTwoThreeWay']):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        last_updated (Union[Unset, datetime.datetime]):
        live (Union[Unset, bool]):
        match_time (Union[Unset, str]): [0-9]+:[0-9]+|[0-9]+
        remaining_time (Union[Unset, str]): [0-9]+:[0-9]+|[0-9]+
        remaining_time_in_period (Union[Unset, str]): [0-9]+:[0-9]+|[0-9]+
    """

    name: ProbabilityMarketTwoThreeWayName
    outcomes: List["ProbabilityOutcomeTwoThreeWay"]
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    live: Union[Unset, bool] = UNSET
    match_time: Union[Unset, str] = UNSET
    remaining_time: Union[Unset, str] = UNSET
    remaining_time_in_period: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.value

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        away_score = self.away_score

        home_score = self.home_score

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        live = self.live

        match_time = self.match_time

        remaining_time = self.remaining_time

        remaining_time_in_period = self.remaining_time_in_period

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "outcomes": outcomes,
            }
        )
        if away_score is not UNSET:
            field_dict["away_score"] = away_score
        if home_score is not UNSET:
            field_dict["home_score"] = home_score
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if live is not UNSET:
            field_dict["live"] = live
        if match_time is not UNSET:
            field_dict["match_time"] = match_time
        if remaining_time is not UNSET:
            field_dict["remaining_time"] = remaining_time
        if remaining_time_in_period is not UNSET:
            field_dict["remaining_time_in_period"] = remaining_time_in_period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.probability_outcome_two_three_way import ProbabilityOutcomeTwoThreeWay

        d = src_dict.copy()
        name = ProbabilityMarketTwoThreeWayName(d.pop("name"))

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = ProbabilityOutcomeTwoThreeWay.from_dict(outcomes_item_data)

            outcomes.append(outcomes_item)

        away_score = d.pop("away_score", UNSET)

        home_score = d.pop("home_score", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        live = d.pop("live", UNSET)

        match_time = d.pop("match_time", UNSET)

        remaining_time = d.pop("remaining_time", UNSET)

        remaining_time_in_period = d.pop("remaining_time_in_period", UNSET)

        probability_market_two_three_way = cls(
            name=name,
            outcomes=outcomes,
            away_score=away_score,
            home_score=home_score,
            last_updated=last_updated,
            live=live,
            match_time=match_time,
            remaining_time=remaining_time,
            remaining_time_in_period=remaining_time_in_period,
        )

        return probability_market_two_three_way
