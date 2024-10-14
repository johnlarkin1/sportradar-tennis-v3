from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_stream_events_response_200_type_0_metadata import GetStreamEventsResponse200Type0Metadata
    from ..models.get_stream_events_response_200_type_0_payload import GetStreamEventsResponse200Type0Payload


T = TypeVar("T", bound="GetStreamEventsResponse200Type0")


@_attrs_define
class GetStreamEventsResponse200Type0:
    """
    Attributes:
        metadata (Union[Unset, GetStreamEventsResponse200Type0Metadata]):
        payload (Union[Unset, GetStreamEventsResponse200Type0Payload]):
    """

    metadata: Union[Unset, "GetStreamEventsResponse200Type0Metadata"] = UNSET
    payload: Union[Unset, "GetStreamEventsResponse200Type0Payload"] = UNSET
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
        from ..models.get_stream_events_response_200_type_0_metadata import GetStreamEventsResponse200Type0Metadata
        from ..models.get_stream_events_response_200_type_0_payload import GetStreamEventsResponse200Type0Payload

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, GetStreamEventsResponse200Type0Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GetStreamEventsResponse200Type0Metadata.from_dict(_metadata)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, GetStreamEventsResponse200Type0Payload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = GetStreamEventsResponse200Type0Payload.from_dict(_payload)

        get_stream_events_response_200_type_0 = cls(
            metadata=metadata,
            payload=payload,
        )

        get_stream_events_response_200_type_0.additional_properties = d
        return get_stream_events_response_200_type_0

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
