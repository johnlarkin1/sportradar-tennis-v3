from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.venue import Venue


T = TypeVar("T", bound="Complex")


@_attrs_define
class Complex:
    """
    Attributes:
        id (str): Complex URN (sr:complex:xx)
        name (str):
        venues (Union[Unset, List['Venue']]):
    """

    id: str
    name: str
    venues: Union[Unset, List["Venue"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        venues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.venues, Unset):
            venues = []
            for venues_item_data in self.venues:
                venues_item = venues_item_data.to_dict()
                venues.append(venues_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if venues is not UNSET:
            field_dict["venues"] = venues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.venue import Venue

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        venues = []
        _venues = d.pop("venues", UNSET)
        for venues_item_data in _venues or []:
            venues_item = Venue.from_dict(venues_item_data)

            venues.append(venues_item)

        complex_ = cls(
            id=id,
            name=name,
            venues=venues,
        )

        return complex_
