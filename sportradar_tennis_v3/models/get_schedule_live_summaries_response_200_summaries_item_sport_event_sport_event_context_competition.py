from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_schedule_live_summaries_response_200_summaries_item_sport_event_sport_event_context_competition_level import (
    GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetitionLevel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetition")


@_attrs_define
class GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetition:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        alternative_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        level (Union[Unset,
            GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetitionLevel]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    alternative_name: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    level: Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetitionLevel] = (
        UNSET
    )
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        alternative_name = self.alternative_name

        gender = self.gender

        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        parent_id = self.parent_id

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if level is not UNSET:
            field_dict["level"] = level
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        alternative_name = d.pop("alternative_name", UNSET)

        gender = d.pop("gender", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetitionLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = GetScheduleLiveSummariesResponse200SummariesItemSportEventSportEventContextCompetitionLevel(_level)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        get_schedule_live_summaries_response_200_summaries_item_sport_event_sport_event_context_competition = cls(
            id=id,
            name=name,
            alternative_name=alternative_name,
            gender=gender,
            level=level,
            parent_id=parent_id,
            type=type,
        )

        return get_schedule_live_summaries_response_200_summaries_item_sport_event_sport_event_context_competition
