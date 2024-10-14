from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport")


@_attrs_define
class GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport:
    """
    Attributes:
        id (str): Sport URN (sr:sport:x)
        name (str):
    """

    id: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_sport = cls(
            id=id,
            name=name,
        )

        return get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_sport
