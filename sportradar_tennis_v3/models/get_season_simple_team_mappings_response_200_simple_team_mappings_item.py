from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_simple_team_mappings_response_200_simple_team_mappings_item_mappings_item import (
        GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItemMappingsItem,
    )


T = TypeVar("T", bound="GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem")


@_attrs_define
class GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem:
    """
    Attributes:
        id (str): Competitor URN (sr:competitor:x)
        name (str):
        division (Union[Unset, int]):
        mappings (Union[Unset, List['GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItemMappingsItem']]):
        state (Union[Unset, str]):
        virtual (Union[Unset, bool]):
    """

    id: str
    name: str
    division: Union[Unset, int] = UNSET
    mappings: Union[Unset, List["GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItemMappingsItem"]] = UNSET
    state: Union[Unset, str] = UNSET
    virtual: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        division = self.division

        mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        state = self.state

        virtual = self.virtual

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if division is not UNSET:
            field_dict["division"] = division
        if mappings is not UNSET:
            field_dict["mappings"] = mappings
        if state is not UNSET:
            field_dict["state"] = state
        if virtual is not UNSET:
            field_dict["virtual"] = virtual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_simple_team_mappings_response_200_simple_team_mappings_item_mappings_item import (
            GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItemMappingsItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        division = d.pop("division", UNSET)

        mappings = []
        _mappings = d.pop("mappings", UNSET)
        for mappings_item_data in _mappings or []:
            mappings_item = GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItemMappingsItem.from_dict(
                mappings_item_data
            )

            mappings.append(mappings_item)

        state = d.pop("state", UNSET)

        virtual = d.pop("virtual", UNSET)

        get_season_simple_team_mappings_response_200_simple_team_mappings_item = cls(
            id=id,
            name=name,
            division=division,
            mappings=mappings,
            state=state,
            virtual=virtual,
        )

        return get_season_simple_team_mappings_response_200_simple_team_mappings_item
