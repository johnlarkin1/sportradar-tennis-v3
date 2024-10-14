import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItem,
    )


T = TypeVar("T", bound="GetSeasonProbabilitiesResponse200")


@_attrs_define
class GetSeasonProbabilitiesResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        sport_event_probabilities (Union[Unset, List['GetSeasonProbabilitiesResponse200SportEventProbabilitiesItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    sport_event_probabilities: Union[Unset, List["GetSeasonProbabilitiesResponse200SportEventProbabilitiesItem"]] = (
        UNSET
    )

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        sport_event_probabilities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_event_probabilities, Unset):
            sport_event_probabilities = []
            for sport_event_probabilities_item_data in self.sport_event_probabilities:
                sport_event_probabilities_item = sport_event_probabilities_item_data.to_dict()
                sport_event_probabilities.append(sport_event_probabilities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if sport_event_probabilities is not UNSET:
            field_dict["sport_event_probabilities"] = sport_event_probabilities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        sport_event_probabilities = []
        _sport_event_probabilities = d.pop("sport_event_probabilities", UNSET)
        for sport_event_probabilities_item_data in _sport_event_probabilities or []:
            sport_event_probabilities_item = GetSeasonProbabilitiesResponse200SportEventProbabilitiesItem.from_dict(
                sport_event_probabilities_item_data
            )

            sport_event_probabilities.append(sport_event_probabilities_item)

        get_season_probabilities_response_200 = cls(
            generated_at=generated_at,
            sport_event_probabilities=sport_event_probabilities,
        )

        return get_season_probabilities_response_200
