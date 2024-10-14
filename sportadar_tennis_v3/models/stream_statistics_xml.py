from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stream_metadata import StreamMetadata
    from ..models.stream_statistics_xml_payload import StreamStatisticsXmlPayload


T = TypeVar("T", bound="StreamStatisticsXml")


@_attrs_define
class StreamStatisticsXml:
    """
    Attributes:
        metadata (Union[Unset, StreamMetadata]):
        payload (Union[Unset, StreamStatisticsXmlPayload]):
    """

    metadata: Union[Unset, "StreamMetadata"] = UNSET
    payload: Union[Unset, "StreamStatisticsXmlPayload"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stream_metadata import StreamMetadata
        from ..models.stream_statistics_xml_payload import StreamStatisticsXmlPayload

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, StreamMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StreamMetadata.from_dict(_metadata)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, StreamStatisticsXmlPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = StreamStatisticsXmlPayload.from_dict(_payload)

        stream_statistics_xml = cls(
            metadata=metadata,
            payload=payload,
        )

        stream_statistics_xml.additional_properties = d
        return stream_statistics_xml

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
