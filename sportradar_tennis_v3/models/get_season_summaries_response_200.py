import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_summaries_response_200_summaries_item import GetSeasonSummariesResponse200SummariesItem


T = TypeVar("T", bound="GetSeasonSummariesResponse200")


@_attrs_define
class GetSeasonSummariesResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        summaries (Union[Unset, List['GetSeasonSummariesResponse200SummariesItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    summaries: Union[Unset, List["GetSeasonSummariesResponse200SummariesItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        summaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = []
            for summaries_item_data in self.summaries:
                summaries_item = summaries_item_data.to_dict()
                summaries.append(summaries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if summaries is not UNSET:
            field_dict["summaries"] = summaries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_summaries_response_200_summaries_item import GetSeasonSummariesResponse200SummariesItem

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        summaries = []
        _summaries = d.pop("summaries", UNSET)
        for summaries_item_data in _summaries or []:
            summaries_item = GetSeasonSummariesResponse200SummariesItem.from_dict(summaries_item_data)

            summaries.append(summaries_item)

        get_season_summaries_response_200 = cls(
            generated_at=generated_at,
            summaries=summaries,
        )

        return get_season_summaries_response_200
