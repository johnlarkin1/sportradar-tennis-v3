from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category
    from ..models.competition import Competition
    from ..models.season import Season
    from ..models.sport import Sport
    from ..models.sport_event_context_group import SportEventContextGroup
    from ..models.sport_event_context_round import SportEventContextRound
    from ..models.sport_event_context_stage import SportEventContextStage
    from ..models.sport_event_mode import SportEventMode


T = TypeVar("T", bound="SportEventContext")


@_attrs_define
class SportEventContext:
    """
    Attributes:
        category (Category):
        competition (Competition):
        season (Season):
        sport (Sport):
        groups (Union[Unset, List['SportEventContextGroup']]):
        mode (Union[Unset, SportEventMode]):
        round_ (Union[Unset, SportEventContextRound]):
        stage (Union[Unset, SportEventContextStage]):
    """

    category: "Category"
    competition: "Competition"
    season: "Season"
    sport: "Sport"
    groups: Union[Unset, List["SportEventContextGroup"]] = UNSET
    mode: Union[Unset, "SportEventMode"] = UNSET
    round_: Union[Unset, "SportEventContextRound"] = UNSET
    stage: Union[Unset, "SportEventContextStage"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.to_dict()

        competition = self.competition.to_dict()

        season = self.season.to_dict()

        sport = self.sport.to_dict()

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.to_dict()

        round_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.round_, Unset):
            round_ = self.round_.to_dict()

        stage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "category": category,
                "competition": competition,
                "season": season,
                "sport": sport,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if mode is not UNSET:
            field_dict["mode"] = mode
        if round_ is not UNSET:
            field_dict["round"] = round_
        if stage is not UNSET:
            field_dict["stage"] = stage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category import Category
        from ..models.competition import Competition
        from ..models.season import Season
        from ..models.sport import Sport
        from ..models.sport_event_context_group import SportEventContextGroup
        from ..models.sport_event_context_round import SportEventContextRound
        from ..models.sport_event_context_stage import SportEventContextStage
        from ..models.sport_event_mode import SportEventMode

        d = src_dict.copy()
        category = Category.from_dict(d.pop("category"))

        competition = Competition.from_dict(d.pop("competition"))

        season = Season.from_dict(d.pop("season"))

        sport = Sport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SportEventContextGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, SportEventMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SportEventMode.from_dict(_mode)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, SportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = SportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, SportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = SportEventContextStage.from_dict(_stage)

        sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return sport_event_context
