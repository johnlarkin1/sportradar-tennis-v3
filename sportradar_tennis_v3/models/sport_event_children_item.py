import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sport_event_children_item_type import SportEventChildrenItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_event_children_item_competitors_item import SportEventChildrenItemCompetitorsItem
    from ..models.sport_event_children_item_venue import SportEventChildrenItemVenue


T = TypeVar("T", bound="SportEventChildrenItem")


@_attrs_define
class SportEventChildrenItem:
    """
    Attributes:
        id (str):
        start_time (datetime.datetime): Scheduled event start
        start_time_confirmed (bool):
        competitors (Union[Unset, List['SportEventChildrenItemCompetitorsItem']]):
        parent_id (Union[Unset, str]):
        replaced_by (Union[Unset, str]): Match has been replaced with another match.
        resume_time (Union[Unset, datetime.datetime]): Resume time if sport event has been suspended
        type (Union[Unset, SportEventChildrenItemType]):
        venue (Union[Unset, SportEventChildrenItemVenue]):
    """

    id: str
    start_time: datetime.datetime
    start_time_confirmed: bool
    competitors: Union[Unset, List["SportEventChildrenItemCompetitorsItem"]] = UNSET
    parent_id: Union[Unset, str] = UNSET
    replaced_by: Union[Unset, str] = UNSET
    resume_time: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, SportEventChildrenItemType] = UNSET
    venue: Union[Unset, "SportEventChildrenItemVenue"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start_time = self.start_time.isoformat()

        start_time_confirmed = self.start_time_confirmed

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        parent_id = self.parent_id

        replaced_by = self.replaced_by

        resume_time: Union[Unset, str] = UNSET
        if not isinstance(self.resume_time, Unset):
            resume_time = self.resume_time.isoformat()

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
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if replaced_by is not UNSET:
            field_dict["replaced_by"] = replaced_by
        if resume_time is not UNSET:
            field_dict["resume_time"] = resume_time
        if type is not UNSET:
            field_dict["type"] = type
        if venue is not UNSET:
            field_dict["venue"] = venue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sport_event_children_item_competitors_item import SportEventChildrenItemCompetitorsItem
        from ..models.sport_event_children_item_venue import SportEventChildrenItemVenue

        d = src_dict.copy()
        id = d.pop("id")

        start_time = isoparse(d.pop("start_time"))

        start_time_confirmed = d.pop("start_time_confirmed")

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = SportEventChildrenItemCompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        parent_id = d.pop("parent_id", UNSET)

        replaced_by = d.pop("replaced_by", UNSET)

        _resume_time = d.pop("resume_time", UNSET)
        resume_time: Union[Unset, datetime.datetime]
        if isinstance(_resume_time, Unset):
            resume_time = UNSET
        else:
            resume_time = isoparse(_resume_time)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SportEventChildrenItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SportEventChildrenItemType(_type)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, SportEventChildrenItemVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = SportEventChildrenItemVenue.from_dict(_venue)

        sport_event_children_item = cls(
            id=id,
            start_time=start_time,
            start_time_confirmed=start_time_confirmed,
            competitors=competitors,
            parent_id=parent_id,
            replaced_by=replaced_by,
            resume_time=resume_time,
            type=type,
            venue=venue,
        )

        return sport_event_children_item
