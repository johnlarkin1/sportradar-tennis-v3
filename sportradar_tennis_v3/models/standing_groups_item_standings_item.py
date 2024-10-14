from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_groups_item_standings_item_comments_item import StandingGroupsItemStandingsItemCommentsItem
    from ..models.standing_groups_item_standings_item_competitor import StandingGroupsItemStandingsItemCompetitor


T = TypeVar("T", bound="StandingGroupsItemStandingsItem")


@_attrs_define
class StandingGroupsItemStandingsItem:
    """
    Attributes:
        comments (Union[Unset, List['StandingGroupsItemStandingsItemCommentsItem']]):
        competitor (Union[Unset, StandingGroupsItemStandingsItemCompetitor]):
        current_outcome (Union[Unset, str]):
        loss (Union[Unset, int]):
        played (Union[Unset, int]):
        points (Union[Unset, int]):
        rank (Union[Unset, int]):
        sets_lost (Union[Unset, int]):
        sets_won (Union[Unset, int]):
        win (Union[Unset, int]):
    """

    comments: Union[Unset, List["StandingGroupsItemStandingsItemCommentsItem"]] = UNSET
    competitor: Union[Unset, "StandingGroupsItemStandingsItemCompetitor"] = UNSET
    current_outcome: Union[Unset, str] = UNSET
    loss: Union[Unset, int] = UNSET
    played: Union[Unset, int] = UNSET
    points: Union[Unset, int] = UNSET
    rank: Union[Unset, int] = UNSET
    sets_lost: Union[Unset, int] = UNSET
    sets_won: Union[Unset, int] = UNSET
    win: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        current_outcome = self.current_outcome

        loss = self.loss

        played = self.played

        points = self.points

        rank = self.rank

        sets_lost = self.sets_lost

        sets_won = self.sets_won

        win = self.win

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if current_outcome is not UNSET:
            field_dict["current_outcome"] = current_outcome
        if loss is not UNSET:
            field_dict["loss"] = loss
        if played is not UNSET:
            field_dict["played"] = played
        if points is not UNSET:
            field_dict["points"] = points
        if rank is not UNSET:
            field_dict["rank"] = rank
        if sets_lost is not UNSET:
            field_dict["sets_lost"] = sets_lost
        if sets_won is not UNSET:
            field_dict["sets_won"] = sets_won
        if win is not UNSET:
            field_dict["win"] = win

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standing_groups_item_standings_item_comments_item import (
            StandingGroupsItemStandingsItemCommentsItem,
        )
        from ..models.standing_groups_item_standings_item_competitor import StandingGroupsItemStandingsItemCompetitor

        d = src_dict.copy()
        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = StandingGroupsItemStandingsItemCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, StandingGroupsItemStandingsItemCompetitor]
        if isinstance(_competitor, Unset):
            competitor = UNSET
        else:
            competitor = StandingGroupsItemStandingsItemCompetitor.from_dict(_competitor)

        current_outcome = d.pop("current_outcome", UNSET)

        loss = d.pop("loss", UNSET)

        played = d.pop("played", UNSET)

        points = d.pop("points", UNSET)

        rank = d.pop("rank", UNSET)

        sets_lost = d.pop("sets_lost", UNSET)

        sets_won = d.pop("sets_won", UNSET)

        win = d.pop("win", UNSET)

        standing_groups_item_standings_item = cls(
            comments=comments,
            competitor=competitor,
            current_outcome=current_outcome,
            loss=loss,
            played=played,
            points=points,
            rank=rank,
            sets_lost=sets_lost,
            sets_won=sets_won,
            win=win,
        )

        standing_groups_item_standings_item.additional_properties = d
        return standing_groups_item_standings_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
