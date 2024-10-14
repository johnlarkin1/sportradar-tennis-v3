import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_simple_team_mappings_response_200_simple_team_mappings_item import (
        GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem,
    )


T = TypeVar("T", bound="GetSeasonSimpleTeamMappingsResponse200")


@_attrs_define
class GetSeasonSimpleTeamMappingsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        simple_team_mappings (Union[Unset, List['GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    simple_team_mappings: Union[Unset, List["GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        simple_team_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.simple_team_mappings, Unset):
            simple_team_mappings = []
            for simple_team_mappings_item_data in self.simple_team_mappings:
                simple_team_mappings_item = simple_team_mappings_item_data.to_dict()
                simple_team_mappings.append(simple_team_mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if simple_team_mappings is not UNSET:
            field_dict["simple_team_mappings"] = simple_team_mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_simple_team_mappings_response_200_simple_team_mappings_item import (
            GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        simple_team_mappings = []
        _simple_team_mappings = d.pop("simple_team_mappings", UNSET)
        for simple_team_mappings_item_data in _simple_team_mappings or []:
            simple_team_mappings_item = GetSeasonSimpleTeamMappingsResponse200SimpleTeamMappingsItem.from_dict(
                simple_team_mappings_item_data
            )

            simple_team_mappings.append(simple_team_mappings_item)

        get_season_simple_team_mappings_response_200 = cls(
            generated_at=generated_at,
            simple_team_mappings=simple_team_mappings,
        )

        return get_season_simple_team_mappings_response_200
