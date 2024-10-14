from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.probability_market_two_three_way_outcomes_item_name import ProbabilityMarketTwoThreeWayOutcomesItemName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProbabilityMarketTwoThreeWayOutcomesItem")


@_attrs_define
class ProbabilityMarketTwoThreeWayOutcomesItem:
    """
    Attributes:
        name (Union[Unset, ProbabilityMarketTwoThreeWayOutcomesItemName]):
        probability (Union[Unset, float]):
    """

    name: Union[Unset, ProbabilityMarketTwoThreeWayOutcomesItemName] = UNSET
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
        name: Union[Unset, ProbabilityMarketTwoThreeWayOutcomesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ProbabilityMarketTwoThreeWayOutcomesItemName(_name)

        probability = d.pop("probability", UNSET)

        probability_market_two_three_way_outcomes_item = cls(
            name=name,
            probability=probability,
        )

        return probability_market_two_three_way_outcomes_item
