from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_season_stages_groups_cup_rounds_response_200_stages_item_groups_item_cup_rounds_item_linked_cup_rounds_item_type import (
    GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItem")


@_attrs_define
class GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItem:
    """
    Attributes:
        id (str): Cup round id URN (sr:cup_round:x)
        type (GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItemType):
        name (Union[Unset, str]): Name of round. Ex. quarterfinal
        order (Union[Unset, int]):
        state (Union[Unset, str]): Ex. winner, decided, unstarted, cancelled
        winner_id (Union[Unset, str]): Competitor URN. Ex. sr:competitor:23432
    """

    id: str
    type: GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItemType
    name: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    winner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        name = self.name

        order = self.order

        state = self.state

        winner_id = self.winner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if state is not UNSET:
            field_dict["state"] = state
        if winner_id is not UNSET:
            field_dict["winner_id"] = winner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = GetSeasonStagesGroupsCupRoundsResponse200StagesItemGroupsItemCupRoundsItemLinkedCupRoundsItemType(
            d.pop("type")
        )

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        state = d.pop("state", UNSET)

        winner_id = d.pop("winner_id", UNSET)

        get_season_stages_groups_cup_rounds_response_200_stages_item_groups_item_cup_rounds_item_linked_cup_rounds_item = cls(
            id=id,
            type=type,
            name=name,
            order=order,
            state=state,
            winner_id=winner_id,
        )

        get_season_stages_groups_cup_rounds_response_200_stages_item_groups_item_cup_rounds_item_linked_cup_rounds_item.additional_properties = d
        return get_season_stages_groups_cup_rounds_response_200_stages_item_groups_item_cup_rounds_item_linked_cup_rounds_item

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
