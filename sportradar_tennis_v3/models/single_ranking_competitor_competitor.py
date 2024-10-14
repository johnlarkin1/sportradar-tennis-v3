from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleRankingCompetitorCompetitor")


@_attrs_define
class SingleRankingCompetitorCompetitor:
    """
    Attributes:
        id (str): Competitor URN (sr:competitor:x)
        name (str):
        abbreviation (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        date_of_birth (Union[Unset, str]):
        qualifier (Union[Unset, str]):
        virtual (Union[Unset, bool]):
    """

    id: str
    name: str
    abbreviation: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    qualifier: Union[Unset, str] = UNSET
    virtual: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        abbreviation = self.abbreviation

        country = self.country

        country_code = self.country_code

        date_of_birth = self.date_of_birth

        qualifier = self.qualifier

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
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if qualifier is not UNSET:
            field_dict["qualifier"] = qualifier
        if virtual is not UNSET:
            field_dict["virtual"] = virtual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        abbreviation = d.pop("abbreviation", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("country_code", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        qualifier = d.pop("qualifier", UNSET)

        virtual = d.pop("virtual", UNSET)

        single_ranking_competitor_competitor = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            country=country,
            country_code=country_code,
            date_of_birth=date_of_birth,
            qualifier=qualifier,
            virtual=virtual,
        )

        single_ranking_competitor_competitor.additional_properties = d
        return single_ranking_competitor_competitor

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
