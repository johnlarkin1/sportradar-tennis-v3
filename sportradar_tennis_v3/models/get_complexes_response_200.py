import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_complexes_response_200_complexes_item import GetComplexesResponse200ComplexesItem


T = TypeVar("T", bound="GetComplexesResponse200")


@_attrs_define
class GetComplexesResponse200:
    """
    Attributes:
        complexes (Union[Unset, List['GetComplexesResponse200ComplexesItem']]):
        generated_at (Union[Unset, datetime.datetime]):
    """

    complexes: Union[Unset, List["GetComplexesResponse200ComplexesItem"]] = UNSET
    generated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        complexes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.complexes, Unset):
            complexes = []
            for complexes_item_data in self.complexes:
                complexes_item = complexes_item_data.to_dict()
                complexes.append(complexes_item)

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complexes is not UNSET:
            field_dict["complexes"] = complexes
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_complexes_response_200_complexes_item import GetComplexesResponse200ComplexesItem

        d = src_dict.copy()
        complexes = []
        _complexes = d.pop("complexes", UNSET)
        for complexes_item_data in _complexes or []:
            complexes_item = GetComplexesResponse200ComplexesItem.from_dict(complexes_item_data)

            complexes.append(complexes_item)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        get_complexes_response_200 = cls(
            complexes=complexes,
            generated_at=generated_at,
        )

        get_complexes_response_200.additional_properties = d
        return get_complexes_response_200

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
