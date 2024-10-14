import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason")


@_attrs_define
class GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason:
    """
    Attributes:
        competition_id (str):
        end_date (datetime.date):
        id (str): URN
        name (str):
        start_date (datetime.date):
        year (str):
        disabled (Union[Unset, bool]):
    """

    competition_id: str
    end_date: datetime.date
    id: str
    name: str
    start_date: datetime.date
    year: str
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competition_id = self.competition_id

        end_date = self.end_date.isoformat()

        id = self.id

        name = self.name

        start_date = self.start_date.isoformat()

        year = self.year

        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "competition_id": competition_id,
                "end_date": end_date,
                "id": id,
                "name": name,
                "start_date": start_date,
                "year": year,
            }
        )
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        competition_id = d.pop("competition_id")

        end_date = isoparse(d.pop("end_date")).date()

        id = d.pop("id")

        name = d.pop("name")

        start_date = isoparse(d.pop("start_date")).date()

        year = d.pop("year")

        disabled = d.pop("disabled", UNSET)

        get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_season = cls(
            competition_id=competition_id,
            end_date=end_date,
            id=id,
            name=name,
            start_date=start_date,
            year=year,
            disabled=disabled,
        )

        return get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_season
