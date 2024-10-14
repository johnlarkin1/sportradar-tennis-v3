from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_competition_with_category_category import BaseCompetitionWithCategoryCategory


T = TypeVar("T", bound="BaseCompetitionWithCategory")


@_attrs_define
class BaseCompetitionWithCategory:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        category (Union[Unset, BaseCompetitionWithCategoryCategory]):
        gender (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    category: Union[Unset, "BaseCompetitionWithCategoryCategory"] = UNSET
    gender: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        gender = self.gender

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
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_competition_with_category_category import BaseCompetitionWithCategoryCategory

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _category = d.pop("category", UNSET)
        category: Union[Unset, BaseCompetitionWithCategoryCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = BaseCompetitionWithCategoryCategory.from_dict(_category)

        gender = d.pop("gender", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        base_competition_with_category = cls(
            id=id,
            name=name,
            category=category,
            gender=gender,
            parent_id=parent_id,
            type=type,
        )

        return base_competition_with_category
