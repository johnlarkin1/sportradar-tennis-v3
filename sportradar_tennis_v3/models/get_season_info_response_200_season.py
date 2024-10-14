import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_info_response_200_season_category import GetSeasonInfoResponse200SeasonCategory
    from ..models.get_season_info_response_200_season_competition import GetSeasonInfoResponse200SeasonCompetition
    from ..models.get_season_info_response_200_season_info import GetSeasonInfoResponse200SeasonInfo
    from ..models.get_season_info_response_200_season_sport import GetSeasonInfoResponse200SeasonSport


T = TypeVar("T", bound="GetSeasonInfoResponse200Season")


@_attrs_define
class GetSeasonInfoResponse200Season:
    """
    Attributes:
        competition_id (str):
        end_date (datetime.date):
        id (str): URN
        name (str):
        start_date (datetime.date):
        year (str):
        category (Union[Unset, GetSeasonInfoResponse200SeasonCategory]):
        competition (Union[Unset, GetSeasonInfoResponse200SeasonCompetition]):
        disabled (Union[Unset, bool]):
        info (Union[Unset, GetSeasonInfoResponse200SeasonInfo]):
        sport (Union[Unset, GetSeasonInfoResponse200SeasonSport]):
    """

    competition_id: str
    end_date: datetime.date
    id: str
    name: str
    start_date: datetime.date
    year: str
    category: Union[Unset, "GetSeasonInfoResponse200SeasonCategory"] = UNSET
    competition: Union[Unset, "GetSeasonInfoResponse200SeasonCompetition"] = UNSET
    disabled: Union[Unset, bool] = UNSET
    info: Union[Unset, "GetSeasonInfoResponse200SeasonInfo"] = UNSET
    sport: Union[Unset, "GetSeasonInfoResponse200SeasonSport"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competition_id = self.competition_id

        end_date = self.end_date.isoformat()

        id = self.id

        name = self.name

        start_date = self.start_date.isoformat()

        year = self.year

        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        disabled = self.disabled

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        sport: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport, Unset):
            sport = self.sport.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "competition_id": competition_id,
                "end_date": end_date,
                "id": id,
                "name": name,
                "start_date": start_date,
                "year": year,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if competition is not UNSET:
            field_dict["competition"] = competition
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if info is not UNSET:
            field_dict["info"] = info
        if sport is not UNSET:
            field_dict["sport"] = sport

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_info_response_200_season_category import GetSeasonInfoResponse200SeasonCategory
        from ..models.get_season_info_response_200_season_competition import GetSeasonInfoResponse200SeasonCompetition
        from ..models.get_season_info_response_200_season_info import GetSeasonInfoResponse200SeasonInfo
        from ..models.get_season_info_response_200_season_sport import GetSeasonInfoResponse200SeasonSport

        d = src_dict.copy()
        competition_id = d.pop("competition_id")

        end_date = isoparse(d.pop("end_date")).date()

        id = d.pop("id")

        name = d.pop("name")

        start_date = isoparse(d.pop("start_date")).date()

        year = d.pop("year")

        _category = d.pop("category", UNSET)
        category: Union[Unset, GetSeasonInfoResponse200SeasonCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = GetSeasonInfoResponse200SeasonCategory.from_dict(_category)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, GetSeasonInfoResponse200SeasonCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = GetSeasonInfoResponse200SeasonCompetition.from_dict(_competition)

        disabled = d.pop("disabled", UNSET)

        _info = d.pop("info", UNSET)
        info: Union[Unset, GetSeasonInfoResponse200SeasonInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = GetSeasonInfoResponse200SeasonInfo.from_dict(_info)

        _sport = d.pop("sport", UNSET)
        sport: Union[Unset, GetSeasonInfoResponse200SeasonSport]
        if isinstance(_sport, Unset):
            sport = UNSET
        else:
            sport = GetSeasonInfoResponse200SeasonSport.from_dict(_sport)

        get_season_info_response_200_season = cls(
            competition_id=competition_id,
            end_date=end_date,
            id=id,
            name=name,
            start_date=start_date,
            year=year,
            category=category,
            competition=competition,
            disabled=disabled,
            info=info,
            sport=sport,
        )

        return get_season_info_response_200_season
