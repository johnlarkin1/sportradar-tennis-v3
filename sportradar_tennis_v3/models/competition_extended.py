from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.competition_extended_level import CompetitionExtendedLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_extended_category import CompetitionExtendedCategory
    from ..models.competition_extended_children_item import CompetitionExtendedChildrenItem


T = TypeVar("T", bound="CompetitionExtended")


@_attrs_define
class CompetitionExtended:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        alternative_name (Union[Unset, str]):
        category (Union[Unset, CompetitionExtendedCategory]):
        children (Union[Unset, List['CompetitionExtendedChildrenItem']]):
        gender (Union[Unset, str]):
        level (Union[Unset, CompetitionExtendedLevel]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    alternative_name: Union[Unset, str] = UNSET
    category: Union[Unset, "CompetitionExtendedCategory"] = UNSET
    children: Union[Unset, List["CompetitionExtendedChildrenItem"]] = UNSET
    gender: Union[Unset, str] = UNSET
    level: Union[Unset, CompetitionExtendedLevel] = UNSET
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        alternative_name = self.alternative_name

        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

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
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if category is not UNSET:
            field_dict["category"] = category
        if children is not UNSET:
            field_dict["children"] = children
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
        from ..models.competition_extended_category import CompetitionExtendedCategory
        from ..models.competition_extended_children_item import CompetitionExtendedChildrenItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        alternative_name = d.pop("alternative_name", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, CompetitionExtendedCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CompetitionExtendedCategory.from_dict(_category)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = CompetitionExtendedChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        gender = d.pop("gender", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, CompetitionExtendedLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = CompetitionExtendedLevel(_level)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        competition_extended = cls(
            id=id,
            name=name,
            alternative_name=alternative_name,
            category=category,
            children=children,
            gender=gender,
            level=level,
            parent_id=parent_id,
            type=type,
        )

        return competition_extended
