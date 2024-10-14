from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_summary_sport_event_sport_event_context_category import (
        BaseSummarySportEventSportEventContextCategory,
    )
    from ..models.base_summary_sport_event_sport_event_context_competition import (
        BaseSummarySportEventSportEventContextCompetition,
    )
    from ..models.base_summary_sport_event_sport_event_context_groups_item import (
        BaseSummarySportEventSportEventContextGroupsItem,
    )
    from ..models.base_summary_sport_event_sport_event_context_mode import BaseSummarySportEventSportEventContextMode
    from ..models.base_summary_sport_event_sport_event_context_round import BaseSummarySportEventSportEventContextRound
    from ..models.base_summary_sport_event_sport_event_context_season import (
        BaseSummarySportEventSportEventContextSeason,
    )
    from ..models.base_summary_sport_event_sport_event_context_sport import BaseSummarySportEventSportEventContextSport
    from ..models.base_summary_sport_event_sport_event_context_stage import BaseSummarySportEventSportEventContextStage


T = TypeVar("T", bound="BaseSummarySportEventSportEventContext")


@_attrs_define
class BaseSummarySportEventSportEventContext:
    """
    Attributes:
        category (BaseSummarySportEventSportEventContextCategory):
        competition (BaseSummarySportEventSportEventContextCompetition):
        season (BaseSummarySportEventSportEventContextSeason):
        sport (BaseSummarySportEventSportEventContextSport):
        groups (Union[Unset, List['BaseSummarySportEventSportEventContextGroupsItem']]):
        mode (Union[Unset, BaseSummarySportEventSportEventContextMode]):
        round_ (Union[Unset, BaseSummarySportEventSportEventContextRound]):
        stage (Union[Unset, BaseSummarySportEventSportEventContextStage]):
    """

    category: "BaseSummarySportEventSportEventContextCategory"
    competition: "BaseSummarySportEventSportEventContextCompetition"
    season: "BaseSummarySportEventSportEventContextSeason"
    sport: "BaseSummarySportEventSportEventContextSport"
    groups: Union[Unset, List["BaseSummarySportEventSportEventContextGroupsItem"]] = UNSET
    mode: Union[Unset, "BaseSummarySportEventSportEventContextMode"] = UNSET
    round_: Union[Unset, "BaseSummarySportEventSportEventContextRound"] = UNSET
    stage: Union[Unset, "BaseSummarySportEventSportEventContextStage"] = UNSET

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
        from ..models.base_summary_sport_event_sport_event_context_category import (
            BaseSummarySportEventSportEventContextCategory,
        )
        from ..models.base_summary_sport_event_sport_event_context_competition import (
            BaseSummarySportEventSportEventContextCompetition,
        )
        from ..models.base_summary_sport_event_sport_event_context_groups_item import (
            BaseSummarySportEventSportEventContextGroupsItem,
        )
        from ..models.base_summary_sport_event_sport_event_context_mode import (
            BaseSummarySportEventSportEventContextMode,
        )
        from ..models.base_summary_sport_event_sport_event_context_round import (
            BaseSummarySportEventSportEventContextRound,
        )
        from ..models.base_summary_sport_event_sport_event_context_season import (
            BaseSummarySportEventSportEventContextSeason,
        )
        from ..models.base_summary_sport_event_sport_event_context_sport import (
            BaseSummarySportEventSportEventContextSport,
        )
        from ..models.base_summary_sport_event_sport_event_context_stage import (
            BaseSummarySportEventSportEventContextStage,
        )

        d = src_dict.copy()
        category = BaseSummarySportEventSportEventContextCategory.from_dict(d.pop("category"))

        competition = BaseSummarySportEventSportEventContextCompetition.from_dict(d.pop("competition"))

        season = BaseSummarySportEventSportEventContextSeason.from_dict(d.pop("season"))

        sport = BaseSummarySportEventSportEventContextSport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = BaseSummarySportEventSportEventContextGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, BaseSummarySportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = BaseSummarySportEventSportEventContextMode.from_dict(_mode)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, BaseSummarySportEventSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = BaseSummarySportEventSportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, BaseSummarySportEventSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = BaseSummarySportEventSportEventContextStage.from_dict(_stage)

        base_summary_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return base_summary_sport_event_sport_event_context
