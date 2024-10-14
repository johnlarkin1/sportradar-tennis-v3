import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_itf_mappings_response_200_mappings_item import (
        GetCompetitorItfMappingsResponse200MappingsItem,
    )


T = TypeVar("T", bound="GetCompetitorItfMappingsResponse200")


@_attrs_define
class GetCompetitorItfMappingsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        mappings (Union[Unset, List['GetCompetitorItfMappingsResponse200MappingsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    mappings: Union[Unset, List["GetCompetitorItfMappingsResponse200MappingsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_itf_mappings_response_200_mappings_item import (
            GetCompetitorItfMappingsResponse200MappingsItem,
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
            mappings_item = GetCompetitorItfMappingsResponse200MappingsItem.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        get_competitor_itf_mappings_response_200 = cls(
            generated_at=generated_at,
            mappings=mappings,
        )

        get_competitor_itf_mappings_response_200.additional_properties = d
        return get_competitor_itf_mappings_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
