import asyncio
import re
from datetime import date
from typing import Any, Optional

from app.agent.result import AgentResult
from app.agent.state_factory import initial_state
from app.agent.states import ConversationIntent, ConversationStage
from app.catalog import SERVICE_CATALOG, ServiceDefinition
from app.catalog.services import detect_service, get_service
from app.domains.appointments.appointment_service import AppointmentService
from app.domains.appointments.availability_service import AvailabilityService
from app.utils.slot_resolver import (
    format_date_es,
    is_past_date,
    is_working_day,
    resolve_date,
    resolve_slot,
)

from app.domains.dental.dental_prompts import WELCOME_TEMPLATE, ADDRESS_TEMPLATE, OPENING_HOURS_TEMPLATE

# ------------------------------------------------------------------ #
#  Vocabulario de intenciones                                          #
# ------------------------------------------------------------------ #

AFFIRMATIONS = {
    "sí", "si", "confirmo", "vale", "ok", "perfecto", "claro",
    "dale", "por supuesto", "exacto", "correcto", "venga", "adelante",
    "de acuerdo", "listo", "sip", "yes", "obvio", "genial", "bien",
}

NEGATIONS = {
    "no", "nope", "para nada", "mejor no", "mantener", "déjala",
    "dejala", "no me interesa", "cambiar", "otra", "mejor", "negativo",
    "cancela", "olvídalo", "olvidalo",
}

RESTART_KEYWORDS = {
    "reiniciar", "empezar de nuevo", "menú", "menu", "inicio",
    "volver", "reset", "otra cosa",
}

CANCEL_KEYWORDS = {
    "cancelar", "anular", "eliminar", "borrar", "quitar la cita",
    "cancelar cita", "anular cita", "borrala", "elimínala", "eliminala",
    "no la quiero", "quitar cita",
}

GREETING_KEYWORDS = {
    "hola", "buenas", "buenos días", "buenos dias", "buenas tardes",
    "buenas noches", "hey", "ey", "saludos", "hello",
}

BOOKING_KEYWORDS = {
    "cita", "reservar", "agenda", "agendar", "quiero", "necesito",
    "pedir cita", "solicitar", "apuntar", "reserva",
}

URGENT_KEYWORDS = {
    "urgente", "dolor fuerte", "sangrado", "infección", "infeccion",
    "fiebre", "no puedo respirar", "emergencia", "diagnóstico",
    "diagnostico", "receta", "medicación", "medicacion",
}


def _time_greeting() -> str:
    """Devuelve 'Buenos días', 'Buenas tardes' o 'Buenas noches' según la hora local."""
    from datetime import datetime
    hour = datetime.now().hour
    if 6 <= hour < 14:
        return "Buenos días"
    elif 14 <= hour < 21:
        return "Buenas tardes"
    else:
        return "Buenas noches"


class DentalAgent:
    def __init__(self) -> None:
        self.appointment_service = AppointmentService()
        self.availability_service = AvailabilityService()

    # ------------------------------------------------------------------ #
    #  Entry point                                                         #
    # ------------------------------------------------------------------ #

    async def run(
        self,
        *,
        phone: str,
        user_text: str,
        state: Optional[dict[str, Any]] = None,
    ) -> AgentResult:
        state = state or self._initial_state(phone)
        text = self._normalize(user_text)
        stage = state.get("stage", "IDLE")

        # ── Saludo de bienvenida (solo primer mensaje) ─────────────────
        is_first = state.pop("is_first_message", False)
        if is_first:
            greeting = _time_greeting()
            welcome = (
                greeting + WELCOME_TEMPLATE
            )
        else:
            welcome = ""

        # ── Urgencias: prioridad absoluta ──────────────────────────────
        if self._is_handoff_required(text):
            state["stage"] = "WAITING_HUMAN"
            return AgentResult(
                reply=(
                    "Entiendo, parece algo que necesita atención especial. "
                    "Te paso ahora con alguien del equipo para que te ayude bien 🙏"
                ),
                new_state=state,
            )

        # ── Intenciones globales (funcionan desde cualquier stage) ──────
        # FAQ: dirección / ubicación de la clínica
        if self._is_location_question(text):
            state["stage"] = "IDLE"
            return AgentResult(
                reply=ADDRESS_TEMPLATE,
                new_state=state,
            )
        
        # FAQ: horario de atención de la clínica
        if self._is_opening_hours_question(text):
            state["stage"] = "IDLE"
            return AgentResult(
                reply=OPENING_HOURS_TEMPLATE,
                new_state=state,
            )
        
        # Reinicio de conversación
        if any(kw in text for kw in RESTART_KEYWORDS):
            return AgentResult(
                reply="Claro, empezamos de cero. ¿En qué puedo ayudarte?",
                new_state=self._initial_state(state["phone"]),
            )

        # Cancelar desde cualquier punto (salvo que ya estemos confirmando cancel)
        if self._wants_to_cancel(text) and stage not in (
            "CONFIRMING_CANCEL_APPOINTMENT", "IDLE"
        ):
            state["current_intent"] = "cancel_appointment"
            state["stage"] = "CONFIRMING_CANCEL_APPOINTMENT"
            return AgentResult(
                reply="Entendido. ¿Confirmas que quieres cancelar tu cita? Respóndeme con sí o no.",
                new_state=state,
            )

        # ── Dispatch por stage ─────────────────────────────────────────
        handlers = {
            "IDLE": lambda: self._handle_idle(text, user_text, state),
            "COLLECTING_SERVICE": lambda: self._handle_collecting_service(text, state),
            "COLLECTING_DATE": lambda: self._handle_collecting_date(text, state),
            "COLLECTING_PERIOD": lambda: self._handle_collecting_period(text, state),
            "SHOWING_SLOT_OPTIONS": lambda: self._handle_slot_selection(text, user_text, state),
            "COLLECTING_PATIENT_NAME": lambda: self._handle_patient_name(user_text, state),
            "CONFIRMING_APPOINTMENT": lambda: self._handle_confirmation(text, state),
            "APPOINTMENT_CREATED": lambda: self._handle_existing_appointment(text, state),
            "CONFIRMING_CANCEL_APPOINTMENT": lambda: self._handle_cancel_confirmation(text, state),
            "WAITING_HUMAN": lambda: AgentResult(
                reply="Espera un momento, en breve te atiende alguien del equipo 🙏",
                new_state=state,
            ),
        }
        
        handler = handlers.get(stage)
        if handler:
            result = handler()
            if asyncio.iscoroutine(result):
                result = await result
            if welcome:
                if result.reply.startswith("¡Hola!"):
                    result = AgentResult(reply=welcome, new_state=result.new_state)
                else:
                    result = AgentResult(reply=f"{welcome}\n\n{result.reply}", new_state=result.new_state)
            return result


        return AgentResult(
            reply=welcome + "Perdona, no he entendido bien. ¿Quieres pedir, cambiar o cancelar una cita?",
            new_state=self._initial_state(phone),
        )

    # ------------------------------------------------------------------ #
    #  State                                                               #
    # ------------------------------------------------------------------ #

    def _initial_state(self, phone: str) -> dict[str, Any]:
        return initial_state(phone=phone)

    # ------------------------------------------------------------------ #
    #  Helpers de intención                                                #
    # ------------------------------------------------------------------ #

    def _normalize(self, text: str) -> str:
        return text.lower().strip()

    def _is_affirmation(self, text: str) -> bool:
        return any(w in text.split() or text == w for w in AFFIRMATIONS)

    def _is_negation(self, text: str) -> bool:
        return any(w in text.split() or text == w for w in NEGATIONS)

    def _is_handoff_required(self, text: str) -> bool:
        return any(kw in text for kw in URGENT_KEYWORDS)

    def _wants_to_cancel(self, text: str) -> bool:
        return any(kw in text for kw in CANCEL_KEYWORDS)

    def _get_service(self, state: dict) -> "ServiceDefinition | None":
        sid = state.get("service_id")
        return SERVICE_CATALOG.get(sid) if sid else None

    def _service_list_text(self) -> str:
        lines = [f"• {s.label}" for s in SERVICE_CATALOG.values()]
        return "\n".join(lines)

    def _format_date_human(self, iso_date: str) -> str:
        """Convierte '2026-05-26' en 'el lunes 26 de mayo' usando format_date_es."""
        try:
            return format_date_es(date.fromisoformat(iso_date))
        except Exception:
            return iso_date

    # ------------------------------------------------------------------ #
    #  Stage handlers                                                      #
    # ------------------------------------------------------------------ #

    def _handle_idle(self, text: str, original: str, state: dict) -> AgentResult:
        if self._wants_to_cancel(text):
            state["current_intent"] = "cancel_appointment"
            state["stage"] = "CONFIRMING_CANCEL_APPOINTMENT"
            return AgentResult(
                reply="Entendido. ¿Confirmas que quieres cancelar tu cita? Respóndeme con sí o no.",
                new_state=state,
            )

        if any(w in text for w in BOOKING_KEYWORDS):
            state["current_intent"] = "book_appointment"

            # Intentar detectar servicio, fecha y periodo ya en el primer mensaje
            service = detect_service(text)
            resolved_date = resolve_date(text)
            slot = resolve_slot(text)

            if service:
                state["service_id"] = service.service_id

            if service and resolved_date and is_working_day(resolved_date) and not is_past_date(resolved_date):
                state["preferred_date"] = resolved_date.isoformat()

                if slot:
                    # Tenemos todo: servicio + fecha + hora
                    state["selected_slot"] = slot
                    state["offered_slots"] = [slot]
                    hour = int(slot.split(":")[0])
                    state["preferred_period"] = "morning" if hour < 14 else "afternoon"
                    state["stage"] = "COLLECTING_PATIENT_NAME"
                    return AgentResult(
                        reply=(
                            f"Perfecto, una {service.label} "
                            f"{self._format_date_human(state['preferred_date'])} a las {slot}. "
                            "¿Me dices tu nombre completo para reservarlo?"
                        ),
                        new_state=state,
                    )

                # Servicio + fecha, sin hora
                state["stage"] = "COLLECTING_PERIOD"
                return AgentResult(
                    reply=(
                        f"Perfecto, una {service.label} "
                        f"{self._format_date_human(state['preferred_date'])}. "
                        "¿Prefieres por la mañana o por la tarde?"
                    ),
                    new_state=state,
                )

            if service and not resolved_date:
                state["stage"] = "COLLECTING_DATE"
                return AgentResult(
                    reply=f"Claro, una {service.label} 👍 ¿Qué día te vendría bien?",
                    new_state=state,
                )

            if not service:
                state["stage"] = "COLLECTING_SERVICE"
                return AgentResult(
                    reply=(
                        "Con mucho gusto 😊 ¿Qué tipo de consulta necesitas?\n"
                        + self._service_list_text()
                    ),
                    new_state=state,
                )
        
        if any(w in text for w in GREETING_KEYWORDS):
            return AgentResult(
                reply="¡Hola! ¿En qué puedo ayudarte?",
                new_state=state,
            )

        return AgentResult(
            reply="Puedo ayudarte a pedir, cambiar o cancelar una cita. ¿Qué necesitas?",
            new_state=state,
        )

    def _handle_collecting_service(self, text: str, state: dict) -> AgentResult:
        service = detect_service(text)
        if service:
            state["service_id"] = service.service_id
            state["stage"] = "COLLECTING_DATE"
            return AgentResult(
                reply=f"Perfecto, una {service.label} 👍 ¿Qué día te vendría bien?",
                new_state=state,
            )

        return AgentResult(
            reply=(
                "Mmm, no estoy seguro de a qué te refieres 😅 Estos son los servicios disponibles:\n"
                + self._service_list_text()
                + "\n¿Cuál necesitas?"
            ),
            new_state=state,
        )

    def _handle_collecting_date(self, text: str, state: dict) -> AgentResult:
        resolved = resolve_date(text)

        if not resolved:
            return AgentResult(
                reply=(
                    "No he entendido bien la fecha 😕 Puedes decirme algo como "
                    "«mañana», «el martes» o «el 26 de mayo»."
                ),
                new_state=state,
            )

        if not is_working_day(resolved):
            return AgentResult(
                reply=(
                    f"Uy, {format_date_es(resolved)} es fin de semana y no tenemos consulta 😅 "
                    "¿Te viene bien algún día entre semana?"
                ),
                new_state=state,
            )

        if is_past_date(resolved):
            return AgentResult(
                reply=(
                    f"Parece que {format_date_es(resolved)} ya ha pasado 😕 "
                    "¿Qué otro día te viene bien?"
                ),
                new_state=state,
            )

        state["preferred_date"] = resolved.isoformat()

        # Si el usuario ya indicó la hora en el mismo mensaje
        slot = resolve_slot(text)
        if slot:
            state["selected_slot"] = slot
            state["offered_slots"] = [slot]
            hour = int(slot.split(":")[0])
            state["preferred_period"] = "morning" if hour < 14 else "afternoon"
            state["stage"] = "COLLECTING_PATIENT_NAME"
            return AgentResult(
                reply=(
                    f"Perfecto, {format_date_es(resolved)} a las {slot}. "
                    "¿Me dices tu nombre completo para dejarlo reservado?"
                ),
                new_state=state,
            )

        state["stage"] = "COLLECTING_PERIOD"
        return AgentResult(
            reply=(
                f"Perfecto, {format_date_es(resolved)} 👍 "
                "¿Prefieres por la mañana o por la tarde?"
            ),
            new_state=state,
        )

    def _handle_collecting_period(self, text: str, state: dict) -> AgentResult:
        from datetime import date as date_type

        if "tarde" in text:
            state["preferred_period"] = "afternoon"
        else:
            state["preferred_period"] = "morning"

        service = get_service(state.get("service_id", ""))
        target_date = date_type.fromisoformat(state["preferred_date"])

        available_slots = self.availability_service.get_available_slots(
            professional_id=service.professional_id if service else "dra_marta",
            target_date=target_date,
            period=state["preferred_period"],
        )

        if not available_slots:
            state["stage"] = "COLLECTING_DATE"
            period_label = "tarde" if state["preferred_period"] == "afternoon" else "mañana"
            return AgentResult(
                reply=(
                    f"Lo siento, no hay huecos disponibles {format_date_es(target_date)} "
                    f"por la {period_label} 😕 ¿Te viene bien otro día?"
                ),
                new_state=state,
            )

        state["offered_slots"] = available_slots[:2]
        state["stage"] = "SHOWING_SLOT_OPTIONS"
        slots_text = " o a las ".join(state["offered_slots"])

        return AgentResult(
            reply=f"Tengo disponible a las {slots_text}. ¿Cuál te viene mejor?",
            new_state=state,
        )

    def _handle_slot_selection(self, text: str, original_text: str, state: dict) -> AgentResult:
        offered_slots = state.get("offered_slots", [])
        normalized = text.replace(":", "").replace(".", "").replace(" ", "")

        selected_slot = next(
            (s for s in offered_slots if s.replace(":", "") in normalized),
            None,
        )

        if not selected_slot:
            match = re.search(r"\b([01]?\d|2[0-3])[:.]?([0-5]\d)?\b", text)
            if match:
                selected_slot = f"{match.group(1).zfill(2)}:{match.group(2) or '00'}"

        if not selected_slot:
            slots_text = " o a las ".join(offered_slots)
            return AgentResult(
                reply=f"No he pillado bien la hora 😅 Tengo disponible a las {slots_text}. ¿Cuál prefieres?",
                new_state=state,
            )

        state["selected_slot"] = selected_slot

        name = self._extract_name(original_text)
        if name:
            state["patient_name"] = name
            state["stage"] = "CONFIRMING_APPOINTMENT"
            return AgentResult(reply=self._confirmation_text(state), new_state=state)

        state["stage"] = "COLLECTING_PATIENT_NAME"
        return AgentResult(
            reply="Perfecto 👍 ¿Me dices tu nombre completo para dejar la cita preparada?",
            new_state=state,
        )

    def _handle_patient_name(self, user_text: str, state: dict) -> AgentResult:
        name = self._extract_name(user_text) or user_text.strip().title()
        state["patient_name"] = name
        state["stage"] = "CONFIRMING_APPOINTMENT"
        return AgentResult(reply=self._confirmation_text(state), new_state=state)

    async def _handle_confirmation(self, text: str, state: dict) -> AgentResult:
        if self._is_affirmation(text):
            service = self._get_service(state)
            if not service:
                return AgentResult(
                    reply="Vaya, ha habido un problema con el servicio seleccionado 😕 ¿Puedes decirme de nuevo qué consulta necesitas?",
                    new_state={**state, "stage": "COLLECTING_SERVICE"},
                )

            start_datetime = self._build_start_datetime(state)

            appointment = await asyncio.to_thread(
                self.appointment_service.create_appointment,
                clinic_id=state.get("clinic_id", "clinic_demo"),
                patient_name=state.get("patient_name") or "Paciente sin nombre",
                patient_phone=state.get("phone"),
                treatment_id=service.service_id,
                professional_id=service.professional_id,
                resource_id=service.resource_id,
                start_datetime=start_datetime,
                duration_minutes=service.duration_minutes,
            )

            state.update({
                "stage": "APPOINTMENT_CREATED",
                "appointment_status": "confirmed",
                "appointment_id": appointment.get("appointment_id"),
                "google_event_id": appointment.get("google_event_id"),
            })

            date_human = self._format_date_human(state.get("preferred_date", ""))
            return AgentResult(
                reply=(
                    f"¡Listo, {state.get('patient_name')}! ✅ "
                    f"Tu cita de {service.label} queda confirmada "
                    f"{date_human} a las {state.get('selected_slot')}. "
                    "Si necesitas cambiarla o cancelarla, escríbeme aquí."
                ),
                new_state=state,
            )

        if self._is_negation(text):
            state.update({"selected_slot": None, "offered_slots": [], "preferred_date": None, "preferred_period": None})

            # Intentar extraer la nueva fecha del mismo mensaje
            resolved = resolve_date(text)
            if resolved and is_working_day(resolved) and not is_past_date(resolved):
                state["preferred_date"] = resolved.isoformat()
                slot = resolve_slot(text)
                if slot:
                    # Tiene nueva fecha y hora → saltar a confirmar nombre
                    state["selected_slot"] = slot
                    state["offered_slots"] = [slot]
                    hour = int(slot.split(":")[0])
                    state["preferred_period"] = "morning" if hour < 14 else "afternoon"
                    state["stage"] = "COLLECTING_PATIENT_NAME"
                    return AgentResult(
                        reply=f"Sin problema 😊 ¿Me confirmas tu nombre para dejarlo el {format_date_es(resolved)} a las {slot}?",
                        new_state=state,
                    )
                # Tiene nueva fecha, sin hora → preguntar periodo
                state["stage"] = "COLLECTING_PERIOD"
                return AgentResult(
                    reply=f"Sin problema 😊 El {format_date_es(resolved)}, ¿prefieres mañana o tarde?",
                    new_state=state,
                )

            # Sin fecha en el mensaje → preguntar normalmente
            state["stage"] = "COLLECTING_DATE"
            return AgentResult(
                reply="Sin problema 😊 ¿Qué día te vendría mejor?",
                new_state=state,
            )

        return AgentResult(
            reply="¿Lo dejo reservado entonces? Respóndeme con sí o no 😊",
            new_state=state,
        )

    def _handle_existing_appointment(self, text: str, state: dict) -> AgentResult:
        if self._wants_to_cancel(text):
            state.update({"current_intent": "cancel_appointment", "stage": "CONFIRMING_CANCEL_APPOINTMENT"})
            return AgentResult(
                reply="Entendido. ¿Confirmas que quieres cancelar tu cita? Respóndeme con sí o no.",
                new_state=state,
            )

        if any(w in text for w in ["cambiar", "modificar", "mover", "otra fecha", "otro día", "otro dia"]):
            state.update({
                "selected_slot": None,
                "offered_slots": [],
                "preferred_date": None,
                "preferred_period": None,
            })
            resolved = resolve_date(text)
            if resolved and is_working_day(resolved) and not is_past_date(resolved):
                state["preferred_date"] = resolved.isoformat()
                state["stage"] = "COLLECTING_PERIOD"
                return AgentResult(
                    reply=f"Claro 😊 El {format_date_es(resolved)}, ¿prefieres mañana o tarde?",
                    new_state=state,
                )
            state["stage"] = "COLLECTING_DATE"
            return AgentResult(
                reply="Claro, dime qué día te vendría mejor y lo cambiamos 😊",
                new_state=state,
            )

        return AgentResult(
            reply="Ya tienes una cita confirmada 👍 Si quieres cambiarla o cancelarla, dímelo.",
            new_state=state,
        )

    async def _handle_cancel_confirmation(self, text: str, state: dict) -> AgentResult:
        if self._is_affirmation(text):
            appointment_id = state.get("appointment_id")
            google_event_id = state.get("google_event_id")

            if not appointment_id and not google_event_id:
                state["stage"] = "WAITING_HUMAN"
                return AgentResult(
                    reply="No encuentro una cita asociada a tu número 😕 Te paso con recepción para que puedan revisarlo.",
                    new_state=state,
                )

            result = await asyncio.to_thread(
                self.appointment_service.cancel_appointment,
                appointment_id=appointment_id,
                google_event_id=google_event_id,
            )

            if result.get("status") != "cancelled":
                state["stage"] = "WAITING_HUMAN"
                return AgentResult(
                    reply="No he podido cancelarla automáticamente 😕 Te paso con recepción para gestionarlo.",
                    new_state=state,
                )

            state.update({
                "stage": "IDLE",
                "current_intent": None,
                "appointment_status": "cancelled",
                "appointment_id": None,
                "google_event_id": None,
                "selected_slot": None,
                "offered_slots": [],
            })
            return AgentResult(
                reply="Listo, tu cita ha quedado cancelada ✅ Si necesitas pedir una nueva, aquí estoy.",
                new_state=state,
            )

        if self._is_negation(text):
            state.update({"stage": "APPOINTMENT_CREATED", "current_intent": None})
            return AgentResult(
                reply="Perfecto, mantengo tu cita como estaba 👍",
                new_state=state,
            )

        return AgentResult(
            reply="¿Me confirmas si quieres cancelar la cita? Responde sí o no 😊",
            new_state=state,
        )
    
    def _is_location_question(self, text: str) -> bool:
        keywords = {
            "dirección", "direccion", "ubicación", "ubicacion",
            "dónde queda", "donde queda", "dónde están", "donde estan",
            "dónde se encuentran", "donde se encuentran",
            "cómo llegar", "como llegar", "cómo llego", "como llego",
            "dónde es", "donde es", "queda lejos", "localización", "localizacion",
        }
        return any(kw in text for kw in keywords)

    def _is_opening_hours_question(self, text: str) -> bool:
        keywords = {
            "horario", "horarios",
            "hora abren", "hora abrís", "hora abris",
            "a qué hora abren", "a que hora abren",
            "a qué hora abrís", "a que hora abris",
            "hora cierran", "hora cerráis", "hora cerrais",
            "a qué hora cierran", "a que hora cierran",
            "a qué hora cerráis", "a que hora cerrais",
            "están abiertos", "estan abiertos",
            "estáis abiertos", "estais abiertos",
            "abren hoy", "abrís hoy", "abris hoy",
            "cierran hoy", "cerráis hoy", "cerrais hoy",
            "atienden", "atendéis", "atendeis",
            "días atienden", "dias atienden",
            "qué días abren", "que dias abren",
            "cuando abren", "cuándo abren",
        }
        return any(kw in text for kw in keywords)

    # ------------------------------------------------------------------ #
    #  Helpers de texto                                                    #
    # ------------------------------------------------------------------ #

    def _extract_name(self, text: str) -> Optional[str]:
        """
        Extrae el nombre del paciente con tres estrategias:
        1. Patrones explícitos: 'soy / me llamo / mi nombre es'
        2. Nombre compuesto sin patrones (2-4 palabras, sin ruido)
        3. Fallback: None (el caller usará .title() sobre el texto completo)
        """
        explicit_patterns = [
            r"(?:soy|me llamo|mi nombre es)\s+([A-Za-zÁÉÍÓÚáéíóúÑñÜü][a-záéíóúñü]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñÜü][a-záéíóúñü]+)+)",
            r"(?:soy|me llamo|mi nombre es)\s+(.+)",
        ]
        for pattern in explicit_patterns:
            match = re.search(pattern, text.strip(), re.IGNORECASE)
            if match:
                return match.group(1).strip().title()

        # Heurística: texto corto que parece un nombre propio
        noise_words = {
            "el", "la", "los", "las", "un", "una", "quiero", "cita",
            "hola", "gracias", "pedir", "reservar", "sí", "si", "no",
            "vale", "ok", "claro", "mañana", "tarde", "por", "favor",
        }
        words = text.strip().split()
        if 2 <= len(words) <= 4 and not any(w.lower() in noise_words for w in words):
            # Al menos la primera palabra empieza en mayúscula o parece nombre propio
            capitalized = sum(1 for w in words if w[0].isupper())
            if capitalized >= 1 or all(w.isalpha() for w in words):
                return text.strip().title()

        return None

    def _confirmation_text(self, state: dict) -> str:
        service = self._get_service(state)
        label = service.label if service else state.get("service_id", "consulta")
        date_human = self._format_date_human(state.get("preferred_date", ""))
        slot = state.get("selected_slot")
        name = state.get("patient_name")
        return (
            f"Perfecto, {name} 😊 Te confirmo:\n"
            f"• Servicio: {label}\n"
            f"• Día: {date_human}\n"
            f"• Hora: {slot}\n\n"
            "¿Lo dejo reservado?"
        )

    def _build_start_datetime(self, state: dict) -> str:
        date_str = state.get("preferred_date") or date.today().isoformat()
        slot = state.get("selected_slot") or "10:00"
        return f"{date_str}T{slot}:00"