from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.period_score_type import PeriodScoreType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeriodScore")


@_attrs_define
class PeriodScore:
    """
    Attributes:
        away_score (int):
        home_score (int):
        away_tiebreak_score (Union[Unset, int]):
        home_tiebreak_score (Union[Unset, int]):
        number (Union[Unset, int]):
        type (Union[Unset, PeriodScoreType]):
    """

    away_score: int
    home_score: int
    away_tiebreak_score: Union[Unset, int] = UNSET
    home_tiebreak_score: Union[Unset, int] = UNSET
    number: Union[Unset, int] = UNSET
    type: Union[Unset, PeriodScoreType] = UNSET

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
        type: Union[Unset, PeriodScoreType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PeriodScoreType(_type)

        period_score = cls(
            away_score=away_score,
            home_score=home_score,
            away_tiebreak_score=away_tiebreak_score,
            home_tiebreak_score=home_tiebreak_score,
            number=number,
            type=type,
        )

        return period_score
