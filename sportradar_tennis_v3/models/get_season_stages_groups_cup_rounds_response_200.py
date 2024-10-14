import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_season_stages_groups_cup_rounds_response_200_stages_item import (
        GetSeasonStagesGroupsCupRoundsResponse200StagesItem,
    )


T = TypeVar("T", bound="GetSeasonStagesGroupsCupRoundsResponse200")


@_attrs_define
class GetSeasonStagesGroupsCupRoundsResponse200:
    """
    Attributes:
        generated_at (Union[Unset, datetime.datetime]):
        stages (Union[Unset, List['GetSeasonStagesGroupsCupRoundsResponse200StagesItem']]):
    """

    generated_at: Union[Unset, datetime.datetime] = UNSET
    stages: Union[Unset, List["GetSeasonStagesGroupsCupRoundsResponse200StagesItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        stages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_season_stages_groups_cup_rounds_response_200_stages_item import (
            GetSeasonStagesGroupsCupRoundsResponse200StagesItem,
        )

        d = src_dict.copy()
        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = GetSeasonStagesGroupsCupRoundsResponse200StagesItem.from_dict(stages_item_data)

            stages.append(stages_item)

        get_season_stages_groups_cup_rounds_response_200 = cls(
            generated_at=generated_at,
            stages=stages,
        )

        return get_season_stages_groups_cup_rounds_response_200
