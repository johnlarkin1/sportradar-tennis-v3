from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.probability_market_two_three_way import ProbabilityMarketTwoThreeWay
    from ..models.sport_event import SportEvent
    from ..models.sport_event_status import SportEventStatus


T = TypeVar("T", bound="SportEventProbability")


@_attrs_define
class SportEventProbability:
    """
    Attributes:
        markets (Union[Unset, List['ProbabilityMarketTwoThreeWay']]):
        sport_event (Union[Unset, SportEvent]):
        sport_event_status (Union[Unset, SportEventStatus]):
    """

    markets: Union[Unset, List["ProbabilityMarketTwoThreeWay"]] = UNSET
    sport_event: Union[Unset, "SportEvent"] = UNSET
    sport_event_status: Union[Unset, "SportEventStatus"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        markets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.markets, Unset):
            markets = []
            for markets_item_data in self.markets:
                markets_item = markets_item_data.to_dict()
                markets.append(markets_item)

        sport_event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event, Unset):
            sport_event = self.sport_event.to_dict()

        sport_event_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sport_event_status, Unset):
            sport_event_status = self.sport_event_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if markets is not UNSET:
            field_dict["markets"] = markets
        if sport_event is not UNSET:
            field_dict["sport_event"] = sport_event
        if sport_event_status is not UNSET:
            field_dict["sport_event_status"] = sport_event_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.probability_market_two_three_way import ProbabilityMarketTwoThreeWay
        from ..models.sport_event import SportEvent
        from ..models.sport_event_status import SportEventStatus

        d = src_dict.copy()
        markets = []
        _markets = d.pop("markets", UNSET)
        for markets_item_data in _markets or []:
            markets_item = ProbabilityMarketTwoThreeWay.from_dict(markets_item_data)

            markets.append(markets_item)

        _sport_event = d.pop("sport_event", UNSET)
        sport_event: Union[Unset, SportEvent]
        if isinstance(_sport_event, Unset):
            sport_event = UNSET
        else:
            sport_event = SportEvent.from_dict(_sport_event)

        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, SportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = SportEventStatus.from_dict(_sport_event_status)

        sport_event_probability = cls(
            markets=markets,
            sport_event=sport_event,
            sport_event_status=sport_event_status,
        )

        return sport_event_probability
