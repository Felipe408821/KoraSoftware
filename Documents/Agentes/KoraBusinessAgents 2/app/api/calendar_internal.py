from datetime import date
from typing import Any, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.domains.appointments.appointment_service import AppointmentService
from app.domains.appointments.availability_service import AvailabilityService
from app.integrations.calendar.google_calendar_provider import GoogleCalendarProvider


router = APIRouter(prefix="/internal/calendar", tags=["internal-calendar"])


class CreateAppointmentRequest(BaseModel):
    clinic_id: str = "clinic_demo"
    patient_name: str
    patient_phone: str
    treatment_id: str = "cleaning"
    professional_id: str = "Dra María Fernanda Valdivieso"
    resource_id: str = "gabinete_1"
    start_datetime: str
    duration_minutes: int = Field(default=45, gt=0)


class CancelAppointmentRequest(BaseModel):
    appointment_id: Optional[int] = None
    google_event_id: Optional[str] = None


@router.post("/appointments/create")
def create_appointment(payload: CreateAppointmentRequest) -> dict[str, Any]:
    service = AppointmentService()
    return service.create_appointment(**payload.model_dump())


@router.post("/appointments/cancel")
def cancel_appointment(payload: CancelAppointmentRequest) -> dict[str, Any]:
    service = AppointmentService()
    return service.cancel_appointment(
        appointment_id=payload.appointment_id,
        google_event_id=payload.google_event_id,
    )


@router.get("/availability")
def get_availability(
    professional_id: str,
    target_date: date,
    period: str,
) -> dict[str, Any]:
    service = AvailabilityService()
    slots = service.get_available_slots(
        professional_id=professional_id,
        target_date=target_date,
        period="afternoon" if period == "afternoon" else "morning",
    )
    return {"professional_id": professional_id, "target_date": target_date.isoformat(), "period": period, "slots": slots}


# Backward-compatible test endpoints used during local MVP testing.
@router.post("/appointments/test-create")
def test_create_appointment(payload: CreateAppointmentRequest) -> dict[str, Any]:
    return create_appointment(payload)


@router.post("/appointments/test-cancel")
def test_cancel_appointment(payload: CancelAppointmentRequest) -> dict[str, Any]:
    return cancel_appointment(payload)


@router.get("/events")
def list_events(time_min: str, time_max: str) -> dict[str, Any]:
    calendar_client = GoogleCalendarProvider()
    events = calendar_client.list_events(time_min=time_min, time_max=time_max)
    return {"count": len(events), "events": events}
