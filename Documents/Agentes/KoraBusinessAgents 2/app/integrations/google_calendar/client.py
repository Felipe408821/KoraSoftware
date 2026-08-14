from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from app.core.config import settings


SCOPES = ["https://www.googleapis.com/auth/calendar"]


class GoogleCalendarClient:
    def __init__(self) -> None:
        self.calendar_id = settings.google_calendar_id
        self.credentials_path = Path(settings.google_credentials_path)
        self.token_path = Path(settings.google_token_path)

    def _service(self):
        if not self.token_path.exists():
            raise FileNotFoundError(
                "No existe google_token.json. Ejecuta primero: python scripts/google_auth.py"
            )

        creds = Credentials.from_authorized_user_file(
            str(self.token_path),
            SCOPES,
        )

        return build("calendar", "v3", credentials=creds)

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
        service = self._service()

        start = datetime.fromisoformat(start_datetime)
        end = start + timedelta(minutes=duration_minutes)

        event = {
            "summary": f"[{treatment_id}] {patient_name}",
            "description": (
                f"Paciente: {patient_name}\n"
                f"Teléfono: {patient_phone}\n"
                f"Tratamiento: {treatment_id}\n"
                f"Profesional: {professional_id}\n"
                f"Gabinete: {resource_id}\n"
                f"Origen: dental-agent-mvp"
            ),
            "start": {
                "dateTime": start.isoformat(),
                "timeZone": "Europe/Madrid",
            },
            "end": {
                "dateTime": end.isoformat(),
                "timeZone": "Europe/Madrid",
            },
            "extendedProperties": {
                "private": {
                    "patient_phone": patient_phone,
                    "treatment_id": treatment_id,
                    "professional_id": professional_id,
                    "resource_id": resource_id,
                    "source": "dental-agent-mvp",
                }
            },
        }

        return (
            service.events()
            .insert(calendarId=self.calendar_id, body=event)
            .execute()
        )

    def list_events(
        self,
        *,
        time_min: str,
        time_max: str,
        max_results: int = 10,
    ) -> list[dict[str, Any]]:
        service = self._service()

        result = (
            service.events()
            .list(
                calendarId=self.calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                maxResults=max_results,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        return result.get("items", [])

    def delete_event(self, event_id: str) -> None:
        service = self._service()

        service.events().delete(
            calendarId=self.calendar_id,
            eventId=event_id,
        ).execute()