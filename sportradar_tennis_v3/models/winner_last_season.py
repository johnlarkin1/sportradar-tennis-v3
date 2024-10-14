from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.winner_last_season_competitor import WinnerLastSeasonCompetitor


T = TypeVar("T", bound="WinnerLastSeason")


@_attrs_define
class WinnerLastSeason:
    """
    Attributes:
        competitor (Union[Unset, WinnerLastSeasonCompetitor]):
    """

    competitor: Union[Unset, "WinnerLastSeasonCompetitor"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitor is not UNSET:
            field_dict["competitor"] = competitor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.winner_last_season_competitor import WinnerLastSeasonCompetitor

        d = src_dict.copy()
        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, WinnerLastSeasonCompetitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = WinnerLastSeasonCompetitor.from_dict(_competitor)

        winner_last_season = cls(
            competitor=competitor,
        )

        return winner_last_season
