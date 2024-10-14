from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_event_probability_markets_item import SportEventProbabilityMarketsItem
    from ..models.sport_event_probability_sport_event import SportEventProbabilitySportEvent
    from ..models.sport_event_probability_sport_event_status import SportEventProbabilitySportEventStatus


T = TypeVar("T", bound="SportEventProbability")


@_attrs_define
class SportEventProbability:
    """
    Attributes:
        markets (Union[Unset, List['SportEventProbabilityMarketsItem']]):
        sport_event (Union[Unset, SportEventProbabilitySportEvent]):
        sport_event_status (Union[Unset, SportEventProbabilitySportEventStatus]):
    """

    markets: Union[Unset, List["SportEventProbabilityMarketsItem"]] = UNSET
    sport_event: Union[Unset, "SportEventProbabilitySportEvent"] = UNSET
    sport_event_status: Union[Unset, "SportEventProbabilitySportEventStatus"] = UNSET

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
        from ..models.sport_event_probability_markets_item import SportEventProbabilityMarketsItem
        from ..models.sport_event_probability_sport_event import SportEventProbabilitySportEvent
        from ..models.sport_event_probability_sport_event_status import SportEventProbabilitySportEventStatus

        d = src_dict.copy()
        markets = []
        _markets = d.pop("markets", UNSET)
        for markets_item_data in _markets or []:
            markets_item = SportEventProbabilityMarketsItem.from_dict(markets_item_data)

            markets.append(markets_item)

        _sport_event = d.pop("sport_event", UNSET)
        sport_event: Union[Unset, SportEventProbabilitySportEvent]
        if isinstance(_sport_event, Unset):
            sport_event = UNSET
        else:
            sport_event = SportEventProbabilitySportEvent.from_dict(_sport_event)

        _sport_event_status = d.pop("sport_event_status", UNSET)
        sport_event_status: Union[Unset, SportEventProbabilitySportEventStatus]
        if isinstance(_sport_event_status, Unset):
            sport_event_status = UNSET
        else:
            sport_event_status = SportEventProbabilitySportEventStatus.from_dict(_sport_event_status)

        sport_event_probability = cls(
            markets=markets,
            sport_event=sport_event,
            sport_event_status=sport_event_status,
        )

        return sport_event_probability
