from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_event_timeline_response_200_sport_event_coverage_sport_event_properties import (
        GetSportEventTimelineResponse200SportEventCoverageSportEventProperties,
    )


T = TypeVar("T", bound="GetSportEventTimelineResponse200SportEventCoverage")


@_attrs_define
class GetSportEventTimelineResponse200SportEventCoverage:
    """Describes the expected coverage for different entities within this type. When type="sport_event" you will only get
    sport_event_properties. When type="competition" you will get sport_event_properties and competition_properties.

        Attributes:
            sport_event_properties (Union[Unset, GetSportEventTimelineResponse200SportEventCoverageSportEventProperties]):
            type (Union[Unset, str]):
    """

    sport_event_properties: Union[Unset, "GetSportEventTimelineResponse200SportEventCoverageSportEventProperties"] = (
        UNSET
    )
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sport_event_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_properties, Unset):
            sport_event_properties = self.sport_event_properties.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if sport_event_properties is not UNSET:
            field_dict["sport_event_properties"] = sport_event_properties
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_sport_event_timeline_response_200_sport_event_coverage_sport_event_properties import (
            GetSportEventTimelineResponse200SportEventCoverageSportEventProperties,
        )

        d = src_dict.copy()
        _sport_event_properties = d.pop("sport_event_properties", UNSET)
        sport_event_properties: Union[Unset, GetSportEventTimelineResponse200SportEventCoverageSportEventProperties]
        if isinstance(_sport_event_properties, Unset):
            sport_event_properties = UNSET
        else:
            sport_event_properties = GetSportEventTimelineResponse200SportEventCoverageSportEventProperties.from_dict(
                _sport_event_properties
            )

        type = d.pop("type", UNSET)

        get_sport_event_timeline_response_200_sport_event_coverage = cls(
            sport_event_properties=sport_event_properties,
            type=type,
        )

        return get_sport_event_timeline_response_200_sport_event_coverage
