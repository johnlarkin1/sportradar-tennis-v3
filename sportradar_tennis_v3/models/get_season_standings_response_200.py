import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_standings_response_200_standings_item import GetSeasonStandingsResponse200StandingsItem


T = TypeVar("T", bound="GetSeasonStandingsResponse200")


@_attrs_define
class GetSeasonStandingsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        standings (Union[Unset, List['GetSeasonStandingsResponse200StandingsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    standings: Union[Unset, List["GetSeasonStandingsResponse200StandingsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        standings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = []
            for standings_item_data in self.standings:
                standings_item = standings_item_data.to_dict()
                standings.append(standings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if standings is not UNSET:
            field_dict["standings"] = standings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_standings_response_200_standings_item import GetSeasonStandingsResponse200StandingsItem

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        standings = []
        _standings = d.pop("standings", UNSET)
        for standings_item_data in _standings or []:
            standings_item = GetSeasonStandingsResponse200StandingsItem.from_dict(standings_item_data)

            standings.append(standings_item)

        get_season_standings_response_200 = cls(
            generated_at=generated_at,
            standings=standings,
        )

        return get_season_standings_response_200
