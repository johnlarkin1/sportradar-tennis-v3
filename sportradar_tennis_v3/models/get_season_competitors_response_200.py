import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_competitors_response_200_season_competitors_item import (
        GetSeasonCompetitorsResponse200SeasonCompetitorsItem,
    )


T = TypeVar("T", bound="GetSeasonCompetitorsResponse200")


@_attrs_define
class GetSeasonCompetitorsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        season_competitors (Union[Unset, List['GetSeasonCompetitorsResponse200SeasonCompetitorsItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    season_competitors: Union[Unset, List["GetSeasonCompetitorsResponse200SeasonCompetitorsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        season_competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.season_competitors, Unset):
            season_competitors = []
            for season_competitors_item_data in self.season_competitors:
                season_competitors_item = season_competitors_item_data.to_dict()
                season_competitors.append(season_competitors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if season_competitors is not UNSET:
            field_dict["season_competitors"] = season_competitors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_competitors_response_200_season_competitors_item import (
            GetSeasonCompetitorsResponse200SeasonCompetitorsItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        season_competitors = []
        _season_competitors = d.pop("season_competitors", UNSET)
        for season_competitors_item_data in _season_competitors or []:
            season_competitors_item = GetSeasonCompetitorsResponse200SeasonCompetitorsItem.from_dict(
                season_competitors_item_data
            )

            season_competitors.append(season_competitors_item)

        get_season_competitors_response_200 = cls(
            generated_at=generated_at,
            season_competitors=season_competitors,
        )

        return get_season_competitors_response_200
