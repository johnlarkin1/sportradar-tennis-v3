import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_simple_tournament_mappings_response_200_simple_tournament_mappings_item import (
        GetSeasonSimpleTournamentMappingsResponse200SimpleTournamentMappingsItem,
    )


T = TypeVar("T", bound="GetSeasonSimpleTournamentMappingsResponse200")


@_attrs_define
class GetSeasonSimpleTournamentMappingsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        simple_tournament_mappings (Union[Unset,
            List['GetSeasonSimpleTournamentMappingsResponse200SimpleTournamentMappingsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    simple_tournament_mappings: Union[
        Unset, List["GetSeasonSimpleTournamentMappingsResponse200SimpleTournamentMappingsItem"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        simple_tournament_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.simple_tournament_mappings, Unset):
            simple_tournament_mappings = []
            for simple_tournament_mappings_item_data in self.simple_tournament_mappings:
                simple_tournament_mappings_item = simple_tournament_mappings_item_data.to_dict()
                simple_tournament_mappings.append(simple_tournament_mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if simple_tournament_mappings is not UNSET:
            field_dict["simple_tournament_mappings"] = simple_tournament_mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_simple_tournament_mappings_response_200_simple_tournament_mappings_item import (
            GetSeasonSimpleTournamentMappingsResponse200SimpleTournamentMappingsItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        simple_tournament_mappings = []
        _simple_tournament_mappings = d.pop("simple_tournament_mappings", UNSET)
        for simple_tournament_mappings_item_data in _simple_tournament_mappings or []:
            simple_tournament_mappings_item = (
                GetSeasonSimpleTournamentMappingsResponse200SimpleTournamentMappingsItem.from_dict(
                    simple_tournament_mappings_item_data
                )
            )

            simple_tournament_mappings.append(simple_tournament_mappings_item)

        get_season_simple_tournament_mappings_response_200 = cls(
            generated_at=generated_at,
            simple_tournament_mappings=simple_tournament_mappings,
        )

        return get_season_simple_tournament_mappings_response_200
