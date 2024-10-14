from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_groups_item_comments_item import StandingGroupsItemCommentsItem
    from ..models.standing_groups_item_stage import StandingGroupsItemStage
    from ..models.standing_groups_item_standings_item import StandingGroupsItemStandingsItem


T = TypeVar("T", bound="StandingGroupsItem")


@_attrs_define
class StandingGroupsItem:
    """
    Attributes:
        id (str): Group URN (sr:group:x)
        name (str):
        comments (Union[Unset, List['StandingGroupsItemCommentsItem']]):
        group_name (Union[Unset, str]):
        live (Union[Unset, bool]):
        parent_group_id (Union[Unset, str]):
        stage (Union[Unset, StandingGroupsItemStage]):
        standings (Union[Unset, List['StandingGroupsItemStandingsItem']]):
    """

    id: str
    name: str
    comments: Union[Unset, List["StandingGroupsItemCommentsItem"]] = UNSET
    group_name: Union[Unset, str] = UNSET
    live: Union[Unset, bool] = UNSET
    parent_group_id: Union[Unset, str] = UNSET
    stage: Union[Unset, "StandingGroupsItemStage"] = UNSET
    standings: Union[Unset, List["StandingGroupsItemStandingsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        group_name = self.group_name

        live = self.live

        parent_group_id = self.parent_group_id

        stage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        standings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.standings, Unset):
            standings = []
            for standings_item_data in self.standings:
                standings_item = standings_item_data.to_dict()
                standings.append(standings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if comments is not UNSET:
            field_dict["comments"] = comments
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if live is not UNSET:
            field_dict["live"] = live
        if parent_group_id is not UNSET:
            field_dict["parent_group_id"] = parent_group_id
        if stage is not UNSET:
            field_dict["stage"] = stage
        if standings is not UNSET:
            field_dict["standings"] = standings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.standing_groups_item_comments_item import StandingGroupsItemCommentsItem
        from ..models.standing_groups_item_stage import StandingGroupsItemStage
        from ..models.standing_groups_item_standings_item import StandingGroupsItemStandingsItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = StandingGroupsItemCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        group_name = d.pop("group_name", UNSET)

        live = d.pop("live", UNSET)

        parent_group_id = d.pop("parent_group_id", UNSET)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, StandingGroupsItemStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = StandingGroupsItemStage.from_dict(_stage)

        standings = []
        _standings = d.pop("standings", UNSET)
        for standings_item_data in _standings or []:
            standings_item = StandingGroupsItemStandingsItem.from_dict(standings_item_data)

            standings.append(standings_item)

        standing_groups_item = cls(
            id=id,
            name=name,
            comments=comments,
            group_name=group_name,
            live=live,
            parent_group_id=parent_group_id,
            stage=stage,
            standings=standings,
        )

        return standing_groups_item
