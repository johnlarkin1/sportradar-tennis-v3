from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_round_name import (
    GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRoundName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound")


@_attrs_define
class GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound:
    """
    Attributes:
        competition_sport_event_number (Union[Unset, int]):
        cup_round_id (Union[Unset, str]): Cup round URN (sr:cup_round:x)
        cup_round_number_of_sport_events (Union[Unset, int]):
        cup_round_sport_event_number (Union[Unset, int]):
        name (Union[Unset,
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRoundName]):
        number (Union[Unset, int]):
        other_sport_event_id (Union[Unset, str]):
    """

    competition_sport_event_number: Union[Unset, int] = UNSET
    cup_round_id: Union[Unset, str] = UNSET
    cup_round_number_of_sport_events: Union[Unset, int] = UNSET
    cup_round_sport_event_number: Union[Unset, int] = UNSET
    name: Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRoundName] = (
        UNSET
    )
    number: Union[Unset, int] = UNSET
    other_sport_event_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competition_sport_event_number = self.competition_sport_event_number

        cup_round_id = self.cup_round_id

        cup_round_number_of_sport_events = self.cup_round_number_of_sport_events

        cup_round_sport_event_number = self.cup_round_sport_event_number

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        number = self.number

        other_sport_event_id = self.other_sport_event_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competition_sport_event_number is not UNSET:
            field_dict["competition_sport_event_number"] = competition_sport_event_number
        if cup_round_id is not UNSET:
            field_dict["cup_round_id"] = cup_round_id
        if cup_round_number_of_sport_events is not UNSET:
            field_dict["cup_round_number_of_sport_events"] = cup_round_number_of_sport_events
        if cup_round_sport_event_number is not UNSET:
            field_dict["cup_round_sport_event_number"] = cup_round_sport_event_number
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if other_sport_event_id is not UNSET:
            field_dict["other_sport_event_id"] = other_sport_event_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        competition_sport_event_number = d.pop("competition_sport_event_number", UNSET)

        cup_round_id = d.pop("cup_round_id", UNSET)

        cup_round_number_of_sport_events = d.pop("cup_round_number_of_sport_events", UNSET)

        cup_round_sport_event_number = d.pop("cup_round_sport_event_number", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRoundName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRoundName(_name)

        number = d.pop("number", UNSET)

        other_sport_event_id = d.pop("other_sport_event_id", UNSET)

        get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_round = cls(
            competition_sport_event_number=competition_sport_event_number,
            cup_round_id=cup_round_id,
            cup_round_number_of_sport_events=cup_round_number_of_sport_events,
            cup_round_sport_event_number=cup_round_sport_event_number,
            name=name,
            number=number,
            other_sport_event_id=other_sport_event_id,
        )

        return get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_round
