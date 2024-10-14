from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_extended_children_item_competition import CompetitionExtendedChildrenItemCompetition


T = TypeVar("T", bound="CompetitionExtendedChildrenItem")


@_attrs_define
class CompetitionExtendedChildrenItem:
    """
    Attributes:
        competition (Union[Unset, CompetitionExtendedChildrenItemCompetition]):
    """

    competition: Union[Unset, "CompetitionExtendedChildrenItemCompetition"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if competition is not UNSET:
            field_dict["competition"] = competition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_extended_children_item_competition import CompetitionExtendedChildrenItemCompetition

        d = src_dict.copy()
        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, CompetitionExtendedChildrenItemCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = CompetitionExtendedChildrenItemCompetition.from_dict(_competition)

        competition_extended_children_item = cls(
            competition=competition,
        )

        competition_extended_children_item.additional_properties = d
        return competition_extended_children_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
