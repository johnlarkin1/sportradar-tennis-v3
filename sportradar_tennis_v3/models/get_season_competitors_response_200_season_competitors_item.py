from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_competitors_response_200_season_competitors_item_players_item import (
        GetSeasonCompetitorsResponse200SeasonCompetitorsItemPlayersItem,
    )


T = TypeVar("T", bound="GetSeasonCompetitorsResponse200SeasonCompetitorsItem")


@_attrs_define
class GetSeasonCompetitorsResponse200SeasonCompetitorsItem:
    """
    Attributes:
        id (str): Competitor URN (sr:competitor:x)
        name (str):
        abbreviation (Union[Unset, str]):
        players (Union[Unset, List['GetSeasonCompetitorsResponse200SeasonCompetitorsItemPlayersItem']]):
        short_name (Union[Unset, str]):
    """

    id: str
    name: str
    abbreviation: Union[Unset, str] = UNSET
    players: Union[Unset, List["GetSeasonCompetitorsResponse200SeasonCompetitorsItemPlayersItem"]] = UNSET
    short_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        players: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if players is not UNSET:
            field_dict["players"] = players
        if short_name is not UNSET:
            field_dict["short_name"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_competitors_response_200_season_competitors_item_players_item import (
            GetSeasonCompetitorsResponse200SeasonCompetitorsItemPlayersItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in _players or []:
            players_item = GetSeasonCompetitorsResponse200SeasonCompetitorsItemPlayersItem.from_dict(players_item_data)

            players.append(players_item)

        short_name = d.pop("short_name", UNSET)

        get_season_competitors_response_200_season_competitors_item = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            players=players,
            short_name=short_name,
        )

        return get_season_competitors_response_200_season_competitors_item
