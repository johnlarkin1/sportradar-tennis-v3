from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_category import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCategory,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_competition import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCompetition,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_groups_item import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextGroupsItem,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_mode import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextMode,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_round import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_season import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSeason,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_sport import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSport,
    )
    from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_stage import (
        GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStage,
    )


T = TypeVar("T", bound="GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContext")


@_attrs_define
class GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContext:
    """
    Attributes:
        category (GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCategory):
        competition (GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCompetition):
        season (GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSeason):
        sport (GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSport):
        groups (Union[Unset,
            List['GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextGroupsItem']]):
        mode (Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextMode]):
        round_ (Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound]):
        stage (Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStage]):
    """

    category: "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCategory"
    competition: "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCompetition"
    season: "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSeason"
    sport: "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSport"
    groups: Union[
        Unset, List["GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextGroupsItem"]
    ] = UNSET
    mode: Union[Unset, "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextMode"] = UNSET
    round_: Union[Unset, "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound"] = (
        UNSET
    )
    stage: Union[Unset, "GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStage"] = (
        UNSET
    )

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
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_category import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCategory,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_competition import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCompetition,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_groups_item import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextGroupsItem,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_mode import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextMode,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_round import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_season import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSeason,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_sport import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSport,
        )
        from ..models.get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context_stage import (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStage,
        )

        d = src_dict.copy()
        category = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCategory.from_dict(
            d.pop("category")
        )

        competition = (
            GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextCompetition.from_dict(
                d.pop("competition")
            )
        )

        season = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSeason.from_dict(
            d.pop("season")
        )

        sport = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextSport.from_dict(
            d.pop("sport")
        )

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = (
                GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextGroupsItem.from_dict(
                    groups_item_data
                )
            )

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextMode.from_dict(
                _mode
            )

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextRound.from_dict(
                _round_
            )

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = GetCompetitorVersusSummariesResponse200LastMeetingsItemSportEventSportEventContextStage.from_dict(
                _stage
            )

        get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return get_competitor_versus_summaries_response_200_last_meetings_item_sport_event_sport_event_context
