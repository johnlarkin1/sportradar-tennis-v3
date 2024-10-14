from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreamStatisticsXmlMetadata")


@_attrs_define
class StreamStatisticsXmlMetadata:
    """
    Attributes:
        competition_id (str):
        event_id (str):
        format_ (str):
        season_id (str):
        sport_event_id (str):
        sport_id (str):
        channel (Union[Unset, str]):
    """

    competition_id: str
    event_id: str
    format_: str
    season_id: str
    sport_event_id: str
    sport_id: str
    channel: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        competition_id = self.competition_id

        event_id = self.event_id

        format_ = self.format_

        season_id = self.season_id

        sport_event_id = self.sport_event_id

        sport_id = self.sport_id

        channel = self.channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "competition_id": competition_id,
                "event_id": event_id,
                "format": format_,
                "season_id": season_id,
                "sport_event_id": sport_event_id,
                "sport_id": sport_id,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        competition_id = d.pop("competition_id")

        event_id = d.pop("event_id")

        format_ = d.pop("format")

        season_id = d.pop("season_id")

        sport_event_id = d.pop("sport_event_id")

        sport_id = d.pop("sport_id")

        channel = d.pop("channel", UNSET)

        stream_statistics_xml_metadata = cls(
            competition_id=competition_id,
            event_id=event_id,
            format_=format_,
            season_id=season_id,
            sport_event_id=sport_event_id,
            sport_id=sport_id,
            channel=channel,
        )

        stream_statistics_xml_metadata.additional_properties = d
        return stream_statistics_xml_metadata

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
