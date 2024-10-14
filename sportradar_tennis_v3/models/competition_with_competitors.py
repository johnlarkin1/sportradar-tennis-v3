from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.competition_with_competitors_level import CompetitionWithCompetitorsLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_with_competitors_competitors_item import CompetitionWithCompetitorsCompetitorsItem


T = TypeVar("T", bound="CompetitionWithCompetitors")


@_attrs_define
class CompetitionWithCompetitors:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        competitors (Union[Unset, List['CompetitionWithCompetitorsCompetitorsItem']]):
        gender (Union[Unset, str]):
        level (Union[Unset, CompetitionWithCompetitorsLevel]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    competitors: Union[Unset, List["CompetitionWithCompetitorsCompetitorsItem"]] = UNSET
    gender: Union[Unset, str] = UNSET
    level: Union[Unset, CompetitionWithCompetitorsLevel] = UNSET
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        gender = self.gender

        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        parent_id = self.parent_id

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if gender is not UNSET:
            field_dict["gender"] = gender
        if level is not UNSET:
            field_dict["level"] = level
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.competition_with_competitors_competitors_item import CompetitionWithCompetitorsCompetitorsItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = CompetitionWithCompetitorsCompetitorsItem.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        gender = d.pop("gender", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, CompetitionWithCompetitorsLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = CompetitionWithCompetitorsLevel(_level)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        competition_with_competitors = cls(
            id=id,
            name=name,
            competitors=competitors,
            gender=gender,
            level=level,
            parent_id=parent_id,
            type=type,
        )

        return competition_with_competitors
