from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_markets_item_outcomes_item_name import (
    GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItem")


@_attrs_define
class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItem:
    """
    Attributes:
        name (Union[Unset, GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItemName]):
        probability (Union[Unset, float]):
    """

    name: Union[Unset, GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItemName] = UNSET
    probability: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        probability = self.probability

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if probability is not UNSET:
            field_dict["probability"] = probability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemMarketsItemOutcomesItemName(_name)

        probability = d.pop("probability", UNSET)

        get_season_probabilities_response_200_sport_event_probabilities_item_markets_item_outcomes_item = cls(
            name=name,
            probability=probability,
        )

        return get_season_probabilities_response_200_sport_event_probabilities_item_markets_item_outcomes_item
