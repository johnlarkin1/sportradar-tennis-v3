from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stream_statistics_xml_payload_statistics_competitors_item import (
        StreamStatisticsXmlPayloadStatisticsCompetitorsItem,
    )


T = TypeVar("T", bound="StreamStatisticsXmlPayloadStatistics")


@_attrs_define
class StreamStatisticsXmlPayloadStatistics:
    """
    Attributes:
        competitors (Union[Unset, List['StreamStatisticsXmlPayloadStatisticsCompetitorsItem']]):
    """

    competitors: Union[Unset, List["StreamStatisticsXmlPayloadStatisticsCompetitorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if competitors is not UNSET:
            field_dict["competitors"] = competitors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stream_statistics_xml_payload_statistics_competitors_item import (
            StreamStatisticsXmlPayloadStatisticsCompetitorsItem,
        )

        d = src_dict.copy()
        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = StreamStatisticsXmlPayloadStatisticsCompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        stream_statistics_xml_payload_statistics = cls(
            competitors=competitors,
        )

        stream_statistics_xml_payload_statistics.additional_properties = d
        return stream_statistics_xml_payload_statistics

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
