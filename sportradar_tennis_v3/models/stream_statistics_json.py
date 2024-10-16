from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stream_statistics_json_metadata import StreamStatisticsJsonMetadata
    from ..models.stream_statistics_json_payload import StreamStatisticsJsonPayload


T = TypeVar("T", bound="StreamStatisticsJson")


@_attrs_define
class StreamStatisticsJson:
    """
    Attributes:
        metadata (Union[Unset, StreamStatisticsJsonMetadata]):
        payload (Union[Unset, StreamStatisticsJsonPayload]):
    """

    metadata: Union[Unset, "StreamStatisticsJsonMetadata"] = UNSET
    payload: Union[Unset, "StreamStatisticsJsonPayload"] = UNSET
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
        from ..models.stream_statistics_json_metadata import StreamStatisticsJsonMetadata
        from ..models.stream_statistics_json_payload import StreamStatisticsJsonPayload

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, StreamStatisticsJsonMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StreamStatisticsJsonMetadata.from_dict(_metadata)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, StreamStatisticsJsonPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = StreamStatisticsJsonPayload.from_dict(_payload)

        stream_statistics_json = cls(
            metadata=metadata,
            payload=payload,
        )

        stream_statistics_json.additional_properties = d
        return stream_statistics_json

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
