from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompetitorItfMappingsResponse200MappingsItem")


@_attrs_define
class GetCompetitorItfMappingsResponse200MappingsItem:
    """
    Attributes:
        external_id (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    external_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_id = d.pop("external_id", UNSET)

        id = d.pop("id", UNSET)

        get_competitor_itf_mappings_response_200_mappings_item = cls(
            external_id=external_id,
            id=id,
        )

        get_competitor_itf_mappings_response_200_mappings_item.additional_properties = d
        return get_competitor_itf_mappings_response_200_mappings_item

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
