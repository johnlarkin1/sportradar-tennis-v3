from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_category import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCategory,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_competition import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCompetition,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_groups_item import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextGroupsItem,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_mode import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextMode,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_round import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextRound,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_season import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_sport import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport,
    )
    from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_stage import (
        GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextStage,
    )


T = TypeVar("T", bound="GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext")


@_attrs_define
class GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContext:
    """
    Attributes:
        category (GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCategory):
        competition (GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCompetition):
        season (GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason):
        sport (GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport):
        groups (Union[Unset,
            List['GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextGroupsItem']]):
        mode (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextMode]):
        round_ (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextRound]):
        stage (Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextStage]):
    """

    category: "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCategory"
    competition: "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCompetition"
    season: "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason"
    sport: "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport"
    groups: Union[
        Unset, List["GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextGroupsItem"]
    ] = UNSET
    mode: Union[Unset, "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextMode"] = UNSET
    round_: Union[Unset, "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextRound"] = UNSET
    stage: Union[Unset, "GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextStage"] = UNSET

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
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_category import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCategory,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_competition import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCompetition,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_groups_item import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextGroupsItem,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_mode import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextMode,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_round import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextRound,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_season import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_sport import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport,
        )
        from ..models.get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context_stage import (
            GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextStage,
        )

        d = src_dict.copy()
        category = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCategory.from_dict(
            d.pop("category")
        )

        competition = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextCompetition.from_dict(
            d.pop("competition")
        )

        season = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSeason.from_dict(
            d.pop("season")
        )

        sport = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextSport.from_dict(d.pop("sport"))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextGroupsItem.from_dict(
                groups_item_data
            )

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextMode.from_dict(_mode)

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextRound.from_dict(_round_)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = GetCompetitorSummariesResponse200SummariesItemSportEventSportEventContextStage.from_dict(_stage)

        get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return get_competitor_summaries_response_200_summaries_item_sport_event_sport_event_context
