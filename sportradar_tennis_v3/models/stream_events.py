from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stream_events_metadata import StreamEventsMetadata
    from ..models.stream_events_payload import StreamEventsPayload


T = TypeVar("T", bound="StreamEvents")


@_attrs_define
class StreamEvents:
    """
    Attributes:
        metadata (Union[Unset, StreamEventsMetadata]):
        payload (Union[Unset, StreamEventsPayload]):
    """

    metadata: Union[Unset, "StreamEventsMetadata"] = UNSET
    payload: Union[Unset, "StreamEventsPayload"] = UNSET
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
        from ..models.stream_events_metadata import StreamEventsMetadata
        from ..models.stream_events_payload import StreamEventsPayload

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, StreamEventsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StreamEventsMetadata.from_dict(_metadata)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, StreamEventsPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = StreamEventsPayload.from_dict(_payload)

        stream_events = cls(
            metadata=metadata,
            payload=payload,
        )

        stream_events.additional_properties = d
        return stream_events

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
