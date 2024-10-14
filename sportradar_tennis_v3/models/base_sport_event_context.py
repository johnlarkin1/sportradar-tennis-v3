from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_sport_event_context_category import BaseSportEventContextCategory
    from ..models.base_sport_event_context_competition import BaseSportEventContextCompetition
    from ..models.base_sport_event_context_groups_item import BaseSportEventContextGroupsItem
    from ..models.base_sport_event_context_round import BaseSportEventContextRound
    from ..models.base_sport_event_context_season import BaseSportEventContextSeason
    from ..models.base_sport_event_context_sport import BaseSportEventContextSport
    from ..models.base_sport_event_context_stage import BaseSportEventContextStage


T = TypeVar("T", bound="BaseSportEventContext")


@_attrs_define
class BaseSportEventContext:
    """
    Attributes:
        category (BaseSportEventContextCategory):
        competition (BaseSportEventContextCompetition):
        season (BaseSportEventContextSeason):
        sport (BaseSportEventContextSport):
        groups (Union[Unset, List['BaseSportEventContextGroupsItem']]):
        round_ (Union[Unset, BaseSportEventContextRound]):
        stage (Union[Unset, BaseSportEventContextStage]):
    """

    category: "BaseSportEventContextCategory"
    competition: "BaseSportEventContextCompetition"
    season: "BaseSportEventContextSeason"
    sport: "BaseSportEventContextSport"
    groups: Union[Unset, List["BaseSportEventContextGroupsItem"]] = UNSET
    round_: Union[Unset, "BaseSportEventContextRound"] = UNSET
    stage: Union[Unset, "BaseSportEventContextStage"] = UNSET

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
        if round_ is not UNSET:
            field_dict["round"] = round_
        if stage is not UNSET:
            field_dict["stage"] = stage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_sport_event_context_category import BaseSportEventContextCategory
        from ..models.base_sport_event_context_competition import BaseSportEventContextCompetition
        from ..models.base_sport_event_context_groups_item import BaseSportEventContextGroupsItem
        from ..models.base_sport_event_context_round import BaseSportEventContextRound
        from ..models.base_sport_event_context_season import BaseSportEventContextSeason
        from ..models.base_sport_event_context_sport import BaseSportEventContextSport
        from ..models.base_sport_event_context_stage import BaseSportEventContextStage

        d = src_dict.copy()
        category = BaseSportEventContextCategory.from_dict(d.pop("category"))

        competition = BaseSportEventContextCompetition.from_dict(d.pop("competition"))

        season = BaseSportEventContextSeason.from_dict(d.pop("season"))

        sport = BaseSportEventContextSport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = BaseSportEventContextGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, BaseSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = BaseSportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, BaseSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = BaseSportEventContextStage.from_dict(_stage)

        base_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            round_=round_,
            stage=stage,
        )

        return base_sport_event_context
