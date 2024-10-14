from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ranking_competitor_competitor_gender import RankingCompetitorCompetitorGender
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranking_competitor_competitor_players_item import RankingCompetitorCompetitorPlayersItem


T = TypeVar("T", bound="RankingCompetitorCompetitor")


@_attrs_define
class RankingCompetitorCompetitor:
    """
    Attributes:
        id (str): Competitor URN (sr:competitor:x)
        name (str):
        abbreviation (Union[Unset, str]):
        bracket_number (Union[Unset, int]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        gender (Union[Unset, RankingCompetitorCompetitorGender]):
        players (Union[Unset, List['RankingCompetitorCompetitorPlayersItem']]):
        qualifier (Union[Unset, str]):
        seed (Union[Unset, int]):
        virtual (Union[Unset, bool]):
    """

    id: str
    name: str
    abbreviation: Union[Unset, str] = UNSET
    bracket_number: Union[Unset, int] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    gender: Union[Unset, RankingCompetitorCompetitorGender] = UNSET
    players: Union[Unset, List["RankingCompetitorCompetitorPlayersItem"]] = UNSET
    qualifier: Union[Unset, str] = UNSET
    seed: Union[Unset, int] = UNSET
    virtual: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        bracket_number = self.bracket_number

        country = self.country

        country_code = self.country_code

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        players: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        qualifier = self.qualifier

        seed = self.seed

        virtual = self.virtual

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if bracket_number is not UNSET:
            field_dict["bracket_number"] = bracket_number
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if gender is not UNSET:
            field_dict["gender"] = gender
        if players is not UNSET:
            field_dict["players"] = players
        if qualifier is not UNSET:
            field_dict["qualifier"] = qualifier
        if seed is not UNSET:
            field_dict["seed"] = seed
        if virtual is not UNSET:
            field_dict["virtual"] = virtual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ranking_competitor_competitor_players_item import RankingCompetitorCompetitorPlayersItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        bracket_number = d.pop("bracket_number", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("country_code", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, RankingCompetitorCompetitorGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = RankingCompetitorCompetitorGender(_gender)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in _players or []:
            players_item = RankingCompetitorCompetitorPlayersItem.from_dict(players_item_data)

            players.append(players_item)

        qualifier = d.pop("qualifier", UNSET)

        seed = d.pop("seed", UNSET)

        virtual = d.pop("virtual", UNSET)

        ranking_competitor_competitor = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            bracket_number=bracket_number,
            country=country,
            country_code=country_code,
            gender=gender,
            players=players,
            qualifier=qualifier,
            seed=seed,
            virtual=virtual,
        )

        ranking_competitor_competitor.additional_properties = d
        return ranking_competitor_competitor

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
