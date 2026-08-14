"""
Convierte expresiones de fecha en lenguaje natural (español) a objetos date.
No tiene dependencias de negocio: entrada texto → salida date o None.
"""
import re
from datetime import date, timedelta
from typing import Optional


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

MORNING_SLOTS = ["09:00", "10:00", "11:00", "11:30"]
AFTERNOON_SLOTS = ["16:00", "16:30", "17:30", "18:00"]

_WEEKDAY_MAP: dict[str, int] = {
    "lunes": 0,
    "martes": 1,
    "miércoles": 2,
    "miercoles": 2,
    "jueves": 3,
    "viernes": 4,
    "sábado": 5,
    "sabado": 5,
    "domingo": 6,
}

_MONTH_MAP: dict[str, int] = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12,
}


# ---------------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------------

def resolve_date(text: str, today: Optional[date] = None) -> Optional[date]:
    today = today or date.today()

    # ── IMPORTANTE: eliminar "mañana" de expresiones como "por la mañana"
    # antes de buscar fechas relativas, para evitar falsos positivos.
    clean = re.sub(r"por\s+la\s+ma[ñn]ana", "", text.lower().strip())
    clean = re.sub(r"de\s+la\s+ma[ñn]ana", "", clean)
    clean = re.sub(r"a\s+la\s+ma[ñn]ana", "", clean)

    if "pasado mañana" in clean or "pasado manana" in clean:
        return today + timedelta(days=2)

    # "mañana" como día, no como periodo del día
    if re.search(r"\bma[ñn]ana\b", clean):
        return today + timedelta(days=1)

    if "hoy" in clean:
        return today

    # Fecha explícita con mes en texto: "el 26 de mayo", "3 de junio"
    # Se evalúa ANTES que el día de la semana para que "martes 26 de mayo"
    # resuelva por fecha exacta y no por día de la semana.
    for month_name, month_num in _MONTH_MAP.items():
        match = re.search(rf"(\d{{1,2}})\s+de\s+{month_name}", clean)
        if match:
            day = int(match.group(1))
            year = today.year if month_num >= today.month else today.year + 1
            try:
                return date(year, month_num, day)
            except ValueError:
                return None

    # Día de la semana
    for word, target_wd in _WEEKDAY_MAP.items():
        if re.search(rf"\b{word}\b", clean):
            days_ahead = (target_wd - today.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            return today + timedelta(days=days_ahead)

    # Formato numérico: "26/5", "26-05"
    numeric = re.search(r"\b(\d{1,2})[/\-](\d{1,2})\b", clean)
    if numeric:
        try:
            return date(today.year, int(numeric.group(2)), int(numeric.group(1)))
        except ValueError:
            return None

    return None

def resolve_slot(text: str) -> Optional[str]:
    """
    Extrae una hora concreta del texto del usuario.
    Cubre: "a las 11", "a las 11:30", "11 de la mañana", "las 16:30".
    Devuelve formato "HH:MM" o None si no encuentra nada.
    """
    text = text.lower()

    # Formato explícito con minutos: "11:30", "16:30"
    match = re.search(r"\b([01]?\d|2[0-3]):([0-5]\d)\b", text)
    if match:
        return f"{match.group(1).zfill(2)}:{match.group(2)}"

    # Hora en punto con periodo: "11 de la mañana", "5 de la tarde"
    match = re.search(r"\b(\d{1,2})\s+de\s+la\s+(ma[ñn]ana|tarde)\b", text)
    if match:
        hour = int(match.group(1))
        period = match.group(2)
        if "tarde" in period and hour < 12:
            hour += 12
        return f"{str(hour).zfill(2)}:00"

    # "a las 11", "las 9"
    match = re.search(r"\b(?:a\s+las?|las?)\s+(\d{1,2})\b", text)
    if match:
        hour = int(match.group(1))
        # Heurística: horas < 8 se asumen tarde (las 5 → 17:00)
        if hour < 8:
            hour += 12
        return f"{str(hour).zfill(2)}:00"

    return None


# ---------------------------------------------------------------------------
# Helpers de validación
# ---------------------------------------------------------------------------

def is_working_day(d: date) -> bool:
    """Devuelve True si el día es de lunes a viernes."""
    return d.weekday() < 5


def is_past_date(d: date, today: date | None = None) -> bool:
    """Devuelve True si la fecha ya ha pasado."""
    today = today or date.today()
    return d < today


def format_date_es(d: date) -> str:
    """Devuelve la fecha en formato legible en español: '3 de junio de 2026'."""
    month_names = [
        "", "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    ]
    return f"{d.day} de {month_names[d.month]} de {d.year}"