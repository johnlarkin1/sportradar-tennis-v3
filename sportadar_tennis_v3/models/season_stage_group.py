from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_stage_competitor import SeasonStageCompetitor


T = TypeVar("T", bound="SeasonStageGroup")


@_attrs_define
class SeasonStageGroup:
    """
    Attributes:
        id (str):
        name (str):
        competitors (Union[Unset, List['SeasonStageCompetitor']]):
        group_name (Union[Unset, str]):
        max_rounds (Union[Unset, int]):
    """

    id: str
    name: str
    competitors: Union[Unset, List["SeasonStageCompetitor"]] = UNSET
    group_name: Union[Unset, str] = UNSET
    max_rounds: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()
                competitors.append(competitors_item)

        group_name = self.group_name

        max_rounds = self.max_rounds

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if max_rounds is not UNSET:
            field_dict["max_rounds"] = max_rounds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_stage_competitor import SeasonStageCompetitor

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in _competitors or []:
            competitors_item = SeasonStageCompetitor.from_dict(competitors_item_data)

            competitors.append(competitors_item)

        group_name = d.pop("group_name", UNSET)

        max_rounds = d.pop("max_rounds", UNSET)

        season_stage_group = cls(
            id=id,
            name=name,
            competitors=competitors,
            group_name=group_name,
            max_rounds=max_rounds,
        )

        return season_stage_group
