from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SportEventProbabilitySportEventChildrenItemVenue")


@_attrs_define
class SportEventProbabilitySportEventChildrenItemVenue:
    """
    Attributes:
        id (str): Venue URN (sr:venue:x)
        name (str):
        capacity (Union[Unset, int]):
        changed (Union[Unset, bool]):
        city_name (Union[Unset, str]):
        country_code (Union[Unset, str]): ISO 3361-1 A3 Country Code
        country_name (Union[Unset, str]):
        map_coordinates (Union[Unset, str]):
        reduced_capacity (Union[Unset, bool]):
        reduced_capacity_max (Union[Unset, int]):
        timezone (Union[Unset, str]): Australia/Melbourne
    """

    id: str
    name: str
    capacity: Union[Unset, int] = UNSET
    changed: Union[Unset, bool] = UNSET
    city_name: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    country_name: Union[Unset, str] = UNSET
    map_coordinates: Union[Unset, str] = UNSET
    reduced_capacity: Union[Unset, bool] = UNSET
    reduced_capacity_max: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        capacity = self.capacity

        changed = self.changed

        city_name = self.city_name

        country_code = self.country_code

        country_name = self.country_name

        map_coordinates = self.map_coordinates

        reduced_capacity = self.reduced_capacity

        reduced_capacity_max = self.reduced_capacity_max

        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if changed is not UNSET:
            field_dict["changed"] = changed
        if city_name is not UNSET:
            field_dict["city_name"] = city_name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if map_coordinates is not UNSET:
            field_dict["map_coordinates"] = map_coordinates
        if reduced_capacity is not UNSET:
            field_dict["reduced_capacity"] = reduced_capacity
        if reduced_capacity_max is not UNSET:
            field_dict["reduced_capacity_max"] = reduced_capacity_max
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        capacity = d.pop("capacity", UNSET)

        changed = d.pop("changed", UNSET)

        city_name = d.pop("city_name", UNSET)

        country_code = d.pop("country_code", UNSET)

        country_name = d.pop("country_name", UNSET)

        map_coordinates = d.pop("map_coordinates", UNSET)

        reduced_capacity = d.pop("reduced_capacity", UNSET)

        reduced_capacity_max = d.pop("reduced_capacity_max", UNSET)

        timezone = d.pop("timezone", UNSET)

        sport_event_probability_sport_event_children_item_venue = cls(
            id=id,
            name=name,
            capacity=capacity,
            changed=changed,
            city_name=city_name,
            country_code=country_code,
            country_name=country_name,
            map_coordinates=map_coordinates,
            reduced_capacity=reduced_capacity,
            reduced_capacity_max=reduced_capacity_max,
            timezone=timezone,
        )

        return sport_event_probability_sport_event_children_item_venue
