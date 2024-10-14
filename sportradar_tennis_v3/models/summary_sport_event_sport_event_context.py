from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_sport_event_sport_event_context_category import SummarySportEventSportEventContextCategory
    from ..models.summary_sport_event_sport_event_context_competition import (
        SummarySportEventSportEventContextCompetition,
    )
    from ..models.summary_sport_event_sport_event_context_groups_item import (
        SummarySportEventSportEventContextGroupsItem,
    )
    from ..models.summary_sport_event_sport_event_context_mode import SummarySportEventSportEventContextMode
    from ..models.summary_sport_event_sport_event_context_round import SummarySportEventSportEventContextRound
    from ..models.summary_sport_event_sport_event_context_season import SummarySportEventSportEventContextSeason
    from ..models.summary_sport_event_sport_event_context_sport import SummarySportEventSportEventContextSport
    from ..models.summary_sport_event_sport_event_context_stage import SummarySportEventSportEventContextStage


T = TypeVar("T", bound="SummarySportEventSportEventContext")


@_attrs_define
class SummarySportEventSportEventContext:
    """
    Attributes:
        category (SummarySportEventSportEventContextCategory):
        competition (SummarySportEventSportEventContextCompetition):
        season (SummarySportEventSportEventContextSeason):
        sport (SummarySportEventSportEventContextSport):
        groups (Union[Unset, List['SummarySportEventSportEventContextGroupsItem']]):
        mode (Union[Unset, SummarySportEventSportEventContextMode]):
        round_ (Union[Unset, SummarySportEventSportEventContextRound]):
        stage (Union[Unset, SummarySportEventSportEventContextStage]):
    """

    category: "SummarySportEventSportEventContextCategory"
    competition: "SummarySportEventSportEventContextCompetition"
    season: "SummarySportEventSportEventContextSeason"
    sport: "SummarySportEventSportEventContextSport"
    groups: Union[Unset, List["SummarySportEventSportEventContextGroupsItem"]] = UNSET
    mode: Union[Unset, "SummarySportEventSportEventContextMode"] = UNSET
    round_: Union[Unset, "SummarySportEventSportEventContextRound"] = UNSET
    stage: Union[Unset, "SummarySportEventSportEventContextStage"] = UNSET

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
        from ..models.summary_sport_event_sport_event_context_category import SummarySportEventSportEventContextCategory
        from ..models.summary_sport_event_sport_event_context_competition import (
            SummarySportEventSportEventContextCompetition,
        )
        from ..models.summary_sport_event_sport_event_context_groups_item import (
            SummarySportEventSportEventContextGroupsItem,
        )
        from ..models.summary_sport_event_sport_event_context_mode import SummarySportEventSportEventContextMode
        from ..models.summary_sport_event_sport_event_context_round import SummarySportEventSportEventContextRound
        from ..models.summary_sport_event_sport_event_context_season import SummarySportEventSportEventContextSeason
        from ..models.summary_sport_event_sport_event_context_sport import SummarySportEventSportEventContextSport
        from ..models.summary_sport_event_sport_event_context_stage import SummarySportEventSportEventContextStage

        d = src_dict.copy()
        category = SummarySportEventSportEventContextCategory.from_dict(d.pop("category"))

        competition = SummarySportEventSportEventContextCompetition.from_dict(d.pop("competition"))

        season = SummarySportEventSportEventContextSeason.from_dict(d.pop("season"))

        sport = SummarySportEventSportEventContextSport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SummarySportEventSportEventContextGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, SummarySportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SummarySportEventSportEventContextMode.from_dict(_mode)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, SummarySportEventSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = SummarySportEventSportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, SummarySportEventSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = SummarySportEventSportEventContextStage.from_dict(_stage)

        summary_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return summary_sport_event_sport_event_context
