"""
Consulta los slots disponibles para un profesional en una fecha dada,
cruzando los huecos candidatos con los eventos existentes en Google Calendar.

Nota: GoogleCalendarClient usa un único calendario (settings.google_calendar_id)
y etiqueta los eventos con professional_id en extendedProperties.private.
Por eso filtramos por professional_id aquí, en lugar de consultar calendarios separados.
"""
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from typing import Literal

from app.integrations.calendar.google_calendar_provider import GoogleCalendarProvider
from app.utils.slot_resolver import MORNING_SLOTS, AFTERNOON_SLOTS


Period = Literal["morning", "afternoon"]

CLINIC_TZ = ZoneInfo("Europe/Madrid")

# Duración mínima en minutos para considerar un evento como cita real.
# Evita que recordatorios o eventos de 0 min bloqueen huecos.
_MIN_EVENT_DURATION_MINUTES = 10


class AvailabilityService:
    """
    Dado un professional_id, una fecha y un periodo (mañana/tarde),
    devuelve los slots horarios libres consultando Google Calendar.

    Los eventos se filtran por professional_id usando extendedProperties,
    ya que todos los profesionales comparten el mismo calendario.
    """

    def __init__(self) -> None:
        self.calendar_client = GoogleCalendarProvider()

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------

    def get_available_slots(
        self,
        professional_id: str,
        target_date: date,
        period: Period,
    ) -> list[str]:
        """
        Devuelve los slots libres en formato "HH:MM".

        Parámetros:
            professional_id : ej. "dra_marta". Se usa para filtrar eventos
                              dentro del calendario compartido.
            target_date     : Día concreto a comprobar.
            period          : "morning" o "afternoon".

        Devuelve lista vacía si no hay huecos o si Google Calendar falla
        (el agente interpretará esto como "proponer otra fecha").
        """
        candidate_slots = MORNING_SLOTS if period == "morning" else AFTERNOON_SLOTS

        try:
            busy_intervals = self._fetch_busy_intervals(professional_id, target_date)
        except Exception:
            # Fail-safe: si el calendario no responde, no bloqueamos al agente,
            # pero tampoco ofrecemos slots falsos → devolvemos lista vacía.
            return []

        return [
            slot for slot in candidate_slots
            if not self._is_slot_busy(slot, busy_intervals)
        ]

    # ------------------------------------------------------------------
    # Internos
    # ------------------------------------------------------------------

    def _fetch_busy_intervals(
        self,
        professional_id: str,
        target_date: date,
    ) -> list[tuple[datetime, datetime]]:
        """
        Llama a GoogleCalendarClient.list_events() con la ventana del día completo
        en Europe/Madrid, y devuelve solo los intervalos del profesional indicado.
        """
        # Ventana: 00:00:00 → 23:59:59 en hora de Madrid
        day_start = datetime(
            target_date.year, target_date.month, target_date.day,
            0, 0, 0,
            tzinfo=CLINIC_TZ,
        )
        day_end = day_start + timedelta(days=1)

        # list_events espera strings ISO con offset, que datetime.isoformat() produce
        # cuando el objeto tiene tzinfo: "2026-06-03T00:00:00+02:00"
        events = self.calendar_client.list_events(
            time_min=day_start.isoformat(),
            time_max=day_end.isoformat(),
            max_results=50,  # suficiente para un día completo de clínica
        )

        return self._parse_busy_intervals(events, professional_id)

    def _parse_busy_intervals(
        self,
        events: list[dict],
        professional_id: str,
    ) -> list[tuple[datetime, datetime]]:
        """
        Convierte los eventos de Google Calendar en intervalos (start, end).

        Filtra por professional_id usando extendedProperties.private,
        descarta eventos de día completo (sin dateTime) y eventos demasiado cortos.
        """
        intervals: list[tuple[datetime, datetime]] = []

        for event in events:
            # Filtro por profesional: solo procesamos citas de este profesional
            event_professional = (
                event
                .get("extendedProperties", {})
                .get("private", {})
                .get("professional_id")
            )
            if event_professional and event_professional != professional_id:
                continue

            start_str = event.get("start", {}).get("dateTime")
            end_str = event.get("end", {}).get("dateTime")

            # Eventos de día completo no tienen dateTime → los ignoramos
            if not start_str or not end_str:
                continue

            try:
                start_dt = datetime.fromisoformat(start_str)
                end_dt = datetime.fromisoformat(end_str)
            except ValueError:
                continue

            duration_minutes = (end_dt - start_dt).total_seconds() / 60
            if duration_minutes >= _MIN_EVENT_DURATION_MINUTES:
                intervals.append((start_dt, end_dt))

        return intervals

    def _is_slot_busy(
        self,
        slot: str,
        busy_intervals: list[tuple[datetime, datetime]],
    ) -> bool:
        """
        Comprueba si el slot "HH:MM" solapa con algún intervalo ocupado.

        Usa una fecha fija (2000-01-01) para comparar solo horas,
        normalizando todo a Europe/Madrid para evitar problemas de offset.
        """
        hour, minute = map(int, slot.split(":"))

        # Fecha ficticia para comparar solo la hora
        slot_start = datetime(2000, 1, 1, hour, minute, tzinfo=CLINIC_TZ)
        slot_end = slot_start + timedelta(minutes=30)

        for busy_start, busy_end in busy_intervals:
            # Normalizamos a Madrid y reemplazamos la fecha por la ficticia
            busy_start_local = busy_start.astimezone(CLINIC_TZ).replace(
                year=2000, month=1, day=1
            )
            busy_end_local = busy_end.astimezone(CLINIC_TZ).replace(
                year=2000, month=1, day=1
            )

            # Solapamiento: los intervalos se cruzan si no están completamente separados
            if slot_start < busy_end_local and slot_end > busy_start_local:
                return True

        return False