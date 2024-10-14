import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_versus_summaries_response_200_competitors_item import (
        GetCompetitorVersusSummariesResponse200CompetitorsItem,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItem,
    )
    from ..models.get_competitor_versus_summaries_response_200_next_meetings_item import (
        GetCompetitorVersusSummariesResponse200NextMeetingsItem,
    )


T = TypeVar("T", bound="GetCompetitorVersusSummariesResponse200")


@_attrs_define
class GetCompetitorVersusSummariesResponse200:
    """
    Attributes:
        competitors (Union[Unset, List['GetCompetitorVersusSummariesResponse200CompetitorsItem']]):
        generated_at (Union[Unset, datetime.datetime]):
        last_meetings (Union[Unset, List['GetCompetitorVersusSummariesResponse200LastMeetingsItem']]):
        next_meetings (Union[Unset, List['GetCompetitorVersusSummariesResponse200NextMeetingsItem']]):
    """

    competitors: Union[Unset, List["GetCompetitorVersusSummariesResponse200CompetitorsItem"]] = UNSET
    generated_at: Union[Unset, datetime.datetime] = UNSET
    last_meetings: Union[Unset, List["GetCompetitorVersusSummariesResponse200LastMeetingsItem"]] = UNSET
    next_meetings: Union[Unset, List["GetCompetitorVersusSummariesResponse200NextMeetingsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        last_meetings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.last_meetings, Unset):
            last_meetings = []
            for last_meetings_item_data in self.last_meetings:
                last_meetings_item = last_meetings_item_data.to_dict()
                last_meetings.append(last_meetings_item)

        next_meetings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.next_meetings, Unset):
            next_meetings = []
            for next_meetings_item_data in self.next_meetings:
                next_meetings_item = next_meetings_item_data.to_dict()
                next_meetings.append(next_meetings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if last_meetings is not UNSET:
            field_dict["last_meetings"] = last_meetings
        if next_meetings is not UNSET:
            field_dict["next_meetings"] = next_meetings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_versus_summaries_response_200_competitors_item import (
            GetCompetitorVersusSummariesResponse200CompetitorsItem,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItem,
        )
        from ..models.get_competitor_versus_summaries_response_200_next_meetings_item import (
            GetCompetitorVersusSummariesResponse200NextMeetingsItem,
        )

        d = src_dict.copy()
        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = GetCompetitorVersusSummariesResponse200CompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        last_meetings = []
        _last_meetings = d.pop("last_meetings", UNSET)
        for last_meetings_item_data in _last_meetings or []:
            last_meetings_item = GetCompetitorVersusSummariesResponse200LastMeetingsItem.from_dict(
                last_meetings_item_data
            )

            last_meetings.append(last_meetings_item)

        next_meetings = []
        _next_meetings = d.pop("next_meetings", UNSET)
        for next_meetings_item_data in _next_meetings or []:
            next_meetings_item = GetCompetitorVersusSummariesResponse200NextMeetingsItem.from_dict(
                next_meetings_item_data
            )

            next_meetings.append(next_meetings_item)

        get_competitor_versus_summaries_response_200 = cls(
            competitors=competitors,
            generated_at=generated_at,
            last_meetings=last_meetings,
            next_meetings=next_meetings,
        )

        return get_competitor_versus_summaries_response_200
