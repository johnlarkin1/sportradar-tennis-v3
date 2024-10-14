import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_profile_response_200_competitions_played_item import (
        GetCompetitorProfileResponse200CompetitionsPlayedItem,
    )
    from ..models.get_competitor_profile_response_200_competitor import GetCompetitorProfileResponse200Competitor
    from ..models.get_competitor_profile_response_200_competitor_rankings_item import (
        GetCompetitorProfileResponse200CompetitorRankingsItem,
    )
    from ..models.get_competitor_profile_response_200_info import GetCompetitorProfileResponse200Info
    from ..models.get_competitor_profile_response_200_periods_item import GetCompetitorProfileResponse200PeriodsItem


T = TypeVar("T", bound="GetCompetitorProfileResponse200")


@_attrs_define
class GetCompetitorProfileResponse200:
    """
    Attributes:
        competitions_played (Union[Unset, List['GetCompetitorProfileResponse200CompetitionsPlayedItem']]):
        competitor (Union[Unset, GetCompetitorProfileResponse200Competitor]):
        competitor_rankings (Union[Unset, List['GetCompetitorProfileResponse200CompetitorRankingsItem']]):
        generated_at (Union[Unset, datetime.datetime]):
        info (Union[Unset, GetCompetitorProfileResponse200Info]):
        periods (Union[Unset, List['GetCompetitorProfileResponse200PeriodsItem']]):
    """

    competitions_played: Union[Unset, List["GetCompetitorProfileResponse200CompetitionsPlayedItem"]] = UNSET
    competitor: Union[Unset, "GetCompetitorProfileResponse200Competitor"] = UNSET
    competitor_rankings: Union[Unset, List["GetCompetitorProfileResponse200CompetitorRankingsItem"]] = UNSET
    generated_at: Union[Unset, datetime.datetime] = UNSET
    info: Union[Unset, "GetCompetitorProfileResponse200Info"] = UNSET
    periods: Union[Unset, List["GetCompetitorProfileResponse200PeriodsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competitions_played: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitions_played, Unset):
            competitions_played = []
            for competitions_played_item_data in self.competitions_played:
                competitions_played_item = competitions_played_item_data.to_dict()
                competitions_played.append(competitions_played_item)

        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        competitor_rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitor_rankings, Unset):
            competitor_rankings = []
            for competitor_rankings_item_data in self.competitor_rankings:
                competitor_rankings_item = competitor_rankings_item_data.to_dict()
                competitor_rankings.append(competitor_rankings_item)

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competitions_played is not UNSET:
            field_dict["competitions_played"] = competitions_played
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if competitor_rankings is not UNSET:
            field_dict["competitor_rankings"] = competitor_rankings
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if info is not UNSET:
            field_dict["info"] = info
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competitor_profile_response_200_competitions_played_item import (
            GetCompetitorProfileResponse200CompetitionsPlayedItem,
        )
        from ..models.get_competitor_profile_response_200_competitor import GetCompetitorProfileResponse200Competitor
        from ..models.get_competitor_profile_response_200_competitor_rankings_item import (
            GetCompetitorProfileResponse200CompetitorRankingsItem,
        )
        from ..models.get_competitor_profile_response_200_info import GetCompetitorProfileResponse200Info
        from ..models.get_competitor_profile_response_200_periods_item import GetCompetitorProfileResponse200PeriodsItem

        d = src_dict.copy()
        competitions_played = []
        _competitions_played = d.pop("competitions_played", UNSET)
        for competitions_played_item_data in _competitions_played or []:
            competitions_played_item = GetCompetitorProfileResponse200CompetitionsPlayedItem.from_dict(
                competitions_played_item_data
            )

            competitions_played.append(competitions_played_item)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, GetCompetitorProfileResponse200Competitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = GetCompetitorProfileResponse200Competitor.from_dict(_competitor)

        competitor_rankings = []
        _competitor_rankings = d.pop("competitor_rankings", UNSET)
        for competitor_rankings_item_data in _competitor_rankings or []:
            competitor_rankings_item = GetCompetitorProfileResponse200CompetitorRankingsItem.from_dict(
                competitor_rankings_item_data
            )

            competitor_rankings.append(competitor_rankings_item)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        _info = d.pop("info", UNSET)
        info: Union[Unset, GetCompetitorProfileResponse200Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = GetCompetitorProfileResponse200Info.from_dict(_info)

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = GetCompetitorProfileResponse200PeriodsItem.from_dict(periods_item_data)

            periods.append(periods_item)

        get_competitor_profile_response_200 = cls(
            competitions_played=competitions_played,
            competitor=competitor,
            competitor_rankings=competitor_rankings,
            generated_at=generated_at,
            info=info,
            periods=periods,
        )

        return get_competitor_profile_response_200
