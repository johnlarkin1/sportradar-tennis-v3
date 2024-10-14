from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.base_summary_sport_event import BaseSummarySportEvent
    from ..models.base_summary_sport_event_status import BaseSummarySportEventStatus


T = TypeVar("T", bound="BaseSummary")


@_attrs_define
class BaseSummary:
    """
    Attributes:
        sport_event (BaseSummarySportEvent):
        sport_event_status (BaseSummarySportEventStatus):
    """

    sport_event: "BaseSummarySportEvent"
    sport_event_status: "BaseSummarySportEventStatus"

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
        from ..models.base_summary_sport_event import BaseSummarySportEvent
        from ..models.base_summary_sport_event_status import BaseSummarySportEventStatus

        d = src_dict.copy()
        sport_event = BaseSummarySportEvent.from_dict(d.pop("sport_event"))

        sport_event_status = BaseSummarySportEventStatus.from_dict(d.pop("sport_event_status"))

        base_summary = cls(
            sport_event=sport_event,
            sport_event_status=sport_event_status,
        )

        return base_summary
