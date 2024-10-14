from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.competition_with_category_level import CompetitionWithCategoryLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_with_category_category import CompetitionWithCategoryCategory


T = TypeVar("T", bound="CompetitionWithCategory")


@_attrs_define
class CompetitionWithCategory:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        category (Union[Unset, CompetitionWithCategoryCategory]):
        gender (Union[Unset, str]):
        level (Union[Unset, CompetitionWithCategoryLevel]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    category: Union[Unset, "CompetitionWithCategoryCategory"] = UNSET
    gender: Union[Unset, str] = UNSET
    level: Union[Unset, CompetitionWithCategoryLevel] = UNSET
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
        from ..models.competition_with_category_category import CompetitionWithCategoryCategory

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _category = d.pop("category", UNSET)
        category: Union[Unset, CompetitionWithCategoryCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CompetitionWithCategoryCategory.from_dict(_category)

        gender = d.pop("gender", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, CompetitionWithCategoryLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = CompetitionWithCategoryLevel(_level)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        competition_with_category = cls(
            id=id,
            name=name,
            category=category,
            gender=gender,
            level=level,
            parent_id=parent_id,
            type=type,
        )

        return competition_with_category
