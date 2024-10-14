from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoryCompetitionsResponse200CompetitionsItemCategory")


@_attrs_define
class GetCategoryCompetitionsResponse200CompetitionsItemCategory:
    """
    Attributes:
        id (str): Category URN (sr:category:x)
        name (str):
        country_code (Union[Unset, str]): ISO 3361-1 A3 Country Code
    """

    id: str
    name: str
    country_code: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        country_code = d.pop("country_code", UNSET)

        get_category_competitions_response_200_competitions_item_category = cls(
            id=id,
            name=name,
            country_code=country_code,
        )

        return get_category_competitions_response_200_competitions_item_category
