import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_competitions_response_200_competitions_item import (
        GetCategoryCompetitionsResponse200CompetitionsItem,
    )


T = TypeVar("T", bound="GetCategoryCompetitionsResponse200")


@_attrs_define
class GetCategoryCompetitionsResponse200:
    """
    Attributes:
        competitions (Union[Unset, List['GetCategoryCompetitionsResponse200CompetitionsItem']]):
        generated_at (Union[Unset, datetime.datetime]):
    """

    competitions: Union[Unset, List["GetCategoryCompetitionsResponse200CompetitionsItem"]] = UNSET
    generated_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitions, Unset):
            competitions = []
            for competitions_item_data in self.competitions:
                competitions_item = competitions_item_data.to_dict()
                competitions.append(competitions_item)

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitions is not UNSET:
            field_dict["competitions"] = competitions
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_category_competitions_response_200_competitions_item import (
            GetCategoryCompetitionsResponse200CompetitionsItem,
        )

        d = src_dict.copy()
        competitions = []
        _competitions = d.pop("competitions", UNSET)
        for competitions_item_data in _competitions or []:
            competitions_item = GetCategoryCompetitionsResponse200CompetitionsItem.from_dict(competitions_item_data)

            competitions.append(competitions_item)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        get_category_competitions_response_200 = cls(
            competitions=competitions,
            generated_at=generated_at,
        )

        return get_category_competitions_response_200
