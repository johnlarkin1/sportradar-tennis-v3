from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetStreamStatisticsResponse200Type1")


@_attrs_define
class GetStreamStatisticsResponse200Type1:
    """
    Attributes:
        from_ (int):
        package (str):
        to (int):
        type (str):
    """

    from_: int
    package: str
    to: int
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        package = self.package

        to = self.to

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "package": package,
                "to": to,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from")

        package = d.pop("package")

        to = d.pop("to")

        type = d.pop("type")

        get_stream_statistics_response_200_type_1 = cls(
            from_=from_,
            package=package,
            to=to,
            type=type,
        )

        get_stream_statistics_response_200_type_1.additional_properties = d
        return get_stream_statistics_response_200_type_1

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
