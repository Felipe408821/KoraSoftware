from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class ConversationMode(str, Enum):
    AUTO = "AUTO"
    HUMAN = "HUMAN"
    PAUSED = "PAUSED"


class ConversationStatus(str, Enum):
    OPEN = "OPEN"
    PENDING_HUMAN = "PENDING_HUMAN"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"


class ControlAction(str, Enum):
    RUN_BOT = "RUN_BOT"
    DO_NOTHING = "DO_NOTHING"
    HANDOFF_TO_HUMAN = "HANDOFF_TO_HUMAN"


@dataclass
class ControlDecision:
    action: ControlAction
    reason: str
    should_send_handoff_message: bool = False
    handoff_message: str | None = None


class ConversationControlService:
    """
    Decide si el bot puede responder o si la conversación debe quedar en manos humanas.

    Este servicio no ejecuta el agente.
    Este servicio no envía WhatsApps.
    Solo toma decisiones de control.
    """

    HUMAN_KEYWORDS = [
        "humano",
        "persona",
        "asesor",
        "asesora",
        "recepcionista",
        "agente",
        "hablar con alguien",
        "quiero hablar",
        "llamar",
        "llamada",
        "me puede llamar",
        "me pueden llamar",
    ]

    URGENCY_KEYWORDS = [
        "urgencia",
        "emergencia",
        "dolor fuerte",
        "sangrado",
        "hinchado",
        "hinchazón",
        "infección",
        "accidente",
        "no aguanto",
        "me duele mucho",
        "dolor insoportable",
    ]

    def decide_for_inbound_message(
        self,
        *,
        conversation: dict[str, Any],
        text: str,
        now: datetime | None = None,
    ) -> ControlDecision:
        now = now or datetime.now(timezone.utc)

        mode = conversation.get("mode") or ConversationMode.AUTO.value
        status = conversation.get("status") or ConversationStatus.OPEN.value
        paused_until = conversation.get("paused_until")

        normalized_text = self._normalize_text(text)

        if mode == ConversationMode.HUMAN.value:
            return ControlDecision(
                action=ControlAction.DO_NOTHING,
                reason="conversation_in_human_mode",
            )

        if mode == ConversationMode.PAUSED.value:
            if self._pause_is_active(paused_until=paused_until, now=now):
                return ControlDecision(
                    action=ControlAction.DO_NOTHING,
                    reason="conversation_paused",
                )

            return ControlDecision(
                action=ControlAction.RUN_BOT,
                reason="pause_expired",
            )

        if status == ConversationStatus.CLOSED.value:
            return ControlDecision(
                action=ControlAction.RUN_BOT,
                reason="closed_conversation_reopened_by_new_message",
            )

        if self._contains_any(normalized_text, self.URGENCY_KEYWORDS):
            return ControlDecision(
                action=ControlAction.HANDOFF_TO_HUMAN,
                reason="urgency_detected",
                should_send_handoff_message=True,
                handoff_message=(
                    "Te voy a pasar con una persona del equipo para que pueda ayudarte mejor. "
                    "Si es una urgencia médica, por favor contacta directamente con un servicio de emergencia "
                    "o acude al centro de atención más cercano."
                ),
            )

        if self._contains_any(normalized_text, self.HUMAN_KEYWORDS):
            return ControlDecision(
                action=ControlAction.HANDOFF_TO_HUMAN,
                reason="human_requested",
                should_send_handoff_message=True,
                handoff_message="Claro, te paso con una persona del equipo para que pueda ayudarte.",
            )

        return ControlDecision(
            action=ControlAction.RUN_BOT,
            reason="auto_mode",
        )

    def should_send_bot_response_before_delivery(
        self,
        *,
        conversation: dict[str, Any],
        now: datetime | None = None,
    ) -> bool:
        """
        Segunda comprobación justo antes de enviar la respuesta del bot.

        Evita que el bot responda si mientras estaba procesando
        un humano tomó control o pausó la conversación.
        """
        now = now or datetime.now(timezone.utc)

        mode = conversation.get("mode") or ConversationMode.AUTO.value
        paused_until = conversation.get("paused_until")

        if mode == ConversationMode.HUMAN.value:
            return False

        if mode == ConversationMode.PAUSED.value:
            return not self._pause_is_active(paused_until=paused_until, now=now)

        return True

    def _pause_is_active(self, *, paused_until: str | None, now: datetime) -> bool:
        if paused_until is None:
            return True

        try:
            paused_until_dt = datetime.fromisoformat(paused_until)
        except ValueError:
            return True

        if paused_until_dt.tzinfo is None:
            paused_until_dt = paused_until_dt.replace(tzinfo=timezone.utc)

        return paused_until_dt > now

    def _contains_any(self, text: str, keywords: list[str]) -> bool:
        return any(keyword in text for keyword in keywords)

    def _normalize_text(self, text: str) -> str:
        return text.strip().lower()