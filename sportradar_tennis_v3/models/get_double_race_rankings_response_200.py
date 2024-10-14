import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_double_race_rankings_response_200_rankings_item import (
        GetDoubleRaceRankingsResponse200RankingsItem,
    )


T = TypeVar("T", bound="GetDoubleRaceRankingsResponse200")


@_attrs_define
class GetDoubleRaceRankingsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        rankings (Union[Unset, List['GetDoubleRaceRankingsResponse200RankingsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    rankings: Union[Unset, List["GetDoubleRaceRankingsResponse200RankingsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = []
            for rankings_item_data in self.rankings:
                rankings_item = rankings_item_data.to_dict()
                rankings.append(rankings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if rankings is not UNSET:
            field_dict["rankings"] = rankings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_double_race_rankings_response_200_rankings_item import (
            GetDoubleRaceRankingsResponse200RankingsItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        rankings = []
        _rankings = d.pop("rankings", UNSET)
        for rankings_item_data in _rankings or []:
            rankings_item = GetDoubleRaceRankingsResponse200RankingsItem.from_dict(rankings_item_data)

            rankings.append(rankings_item)

        get_double_race_rankings_response_200 = cls(
            generated_at=generated_at,
            rankings=rankings,
        )

        get_double_race_rankings_response_200.additional_properties = d
        return get_double_race_rankings_response_200

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
