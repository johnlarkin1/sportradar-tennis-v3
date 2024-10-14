import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.get_double_race_rankings_response_200_rankings_item_competitor_rankings_item_competitor_players_item_gender import (
    GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItemGender,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItem")


@_attrs_define
class GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItem:
    """
    Attributes:
        id (str):
        name (str):
        abbreviation (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        date_of_birth (Union[Unset, datetime.date]): YYYY-MM-DD
        gender (Union[Unset,
            GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItemGender]):
        height (Union[Unset, int]): Height in cm
        nationality (Union[Unset, str]):
        weight (Union[Unset, int]): Weight in kg
    """

    id: str
    name: str
    abbreviation: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    gender: Union[
        Unset, GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItemGender
    ] = UNSET
    height: Union[Unset, int] = UNSET
    nationality: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        country = self.country

        country_code = self.country_code

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        height = self.height

        nationality = self.nationality

        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if height is not UNSET:
            field_dict["height"] = height
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("country_code", UNSET)

        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

        _gender = d.pop("gender", UNSET)
        gender: Union[
            Unset, GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItemGender
        ]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = GetDoubleRaceRankingsResponse200RankingsItemCompetitorRankingsItemCompetitorPlayersItemGender(
                _gender
            )

        height = d.pop("height", UNSET)

        nationality = d.pop("nationality", UNSET)

        weight = d.pop("weight", UNSET)

        get_double_race_rankings_response_200_rankings_item_competitor_rankings_item_competitor_players_item = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            country=country,
            country_code=country_code,
            date_of_birth=date_of_birth,
            gender=gender,
            height=height,
            nationality=nationality,
            weight=weight,
        )

        return get_double_race_rankings_response_200_rankings_item_competitor_rankings_item_competitor_players_item
