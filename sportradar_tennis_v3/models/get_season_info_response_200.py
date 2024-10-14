import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_info_response_200_coverage import GetSeasonInfoResponse200Coverage
    from ..models.get_season_info_response_200_season import GetSeasonInfoResponse200Season
    from ..models.get_season_info_response_200_stages_item import GetSeasonInfoResponse200StagesItem
    from ..models.get_season_info_response_200_winner_last_season import GetSeasonInfoResponse200WinnerLastSeason


T = TypeVar("T", bound="GetSeasonInfoResponse200")


@_attrs_define
class GetSeasonInfoResponse200:
    """
    Attributes:
        coverage (Union[Unset, GetSeasonInfoResponse200Coverage]): Describes the expected coverage for different
            entities within this type. When type="sport_event" you will only get sport_event_properties. When
            type="competition" you will get sport_event_properties and competition_properties.
        generated_at (Union[Unset, datetime.datetime]):
        season (Union[Unset, GetSeasonInfoResponse200Season]):
        stages (Union[Unset, List['GetSeasonInfoResponse200StagesItem']]):
        winner_last_season (Union[Unset, GetSeasonInfoResponse200WinnerLastSeason]):
    """

    coverage: Union[Unset, "GetSeasonInfoResponse200Coverage"] = UNSET
    generated_at: Union[Unset, datetime.datetime] = UNSET
    season: Union[Unset, "GetSeasonInfoResponse200Season"] = UNSET
    stages: Union[Unset, List["GetSeasonInfoResponse200StagesItem"]] = UNSET
    winner_last_season: Union[Unset, "GetSeasonInfoResponse200WinnerLastSeason"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        coverage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = self.coverage.to_dict()

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        stages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        winner_last_season: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.winner_last_season, Unset):
            winner_last_season = self.winner_last_season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if season is not UNSET:
            field_dict["season"] = season
        if stages is not UNSET:
            field_dict["stages"] = stages
        if winner_last_season is not UNSET:
            field_dict["winner_last_season"] = winner_last_season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_info_response_200_coverage import GetSeasonInfoResponse200Coverage
        from ..models.get_season_info_response_200_season import GetSeasonInfoResponse200Season
        from ..models.get_season_info_response_200_stages_item import GetSeasonInfoResponse200StagesItem
        from ..models.get_season_info_response_200_winner_last_season import GetSeasonInfoResponse200WinnerLastSeason

        d = src_dict.copy()
        _coverage = d.pop("coverage", UNSET)
        coverage: Union[Unset, GetSeasonInfoResponse200Coverage]
        if isinstance(_coverage, Unset):
            coverage = UNSET
        else:
            coverage = GetSeasonInfoResponse200Coverage.from_dict(_coverage)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        _season = d.pop("season", UNSET)
        season: Union[Unset, GetSeasonInfoResponse200Season]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = GetSeasonInfoResponse200Season.from_dict(_season)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = GetSeasonInfoResponse200StagesItem.from_dict(stages_item_data)

            stages.append(stages_item)

        _winner_last_season = d.pop("winner_last_season", UNSET)
        winner_last_season: Union[Unset, GetSeasonInfoResponse200WinnerLastSeason]
        if isinstance(_winner_last_season, Unset):
            winner_last_season = UNSET
        else:
            winner_last_season = GetSeasonInfoResponse200WinnerLastSeason.from_dict(_winner_last_season)

        get_season_info_response_200 = cls(
            coverage=coverage,
            generated_at=generated_at,
            season=season,
            stages=stages,
            winner_last_season=winner_last_season,
        )

        return get_season_info_response_200
