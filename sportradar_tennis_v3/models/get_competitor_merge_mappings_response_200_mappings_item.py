from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompetitorMergeMappingsResponse200MappingsItem")


@_attrs_define
class GetCompetitorMergeMappingsResponse200MappingsItem:
    """
    Attributes:
        merged_id (str):
        retained_id (str):
        name (Union[Unset, str]):
    """

    merged_id: str
    retained_id: str
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        merged_id = self.merged_id

        retained_id = self.retained_id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "merged_id": merged_id,
                "retained_id": retained_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        merged_id = d.pop("merged_id")

        retained_id = d.pop("retained_id")

        name = d.pop("name", UNSET)

        get_competitor_merge_mappings_response_200_mappings_item = cls(
            merged_id=merged_id,
            retained_id=retained_id,
            name=name,
        )

        return get_competitor_merge_mappings_response_200_mappings_item
