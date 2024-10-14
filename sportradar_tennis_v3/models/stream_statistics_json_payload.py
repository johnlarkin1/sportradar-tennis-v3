from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stream_statistics_json_payload_sport_event_status import StreamStatisticsJsonPayloadSportEventStatus
    from ..models.stream_statistics_json_payload_statistics_item import StreamStatisticsJsonPayloadStatisticsItem


T = TypeVar("T", bound="StreamStatisticsJsonPayload")


@_attrs_define
class StreamStatisticsJsonPayload:
    """
    Attributes:
        sport_event_status (Union[Unset, StreamStatisticsJsonPayloadSportEventStatus]):
        statistics (Union[Unset, List['StreamStatisticsJsonPayloadStatisticsItem']]):
    """

    sport_event_status: Union[Unset, "StreamStatisticsJsonPayloadSportEventStatus"] = UNSET
    statistics: Union[Unset, List["StreamStatisticsJsonPayloadStatisticsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sport_event_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_status, Unset):
            sport_event_status = self.sport_event_status.to_dict()

        statistics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = []
            for statistics_item_data in self.statistics:
                statistics_item = statistics_item_data.to_dict()
                statistics.append(statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sport_event_status is not UNSET:
            field_dict["sport_event_status"] = sport_event_status
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stream_statistics_json_payload_sport_event_status import (
            StreamStatisticsJsonPayloadSportEventStatus,
        )
        from ..models.stream_statistics_json_payload_statistics_item import StreamStatisticsJsonPayloadStatisticsItem

        d = src_dict.copy()
        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, StreamStatisticsJsonPayloadSportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = StreamStatisticsJsonPayloadSportEventStatus.from_dict(_sport_event_status)

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = StreamStatisticsJsonPayloadStatisticsItem.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        stream_statistics_json_payload = cls(
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        stream_statistics_json_payload.additional_properties = d
        return stream_statistics_json_payload

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
