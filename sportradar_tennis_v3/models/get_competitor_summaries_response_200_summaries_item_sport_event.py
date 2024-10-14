import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_type import (
    GetCompetitorSummariesResponse200SummariesItemSportEventType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_children_item import (
        GetCompetitorSummariesResponse200SummariesItemSportEventChildrenItem,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_competitors_item import (
        GetCompetitorSummariesResponse200SummariesItemSportEventCompetitorsItem,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_coverage import (
        GetCompetitorSummariesResponse200SummariesItemSportEventCoverage,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_venue import (
        GetCompetitorSummariesResponse200SummariesItemSportEventVenue,
    )


T = TypeVar("T", bound="GetCompetitorSummariesResponse200SummariesItemSportEvent")


@_attrs_define
class GetCompetitorSummariesResponse200SummariesItemSportEvent:
    """
    Attributes:
        id (str):
        start_time (datetime.datetime): Scheduled event start
        start_time_confirmed (bool):
        children (Union[Unset, List['GetCompetitorSummariesResponse200SummariesItemSportEventChildrenItem']]):
        competitors (Union[Unset, List['GetCompetitorSummariesResponse200SummariesItemSportEventCompetitorsItem']]):
        coverage (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventCoverage]): Describes the
            expected coverage for different entities within this type. When type="sport_event" you will only get
            sport_event_properties. When type="competition" you will get sport_event_properties and competition_properties.
        estimated (Union[Unset, bool]):
        parent_id (Union[Unset, str]):
        replaced_by (Union[Unset, str]): Match has been replaced with another match.
        resume_time (Union[Unset, datetime.datetime]): Resume time if sport event has been suspended
        sport_event_context (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext]):
        type (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventType]):
        venue (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventVenue]):
    """

    id: str
    start_time: datetime.datetime
    start_time_confirmed: bool
    children: Union[Unset, List["GetCompetitorSummariesResponse200SummariesItemSportEventChildrenItem"]] = UNSET
    competitors: Union[Unset, List["GetCompetitorSummariesResponse200SummariesItemSportEventCompetitorsItem"]] = UNSET
    coverage: Union[Unset, "GetCompetitorSummariesResponse200SummariesItemSportEventCoverage"] = UNSET
    estimated: Union[Unset, bool] = UNSET
    parent_id: Union[Unset, str] = UNSET
    replaced_by: Union[Unset, str] = UNSET
    resume_time: Union[Unset, datetime.datetime] = UNSET
    sport_event_context: Union[Unset, "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext"] = (
        UNSET
    )
    type: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventType] = UNSET
    venue: Union[Unset, "GetCompetitorSummariesResponse200SummariesItemSportEventVenue"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start_time = self.start_time.isoformat()

        start_time_confirmed = self.start_time_confirmed

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        coverage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = self.coverage.to_dict()

        estimated = self.estimated

        parent_id = self.parent_id

        replaced_by = self.replaced_by

        resume_time: Union[Unset, str] = UNSET
        if not isinstance(self.resume_time, Unset):
            resume_time = self.resume_time.isoformat()

        sport_event_context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_context, Unset):
            sport_event_context = self.sport_event_context.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "start_time": start_time,
                "start_time_confirmed": start_time_confirmed,
            }
        )
        if children is not UNSET:
            field_dict["children"] = children
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if estimated is not UNSET:
            field_dict["estimated"] = estimated
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if replaced_by is not UNSET:
            field_dict["replaced_by"] = replaced_by
        if resume_time is not UNSET:
            field_dict["resume_time"] = resume_time
        if sport_event_context is not UNSET:
            field_dict["sport_event_context"] = sport_event_context
        if type is not UNSET:
            field_dict["type"] = type
        if venue is not UNSET:
            field_dict["venue"] = venue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_children_item import (
            GetCompetitorSummariesResponse200SummariesItemSportEventChildrenItem,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_competitors_item import (
            GetCompetitorSummariesResponse200SummariesItemSportEventCompetitorsItem,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_coverage import (
            GetCompetitorSummariesResponse200SummariesItemSportEventCoverage,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_venue import (
            GetCompetitorSummariesResponse200SummariesItemSportEventVenue,
        )

        d = src_dict.copy()
        id = d.pop("id")

        start_time = isoparse(d.pop("start_time"))

        start_time_confirmed = d.pop("start_time_confirmed")

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = GetCompetitorSummariesResponse200SummariesItemSportEventChildrenItem.from_dict(
                children_item_data
            )

            children.append(children_item)

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = GetCompetitorSummariesResponse200SummariesItemSportEventCompetitorsItem.from_dict(
                competitors_item_data
            )

            competitors.append(competitors_item)

        _coverage = d.pop("coverage", UNSET)
        coverage: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventCoverage]
        if isinstance(_coverage, Unset):
            coverage = UNSET
        else:
            coverage = GetCompetitorSummariesResponse200SummariesItemSportEventCoverage.from_dict(_coverage)

        estimated = d.pop("estimated", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        replaced_by = d.pop("replaced_by", UNSET)

        _resume_time = d.pop("resume_time", UNSET)
        resume_time: Union[Unset, datetime.datetime]
        if isinstance(_resume_time, Unset):
            resume_time = UNSET
        else:
            resume_time = isoparse(_resume_time)

        _sport_event_context = d.pop("sport_event_context", UNSET)
        sport_event_context: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext]
        if isinstance(_sport_event_context, Unset):
            sport_event_context = UNSET
        else:
            sport_event_context = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext.from_dict(
                _sport_event_context
            )

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetCompetitorSummariesResponse200SummariesItemSportEventType(_type)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = GetCompetitorSummariesResponse200SummariesItemSportEventVenue.from_dict(_venue)

        get_competitor_summaries_response_200_summaries_item_sport_event = cls(
            id=id,
            start_time=start_time,
            start_time_confirmed=start_time_confirmed,
            children=children,
            competitors=competitors,
            coverage=coverage,
            estimated=estimated,
            parent_id=parent_id,
            replaced_by=replaced_by,
            resume_time=resume_time,
            sport_event_context=sport_event_context,
            type=type,
            venue=venue,
        )

        return get_competitor_summaries_response_200_summaries_item_sport_event
