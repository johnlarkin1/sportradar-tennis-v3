from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompetitorProfileResponse200Info")


@_attrs_define
class GetCompetitorProfileResponse200Info:
    """
    Attributes:
        date_of_birth (Union[Unset, str]):
        handedness (Union[Unset, str]):
        height (Union[Unset, int]):
        highest_doubles_ranking (Union[Unset, int]):
        highest_doubles_ranking_date (Union[Unset, str]):
        highest_singles_ranking (Union[Unset, int]):
        highest_singles_ranking_date (Union[Unset, str]):
        pro_year (Union[Unset, int]):
        weight (Union[Unset, int]):
    """

    date_of_birth: Union[Unset, str] = UNSET
    handedness: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    highest_doubles_ranking: Union[Unset, int] = UNSET
    highest_doubles_ranking_date: Union[Unset, str] = UNSET
    highest_singles_ranking: Union[Unset, int] = UNSET
    highest_singles_ranking_date: Union[Unset, str] = UNSET
    pro_year: Union[Unset, int] = UNSET
    weight: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date_of_birth = self.date_of_birth

        handedness = self.handedness

        height = self.height

        highest_doubles_ranking = self.highest_doubles_ranking

        highest_doubles_ranking_date = self.highest_doubles_ranking_date

        highest_singles_ranking = self.highest_singles_ranking

        highest_singles_ranking_date = self.highest_singles_ranking_date

        pro_year = self.pro_year

        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if handedness is not UNSET:
            field_dict["handedness"] = handedness
        if height is not UNSET:
            field_dict["height"] = height
        if highest_doubles_ranking is not UNSET:
            field_dict["highest_doubles_ranking"] = highest_doubles_ranking
        if highest_doubles_ranking_date is not UNSET:
            field_dict["highest_doubles_ranking_date"] = highest_doubles_ranking_date
        if highest_singles_ranking is not UNSET:
            field_dict["highest_singles_ranking"] = highest_singles_ranking
        if highest_singles_ranking_date is not UNSET:
            field_dict["highest_singles_ranking_date"] = highest_singles_ranking_date
        if pro_year is not UNSET:
            field_dict["pro_year"] = pro_year
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_of_birth = d.pop("date_of_birth", UNSET)

        handedness = d.pop("handedness", UNSET)

        height = d.pop("height", UNSET)

        highest_doubles_ranking = d.pop("highest_doubles_ranking", UNSET)

        highest_doubles_ranking_date = d.pop("highest_doubles_ranking_date", UNSET)

        highest_singles_ranking = d.pop("highest_singles_ranking", UNSET)

        highest_singles_ranking_date = d.pop("highest_singles_ranking_date", UNSET)

        pro_year = d.pop("pro_year", UNSET)

        weight = d.pop("weight", UNSET)

        get_competitor_profile_response_200_info = cls(
            date_of_birth=date_of_birth,
            handedness=handedness,
            height=height,
            highest_doubles_ranking=highest_doubles_ranking,
            highest_doubles_ranking_date=highest_doubles_ranking_date,
            highest_singles_ranking=highest_singles_ranking,
            highest_singles_ranking_date=highest_singles_ranking_date,
            pro_year=pro_year,
            weight=weight,
        )

        return get_competitor_profile_response_200_info
