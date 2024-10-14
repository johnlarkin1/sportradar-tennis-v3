from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_stream_statistics_response_200_type_0_payload_sport_event_status import (
        GetStreamStatisticsResponse200Type0PayloadSportEventStatus,
    )
    from ..models.get_stream_statistics_response_200_type_0_payload_statistics_item import (
        GetStreamStatisticsResponse200Type0PayloadStatisticsItem,
    )


T = TypeVar("T", bound="GetStreamStatisticsResponse200Type0Payload")


@_attrs_define
class GetStreamStatisticsResponse200Type0Payload:
    """
    Attributes:
        sport_event_status (Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatus]):
        statistics (Union[Unset, List['GetStreamStatisticsResponse200Type0PayloadStatisticsItem']]):
    """

    sport_event_status: Union[Unset, "GetStreamStatisticsResponse200Type0PayloadSportEventStatus"] = UNSET
    statistics: Union[Unset, List["GetStreamStatisticsResponse200Type0PayloadStatisticsItem"]] = UNSET
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
        from ..models.get_stream_statistics_response_200_type_0_payload_sport_event_status import (
            GetStreamStatisticsResponse200Type0PayloadSportEventStatus,
        )
        from ..models.get_stream_statistics_response_200_type_0_payload_statistics_item import (
            GetStreamStatisticsResponse200Type0PayloadStatisticsItem,
        )

        d = src_dict.copy()
        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, GetStreamStatisticsResponse200Type0PayloadSportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = GetStreamStatisticsResponse200Type0PayloadSportEventStatus.from_dict(
                _sport_event_status
            )

        statistics = []
        _statistics = d.pop("statistics", UNSET)
        for statistics_item_data in _statistics or []:
            statistics_item = GetStreamStatisticsResponse200Type0PayloadStatisticsItem.from_dict(statistics_item_data)

            statistics.append(statistics_item)

        get_stream_statistics_response_200_type_0_payload = cls(
            sport_event_status=sport_event_status,
            statistics=statistics,
        )

        get_stream_statistics_response_200_type_0_payload.additional_properties = d
        return get_stream_statistics_response_200_type_0_payload

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
