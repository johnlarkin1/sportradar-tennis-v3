from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_brackets_group_cup_rounds_item import SeasonBracketsGroupCupRoundsItem


T = TypeVar("T", bound="SeasonBracketsGroup")


@_attrs_define
class SeasonBracketsGroup:
    """
    Attributes:
        group_name (str):
        id (str):
        cup_rounds (Union[Unset, List['SeasonBracketsGroupCupRoundsItem']]):
        order (Union[Unset, int]):
    """

    group_name: str
    id: str
    cup_rounds: Union[Unset, List["SeasonBracketsGroupCupRoundsItem"]] = UNSET
    order: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name

        id = self.id

        cup_rounds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cup_rounds, Unset):
            cup_rounds = []
            for cup_rounds_item_data in self.cup_rounds:
                cup_rounds_item = cup_rounds_item_data.to_dict()
                cup_rounds.append(cup_rounds_item)

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "group_name": group_name,
                "id": id,
            }
        )
        if cup_rounds is not UNSET:
            field_dict["cup_rounds"] = cup_rounds
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.season_brackets_group_cup_rounds_item import SeasonBracketsGroupCupRoundsItem

        d = src_dict.copy()
        group_name = d.pop("group_name")

        id = d.pop("id")

        cup_rounds = []
        _cup_rounds = d.pop("cup_rounds", UNSET)
        for cup_rounds_item_data in _cup_rounds or []:
            cup_rounds_item = SeasonBracketsGroupCupRoundsItem.from_dict(cup_rounds_item_data)

            cup_rounds.append(cup_rounds_item)

        order = d.pop("order", UNSET)

        season_brackets_group = cls(
            group_name=group_name,
            id=id,
            cup_rounds=cup_rounds,
            order=order,
        )

        return season_brackets_group
