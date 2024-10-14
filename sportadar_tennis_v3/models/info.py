from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.enum_competition_status import EnumCompetitionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Info")


@_attrs_define
class Info:
    """
    Attributes:
        competition_status (Union[Unset, EnumCompetitionStatus]):
        complex_ (Union[Unset, str]):
        complex_id (Union[Unset, str]):
        number_of_competitors (Union[Unset, int]):
        number_of_qualified_competitors (Union[Unset, int]):
        number_of_scheduled_matches (Union[Unset, int]):
        prize_currency (Union[Unset, str]):
        prize_money (Union[Unset, int]):
        surface (Union[Unset, str]):
        venue_reduced_capacity (Union[Unset, bool]):
        venue_reduced_capacity_max (Union[Unset, int]):
    """

    competition_status: Union[Unset, EnumCompetitionStatus] = UNSET
    complex_: Union[Unset, str] = UNSET
    complex_id: Union[Unset, str] = UNSET
    number_of_competitors: Union[Unset, int] = UNSET
    number_of_qualified_competitors: Union[Unset, int] = UNSET
    number_of_scheduled_matches: Union[Unset, int] = UNSET
    prize_currency: Union[Unset, str] = UNSET
    prize_money: Union[Unset, int] = UNSET
    surface: Union[Unset, str] = UNSET
    venue_reduced_capacity: Union[Unset, bool] = UNSET
    venue_reduced_capacity_max: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competition_status: Union[Unset, str] = UNSET
        if not isinstance(self.competition_status, Unset):
            competition_status = self.competition_status.value

        complex_ = self.complex_

        complex_id = self.complex_id

        number_of_competitors = self.number_of_competitors

        number_of_qualified_competitors = self.number_of_qualified_competitors

        number_of_scheduled_matches = self.number_of_scheduled_matches

        prize_currency = self.prize_currency

        prize_money = self.prize_money

        surface = self.surface

        venue_reduced_capacity = self.venue_reduced_capacity

        venue_reduced_capacity_max = self.venue_reduced_capacity_max

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competition_status is not UNSET:
            field_dict["competition_status"] = competition_status
        if complex_ is not UNSET:
            field_dict["complex"] = complex_
        if complex_id is not UNSET:
            field_dict["complex_id"] = complex_id
        if number_of_competitors is not UNSET:
            field_dict["number_of_competitors"] = number_of_competitors
        if number_of_qualified_competitors is not UNSET:
            field_dict["number_of_qualified_competitors"] = number_of_qualified_competitors
        if number_of_scheduled_matches is not UNSET:
            field_dict["number_of_scheduled_matches"] = number_of_scheduled_matches
        if prize_currency is not UNSET:
            field_dict["prize_currency"] = prize_currency
        if prize_money is not UNSET:
            field_dict["prize_money"] = prize_money
        if surface is not UNSET:
            field_dict["surface"] = surface
        if venue_reduced_capacity is not UNSET:
            field_dict["venue_reduced_capacity"] = venue_reduced_capacity
        if venue_reduced_capacity_max is not UNSET:
            field_dict["venue_reduced_capacity_max"] = venue_reduced_capacity_max

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _competition_status = d.pop("competition_status", UNSET)
        competition_status: Union[Unset, EnumCompetitionStatus]
        if isinstance(_competition_status, Unset):
            competition_status = UNSET
        else:
            competition_status = EnumCompetitionStatus(_competition_status)

        complex_ = d.pop("complex", UNSET)

        complex_id = d.pop("complex_id", UNSET)

        number_of_competitors = d.pop("number_of_competitors", UNSET)

        number_of_qualified_competitors = d.pop("number_of_qualified_competitors", UNSET)

        number_of_scheduled_matches = d.pop("number_of_scheduled_matches", UNSET)

        prize_currency = d.pop("prize_currency", UNSET)

        prize_money = d.pop("prize_money", UNSET)

        surface = d.pop("surface", UNSET)

        venue_reduced_capacity = d.pop("venue_reduced_capacity", UNSET)

        venue_reduced_capacity_max = d.pop("venue_reduced_capacity_max", UNSET)

        info = cls(
            competition_status=competition_status,
            complex_=complex_,
            complex_id=complex_id,
            number_of_competitors=number_of_competitors,
            number_of_qualified_competitors=number_of_qualified_competitors,
            number_of_scheduled_matches=number_of_scheduled_matches,
            prize_currency=prize_currency,
            prize_money=prize_money,
            surface=surface,
            venue_reduced_capacity=venue_reduced_capacity,
            venue_reduced_capacity_max=venue_reduced_capacity_max,
        )

        return info
