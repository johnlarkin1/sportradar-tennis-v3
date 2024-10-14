from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseCompetition")


@_attrs_define
class BaseCompetition:
    """
    Attributes:
        id (str): Competition URN (sr:competition:x)
        name (str):
        gender (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: str
    name: str
    gender: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        gender = self.gender

        parent_id = self.parent_id

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if gender is not UNSET:
            field_dict["gender"] = gender
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        gender = d.pop("gender", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        type = d.pop("type", UNSET)

        base_competition = cls(
            id=id,
            name=name,
            gender=gender,
            parent_id=parent_id,
            type=type,
        )

        return base_competition
