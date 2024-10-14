import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competition_seasons_response_200_seasons_item import GetCompetitionSeasonsResponse200SeasonsItem


T = TypeVar("T", bound="GetCompetitionSeasonsResponse200")


@_attrs_define
class GetCompetitionSeasonsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        seasons (Union[Unset, List['GetCompetitionSeasonsResponse200SeasonsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    seasons: Union[Unset, List["GetCompetitionSeasonsResponse200SeasonsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        seasons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.seasons, Unset):
            seasons = []
            for seasons_item_data in self.seasons:
                seasons_item = seasons_item_data.to_dict()
                seasons.append(seasons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if seasons is not UNSET:
            field_dict["seasons"] = seasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competition_seasons_response_200_seasons_item import (
            GetCompetitionSeasonsResponse200SeasonsItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        seasons = []
        _seasons = d.pop("seasons", UNSET)
        for seasons_item_data in _seasons or []:
            seasons_item = GetCompetitionSeasonsResponse200SeasonsItem.from_dict(seasons_item_data)

            seasons.append(seasons_item)

        get_competition_seasons_response_200 = cls(
            generated_at=generated_at,
            seasons=seasons,
        )

        return get_competition_seasons_response_200
