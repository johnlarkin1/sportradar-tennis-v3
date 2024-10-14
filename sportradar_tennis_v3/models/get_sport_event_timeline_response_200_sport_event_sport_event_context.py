from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_category import (
        GetSportEventTimelineResponse200SportEventSportEventContextCategory,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_competition import (
        GetSportEventTimelineResponse200SportEventSportEventContextCompetition,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_groups_item import (
        GetSportEventTimelineResponse200SportEventSportEventContextGroupsItem,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_mode import (
        GetSportEventTimelineResponse200SportEventSportEventContextMode,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_round import (
        GetSportEventTimelineResponse200SportEventSportEventContextRound,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_season import (
        GetSportEventTimelineResponse200SportEventSportEventContextSeason,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_sport import (
        GetSportEventTimelineResponse200SportEventSportEventContextSport,
    )
    from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_stage import (
        GetSportEventTimelineResponse200SportEventSportEventContextStage,
    )


T = TypeVar("T", bound="GetSportEventTimelineResponse200SportEventSportEventContext")


@_attrs_define
class GetSportEventTimelineResponse200SportEventSportEventContext:
    """
    Attributes:
        category (GetSportEventTimelineResponse200SportEventSportEventContextCategory):
        competition (GetSportEventTimelineResponse200SportEventSportEventContextCompetition):
        season (GetSportEventTimelineResponse200SportEventSportEventContextSeason):
        sport (GetSportEventTimelineResponse200SportEventSportEventContextSport):
        groups (Union[Unset, List['GetSportEventTimelineResponse200SportEventSportEventContextGroupsItem']]):
        mode (Union[Unset, GetSportEventTimelineResponse200SportEventSportEventContextMode]):
        round_ (Union[Unset, GetSportEventTimelineResponse200SportEventSportEventContextRound]):
        stage (Union[Unset, GetSportEventTimelineResponse200SportEventSportEventContextStage]):
    """

    category: "GetSportEventTimelineResponse200SportEventSportEventContextCategory"
    competition: "GetSportEventTimelineResponse200SportEventSportEventContextCompetition"
    season: "GetSportEventTimelineResponse200SportEventSportEventContextSeason"
    sport: "GetSportEventTimelineResponse200SportEventSportEventContextSport"
    groups: Union[Unset, List["GetSportEventTimelineResponse200SportEventSportEventContextGroupsItem"]] = UNSET
    mode: Union[Unset, "GetSportEventTimelineResponse200SportEventSportEventContextMode"] = UNSET
    round_: Union[Unset, "GetSportEventTimelineResponse200SportEventSportEventContextRound"] = UNSET
    stage: Union[Unset, "GetSportEventTimelineResponse200SportEventSportEventContextStage"] = UNSET

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
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_category import (
            GetSportEventTimelineResponse200SportEventSportEventContextCategory,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_competition import (
            GetSportEventTimelineResponse200SportEventSportEventContextCompetition,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_groups_item import (
            GetSportEventTimelineResponse200SportEventSportEventContextGroupsItem,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_mode import (
            GetSportEventTimelineResponse200SportEventSportEventContextMode,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_round import (
            GetSportEventTimelineResponse200SportEventSportEventContextRound,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_season import (
            GetSportEventTimelineResponse200SportEventSportEventContextSeason,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_sport import (
            GetSportEventTimelineResponse200SportEventSportEventContextSport,
        )
        from ..models.get_sport_event_timeline_response_200_sport_event_sport_event_context_stage import (
            GetSportEventTimelineResponse200SportEventSportEventContextStage,
        )

        d = src_dict.copy()
        category = GetSportEventTimelineResponse200SportEventSportEventContextCategory.from_dict(d.pop("category"))

        competition = GetSportEventTimelineResponse200SportEventSportEventContextCompetition.from_dict(
            d.pop("competition")
        )

        season = GetSportEventTimelineResponse200SportEventSportEventContextSeason.from_dict(d.pop("season"))

        sport = GetSportEventTimelineResponse200SportEventSportEventContextSport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GetSportEventTimelineResponse200SportEventSportEventContextGroupsItem.from_dict(
                groups_item_data
            )

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, GetSportEventTimelineResponse200SportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GetSportEventTimelineResponse200SportEventSportEventContextMode.from_dict(_mode)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, GetSportEventTimelineResponse200SportEventSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = GetSportEventTimelineResponse200SportEventSportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, GetSportEventTimelineResponse200SportEventSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = GetSportEventTimelineResponse200SportEventSportEventContextStage.from_dict(_stage)

        get_sport_event_timeline_response_200_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return get_sport_event_timeline_response_200_sport_event_sport_event_context
