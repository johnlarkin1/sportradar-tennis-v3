from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_category_competitions_response_200_competitions_item_level import (
    GetCategoryCompetitionsResponse200CompetitionsItemLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_competitions_response_200_competitions_item_category import (
        GetCategoryCompetitionsResponse200CompetitionsItemCategory,
    )


T = TypeVar("T", bound="GetCategoryCompetitionsResponse200CompetitionsItem")


@_attrs_define
class GetCategoryCompetitionsResponse200CompetitionsItem:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        category (Union[Unset, GetCategoryCompetitionsResponse200CompetitionsItemCategory]):
        gender (Union[Unset, str]):
        level (Union[Unset, GetCategoryCompetitionsResponse200CompetitionsItemLevel]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    category: Union[Unset, "GetCategoryCompetitionsResponse200CompetitionsItemCategory"] = UNSET
    gender: Union[Unset, str] = UNSET
    level: Union[Unset, GetCategoryCompetitionsResponse200CompetitionsItemLevel] = UNSET
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        gender = self.gender

        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        parent_id = self.parent_id

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if gender is not UNSET:
            field_dict["gender"] = gender
        if level is not UNSET:
            field_dict["level"] = level
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_category_competitions_response_200_competitions_item_category import (
            GetCategoryCompetitionsResponse200CompetitionsItemCategory,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _category = d.pop("category", UNSET)
        category: Union[Unset, GetCategoryCompetitionsResponse200CompetitionsItemCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = GetCategoryCompetitionsResponse200CompetitionsItemCategory.from_dict(_category)

        gender = d.pop("gender", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, GetCategoryCompetitionsResponse200CompetitionsItemLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = GetCategoryCompetitionsResponse200CompetitionsItemLevel(_level)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        get_category_competitions_response_200_competitions_item = cls(
            id=id,
            name=name,
            category=category,
            gender=gender,
            level=level,
            parent_id=parent_id,
            type=type,
        )

        return get_category_competitions_response_200_competitions_item
