from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competition_info_response_200_competition_children_item_competition import (
        GetCompetitionInfoResponse200CompetitionChildrenItemCompetition,
    )


T = TypeVar("T", bound="GetCompetitionInfoResponse200CompetitionChildrenItem")


@_attrs_define
class GetCompetitionInfoResponse200CompetitionChildrenItem:
    """
    Attributes:
        competition (Union[Unset, GetCompetitionInfoResponse200CompetitionChildrenItemCompetition]):
    """

    competition: Union[Unset, "GetCompetitionInfoResponse200CompetitionChildrenItemCompetition"] = UNSET
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
        from ..models.get_competition_info_response_200_competition_children_item_competition import (
            GetCompetitionInfoResponse200CompetitionChildrenItemCompetition,
        )

        d = src_dict.copy()
        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, GetCompetitionInfoResponse200CompetitionChildrenItemCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = GetCompetitionInfoResponse200CompetitionChildrenItemCompetition.from_dict(_competition)

        get_competition_info_response_200_competition_children_item = cls(
            competition=competition,
        )

        get_competition_info_response_200_competition_children_item.additional_properties = d
        return get_competition_info_response_200_competition_children_item

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
