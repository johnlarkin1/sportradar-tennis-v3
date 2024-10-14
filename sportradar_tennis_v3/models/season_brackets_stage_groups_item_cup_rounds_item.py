from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_brackets_stage_groups_item_cup_rounds_item_linked_cup_rounds_item import (
        SeasonBracketsStageGroupsItemCupRoundsItemLinkedCupRoundsItem,
    )
    from ..models.season_brackets_stage_groups_item_cup_rounds_item_sport_events_item import (
        SeasonBracketsStageGroupsItemCupRoundsItemSportEventsItem,
    )


T = TypeVar("T", bound="SeasonBracketsStageGroupsItemCupRoundsItem")


@_attrs_define
class SeasonBracketsStageGroupsItemCupRoundsItem:
    """
    Attributes:
        id (str): Cup round id URN (sr:cup_round:x)
        linked_cup_rounds (Union[Unset, List['SeasonBracketsStageGroupsItemCupRoundsItemLinkedCupRoundsItem']]):
        name (Union[Unset, str]): Name of round. Ex. quarterfinal
        order (Union[Unset, int]):
        sport_events (Union[Unset, List['SeasonBracketsStageGroupsItemCupRoundsItemSportEventsItem']]):
        state (Union[Unset, str]): Ex. ended, decided, unstarted, cancelled, winner
        winner_id (Union[Unset, str]): Competitor URN. Ex. sr:competitor:23432
    """

    id: str
    linked_cup_rounds: Union[Unset, List["SeasonBracketsStageGroupsItemCupRoundsItemLinkedCupRoundsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    sport_events: Union[Unset, List["SeasonBracketsStageGroupsItemCupRoundsItemSportEventsItem"]] = UNSET
    state: Union[Unset, str] = UNSET
    winner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        linked_cup_rounds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.linked_cup_rounds, Unset):
            linked_cup_rounds = []
            for linked_cup_rounds_item_data in self.linked_cup_rounds:
                linked_cup_rounds_item = linked_cup_rounds_item_data.to_dict()
                linked_cup_rounds.append(linked_cup_rounds_item)

        name = self.name

        order = self.order

        sport_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sport_events, Unset):
            sport_events = []
            for sport_events_item_data in self.sport_events:
                sport_events_item = sport_events_item_data.to_dict()
                sport_events.append(sport_events_item)

        state = self.state

        winner_id = self.winner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if linked_cup_rounds is not UNSET:
            field_dict["linked_cup_rounds"] = linked_cup_rounds
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if sport_events is not UNSET:
            field_dict["sport_events"] = sport_events
        if state is not UNSET:
            field_dict["state"] = state
        if winner_id is not UNSET:
            field_dict["winner_id"] = winner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_brackets_stage_groups_item_cup_rounds_item_linked_cup_rounds_item import (
            SeasonBracketsStageGroupsItemCupRoundsItemLinkedCupRoundsItem,
        )
        from ..models.season_brackets_stage_groups_item_cup_rounds_item_sport_events_item import (
            SeasonBracketsStageGroupsItemCupRoundsItemSportEventsItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        linked_cup_rounds = []
        _linked_cup_rounds = d.pop("linked_cup_rounds", UNSET)
        for linked_cup_rounds_item_data in _linked_cup_rounds or []:
            linked_cup_rounds_item = SeasonBracketsStageGroupsItemCupRoundsItemLinkedCupRoundsItem.from_dict(
                linked_cup_rounds_item_data
            )

            linked_cup_rounds.append(linked_cup_rounds_item)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        sport_events = []
        _sport_events = d.pop("sport_events", UNSET)
        for sport_events_item_data in _sport_events or []:
            sport_events_item = SeasonBracketsStageGroupsItemCupRoundsItemSportEventsItem.from_dict(
                sport_events_item_data
            )

            sport_events.append(sport_events_item)

        state = d.pop("state", UNSET)

        winner_id = d.pop("winner_id", UNSET)

        season_brackets_stage_groups_item_cup_rounds_item = cls(
            id=id,
            linked_cup_rounds=linked_cup_rounds,
            name=name,
            order=order,
            sport_events=sport_events,
            state=state,
            winner_id=winner_id,
        )

        season_brackets_stage_groups_item_cup_rounds_item.additional_properties = d
        return season_brackets_stage_groups_item_cup_rounds_item

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
