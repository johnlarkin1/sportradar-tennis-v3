from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_category import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCategory,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_competition import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCompetition,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_groups_item import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextGroupsItem,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_mode import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextMode,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_round import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextRound,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_season import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSeason,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_sport import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSport,
    )
    from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_stage import (
        GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStage,
    )


T = TypeVar("T", bound="GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContext")


@_attrs_define
class GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContext:
    """
    Attributes:
        category (GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCategory):
        competition
            (GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCompetition):
        season (GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSeason):
        sport (GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSport):
        groups (Union[Unset,
            List['GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextGroupsItem']]):
        mode (Union[Unset,
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextMode]):
        round_ (Union[Unset,
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextRound]):
        stage (Union[Unset,
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStage]):
    """

    category: "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCategory"
    competition: "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCompetition"
    season: "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSeason"
    sport: "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSport"
    groups: Union[
        Unset, List["GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextGroupsItem"]
    ] = UNSET
    mode: Union[
        Unset, "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextMode"
    ] = UNSET
    round_: Union[
        Unset, "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextRound"
    ] = UNSET
    stage: Union[
        Unset, "GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStage"
    ] = UNSET

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
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_category import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCategory,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_competition import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCompetition,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_groups_item import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextGroupsItem,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_mode import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextMode,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_round import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextRound,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_season import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSeason,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_sport import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSport,
        )
        from ..models.get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context_stage import (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStage,
        )

        d = src_dict.copy()
        category = (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCategory.from_dict(
                d.pop("category")
            )
        )

        competition = GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextCompetition.from_dict(
            d.pop("competition")
        )

        season = (
            GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSeason.from_dict(
                d.pop("season")
            )
        )

        sport = GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextSport.from_dict(
            d.pop("sport")
        )

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextGroupsItem.from_dict(
                groups_item_data
            )

            groups.append(groups_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = (
                GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextMode.from_dict(
                    _mode
                )
            )

        _round_ = d.pop("round", UNSET)
        round_: Union[
            Unset, GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextRound
        ]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = (
                GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextRound.from_dict(
                    _round_
                )
            )

        _stage = d.pop("stage", UNSET)
        stage: Union[
            Unset, GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStage
        ]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = (
                GetSeasonProbabilitiesResponse200SportEventProbabilitiesItemSportEventSportEventContextStage.from_dict(
                    _stage
                )
            )

        get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context = cls(
            category=category,
            competition=competition,
            season=season,
            sport=sport,
            groups=groups,
            mode=mode,
            round_=round_,
            stage=stage,
        )

        return get_season_probabilities_response_200_sport_event_probabilities_item_sport_event_sport_event_context
