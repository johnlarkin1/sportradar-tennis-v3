from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.probability_outcome_two_three_way_name import ProbabilityOutcomeTwoThreeWayName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProbabilityOutcomeTwoThreeWay")


@_attrs_define
class ProbabilityOutcomeTwoThreeWay:
    """
    Attributes:
        name (Union[Unset, ProbabilityOutcomeTwoThreeWayName]):
        probability (Union[Unset, float]):
    """

    name: Union[Unset, ProbabilityOutcomeTwoThreeWayName] = UNSET
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
        name: Union[Unset, ProbabilityOutcomeTwoThreeWayName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ProbabilityOutcomeTwoThreeWayName(_name)

        probability = d.pop("probability", UNSET)

        probability_outcome_two_three_way = cls(
            name=name,
            probability=probability,
        )

        return probability_outcome_two_three_way
