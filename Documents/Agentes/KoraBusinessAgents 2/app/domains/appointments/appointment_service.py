from datetime import datetime, timedelta
from typing import Any, Optional

from app.integrations.calendar.google_calendar_provider import GoogleCalendarProvider
from app.storage.appointment_repository import AppointmentRepository


class AppointmentService:
    def __init__(self) -> None:
        self.calendar_client = GoogleCalendarProvider()
        self.appointment_repo = AppointmentRepository()

    def create_appointment(
        self,
        *,
        clinic_id: str,
        patient_name: str,
        patient_phone: str,
        treatment_id: str,
        professional_id: str,
        resource_id: str,
        start_datetime: str,
        duration_minutes: int,
    ) -> dict[str, Any]:
        event = self.calendar_client.create_appointment_event(
            patient_name=patient_name,
            patient_phone=patient_phone,
            treatment_id=treatment_id,
            professional_id=professional_id,
            resource_id=resource_id,
            start_datetime=start_datetime,
            duration_minutes=duration_minutes,
        )

        start = datetime.fromisoformat(start_datetime)
        end = start + timedelta(minutes=duration_minutes)

        appointment_id = self.appointment_repo.create(
            clinic_id=clinic_id,
            patient_name=patient_name,
            patient_phone=patient_phone,
            treatment_id=treatment_id,
            professional_id=professional_id,
            resource_id=resource_id,
            start_datetime=start.isoformat(),
            end_datetime=end.isoformat(),
            google_event_id=event.get("id"),
            status="confirmed",
        )

        return {
            "status": "created",
            "appointment_id": appointment_id,
            "google_event_id": event.get("id"),
            "html_link": event.get("htmlLink"),
        }

    def cancel_appointment(
        self,
        *,
        appointment_id: Optional[int] = None,
        google_event_id: Optional[str] = None,
    ) -> dict[str, Any]:
        if not google_event_id and appointment_id:
            appointment = self.appointment_repo.get_by_id(appointment_id)
            if appointment:
                google_event_id = appointment.get("google_event_id")

        if not google_event_id:
            return {
                "status": "not_found",
                "message": "No se encontró una cita para cancelar.",
            }

        self.calendar_client.delete_event(google_event_id)

        if appointment_id:
            self.appointment_repo.update_status(
                appointment_id=appointment_id,
                status="cancelled",
            )

        return {
            "status": "cancelled",
            "google_event_id": google_event_id,
        }