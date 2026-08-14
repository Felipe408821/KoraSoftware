"""Google Calendar implementation of the CalendarProvider contract.

The Google SDK import is deferred until a calendar operation is executed. This
keeps the agent importable in lightweight test environments while preserving the
same runtime behaviour once requirements are installed.
"""

from typing import Any


class GoogleCalendarProvider:
    def __init__(self) -> None:
        self._client = None

    def _get_client(self):
        if self._client is None:
            from app.integrations.google_calendar.client import GoogleCalendarClient

            self._client = GoogleCalendarClient()
        return self._client

    def create_appointment_event(self, **kwargs: Any) -> dict[str, Any]:
        return self._get_client().create_appointment_event(**kwargs)

    def list_events(self, **kwargs: Any) -> list[dict[str, Any]]:
        return self._get_client().list_events(**kwargs)

    def delete_event(self, event_id: str) -> None:
        return self._get_client().delete_event(event_id)
