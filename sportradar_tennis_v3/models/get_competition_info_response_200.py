import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_competition_info_response_200_competition import GetCompetitionInfoResponse200Competition
    from ..models.get_competition_info_response_200_info import GetCompetitionInfoResponse200Info


T = TypeVar("T", bound="GetCompetitionInfoResponse200")


@_attrs_define
class GetCompetitionInfoResponse200:
    """
    Attributes:
        competition (Union[Unset, GetCompetitionInfoResponse200Competition]):
        generated_at (Union[Unset, datetime.datetime]):
        info (Union[Unset, GetCompetitionInfoResponse200Info]):
    """

    competition: Union[Unset, "GetCompetitionInfoResponse200Competition"] = UNSET
    generated_at: Union[Unset, datetime.datetime] = UNSET
    info: Union[Unset, "GetCompetitionInfoResponse200Info"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        competition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        generated_at: Union[Unset, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if competition is not UNSET:
            field_dict["competition"] = competition
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_competition_info_response_200_competition import GetCompetitionInfoResponse200Competition
        from ..models.get_competition_info_response_200_info import GetCompetitionInfoResponse200Info

        d = src_dict.copy()
        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, GetCompetitionInfoResponse200Competition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = GetCompetitionInfoResponse200Competition.from_dict(_competition)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, datetime.datetime]
        if isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        _info = d.pop("info", UNSET)
        info: Union[Unset, GetCompetitionInfoResponse200Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = GetCompetitionInfoResponse200Info.from_dict(_info)

        get_competition_info_response_200 = cls(
            competition=competition,
            generated_at=generated_at,
            info=info,
        )

        return get_competition_info_response_200
