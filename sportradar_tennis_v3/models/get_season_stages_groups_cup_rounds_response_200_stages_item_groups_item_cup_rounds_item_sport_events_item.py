import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemSportEventsItem")


@_attrs_define
class GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemSportEventsItem:
    """
    Attributes:
        id (str):
        start_time (datetime.datetime): Scheduled event start
        start_time_confirmed (bool):
        order (Union[Unset, int]):
        replaced_by (Union[Unset, str]):
        resume_time (Union[Unset, datetime.datetime]): Resume time if sport event has been suspended
    """

    id: str
    start_time: datetime.datetime
    start_time_confirmed: bool
    order: Union[Unset, int] = UNSET
    replaced_by: Union[Unset, str] = UNSET
    resume_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        start_time = self.start_time.isoformat()

        start_time_confirmed = self.start_time_confirmed

        order = self.order

        replaced_by = self.replaced_by

        resume_time: Union[Unset, str] = UNSET
        if not isinstance(self.resume_time, Unset):
            resume_time = self.resume_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "start_time": start_time,
                "start_time_confirmed": start_time_confirmed,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if replaced_by is not UNSET:
            field_dict["replaced_by"] = replaced_by
        if resume_time is not UNSET:
            field_dict["resume_time"] = resume_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        start_time = isoparse(d.pop("start_time"))

        start_time_confirmed = d.pop("start_time_confirmed")

        order = d.pop("order", UNSET)

        replaced_by = d.pop("replaced_by", UNSET)

        _resume_time = d.pop("resume_time", UNSET)
        resume_time: Union[Unset, datetime.datetime]
        if isinstance(_resume_time, Unset):
            resume_time = UNSET
        else:
            resume_time = isoparse(_resume_time)

        get_season_stages_groups_cup_rounds_response_200_stages_item_groups_item_cup_rounds_item_sport_events_item = (
            cls(
                id=id,
                start_time=start_time,
                start_time_confirmed=start_time_confirmed,
                order=order,
                replaced_by=replaced_by,
                resume_time=resume_time,
            )
        )

        return (
            get_season_stages_groups_cup_rounds_response_200_stages_item_groups_item_cup_rounds_item_sport_events_item
        )
