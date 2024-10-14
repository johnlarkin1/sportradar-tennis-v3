from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sport_event import SportEvent
    from ..models.sport_event_status import SportEventStatus


T = TypeVar("T", bound="BaseSummary")


@_attrs_define
class BaseSummary:
    """
    Attributes:
        sport_event (SportEvent):
        sport_event_status (SportEventStatus):
    """

    sport_event: "SportEvent"
    sport_event_status: "SportEventStatus"

    def to_dict(self) -> Dict[str, Any]:
        sport_event = self.sport_event.to_dict()

        sport_event_status = self.sport_event_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sport_event": sport_event,
                "sport_event_status": sport_event_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sport_event import SportEvent
        from ..models.sport_event_status import SportEventStatus

        d = src_dict.copy()
        sport_event = SportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = SportEventStatus.from_dict(d.pop("sport_event_status"))

        base_summary = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
        )

        return base_summary
