from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_category import (
        GetSportEventSummaryResponse200SportEventSportEventContextCategory,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_competition import (
        GetSportEventSummaryResponse200SportEventSportEventContextCompetition,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_groups_item import (
        GetSportEventSummaryResponse200SportEventSportEventContextGroupsItem,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_mode import (
        GetSportEventSummaryResponse200SportEventSportEventContextMode,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_round import (
        GetSportEventSummaryResponse200SportEventSportEventContextRound,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_season import (
        GetSportEventSummaryResponse200SportEventSportEventContextSeason,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_sport import (
        GetSportEventSummaryResponse200SportEventSportEventContextSport,
    )
    from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_stage import (
        GetSportEventSummaryResponse200SportEventSportEventContextStage,
    )


T = TypeVar("T", bound="GetSportEventSummaryResponse200SportEventSportEventContext")


@_attrs_define
class GetSportEventSummaryResponse200SportEventSportEventContext:
    """
    Attributes:
        category (GetSportEventSummaryResponse200SportEventSportEventContextCategory):
        competition (GetSportEventSummaryResponse200SportEventSportEventContextCompetition):
        season (GetSportEventSummaryResponse200SportEventSportEventContextSeason):
        sport (GetSportEventSummaryResponse200SportEventSportEventContextSport):
        groups (Union[Unset, List['GetSportEventSummaryResponse200SportEventSportEventContextGroupsItem']]):
        mode (Union[Unset, GetSportEventSummaryResponse200SportEventSportEventContextMode]):
        round_ (Union[Unset, GetSportEventSummaryResponse200SportEventSportEventContextRound]):
        stage (Union[Unset, GetSportEventSummaryResponse200SportEventSportEventContextStage]):
    """

    category: "GetSportEventSummaryResponse200SportEventSportEventContextCategory"
    competition: "GetSportEventSummaryResponse200SportEventSportEventContextCompetition"
    season: "GetSportEventSummaryResponse200SportEventSportEventContextSeason"
    sport: "GetSportEventSummaryResponse200SportEventSportEventContextSport"
    groups: Union[Unset, List["GetSportEventSummaryResponse200SportEventSportEventContextGroupsItem"]] = UNSET
    mode: Union[Unset, "GetSportEventSummaryResponse200SportEventSportEventContextMode"] = UNSET
    round_: Union[Unset, "GetSportEventSummaryResponse200SportEventSportEventContextRound"] = UNSET
    stage: Union[Unset, "GetSportEventSummaryResponse200SportEventSportEventContextStage"] = UNSET

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
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_category import (
            GetSportEventSummaryResponse200SportEventSportEventContextCategory,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_competition import (
            GetSportEventSummaryResponse200SportEventSportEventContextCompetition,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_groups_item import (
            GetSportEventSummaryResponse200SportEventSportEventContextGroupsItem,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_mode import (
            GetSportEventSummaryResponse200SportEventSportEventContextMode,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_round import (
            GetSportEventSummaryResponse200SportEventSportEventContextRound,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_season import (
            GetSportEventSummaryResponse200SportEventSportEventContextSeason,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_sport import (
            GetSportEventSummaryResponse200SportEventSportEventContextSport,
        )
        from ..models.get_sport_event_summary_response_200_sport_event_sport_event_context_stage import (
            GetSportEventSummaryResponse200SportEventSportEventContextStage,
        )

        d = src_dict.copy()
        category = GetSportEventSummaryResponse200SportEventSportEventContextCategory.from_dict(d.pop("category"))

        competition = GetSportEventSummaryResponse200SportEventSportEventContextCompetition.from_dict(
            d.pop("competition")
        )

        season = GetSportEventSummaryResponse200SportEventSportEventContextSeason.from_dict(d.pop("season"))

        sport = GetSportEventSummaryResponse200SportEventSportEventContextSport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GetSportEventSummaryResponse200SportEventSportEventContextGroupsItem.from_dict(
                groups_item_data
            )

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, GetSportEventSummaryResponse200SportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GetSportEventSummaryResponse200SportEventSportEventContextMode.from_dict(_mode)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, GetSportEventSummaryResponse200SportEventSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = GetSportEventSummaryResponse200SportEventSportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, GetSportEventSummaryResponse200SportEventSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = GetSportEventSummaryResponse200SportEventSportEventContextStage.from_dict(_stage)

        get_sport_event_summary_response_200_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return get_sport_event_summary_response_200_sport_event_sport_event_context
