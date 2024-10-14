from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.simple_tournament_mapping_level import SimpleTournamentMappingLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_tournament_mapping_groups_item import SimpleTournamentMappingGroupsItem


T = TypeVar("T", bound="SimpleTournamentMapping")


@_attrs_define
class SimpleTournamentMapping:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        alternative_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        groups (Union[Unset, List['SimpleTournamentMappingGroupsItem']]):
        level (Union[Unset, SimpleTournamentMappingLevel]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    alternative_name: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    groups: Union[Unset, List["SimpleTournamentMappingGroupsItem"]] = UNSET
    level: Union[Unset, SimpleTournamentMappingLevel] = UNSET
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        alternative_name = self.alternative_name

        gender = self.gender

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

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
        if gender is not UNSET:
            field_dict["gender"] = gender
        if groups is not UNSET:
            field_dict["groups"] = groups
        if level is not UNSET:
            field_dict["level"] = level
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.simple_tournament_mapping_groups_item import SimpleTournamentMappingGroupsItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        alternative_name = d.pop("alternative_name", UNSET)

        gender = d.pop("gender", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SimpleTournamentMappingGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        _level = d.pop("level", UNSET)
        level: Union[Unset, SimpleTournamentMappingLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = SimpleTournamentMappingLevel(_level)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        simple_tournament_mapping = cls(
            id=id,
            name=name,
            alternative_name=alternative_name,
            gender=gender,
            groups=groups,
            level=level,
            parent_id=parent_id,
            type=type,
        )

        return simple_tournament_mapping
