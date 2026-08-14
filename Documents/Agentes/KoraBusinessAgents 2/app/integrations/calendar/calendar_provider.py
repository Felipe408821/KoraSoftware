from typing import Any, Protocol


class CalendarProvider(Protocol):
    def create_appointment_event(
        self,
        *,
        patient_name: str,
        patient_phone: str,
        treatment_id: str,
        professional_id: str,
        resource_id: str,
        start_datetime: str,
        duration_minutes: int = 45,
    ) -> dict[str, Any]:
        ...

    def list_events(
        self,
        *,
        time_min: str,
        time_max: str,
        max_results: int = 10,
    ) -> list[dict[str, Any]]:
        ...

    def delete_event(self, event_id: str) -> None:
        ...
