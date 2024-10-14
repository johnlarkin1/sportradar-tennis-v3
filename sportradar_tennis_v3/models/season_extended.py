import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_extended_category import SeasonExtendedCategory
    from ..models.season_extended_competition import SeasonExtendedCompetition
    from ..models.season_extended_info import SeasonExtendedInfo
    from ..models.season_extended_sport import SeasonExtendedSport


T = TypeVar("T", bound="SeasonExtended")


@_attrs_define
class SeasonExtended:
    """
    Attributes:
        competition_id (str):
        end_date (datetime.date):
        id (str): URN
        name (str):
        start_date (datetime.date):
        year (str):
        category (Union[Unset, SeasonExtendedCategory]):
        competition (Union[Unset, SeasonExtendedCompetition]):
        disabled (Union[Unset, bool]):
        info (Union[Unset, SeasonExtendedInfo]):
        sport (Union[Unset, SeasonExtendedSport]):
    """

    competition_id: str
    end_date: datetime.date
    id: str
    name: str
    start_date: datetime.date
    year: str
    category: Union[Unset, "SeasonExtendedCategory"] = UNSET
    competition: Union[Unset, "SeasonExtendedCompetition"] = UNSET
    disabled: Union[Unset, bool] = UNSET
    info: Union[Unset, "SeasonExtendedInfo"] = UNSET
    sport: Union[Unset, "SeasonExtendedSport"] = UNSET

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
        from ..models.season_extended_category import SeasonExtendedCategory
        from ..models.season_extended_competition import SeasonExtendedCompetition
        from ..models.season_extended_info import SeasonExtendedInfo
        from ..models.season_extended_sport import SeasonExtendedSport

        d = src_dict.copy()
        competition_id = d.pop("competition_id")

        end_date = isoparse(d.pop("end_date")).date()

        id = d.pop("id")

        name = d.pop("name")

        start_date = isoparse(d.pop("start_date")).date()

        year = d.pop("year")

        _category = d.pop("category", UNSET)
        category: Union[Unset, SeasonExtendedCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = SeasonExtendedCategory.from_dict(_category)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, SeasonExtendedCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = SeasonExtendedCompetition.from_dict(_competition)

        disabled = d.pop("disabled", UNSET)

        _info = d.pop("info", UNSET)
        info: Union[Unset, SeasonExtendedInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = SeasonExtendedInfo.from_dict(_info)

        _sport = d.pop("sport", UNSET)
        sport: Union[Unset, SeasonExtendedSport]
        if isinstance(_sport, Unset):
            sport = UNSET
        else:
            sport = SeasonExtendedSport.from_dict(_sport)

        season_extended = cls(
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

        return season_extended
