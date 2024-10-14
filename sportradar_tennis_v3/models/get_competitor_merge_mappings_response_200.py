import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_merge_mappings_response_200_mappings_item import (
        GetCompetitorMergeMappingsResponse200MappingsItem,
    )


T = TypeVar("T", bound="GetCompetitorMergeMappingsResponse200")


@_attrs_define
class GetCompetitorMergeMappingsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        mappings (Union[Unset, List['GetCompetitorMergeMappingsResponse200MappingsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    mappings: Union[Unset, List["GetCompetitorMergeMappingsResponse200MappingsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_merge_mappings_response_200_mappings_item import (
            GetCompetitorMergeMappingsResponse200MappingsItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        mappings = []
        _mappings = d.pop("mappings", UNSET)
        for mappings_item_data in _mappings or []:
            mappings_item = GetCompetitorMergeMappingsResponse200MappingsItem.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        get_competitor_merge_mappings_response_200 = cls(
            generated_at=generated_at,
            mappings=mappings,
        )

        return get_competitor_merge_mappings_response_200
