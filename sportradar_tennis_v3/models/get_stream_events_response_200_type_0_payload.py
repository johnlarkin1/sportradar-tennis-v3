from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_stream_events_response_200_type_0_payload_event import GetStreamEventsResponse200Type0PayloadEvent
    from ..models.get_stream_events_response_200_type_0_payload_sport_event_status import (
        GetStreamEventsResponse200Type0PayloadSportEventStatus,
    )


T = TypeVar("T", bound="GetStreamEventsResponse200Type0Payload")


@_attrs_define
class GetStreamEventsResponse200Type0Payload:
    """
    Attributes:
        event (Union[Unset, GetStreamEventsResponse200Type0PayloadEvent]):
        sport_event_status (Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatus]):
    """

    event: Union[Unset, "GetStreamEventsResponse200Type0PayloadEvent"] = UNSET
    sport_event_status: Union[Unset, "GetStreamEventsResponse200Type0PayloadSportEventStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        sport_event_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_status, Unset):
            sport_event_status = self.sport_event_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if sport_event_status is not UNSET:
            field_dict["sport_event_status"] = sport_event_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_stream_events_response_200_type_0_payload_event import (
            GetStreamEventsResponse200Type0PayloadEvent,
        )
        from ..models.get_stream_events_response_200_type_0_payload_sport_event_status import (
            GetStreamEventsResponse200Type0PayloadSportEventStatus,
        )

        d = src_dict.copy()
        _event = d.pop("event", UNSET)
        event: Union[Unset, GetStreamEventsResponse200Type0PayloadEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = GetStreamEventsResponse200Type0PayloadEvent.from_dict(_event)

        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, GetStreamEventsResponse200Type0PayloadSportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = GetStreamEventsResponse200Type0PayloadSportEventStatus.from_dict(_sport_event_status)

        get_stream_events_response_200_type_0_payload = cls(
            event=event,
            sport_event_status=sport_event_status,
        )

        get_stream_events_response_200_type_0_payload.additional_properties = d
        return get_stream_events_response_200_type_0_payload

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
