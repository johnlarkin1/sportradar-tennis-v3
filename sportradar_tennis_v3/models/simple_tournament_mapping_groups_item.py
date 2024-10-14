from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_tournament_mapping_groups_item_mappings_item import (
        SimpleTournamentMappingGroupsItemMappingsItem,
    )


T = TypeVar("T", bound="SimpleTournamentMappingGroupsItem")


@_attrs_define
class SimpleTournamentMappingGroupsItem:
    """
    Attributes:
        id (str):
        name (str):
        mappings (Union[Unset, List['SimpleTournamentMappingGroupsItemMappingsItem']]):
    """

    id: str
    name: str
    mappings: Union[Unset, List["SimpleTournamentMappingGroupsItemMappingsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.simple_tournament_mapping_groups_item_mappings_item import (
            SimpleTournamentMappingGroupsItemMappingsItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        mappings = []
        _mappings = d.pop("mappings", UNSET)
        for mappings_item_data in _mappings or []:
            mappings_item = SimpleTournamentMappingGroupsItemMappingsItem.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        simple_tournament_mapping_groups_item = cls(
            id=id,
            name=name,
            mappings=mappings,
        )

        return simple_tournament_mapping_groups_item
